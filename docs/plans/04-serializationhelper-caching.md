# Plan: SerializationHelper Caching

## Priority
**P2 - Medium Impact (15-25% improvement), Medium Risk**

## Problem

SerializationHelper repeatedly converts attribute names to XML tags during validation and serialization loops.

**Location**: `src/armodel2/serialization/serialization_helper.py`

**Current Hot Path** (line 423-424):
```python
# Called during validation for every object
expected_tags = {NameConverter.to_xml_tag(name) for name in type_hints.keys()}
```

**Performance Impact**:
- Name conversion in validation loops
- Re-computed for each object even when identical
- O(n) conversions where n = number of attributes

## Solution

Add class-level caching of XML tag mappings to avoid repeated conversions.

### Files to Modify

1. **`src/armodel2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ArObject/ar_object.py`**
   - Add `_XML_TAG_MAPPING` class attribute
   - Pre-compute at class definition

2. **`tools/generate_models/generators.py`**
   - Update code generation to include tag mapping cache

3. **`src/armodel2/serialization/serialization_helper.py`**
   - Add optional cache parameter to methods
   - Use pre-computed mappings when available

### Implementation Details

#### Option 1: Class-Level Tag Mapping Cache (Recommended)

Add to ARObject base class:

```python
class ARObject:
    _XML_TAG = "AR-OBJECT"

    # Add class-level cache for tag mappings
    _XML_TAG_MAPPING: dict[str, str] = {}

    @classmethod
    def _get_xml_tag_mapping(cls) -> dict[str, str]:
        """Get cached XML tag mapping for this class."""
        if not cls._XML_TAG_MAPPING:
            # Build mapping once
            hints = getattr(cls, '__annotations__', {})
            cls._XML_TAG_MAPPING = {
                name: NameConverter.to_xml_tag(name)
                for name in hints.keys()
            }
        return cls._XML_TAG_MAPPING
```

#### Option 2: SerializationHelper Optimization

Update validation to use cached mapping:

```python
@staticmethod
def validate_deserialization(
    obj: ARObject,
    element: ET.Element,
    expected_tags: Optional[set[str]] = None
) -> None:
    """Validate deserialization with optional cached tags."""
    if not GlobalSettingsManager().strict_validation:
        return

    # Use provided tags or compute from cache
    if expected_tags is None:
        # Check if object has cached mapping
        if hasattr(obj, '_get_xml_tag_mapping'):
            expected_tags = set(obj._get_xml_tag_mapping().values())
        else:
            # Fallback to old method
            hints = get_type_hints(type(obj))
            expected_tags = {NameConverter.to_xml_tag(name) for name in hints.keys()}

    # ... rest of validation
```

#### Option 3: Generator Pre-computation

Update `tools/generate_models/generators.py`:

```python
# Generate class with pre-computed mapping
def generate_class_with_cache(class_name: str, attribute_types: dict) -> str:
    """Generate class with XML tag mapping cache."""

    # Pre-compute XML tags for all attributes
    tag_mappings = {
        attr_name: NameConverter.to_xml_tag(attr_name)
        for attr_name in attribute_types.keys()
    }

    # Generate code
    lines = [
        f"class {class_name}({parent_class}):",
        f'    _XML_TAG = "{class_xml_tag}"',
        f'    _XML_TAG_MAPPING = {{',
    ]

    for attr_name, xml_tag in tag_mappings.items():
        lines.append(f'        "{attr_name}": "{xml_tag}",')

    lines.extend([
        '    }',
        '',
        '    @classmethod',
        '    def _get_xml_tag_mapping(cls) -> dict[str, str]:',
        '        return cls._XML_TAG_MAPPING',
        # ... rest of class
    ])

    return '\n'.join(lines)
```

### Optimization Priority

1. **Phase 1**: Add cache to ARObject base class (safe, affects all classes)
2. **Phase 2**: Update SerializationHelper to use cache (medium risk)
3. **Phase 3**: Update generator to pre-compute mappings (affects new classes)

## Testing

### Unit Tests
```bash
# Test cache behavior
PYTHONPATH=./src python -m pytest tests/unit/test_serialization/test_serialization_helper_caching.py -v

# Test ARObject cache
PYTHONPATH=./src python -m pytest tests/unit/test_models/test_ar_object_caching.py -v
```

### Integration Tests
```bash
# Binary comparison
PYTHONPATH=./src python -m pytest tests/integration/test_binary_comparison.py -v
```

### Cache Effectiveness Test
```python
# Verify cache is being used
from armodel2.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.autosar import AUTOSAR

# First access - builds cache
mapping1 = AUTOSAR._get_xml_tag_mapping()

# Second access - uses cache
mapping2 = AUTOSAR._get_xml_tag_mapping()

assert mapping1 is mapping2  # Same dict object
print(f"Cache size: {len(mapping1)} entries")
```

## Verification Commands

```bash
# 1. Run all tests
PYTHONPATH=./src python -m pytest

# 2. Profile validation specifically
python -m cProfile -o before.prof -c "
from armodel2.core import GlobalSettingsManager
GlobalSettingsManager().strict_validation = True
from armodel2.reader import ARXMLReader
reader = ARXMLReader()
autosar = reader.load_arxml('tests/fixtures/arxml/Base_Bswmd.arxml')
"

# 3. After changes
python -m cProfile -o after.prof -c "
from armodel2.core import GlobalSettingsManager
GlobalSettingsManager().strict_validation = True
from armodel2.reader import ARXMLReader
reader = ARXMLReader()
autosar = reader.load_arxml('tests/fixtures/arxml/Base_Bswmd.arxml')
"

# 4. Compare
python -m pstats before.prof after.prof
```

## Risk Assessment

**Risk Level**: MEDIUM

**Potential Issues**:
- Class-level caches increase memory usage
- Cache invalidation if classes are modified (unlikely in this codebase)
- Need to ensure cache is built correctly for all classes

**Mitigation**:
- Cache is built once per class (acceptable memory trade-off)
- Read-only cache (no invalidation needed)
- Comprehensive testing
- Can be disabled via settings if needed

**Memory Impact**:
- ~2,200 classes × average 10 attributes × 50 bytes = ~1 MB
- Acceptable trade-off for 15-25% performance improvement

## Expected Outcome

- **15-25% reduction** in validation overhead
- **5-10% overall improvement** in deserialize performance
- Minimal memory increase (~1-2 MB)
- No changes to API or behavior

## Dependencies

- **01-nameconverter-caching.md** should be completed first (will enhance this optimization)
- Can be implemented independently but works better together

## Status

**TODO** - Ready to implement (start with Phase 1)
