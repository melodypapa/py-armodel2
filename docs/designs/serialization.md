# Serialization Framework Documentation

## Overview

py-armodel2 uses a **reflection-based serialization framework** that automatically handles XML serialization/deserialization without boilerplate code. The framework consists of:

- **Base class**: `ARObject` - provides `serialize()` and `deserialize()` methods
- **Name converter**: `NameConverter` - handles snake_case ↔ UPPER-CASE-WITH-HYPHENS conversion
- **Decorators**: Edge case handlers for special XML scenarios

### Key Benefits

- **Zero boilerplate**: 95% of classes need no metadata
- **Type-safe**: Type hints drive deserialization
- **Automatic**: Reflection discovers attributes via `vars()` and `get_type_hints()`
- **Minimal decorators**: Only needed for edge cases

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
│   ARPrimitive (Primitive Types)         │
│  - Wraps primitive values               │
│  - Supports additional attributes       │
│  - Enum attributes always uppercase     │
└────────────┬────────────────────────────┘
             │
             ▼
┌─────────────────────────────────────────┐
│      AREnum (Enumeration Types)         │
│  - Case-insensitive deserialization     │
│  - Uppercase serialization              │
└────────────┬────────────────────────────┘
             │
             ▼
┌─────────────────────────────────────────┐
│      Decorators (edge cases)            │
│  @xml_attribute  @atp_variant()  @l_prefix() │
└─────────────────────────────────────────┘
```

### File Locations

- **Base class**: `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ArObject/ar_object.py`
- **Primitive types**: `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes/ar_primitive.py`
- **Enum types**: `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes/ar_enum.py`
- **Decorators**: `src/armodel/serialization/decorators.py`
- **Name converter**: `src/armodel/serialization/name_converter.py`

## Decorators

### 1. `@xml_attribute`

**Purpose**: Mark a property/attribute to be serialized as an **XML attribute** instead of a child element.

**When to use**:
- When the XML schema requires data as an attribute (e.g., `<AUTOSAR schema-version="4.5.0">`)
- For metadata like IDs, versions, UUIDs, etc.

**Location**: `src/armodel/serialization/decorators.py:6-27`

#### Usage Example

```python
from armodel.serialization.decorators import xml_attribute
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject

class AUTOSAR(ARObject):
    def __init__(self) -> None:
        self._schema_version: str = "4.5.0"
        self.ar_packages: list[ARPackage] = []

    @xml_attribute
    @property
    def schema_version(self) -> str:
        """Schema version serialized as XML attribute."""
        return self._schema_version

    @schema_version.setter
    def schema_version(self, value: str) -> None:
        self._schema_version = value

# Results in:
# <AUTOSAR SCHEMA-VERSION="4.5.0">
#     <AR-PACKAGES>...</AR-PACKAGES>
# </AUTOSAR>
```

**Without the decorator**, it would serialize as:
```xml
<AUTOSAR>
    <SCHEMA-VERSION>4.5.0</SCHEMA-VERSION>
</AUTOSAR>
```

#### Important Implementation Details

1. **Decorator order**: `@xml_attribute` must come **before** `@property`
2. **Property pattern**: Requires property getter/setter pattern
3. **Private storage**: Use underscore-prefixed private attribute (e.g., `_schema_version`)

#### Common Use Cases

- `schema_version` - AUTOSAR schema version
- `uuid` - Unique identifiers
- `id` - Element IDs
- `version` - Version attributes

---

### 2. `@atp_variant()`

**Purpose**: Mark a class as using the AUTOSAR **atpVariation** pattern.

**When to use**:
- When AUTOSAR schema defines elements with `<CLASS-TAG>-VARIANTS/<CLASS-TAG>-CONDITIONAL` wrapper structure
- Automatically applied by code generator based on JSON mapping data

**Location**: `src/armodel/serialization/decorators.py:30-55`

#### Usage Example

```python
from armodel.serialization.decorators import atp_variant
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject

@atp_variant()
class SwDataDefProps(ARObject):
    base_type_ref: Optional[ARRef] = None
    sw_calibration_access: Optional[SwCalibrationAccessEnum] = None

