# Plan: Batch List Serialization

## Priority
**P3 - Lower Impact (10-15% improvement), Higher Risk/Complexity**

## Problem

List serialization creates many individual append operations, causing DOM manipulation overhead.

**Location**: Generated serialize methods for list attributes

**Current Pattern**:
```python
# For each item in list
if self.items is not None:
    for item in self.items:
        serialized = SerializationHelper.serialize_item(item, "ItemType")
        wrapped = ET.Element("ITEM-TAG")
        # ... wrapping logic
        elem.append(wrapped)  # Individual append
```

**Performance Impact**:
- O(n) individual `append()` calls
- DOM tree modification overhead for each item
- Inefficient for large lists (100+ items)

## Solution

Implement batch element creation and append operations for lists.

### Files to Modify

1. **`tools/generate_models/generators.py`**
   - Update list serialization code generation pattern
   - Implement batch append for list attributes

2. **`src/armodel2/serialization/serialization_helper.py`**
   - Add `serialize_list()` helper method

### Implementation Details

#### Option 1: Batch Append Pattern (Recommended)

Update generator to produce:

```python
if self.items is not None:
    # Pre-allocate list for elements
    item_elements = []
    for item in self.items:
        serialized = SerializationHelper.serialize_item(item, "ItemType")
        if serialized is not None:
            wrapped = ET.Element("ITEM-TAG")
            # ... wrapping logic
            item_elements.append(wrapped)

    # Batch append all at once
    elem.extend(item_elements)
```

**Benefits**:
- Reduces DOM tree modifications
- `extend()` is more efficient than multiple `append()` calls

#### Option 2: SerializationHelper List Method

Add to `serialization_helper.py`:

```python
@staticmethod
def serialize_list(
    items: list[Any],
    item_tag: str,
    expected_type: str,
    parent: ET.Element
) -> None:
    """Serialize a list of items and append to parent in batch.

    Args:
        items: List of items to serialize
        item_tag: XML tag name for each item
        expected_type: Expected type hint for items
        parent: Parent element to append to
    """
    if not items:
        return

    # Collect all elements first
    elements = []
    for item in items:
        serialized = SerializationHelper.serialize_item(item, expected_type)
        if serialized is not None:
            wrapped = ET.Element(item_tag)
            # ... wrapping logic
            elements.append(wrapped)

    # Batch append
    parent.extend(elements)
```

#### Option 3: Specialized List Handlers

For common list types, generate specialized handlers:

```python
@staticmethod
def _serialize_items(elem: ET.Element, items: list) -> None:
    """Specialized handler for item lists."""
    if not items:
        return

    # Pre-calculate common data
    item_tag = "ITEM"
    elements = []

    for item in items:
        child = ET.Element(item_tag)
        if hasattr(item, 'serialize'):
            serialized = item.serialize()
            if serialized is not None:
                elements.append(serialized)
        else:
            child.text = str(item)
            elements.append(child)

    elem.extend(elements)
```

### Complexity Considerations

This optimization is more complex because:
1. Requires changes to code generation patterns
2. Need to handle special cases (lists with wrappers, polymorphic lists, etc.)
3. Must maintain exact XML equivalence for binary comparison tests
4. Interacts with other optimizations (ref_conditional, instance_ref, etc.)

### Special Cases to Handle

1. **Wrapped lists** (e.g., `<ITEMS><ITEM>...</ITEM></ITEMS>`)
2. **Polymorphic lists** (different item types)
3. **Ref-conditional lists** (reference lists with conditional wrappers)
4. **Direct child lists** (items serialized directly under parent)

## Testing

### Unit Tests
```bash
# Test list serialization specifically
PYTHONPATH=./src python -m pytest tests/unit/test_serialization/test_list_serialization.py -v

# Test large lists
PYTHONPATH=./src python -m pytest tests/unit/test_serialization/test_large_lists.py -v
```

### Integration Tests
```bash
# Binary comparison (critical)
PYTHONPATH=./src python -m pytest tests/integration/test_binary_comparison.py -v
```

### Performance Test
```python
# Benchmark list serialization
import time
from armodel2.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.autosar import AUTOSAR

# Create large list
autosar = AUTOSAR()
pkg = ARPackageBuilder().with_short_name("Test").build()
for i in range(1000):
    pkg.ar_packages.append(ARPackageBuilder().with_short_name(f"Pkg{i}").build())
autosar.ar_packages.append(pkg)

# Time serialization
start = time.time()
elem = autosar.serialize()
duration = time.time() - start

print(f"Serialized {len(pkg.ar_packages)} items in {duration:.4f}s")
print(f"Rate: {len(pkg.ar_packages) / duration:.0f} items/sec")
```

## Verification Commands

```bash
# 1. Binary comparison (must pass)
PYTHONPATH=./src python -m pytest tests/integration/test_binary_comparison.py -v

# 2. Profile list serialization
python -m cProfile -o lists.prof -c "
from armodel2.models import ARPackage, ARPackageBuilder
pkg = ARPackageBuilder().with_short_name('Test').build()
for i in range(100):
    pkg.ar_packages.append(ARPackageBuilder().with_short_name(f'P{i}').build())
elem = pkg.serialize()
"

# 3. Check append vs extend frequency
python -m pstats lists.prof | grep -E "(append|extend)"
```

## Risk Assessment

**Risk Level**: MEDIUM to HIGH

**Potential Issues**:
- Complex interaction with existing serialization patterns
- Must handle all special cases correctly
- Code generation changes affect 2,200+ classes
- Risk of breaking binary comparison tests

**Mitigation**:
- Implement incrementally
- Start with simple lists, add special cases gradually
- Extensive testing with various list types
- Can be rolled back via code regeneration
- Feature flag to enable/disable

**Recommended Approach**:
1. Phase 1: Implement SerializationHelper helper (low risk)
2. Phase 2: Update generator for new classes (medium risk)
3. Phase 3: Add specialized handlers for common patterns (medium risk)
4. Phase 4: Regenerate existing classes (high risk, thorough testing)

## Expected Outcome

- **10-15% improvement** in list serialization performance
- Most noticeable for large lists (100+ items)
- Reduced DOM tree modification overhead
- Binary equivalence maintained

## Dependencies

- Should complete **01-nameconverter-caching.md** and **02-typehint-caching.md** first
- **03-xml-element-optimization.md** may provide complementary benefits
- **04-serializationhelper-caching.md** may provide infrastructure

## Status

**TODO** - Defer until higher priority items are complete

## Notes

This optimization provides diminishing returns compared to P1 and P2 items. Consider implementing only if profiling shows list serialization is a significant bottleneck in your specific use case.
