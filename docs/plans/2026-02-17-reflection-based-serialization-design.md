# Reflection-Based Serialization Design

**Date:** 2026-02-17
**Status:** Approved
**Author:** Design brainstorming session

## Problem Statement

The current serialization architecture has 3 layers of abstraction (XMLMember metadata, SerializationRegistry, Strategy pattern) making it difficult to maintain:
- ~800 lines of code across registry, strategies, and metadata
- Complex execution flow: obj → registry → strategy → metadata → serialize
- Generated classes require verbose `_xml_members` dict in every class
- Hard to trace execution and debug

## Solution: Pure Reflection with Decorator Overrides

Replace the 3-layer architecture with a single-layer approach using Python's built-in reflection:

**Key changes:**
1. ARObject.serialize() and deserialize() use `vars()` and `get_type_hints()` directly
2. Automatic name conversion: `short_name` ↔ `SHORT-NAME`
3. Decorators (`@xml_attribute`, `@xml_tag()`) for edge cases only
4. Eliminate SerializationRegistry, strategies, and XMLMember descriptors

**Result:** ~800 lines → ~150 lines in ARObject

## Architecture

### Components

```
┌─────────────────────────────────────────┐
│           ARXMLReader                   │
│  (Thin I/O wrapper: lxml → ElementTree) │
└────────────┬────────────────────────────┘
             │
             ▼
┌─────────────────────────────────────────┐
│           ARObject                      │
│  serialize()  deserialize()             │
│  - Uses vars() for attributes           │
│  - Uses get_type_hints() for types      │
│  - NameConverter for tag conversion     │
└────────────┬────────────────────────────┘
             │
             ▼
┌─────────────────────────────────────────┐
│      Decorators (edge cases)            │
│  @xml_attribute  @xml_tag()             │
└─────────────────────────────────────────┘
```

### Data Flow

**Read:**
```
ARXML File → ARXMLReader.load_arxml()
→ lxml parsing → ElementTree.Element
→ ARObject.deserialize(element)
→ vars() + get_type_hints()
→ Python object
```

**Write:**
```
Python object → ARObject.serialize(namespace)
→ vars() iterate attributes
→ NameConverter.to_xml_tag()
→ ElementTree.Element
→ ARXMLWriter.save_arxml()
→ XML File
```

## Name Conversion

**NameConverter utility:**

```python
class NameConverter:
    @staticmethod
    def to_xml_tag(name: str) -> str:
        """short_name → SHORT-NAME"""
        if name.startswith('_'):
            name = name[1:]
        return name.upper().replace('_', '-')

    @staticmethod
    def to_python_name(tag: str) -> str:
        """SHORT-NAME → short_name"""
        return tag.lower().replace('-', '_')
```

**Examples:**
- `short_name` ↔ `SHORT-NAME`
- `category` ↔ `CATEGORY`
- `base_type_size` ↔ `BASE-TYPE-SIZE`
- `sw_data_def_props` ↔ `SW-DATA-DEF-PROPS`

## Core Implementation

### ARObject Base Class

```python
class ARObject:
    def serialize(self, namespace: str) -> Element:
        """Serialize object to XML using reflection."""
        elem = Element(self._get_xml_tag())

        for name, value in vars(self).items():
            if name.startswith('_'):
                continue

            xml_tag = NameConverter.to_xml_tag(name)

            if self._is_xml_attribute(name):
                elem.set(xml_tag, str(value))
            elif value is not None:
                self._serialize_child(elem, name, value, namespace)

        return elem

    @classmethod
    def deserialize(cls, element: Element) -> Self:
        """Deserialize XML element to Python object."""
        obj = cls.__new__(cls)
        obj.__init__()  # Set defaults

        type_hints = get_type_hints(cls)

        for attr_name, attr_type in type_hints.items():
            xml_tag = NameConverter.to_xml_tag(attr_name)

            if cls._is_xml_attribute(attr_name):
                value = element.get(xml_tag)
            else:
                child = element.find(xml_tag)
                value = cls._deserialize_value(child, attr_type)

            setattr(obj, attr_name, value)

        return obj
```

### Decorators

```python
def xml_attribute(func):
    """Mark property as XML attribute instead of element."""
    func._is_xml_attribute = True
    return func

def xml_tag(tag_name: str):
    """Specify custom XML tag name."""
    def decorator(cls_or_func):
        cls_or_func._xml_tag = tag_name
        return cls_or_func
    return decorator
```

## Generated Classes

### Before (Current)

```python
class SwBaseType(ARObject):
    _xml_members: dict[str, XMLMember] = {
        "short_name": XMLMember(xml_tag="SHORT-NAME", is_attribute=False, multiplicity="1"),
        "category": XMLMember(xml_tag="CATEGORY", is_attribute=True, multiplicity="0..1"),
        "base_type_size": XMLMember(xml_tag="BASE-TYPE-SIZE", is_attribute=False, multiplicity="0..1"),
    }

    def __init__(self):
        self.short_name: String = None
        self.category: Optional[str] = None
        self.base_type_size: Optional[int] = None
```

### After (Proposed)

```python
class SwBaseType(ARObject):
    # No _xml_members dict!

    def __init__(self):
        self.short_name: String = None
        self.category: Optional[str] = None
        self.base_type_size: Optional[int] = None

    @xml_attribute
    @property
    def category(self) -> Optional[str]:
        """XML attribute marker."""
        return self._category

    @category.setter
    def category(self, value: Optional[str]):
        self._category = value
```