# Serializes as:
# <SW-DATA-DEF-PROPS>
#   <SW-DATA-DEF-PROPS-VARIANTS>
#     <SW-DATA-DEF-PROPS-CONDITIONAL>
#       <BASE-TYPE-REF>...</BASE-TYPE-REF>
#       <SW-CALIBRATION-ACCESS>...</SW-CALIBRATION-ACCESS>
#     </SW-DATA-DEF-PROPS-CONDITIONAL>
#   </SW-DATA-DEF-PROPS-VARIANTS>
# </SW-DATA-DEF-PROPS>
```

### 3. `@l_prefix(tag_name: str)`

**Purpose**: Mark an attribute as using **language-specific L-N** naming pattern for multilanguage text.

**When to use**:
- For MultiLanguage* classes where content is wrapped in language tags (e.g., L-1, L-2, L-4, L-5, L-10)
- Automatically applied by code generator based on JSON `kind: "l_prefix"` mapping

**Location**: `src/armodel/serialization/decorators.py:58-80`

#### Usage Example

```python
from armodel.serialization.decorators import l_prefix
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject

class MultiLanguagePlainText(ARObject):
    def __init__(self) -> None:
        self._l10: LPlainText = None

    @property
    @l_prefix("L-10")
    def l10(self) -> LPlainText:
        return self._l10

# Serializes as:
# <L-10 L="EN">English text</L-10>
```

## Name Conversion

### NameConverter Utility

**Location**: `src/armodel/serialization/name_converter.py`

### Python → XML Conversion

```python
NameConverter.to_xml_tag(name: str) -> str
```

| Python Name (snake_case) | XML Tag (UPPER-CASE-WITH-HYPHENS) |
|--------------------------|-----------------------------------|
| `short_name` | `SHORT-NAME` |
| `category` | `CATEGORY` |
| `base_type_size` | `BASE-TYPE-SIZE` |
| `sw_data_def_props` | `SW-DATA-DEF-PROPS` |
| `ar_packages` | `AR-PACKAGES` |

### XML → Python Conversion

```python
NameConverter.to_python_name(tag: str) -> str
```

| XML Tag (UPPER-CASE-WITH-HYPHENS) | Python Name (snake_case) |
|-----------------------------------|--------------------------|
| `SHORT-NAME` | `short_name` |
| `CATEGORY` | `category` |
| `BASE-TYPE-SIZE` | `base_type_size` |
| `SW-DATA-DEF-PROPS` | `sw_data_def_props` |
| `AR-PACKAGES` | `ar_packages` |

### Implementation

```python
class NameConverter:
    @staticmethod
    def to_xml_tag(name: str) -> str:
        """Convert Python attribute name to XML tag name."""
        if name.startswith('_'):
            name = name[1:]
        return name.upper().replace('_', '-')

    @staticmethod
    def to_python_name(tag: str) -> str:
        """Convert XML tag name to Python attribute name."""
        return tag.lower().replace('-', '_')
```

## Serialization Behavior

### How `serialize()` Works

```python
def serialize(self, namespace: str = "") -> ET.Element:
```

**Flow**:
1. Get XML tag name (auto-generated from class name using NameConverter)
2. For each attribute in `vars(self)`:
   - Skip private attributes (starting with `_`)
   - Convert name via `NameConverter.to_xml_tag()`
   - Check if `@xml_attribute` decorator is present
     - If yes: serialize as XML attribute (`elem.set()`)
     - If no: serialize as child element
3. Handle different types:
   - **Objects with `serialize()`**: Recursively serialize
   - **Lists**: Create wrapper element, serialize each item
   - **Primitives**: Create element with text content

### How `deserialize()` Works

```python
@classmethod
def deserialize(cls, element: ET.Element) -> ARObject:
```

**Flow**:
1. Create instance using `cls.__new__(cls)` (bypasses `__init__`)
2. Call `__init__()` to set default values
3. Get type hints using `get_type_hints()`
   - Falls back to `__annotations__` if circular imports
4. For each expected attribute:
   - Convert Python name to XML tag
   - Check if `@xml_attribute` decorator is present
     - If yes: extract from XML attributes (`element.get()`)
     - If no: find child element
   - Parse value based on type hint:
     - `list[T]`: Deserialize all child elements
     - `Optional[T]`: Deserialize if present, else `None`
     - Object types: Call `deserialize()` recursively
     - Primitives: Convert text content

## Type Hints and Multiplicity

Type hints drive deserialization behavior:

| AUTOSAR Multiplicity | Python Type | Initial Value | Example |
|---------------------|-------------|---------------|---------|
| `0..1` | `Optional[Type]` | `None` | `admin_data: Optional[AdminData] = None` |
| `1` | `Type` | `None` (set during deserialize) | `short_name: String = None` |
| `*` | `list[Type]` | `[]` | `ar_packages: list[ARPackage] = []` |
| `0..*` | `list[Type]` | `[]` | `descriptions: list[Description] = []` |

## Common Patterns

### Pattern 1: Simple Class (No Decorators)

95% of classes don't need any decorators:

```python
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject

