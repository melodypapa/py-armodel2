# Plan: Type Hint Resolution Caching

## Priority
**P1 - High Impact (70-90% improvement), Low Risk**

## Problem

`get_type_hints()` is called repeatedly during deserialization. Python's `get_type_hints()` performs expensive runtime evaluation including forward reference resolution.

**Location**: `src/armodel2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes/ar_primitive.py`

**Current Hot Paths**:
- `ARPrimitive.deserialize()` - Calls `get_type_hints(cls)` on every call
- Generated classes - May use similar patterns

**Performance Impact**:
- Called for every object deserialization
- `get_type_hints()` is 10-100x slower than accessing `__annotations__`
- For large files: ~10,000+ expensive calls

## Solution

Replace `get_type_hints()` with direct `__annotations__` access and implement class-level caching.

### Files to Modify

1. **`src/armodel2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes/ar_primitive.py`**
   - Replace `get_type_hints()` with `__annotations__`
   - Add class-level cache

2. **`tools/generate_models/generators.py`**
   - Update code generation to use `__annotations__` pattern

### Implementation Details

#### For ARPrimitive (ar_primitive.py)

**Current Code** (lines 104-111):
```python
try:
    type_hints = get_type_hints(cls)
except Exception:
    type_hints = cls.__annotations__
```

**Optimized Code**:
```python
# Add class-level cache
_type_hints_cache = None

@classmethod
def _get_type_hints(cls) -> dict:
    """Get type hints with caching."""
    if cls._type_hints_cache is None:
        # Use __annotations__ directly (much faster than get_type_hints)
        cls._type_hints_cache = getattr(cls, '__annotations__', {})
    return cls._type_hints_cache

@classmethod
def deserialize(cls, element: ET.Element) -> "ARPrimitive":
    # Use cached type hints
    type_hints = cls._get_type_hints()
    # ... rest of implementation
```

#### For Code Generator (generators.py)

Update the deserialize method generation pattern:

**Current Pattern**:
```python
try:
    type_hints = get_type_hints(cls)
except Exception:
    type_hints = cls.__annotations__
```

**Optimized Pattern**:
```python
# Use __annotations__ directly for performance
type_hints = getattr(cls, '__annotations__', {})
```

### Additional Optimization: Skip Type Hints When Possible

For simple serialization, type hints may not be needed:

```python
# In serialize(), often we don't need type hints at all
# Just serialize the value directly
```

## Testing

### Unit Tests
```bash
# Run ARPrimitive tests
PYTHONPATH=./src python -m pytest tests/unit/test_models/test_ar_primitive.py -v
```

### Integration Tests
```bash
# Binary comparison tests
PYTHONPATH=./src python -m pytest tests/integration/test_binary_comparison.py -v
```

### Performance Verification
```python
# Benchmark script
import time
from typing import get_type_hints
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_primitive import ARPrimitive

# Compare get_type_hints vs __annotations__
iterations = 10000

# Test get_type_hints()
start = time.time()
for _ in range(iterations):
    get_type_hints(ARPrimitive)
time_gethints = time.time() - start

# Test __annotations__
start = time.time()
for _ in range(iterations):
    ARPrimitive.__annotations__
time_annotations = time.time() - start

print(f"get_type_hints: {time_gethints:.4f}s")
print(f"__annotations__: {time_annotations:.4f}s")
print(f"Speedup: {time_gethints / time_annotations:.1f}x")
```

## Verification Commands

```bash
# 1. Run all tests
PYTHONPATH=./src python -m pytest

# 2. Profile deserialization specifically
python -m cProfile -o before.prof -c "
from armodel2.reader import ARXMLReader
reader = ARXMLReader()
autosar = reader.load_arxml('tests/fixtures/arxml/Base_Bswmd.arxml')
"

# 3. After changes, compare
python -m cProfile -o after.prof -c "
from armodel2.reader import ARXMLReader
reader = ARXMLReader()
autosar = reader.load_arxml('tests/fixtures/arxml/Base_Bswmd.arxml')
"
```

## Risk Assessment

**Risk Level**: LOW to MEDIUM

**Potential Issues**:
- `__annotations__` may not resolve forward references in all cases
- Need to verify TYPE_CHECKING imports work correctly

**Mitigation**:
- Keep fallback to `get_type_hints()` if `__annotations__` is empty
- Comprehensive testing with all model classes
- Binary comparison tests ensure identical output

**Note**: The codebase uses `from __future__ import annotations`, which makes `__annotations__` contain strings. This is actually preferred since the codebase has custom `_import_class_by_name()` logic.

## Expected Outcome

- **70-90% reduction** in type hint resolution overhead
- **5-15% overall improvement** in deserialization performance
- No changes to API or behavior
- Minimal memory increase (one dict per class)

## Dependencies

None - This can be implemented independently.

## Status

**TODO** - Ready to implement