**Benefits:**
- Zero metadata boilerplate for 95% of classes
- Type hints drive deserialization
- Decorators clearly signal special cases
- Easier to read and maintain

## Generator Changes (tools/generate_models.py)

### Remove

1. Lines 529-601: `_xml_members` dict generation
2. XMLMember imports
3. Lines 572-597: Circular import string class handling in XMLMember

### Add

1. Decorator generation for edge cases:
   - `@xml_attribute` for attributes
   - `@xml_tag()` for custom tag names
2. Property wrappers when decorators are needed

### Keep

1. Type hints - essential for deserialization
2. `__init__` with default values
3. Parent class inheritance
4. Builder classes

## Reader/Writer Simplification

### ARXMLReader

```python
class ARXMLReader:
    def load_arxml(self, file_path: str) -> AUTOSAR:
        # Parse with lxml
        tree = lxml.parse(file_path)
        root = tree.getroot()

        # Convert to ElementTree
        root_et = self._lxml_to_elementtree(root)

        # Delegate to ARObject
        return AUTOSAR.deserialize(root_et)
```

### ARXMLWriter

```python
class ARXMLWriter:
    def save_arxml(self, autosar: AUTOSAR, file_path: str):
        # Delegate to ARObject
        root = autosar.serialize(namespace)

        # Write to file
        tree = ElementTree.ElementTree(root)
        tree.write(file_path, encoding=self.encoding)
```

## Edge Cases

### 1. XML Attributes

Use `@xml_attribute` decorator:

```python
class AUTOSAR(ARObject):
    @xml_attribute
    @property
    def schema_version(self) -> str:
        return self._schema_version
```

### 2. Custom Tag Names

Use `@xml_tag()` decorator:

```python
@xml_tag("AUTOSAR")
class AUTOSAR(ARObject):
    pass
```

### 3. Python Keywords

Handled automatically by generator (appends underscore):

```python
# Attribute "class" in XML becomes:
self.class_: Optional[str] = None
```

### 4. Lists and Optional

Handled via type hints:

```python
self.admin_data: Optional[AdminData] = None  # Optional
self.ar_packages: list[ARPackage] = []       # List
```

## Error Handling

### Validation During Deserialization

1. **Missing required fields:** Raise `ValueError` if required attribute missing
2. **Type mismatches:** Validate against type hints
3. **Invalid XML:** Parse errors raised by lxml
4. **Circular references:** Handled by lazy evaluation

### Validation During Serialization

1. **None values:** Skip optional fields, error on required
2. **Type checking:** Validate values match type hints
3. **Namespace handling:** Ensure proper namespace prefix

## Testing Strategy

### Unit Tests

1. **NameConverter** - bidirectional conversion
2. **ARObject.serialize()** - mock objects
3. **ARObject.deserialize()** - XML fragments
4. **Decorators** - edge case handling

### Integration Test

1. **Round-trip test:** Read AUTOSAR_Datatypes.arxml → Python objects → Write ARXML → Compare
2. **Validation:** Missing fields, type mismatches
3. **Performance:** Large file handling

### Test Coverage

```python
def test_round_trip():
    reader = ARXMLReader()
    autosar = reader.load_arxml('demos/arxml/AUTOSAR_Datatypes.arxml')

    writer = ARXMLWriter()
    writer.save_arxml(autosar, 'output.arxml')

    # Verify output matches input
    assert files_equal('demos/arxml/AUTOSAR_Datatypes.arxml', 'output.arxml')
```

## Migration Path

### Phase 1: Core Implementation
1. Implement ARObject.serialize() and deserialize()
2. Implement NameConverter
3. Implement decorators

### Phase 2: Generator Update
1. Modify tools/generate_models.py
2. Regenerate all model classes
3. Verify no regressions

### Phase 3: Reader/Writer Update
1. Simplify ARXMLReader
2. Simplify ARXMLWriter
3. Remove deprecated code

### Phase 4: Testing
1. Unit tests
2. Integration test with AUTOSAR_Datatypes.arxml
3. Fix any issues

### Phase 5: Cleanup
1. Remove SerializationRegistry
2. Remove strategy classes
3. Remove XMLMember descriptor
4. Update documentation

## Files to Change

### New Files

- `src/armodel/serialization/name_converter.py` - Name conversion utility
- `src/armodel/serialization/decorators.py` - @xml_attribute, @xml_tag

### Modified Files

- `src/armodel/models/M2/AUTOSARTemplates/.../ArObject/ar_object.py` - Add serialize/deserialize
- `tools/generate_models.py` - Remove XMLMember generation
- `src/armodel/reader/__init__.py` - Simplify
- `src/armodel/writer/__init__.py` - Simplify

### Removed Files (Phase 5)

- `src/armodel/serialization/registry.py`
- `src/armodel/serialization/strategies/reflection_serializer.py`
- `src/armodel/serialization/strategies/custom_autosar.py`
- `src/armodel/serialization/metadata.py` (XMLMember)

## Success Criteria

1. ✅ Generated classes have no `_xml_members` dict
2. ✅ AUTOSAR_Datatypes.arxml can be read successfully
3. ✅ Round-trip test passes (read → write → compare)
4. ✅ Code is simpler and easier to understand
5. ✅ All existing functionality preserved

## Open Questions

None - design approved and ready for implementation.