class ARPackage(ARObject):
    short_name: Optional[str] = None
    ar_packages: list[ARPackage] = []
    category: Optional[str] = None

# Automatically serializes to:
# <AR-PACKAGE>
#     <SHORT-NAME>MyPackage</SHORT-NAME>
#     <AR-PACKAGES>
#         <AR-PACKAGE>...</AR-PACKAGE>
#     </AR-PACKAGES>
#     <CATEGORY>DataTypes</CATEGORY>
# </AR-PACKAGE>
```

### Pattern 2: Primitive Type with Attributes

Some primitive types have additional attributes beyond just a value:

```python
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_primitive import ARPrimitive
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.interval_type_enum import IntervalTypeEnum

class Limit(ARPrimitive):
    """Primitive type with value and interval_type attribute."""
    
    python_type: type = str
    interval_type: Optional[IntervalTypeEnum] = None

    def __init__(self, value: Optional[str] = None, interval_type: Optional[IntervalTypeEnum] = None) -> None:
        super().__init__()
        self.value = value
        self.interval_type = interval_type

# Serializes to:
# <LOWER-LIMIT INTERVAL-TYPE="CLOSED">100</LOWER-LIMIT>

# Note: Enum attributes are always serialized as uppercase
# The interval_type value "closed" is serialized as "CLOSED"
```

### Pattern 2: XML Attribute

```python
from armodel.serialization.decorators import xml_attribute

class ImplementationDataType(ARObject):
    def __init__(self) -> None:
        self._uuid: str = ""
        self.short_name: Optional[str] = None

    @xml_attribute
    @property
    def uuid(self) -> str:
        return self._uuid

    @uuid.setter
    def uuid(self, value: str) -> None:
        self._uuid = value

# Serializes to:
# <IMPLEMENTATION-DATA-TYPE UUID="abc-123">
#     <SHORT-NAME>MyType</SHORT-NAME>
# </IMPLEMENTATION-DATA-TYPE>
```

### Pattern 3: XML Attribute with Nested Objects

```python
from armodel.serialization.decorators import xml_attribute

class AUTOSAR(ARObject):
    def __init__(self) -> None:
        self._schema_version: str = "4.5.0"
        self.ar_packages: list[ARPackage] = []

    @xml_attribute
    @property
    def schema_version(self) -> str:
        return self._schema_version

    @schema_version.setter
    def schema_version(self, value: str) -> None:
        self._schema_version = value

# Serializes to:
# <AUTOSAR SCHEMA-VERSION="4.5.0">
#     <AR-PACKAGES>
#         <AR-PACKAGE>...</AR-PACKAGE>
#     </AR-PACKAGES>
# </AUTOSAR>
```

**Note**: XML tag names are automatically generated from class names using `NameConverter.to_xml_tag()`. For example, `AdminData` becomes `ADMIN-DATA`, `AUTOSAR` stays as `AUTOSAR`.

## Circular Import Handling

For classes with circular dependencies, use string class names with `TYPE_CHECKING`:

```python
from __future__ import annotations  # Must be first import
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from armodel.models.M2.SomeModule import SomeClass

class MyClass(ARObject):
    related: Optional[SomeClass] = None  # Type hint works, no runtime import
```

The `ARObject.deserialize()` method handles this by:
1. First trying `get_type_hints()` for actual types
2. Falling back to `__annotations__` (strings) if that fails
3. Dynamically importing classes by name using `_import_class_by_name()`

## Edge Cases

### Python Keywords

XML attributes that are Python keywords get an underscore suffix:

```python
# XML: <ELEMENT class="some-class">
# Python:
self.class_: Optional[str] = None
```

### Private Attributes

Attributes starting with `_` are automatically skipped during serialization:

```python
class MyClass(ARObject):
    short_name: Optional[str] = None  # Serialized
    _internal_cache: dict = {}       # NOT serialized (private)
```

### None Values

`None` values are automatically skipped during serialization:

```python
class MyClass(ARObject):
    required: str = None          # Serialized if not None
    optional: Optional[str] = None  # Skipped if None

