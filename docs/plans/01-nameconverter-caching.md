# Plan: NameConverter Caching

## Priority
**P1 - High Impact (60-80% improvement), Low Risk**

## Problem

`NameConverter.to_xml_tag()` and related conversion methods are called **tens of thousands of times** during serialization/deserialization of large ARXML files. Each call performs expensive string processing:

**Location**: `src/armodel2/serialization/name_converter.py`

**Current Hot Paths**:
- `to_xml_tag()` - Called once per attribute per object
- `to_snake_case()` - Called during deserialization
- `to_class_name()` - Called for class resolution
- `to_singular()` - Called for list attribute handling

**Performance Impact**:
- Large file (7,000+ lines, ~10,000 objects): ~100,000+ calls
- Complex string operations: splitting, joining, dictionary lookups
- No caching of repeated conversions

## Solution

Add LRU caching to NameConverter conversion methods.

### Files to Modify

1. **`src/armodel2/serialization/name_converter.py`**
   - Add `@lru_cache` decorator to conversion methods
   - Pre-compute common conversions at module import

### Implementation Details

```python
from functools import lru_cache

class NameConverter:
    @staticmethod
    @lru_cache(maxsize=10000)
    def to_xml_tag(name: str) -> str:
        """Convert Python attribute name to XML tag name."""
        # Existing implementation - now cached

    @staticmethod
    @lru_cache(maxsize=10000)
    def to_snake_case(tag: str) -> str:
        """Convert XML tag name to Python attribute name."""
        # Existing implementation - now cached

    @staticmethod
    @lru_cache(maxsize=10000)
    def to_class_name(tag: str) -> str:
        """Convert XML tag to PascalCase class name."""
        # Existing implementation - now cached

    @staticmethod
    @lru_cache(maxsize=1000)
    def to_singular(tag: str) -> str:
        """Convert plural XML tag to singular form."""
        # Existing implementation - now cached
```

### Additional Optimization: Pre-compute Common Tags

Add module-level initialization for frequently used conversions:

```python
# At module level, after class definition
_common_xml_tags = {
    "short_name": "SHORT-NAME",
    "long_name": "LONG-NAME",
    "admin_data": "ADMIN-DATA",
    "ar_packages": "AR-PACKAGES",
    "ar_package": "AR-PACKAGE",
    # Add more common attributes...
}

# Warm up the cache
for attr_name, xml_tag in _common_xml_tags.items():
    NameConverter.to_xml_tag(attr_name)
```

## Testing

### Unit Tests
```bash
# Run existing unit tests
PYTHONPATH=./src python -m pytest tests/unit/test_serialization/test_name_converter.py -v

# Add new test for caching behavior
PYTHONPATH=./src python -m pytest tests/unit/test_serialization/test_name_converter_caching.py -v
```

### Integration Tests
```bash
# Binary comparison tests to ensure correctness
PYTHONPATH=./src python -m pytest tests/integration/test_binary_comparison.py -v
```

### Performance Verification
```python
# Create benchmark script
import time
from armodel2.serialization.name_converter import NameConverter

# Test cache effectiveness
test_names = ["short_name", "long_name", "admin_data"] * 10000

start = time.time()
for name in test_names:
    NameConverter.to_xml_tag(name)
end = time.time()

print(f"Time with caching: {end - start:.4f}s")
print(f"Cache info: {NameConverter.to_xml_tag.cache_info()}")
```

## Verification Commands

```bash
# 1. Run all tests to ensure correctness
PYTHONPATH=./src python -m pytest

# 2. Profile before and after
python -m cProfile -o before.prof -m armodel2.cli.cli format tests/fixtures/arxml/Base_Bswmd.arxml -o /dev/null
# [Apply changes]
python -m cProfile -o after.prof -m armodel2.cli.cli format tests/fixtures/arxml/Base_Bswmd.arxml -o /dev/null

# 3. Compare profiles
python -m pstats before.prof after.prof
```

## Risk Assessment

**Risk Level**: LOW

- Changes are localized to a single file
- LRU caching is a well-understood pattern
- No changes to serialization logic
- Cache size (10,000) is sufficient for most AUTOSAR models

**Mitigation**:
- Cache has bounded size (won't grow unbounded)
- Unit tests verify correctness
- Binary comparison tests ensure identical output

## Expected Outcome

- **60-80% reduction** in name conversion overhead
- **10-20% overall improvement** in serialize/deserialize performance
- No changes to API or behavior
- Minimal memory increase (~1-2 MB for cache)

## Dependencies

None - This can be implemented independently.

## Status

**TODO** - Ready to implement