# Results in:
# <MY-CLASS>
#     <REQUIRED>value</REQUIRED>
#     <!-- OPTIONAL omitted because it's None -->
# </MY-CLASS>
```

## Development Guidelines

### When Creating New Model Classes

1. **Always inherit from `ARObject`**
2. **Use type hints** for all attributes
3. **Initialize attributes** with appropriate defaults (`None` for Optional, `[]` for lists)
4. **Only use decorators** when XML structure doesn't match default behavior
5. **Use property pattern** with `@xml_attribute` (getter/setter with private backing field)

### Example: Complete Class Definition

```python
from __future__ import annotations
from typing import TYPE_CHECKING, Optional
from armodel.serialization.decorators import xml_attribute
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_package import ARPackage

class ARPackage(ARObject):
    short_name: Optional[str] = None
    category: Optional[str] = None
    ar_packages: list[ARPackage] = []

    def __init__(self) -> None:
        self.short_name = None
        self.category = None
        self.ar_packages = []
        # XML tag name is auto-generated as AR-PACKAGE
```

### When to Use Decorators

| Scenario | Decorator | Example |
|----------|-----------|---------|
| XML attribute needed | `@xml_attribute` | `<ELEMENT uuid="abc">` |
| AUTOSAR atpVariation pattern | `@atp_variant()` | SwDataDefProps with VARIANTS/CONDITIONAL wrappers |
| Language-specific content | `@l_prefix("L-N")` | MultiLanguagePlainText with L-10 wrapper |

## Troubleshooting

### Issue: Attribute Not Serializing

**Symptom**: Expected XML element/attribute is missing

**Solutions**:
1. Check attribute is not private (doesn't start with `_`)
2. Check value is not `None`
3. Verify attribute is in `vars(self)`
4. Check if `@xml_attribute` decorator is applied correctly
5. For `ARPrimitive` objects with attributes: Verify they are wrapped with correct tag name in parent serialization

### Issue: Enum Values Not Uppercase

**Symptom**: Enum values are serialized as lowercase instead of uppercase

**Solutions**:
1. Verify enum class inherits from `AREnum`
2. Check that `ARPrimitive.serialize()` is using the uppercase conversion for enum attributes
3. Ensure enum values are defined with uppercase names (e.g., `CLOSED = "closed"`)
4. The serialization framework automatically converts enum values to uppercase in XML

### Issue: Wrong XML Tag Name

**Symptom**: XML tag doesn't match expected name

**Solutions**:
1. Verify `NameConverter.to_xml_tag()` output from class name
2. Check for private prefix (underscores stripped)
3. Ensure class name follows AUTOSAR naming conventions

### Issue: Deserialization Fails

**Symptom**: `deserialize()` raises exception or returns wrong values

**Solutions**:
1. Verify type hints are correct
2. Check for circular imports (use `TYPE_CHECKING`)
3. Ensure XML structure matches expected format
4. Check if `@xml_attribute` decorator is applied

### Issue: Circular Import Errors

**Symptom**: ImportError or circular reference errors

**Solutions**:
1. Add `from __future__ import annotations` at top of file
2. Use `TYPE_CHECKING` pattern for type hints
3. Ensure `get_type_hints()` fallback works in `ARObject.deserialize()`

## Testing

### Unit Testing Decorators

```python
def test_xml_attribute():
    obj = MyClass()
    obj.uuid = "abc-123"
    elem = obj.serialize("")

    assert elem.get("UUID") == "abc-123"
    assert elem.find("UUID") is None  # Not an element

def test_xml_tag():
    elem = MyCustomClass().serialize("")
    assert elem.tag == "CUSTOM-TAG"
```

### Integration Testing

```python
def test_round_trip():
    reader = ARXMLReader()
    autosar = reader.load_arxml('demos/arxml/AUTOSAR_Datatypes.arxml')

    writer = ARXMLWriter()
    writer.save_arxml(autosar, 'output.arxml')

    # Verify output matches input
    assert files_equal('demos/arxml/AUTOSAR_Datatypes.arxml', 'output.arxml')
```

## References

- **Base class implementation**: `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ArObject/ar_object.py`
- **Decorator implementations**: `src/armodel/serialization/decorators.py`
- **Name converter**: `src/armodel/serialization/name_converter.py`
- **Design document**: `docs/plans/2026-02-17-reflection-based-serialization-design.md`
- **Design rules**: `docs/designs/design_rules.md`
