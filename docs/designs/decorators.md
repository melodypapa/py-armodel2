# XML Serialization Decorators

## Overview

Decorators in py-armodel2 provide a declarative way to handle edge cases in XML serialization that cannot be automatically handled by the reflection-based framework. They are used sparingly - only when the XML structure differs from the default behavior of the `ARObject.serialize()` and `ARObject.deserialize()` methods.

**Location**: `src/armodel/serialization/decorators.py`

**Key Principles**:
- **Minimal usage**: 95% of classes need no decorators
- **Declarative**: Decorators mark what needs special handling
- **Automatic**: The serialization framework automatically detects and processes decorators
- **Type-safe**: Decorators work seamlessly with type hints and reflection

## Available Decorators

### 1. `@xml_attribute`

Mark a property/attribute to be serialized as an **XML attribute** instead of a child element.

**When to use**:
- When the XML schema requires data as an attribute (e.g., `<AUTOSAR schema-version="4.5.0">`)
- For metadata like IDs, versions, UUIDs, etc.

**Location**: `decorators.py:9-30`

#### Syntax

```python
from armodel.serialization.decorators import xml_attribute

# Basic usage (auto-generated XML attribute name)
class AUTOSAR(ARObject):
    def __init__(self) -> None:
        self._schema_version: str = "4.5.0"

    @xml_attribute
    @property
    def schema_version(self) -> str:
        return self._schema_version

    @schema_version.setter
    def schema_version(self, value: str) -> None:
        self._schema_version = value

# With custom XML attribute name
class ARObject(ARObject):
    def __init__(self) -> None:
        self._timestamp: Optional[DateTime] = None

    @xml_attribute("T")
    @property
    def timestamp(self) -> Optional[DateTime]:
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value: Optional[DateTime]) -> None:
        self._timestamp = value
```

#### Implementation Details

1. **Decorator order**: `@xml_attribute` must come **before** `@property`
2. **Property pattern**: Requires property getter/setter pattern with private backing field
3. **Marker**: Sets `_is_xml_attribute = True` on the property's `fget` function
4. **Custom attribute name**: Optional parameter to specify a custom XML attribute name (e.g., `"T"` instead of auto-generated `"TIMESTAMP"`)
5. **Marker**: Sets `_xml_attr_name = <custom_name>` on the property's `fget` function when custom name is provided

#### Example Output

```xml
<!-- With @xml_attribute decorator (auto-generated name) -->
<AUTOSAR SCHEMA-VERSION="4.5.0">
    <AR-PACKAGES>...</AR-PACKAGES>
</AUTOSAR>

<!-- With @xml_attribute("T") decorator (custom name) -->
<AR-OBJECT T="2025-01-01T12:00:00">
    <CHECKSUM>abc123</CHECKSUM>
</AR-OBJECT>

<!-- Without decorator (would be) -->
<AUTOSAR>
    <SCHEMA-VERSION>4.5.0</SCHEMA-VERSION>
    <AR-PACKAGES>...</AR-PACKAGES>
</AUTOSAR>
```

#### Common Use Cases

- `schema_version` - AUTOSAR schema version
- `uuid` - Unique identifiers
- `id` - Element IDs
- `version` - Version attributes
- `L` - Language abbreviation (use `@language_abbr` instead for exact control)

---

### 2. `@atp_variant()`

Mark a class as using the AUTOSAR **atpVariation** pattern, which wraps all class attributes in nested XML elements.

**When to use**:
- When AUTOSAR schema defines elements with `<CLASS-TAG>-VARIANTS/<CLASS-TAG>-CONDITIONAL` wrapper structure
- Automatically applied by code generator based on JSON mapping data

**Location**: `decorators.py:33-68`

#### Syntax

```python
from armodel.serialization.decorators import atp_variant

@atp_variant()
class SwDataDefProps(ARObject):
    base_type_ref: Optional[ARRef] = None
    sw_calibration_access: Optional[SwCalibrationAccessEnum] = None
```

#### Implementation Details

1. **Class-level decorator**: Applied to the class, not individual attributes
2. **Wrapper path**: Automatically derived from class name:
   - First level: `<CLASS-TAG>-VARIANTS`
   - Second level: `<CLASS-TAG>-CONDITIONAL`
3. **Marker**: Sets `_atp_variant = True` on the class
4. **Automatic handling**: ARObject serialization framework creates/navigates wrappers automatically

#### Example Output

```xml
<SW-DATA-DEF-PROPS>
  <SW-DATA-DEF-PROPS-VARIANTS>
    <SW-DATA-DEF-PROPS-CONDITIONAL>
      <BASE-TYPE-REF>...</BASE-TYPE-REF>
      <SW-CALIBRATION-ACCESS>...</SW-CALIBRATION-ACCESS>
    </SW-DATA-DEF-PROPS-CONDITIONAL>
  </SW-DATA-DEF-PROPS-VARIANTS>
</SW-DATA-DEF-PROPS>
```

#### AUTOSAR atpVariation Pattern

The atpVariation pattern is used in AUTOSAR schemas to support conditional variants:

```
<Class-Tag>
  <Class-Tag-VARIANTS>
    <Class-Tag-CONDITIONAL>
      <!-- All class attributes go here -->
    </Class-Tag-CONDITIONAL>
  </Class-Tag-VARIANTS>
</Class-Tag>
```

---

### 3. `@lang_prefix(xml_tag: str)`

Mark an attribute as using the **language-specific L-N** naming pattern for multilanguage text.

**When to use**:
- For MultiLanguage* classes where content is wrapped in language tags (e.g., L-1, L-2, L-4, L-5, L-10)
- Automatically applied by code generator based on JSON `decorator: "lang_prefix:L-N"` mapping

**Location**: `decorators.py:71-102`

#### Syntax

```python
from armodel.serialization.decorators import lang_prefix

class MultiLanguagePlainText(ARObject):
    def __init__(self) -> None:
        self._l10: LPlainText = None

    @property
    @lang_prefix("L-10")
    def l10(self) -> LPlainText:
        return self._l10

    @l10.setter
    def l10(self, value: LPlainText) -> None:
        self._l10 = value
```

#### Implementation Details

1. **Decorator order**: `@lang_prefix("L-N")` must come **before** `@property`
2. **Parameter**: Accepts the exact XML tag name (e.g., "L-10", "L-4", "L-2")
3. **Markers**: Sets `_lang_prefix = True` and `_lang_prefix_tag = xml_tag` on the attribute
4. **Property pattern**: Requires property getter/setter with private backing field

#### Example Output

```xml
<L-10 L="EN">English text</L-10>
```

#### Language Tag Pattern

The lang_prefix pattern is used for AUTOSAR multilanguage support:

```
<L-1 L="EN">English text</L-1>
<L-2 L="DE">German text</L-2>
<L-4 L="FR">French text</L-4>
<L-5 L="ES">Spanish text</L-5>
<L-10 L="EN">Long English text</L-10>
```

---

### 4. `@language_abbr(xml_attr_name: str)`

Mark an attribute as a language abbreviation XML attribute with exact control over the attribute name.

**When to use**:
- For LanguageSpecific series classes where the language abbreviation attribute (typically 'l') should be serialized as an XML attribute
- When you need exact control over the XML attribute name (not auto-converted by NameConverter)

**Location**: `decorators.py:105-137`

#### Syntax

```python
from armodel.serialization.decorators import language_abbr

class LanguageSpecific(ARObject):
    def __init__(self) -> None:
        self._l: LEnum = LEnum.EN

    @language_abbr("L")
    @property
    def l(self) -> LEnum:
        return self._l

    @l.setter
    def l(self, value: LEnum) -> None:
        self._l = value
```

#### Implementation Details

1. **Decorator order**: `@language_abbr("L")` must come **before** `@property`
2. **Parameter**: Accepts the exact XML attribute name (e.g., "L")
3. **Markers**: Sets `_language_abbr = True` and `_xml_attr_name = xml_attr_name` on the attribute
4. **Property pattern**: Requires property getter/setter with private backing field

#### Difference from @xml_attribute

| Decorator | Name Conversion | Use Case |
|-----------|----------------|----------|
| `@xml_attribute` | Auto-converted via NameConverter | General XML attributes |
| `@language_abbr` | Exact attribute name specified | Language abbreviation attributes |

#### Example Output

```xml
<L-LONG-NAME L="EN">Long Name</L-LONG-NAME>
```

---

### 5. `@ref_conditional(xml_tag: str)`

Mark an attribute as using the AUTOSAR **-REF-CONDITIONAL** pattern for reference lists in atpVariation scenarios.

**When to use**:
- For reference lists that use the atpVariation pattern with -REF-CONDITIONAL wrappers
- When AUTOSAR schema defines references wrapped in `<TAG>-REF-CONDITIONAL/<TAG>-REF` structure
- Common in FIBEX-related elements (e.g., System.fibexElements, PhysicalChannel.comm_connector_refs)

**Location**: `decorators.py:140-178`

#### Syntax

```python
from armodel.serialization.decorators import ref_conditional

class System(ARElement):
    def __init__(self) -> None:
        self._fibex_element_refs: list[ARRef] = []

    @property
    @ref_conditional("FIBEX-ELEMENTS")
    def fibex_element_refs(self) -> list[ARRef]:
        """Get fibex_element_refs with ref_conditional wrapper."""
        return self._fibex_element_refs

    @fibex_element_refs.setter
    def fibex_element_refs(self, value: list[ARRef]) -> None:
        """Set fibex_element_refs with ref_conditional wrapper."""
        self._fibex_element_refs = value
```

#### JSON Configuration

The `@ref_conditional` decorator is configured via JSON mapping data in the class definition:

```json
{
  "name": "System",
  "attributes": {
    "fibexElements": {
      "type": "FibexElement",
      "multiplicity": "*",
      "kind": "ref",
      "is_ref": true,
      "decorator": "ref_conditional:FIBEX-ELEMENTS"
    }
  }
}
```

**JSON decorator format**: `"decorator_name:decorator_params"`

- **decorator_name**: The decorator function name (e.g., `ref_conditional`)
- **decorator_params**: Parameters passed to the decorator (e.g., `FIBEX-ELEMENTS`)

#### Implementation Details

1. **Decorator order**: `@ref_conditional("TAG")` must come **before** `@property`
2. **Parameter**: Accepts the container element name (e.g., "FIBEX-ELEMENTS")
3. **Markers**: Sets `_is_ref_conditional = True` and `_xml_tag = xml_tag` on the attribute
4. **Property pattern**: Requires property getter/setter with private backing field
5. **Automatic code generation**: The decorator is processed by the code generator to generate correct serialize/deserialize methods

#### XML Structure

The -REF-CONDITIONAL pattern creates a three-level nesting:

```
<CONTAINER-TAG>
  <SINGULAR-TAG>-REF-CONDITIONAL>
    <SINGULAR-TAG>-REF DEST="...">...</SINGULAR-TAG-REF>
  </SINGULAR-TAG>-REF-CONDITIONAL>
</CONTAINER-TAG>
```

Where:
- **CONTAINER-TAG**: The plural container name (e.g., "FIBEX-ELEMENTS")
- **SINGULAR-TAG**: The singular form minus trailing "S" (e.g., "FIBEX-ELEMENT")
- **-REF-CONDITIONAL**: The atpVariation wrapper
- **-REF**: The actual reference element with DEST attribute

#### Example Output

```xml
<FIBEX-ELEMENTS>
  <FIBEX-ELEMENT-REF-CONDITIONAL>
    <FIBEX-ELEMENT-REF DEST="CAN-CLUSTER">/CanSystem/CLUSTERS/CanNetwork</FIBEX-ELEMENT-REF>
  </FIBEX-ELEMENT-REF-CONDITIONAL>
  <FIBEX-ELEMENT-REF-CONDITIONAL>
    <FIBEX-ELEMENT-REF DEST="I-SIGNAL">/CanSystem/ISIGNALS/CounterIn</FIBEX-ELEMENT-REF>
  </FIBEX-ELEMENT-REF-CONDITIONAL>
  <FIBEX-ELEMENT-REF-CONDITIONAL>
    <FIBEX-ELEMENT-REF DEST="ECU-INSTANCE">/CanSystem/ECUINSTANCES/DebugNode</FIBEX-ELEMENT-REF>
  </FIBEX-ELEMENT-REF-CONDITIONAL>
</FIBEX-ELEMENTS>
```

#### Difference from Standard Reference Lists

| Pattern | Container | Child Wrapper | Reference |
|---------|-----------|---------------|-----------|
| Standard (no decorator) | `<TAG>-REFS` | None | `<TAG>-REF` |
| ref_conditional | `<TAG>S` | `<TAG>-REF-CONDITIONAL` | `<TAG>-REF` |

#### Common Use Cases

- **System.fibexElements**: References to FIBEX topology elements
- **PhysicalChannel.comm_connector_refs**: CAN communication connectors
- **EcuInstance.managed_refs**: Managed references in ECU instances

---

### 6. `@xml_element_name(xml_tag: str)`

Specify a custom XML element name for attributes when the auto-generated name differs from the schema, or when multi-level nesting is required.

**When to use**:
- When the XML element name differs from the auto-generated name via NameConverter
- When AUTOSAR schema uses non-standard naming (e.g., "PROVIDED-ENTRYS" instead of "PROVIDED-CLIENT-SERVER-ENTRIES")
- When multi-level nesting is required (nested container elements)
- When reference lists need custom wrapper elements

**Location**: `decorators.py:140-167`

#### Syntax

**Single parameter** (override container tag):
```python
from armodel.serialization.decorators import xml_element_name

class BswModuleDescription(ARElement):
    @xml_element_name("PROVIDED-ENTRYS")
    provided_client_server_entries: list[BswModuleClientServerEntry] = []

    @xml_element_name("REQUIRED-ENTRYS")
    required_client_server_entries: list[BswModuleClientServerEntry] = []
```

**Multi-level path** (nested containers):
```python
from armodel.serialization.decorators import xml_element_name

class ExecutableEntity(ARObject):
    _can_enter_refs: list[ARRef] = []
    
    @property
    @xml_element_name("CAN-ENTER-EXCLUSIVE-AREA-REFS/CAN-ENTER-EXCLUSIVE-AREA/CAN-ENTER-EXCLUSIVE-AREA-REF")
    def can_enter_refs(self) -> list[ARRef]:
        """Get can_enter_refs with custom XML element name."""
        return self._can_enter_refs
    
    @can_enter_refs.setter
    def can_enter_refs(self, value: list[ARRef]) -> None:
        """Set can_enter_refs with custom XML element name."""
        self._can_enter_refs = value
```

#### Implementation Details

1. **Attribute-level decorator**: Applied to individual attributes
2. **Parameter formats**:
   - **Single parameter**: Accepts the exact XML element name (e.g., "PROVIDED-ENTRYS")
   - **Multi-level path**: Accepts nested container path separated by `/` (e.g., "TAG1/TAG2/TAG3")
3. **Markers**: Sets `_xml_element_name = True` and `_xml_tag = xml_tag` on the attribute
4. **Overrides NameConverter**: The specified tag(s) are used instead of auto-conversion
5. **Multi-level nesting**: When `/` separator is used, the code generator:
   - Creates nested wrapper elements during serialization
   - Navigates through nested containers during deserialization
   - Uses the last level tag for individual child elements

#### Example Output

**Single parameter** (override container tag):
```xml
<!-- With @xml_element_name("PROVIDED-ENTRYS") -->
<BSW-MODULE-DESCRIPTION>
  <SHORT-NAME>MyModule</SHORT-NAME>
  <PROVIDED-ENTRYS>
    <BSW-MODULE-CLIENT-SERVER-ENTRY>...</BSW-MODULE-CLIENT-SERVER-ENTRY>
  </PROVIDED-ENTRYS>
</BSW-MODULE-DESCRIPTION>

<!-- Without decorator (would be) -->
<BSW-MODULE-DESCRIPTION>
  <SHORT-NAME>MyModule</SHORT-NAME>
  <PROVIDED-CLIENT-SERVER-ENTRYS>
    <BSW-MODULE-CLIENT-SERVER-ENTRY>...</BSW-MODULE-CLIENT-SERVER-ENTRY>
  </PROVIDED-CLIENT-SERVER-ENTRYS>
</BSW-MODULE-DESCRIPTION>
```

**Multi-level path** (nested containers):
```xml
<!-- With @xml_element_name("CAN-ENTER-EXCLUSIVE-AREA-REFS/CAN-ENTER-EXCLUSIVE-AREA/CAN-ENTER-EXCLUSIVE-AREA-REF") -->
<EXECUTABLE-ENTITY>
  <SHORT-NAME>MyEntity</SHORT-NAME>
  <CAN-ENTER-EXCLUSIVE-AREA-REFS>
    <CAN-ENTER-EXCLUSIVE-AREA>
      <CAN-ENTER-EXCLUSIVE-AREA-REF DEST="EXCLUSIVE-AREA">/AUTOSAR/EcucDefs/MyExclusiveArea</CAN-ENTER-EXCLUSIVE-AREA-REF>
    </CAN-ENTER-EXCLUSIVE-AREA>
  </CAN-ENTER-EXCLUSIVE-AREA-REFS>
</EXECUTABLE-ENTITY>
```

#### When to Use

- AUTOSAR schema irregularities where element names don't follow standard conventions
- Legacy schema versions with non-standard naming
- Compatibility with existing ARXML files that use older naming

## JSON Configuration for Decorators

Decorators can be configured via JSON mapping data in the AUTOSAR class definitions. This allows the code generator to automatically generate the correct decorator usage.

### JSON Decorator Format

```json
{
  "name": "ClassName",
  "attributes": {
    "attributeName": {
      "type": "SomeType",
      "multiplicity": "*",
      "kind": "ref",
      "is_ref": true,
      "decorator": "decorator_name:decorator_params"
    }
  }
}
```

**Format**: `"decorator_name:decorator_params"`

- **decorator_name**: The decorator function name (e.g., `xml_element_name`, `ref_conditional`, `lang_prefix`)
- **decorator_params**: Parameters passed to the decorator (e.g., `FIBEX-ELEMENTS`, `L-10`)

### Decorator Types in JSON

| Decorator | JSON Example | When to Use |
|-----------|--------------|-------------|
| `xml_element_name` | `"decorator": "xml_element_name:PROVIDED-ENTRYS"` | Custom element name |
| `xml_element_name` | `"decorator": "xml_element_name:TAG1/TAG2/TAG3"` | Multi-level nesting |
| `ref_conditional` | `"decorator": "ref_conditional:FIBEX-ELEMENTS"` | -REF-CONDITIONAL pattern |
| `lang_prefix` | `"decorator": "lang_prefix:L-10"` | Language-specific content |
| `language_abbr` | `"kind": "language_abbr"` | Language abbreviation attribute |
| `xml_attribute` | `"decorator": "xml_attribute"` | XML attribute (auto-generated name) |
| `xml_attribute` | `"decorator": "xml_attribute:T"` | XML attribute (custom name) |

### Special Cases

**Attribute-level decorators** (ref_conditional, xml_element_name, xml_attribute, lang_prefix):
- Use the `decorator` field with format `"name:params"`
- The code generator applies the decorator to the generated property
- For xml_attribute and lang_prefix, params are required (e.g., "xml_attribute:T", "lang_prefix:L-10")

**Kind-based decorators** (language_abbr):
- Use the `kind` field instead of `decorator`
- The code generator automatically applies the appropriate decorator

### Example JSON Configurations

#### ref_conditional for FIBEX-ELEMENTS

```json
{
  "name": "System",
  "attributes": {
    "fibexElements": {
      "type": "FibexElement",
      "multiplicity": "*",
      "kind": "ref",
      "is_ref": true,
      "decorator": "ref_conditional:FIBEX-ELEMENTS",
      "note": "Reference to ASAM FIBEX elements specifying Topology. Elements used within a System Description shall from the System Element. order to describe a product-line, all Fibex be optional. atpVariation"
    }
  }
}
```

#### xml_element_name for multi-level nesting

```json
{
  "name": "ExecutableEntity",
  "attributes": {
    "canEnterRefs": {
      "type": "ARRef",
      "multiplicity": "*",
      "kind": "ref",
      "is_ref": true,
      "decorator": "xml_element_name:CAN-ENTER-EXCLUSIVE-AREA-REFS/CAN-ENTER-EXCLUSIVE-AREA/CAN-ENTER-EXCLUSIVE-AREA-REF"
    }
  }
}
```

#### xml_element_name for custom container name

```json
{
  "name": "BswModuleDescription",
  "attributes": {
    "providedClientServerEntries": {
      "type": "BswModuleClientServerEntry",
      "multiplicity": "*",
      "kind": "aggr",
      "is_ref": false,
      "decorator": "xml_element_name:PROVIDED-ENTRYS"
    }
  }
}
```

#### xml_attribute with custom name

```json
{
  "name": "ARObject",
  "attributes": {
    "timestamp": {
      "type": "DateTime",
      "multiplicity": "0..1",
      "kind": "aggr",
      "decorator": "xml_attribute:T",
      "is_ref": false,
      "note": "Timestamp calculated by the user's tool environment"
    }
  }
}
```

#### lang_prefix for language-specific content

```json
{
  "name": "MultiLanguageParagraph",
  "attributes": {
    "l1": {
      "type": "LParagraph",
      "multiplicity": "*",
      "kind": "aggr",
      "decorator": "lang_prefix:L-1",
      "is_ref": false,
      "note": "Language-specific paragraphs"
    }
  }
}
```

#### xml_attribute without parameter (auto-generated name)

```json
{
  "name": "AUTOSAR",
  "attributes": {
    "schemaVersion": {
      "type": "String",
      "multiplicity": "1",
      "kind": "aggr",
      "decorator": "xml_attribute",
      "is_ref": false,
      "note": "AUTOSAR schema version"
    }
  }
}
```

#### kind-based decorators

```json
{
  "name": "AUTOSAR",
  "attributes": {
    "schemaVersion": {
      "type": "String",
      "multiplicity": "1",
      "kind": "xml_attribute",
      "is_ref": false
    }
  }
}
```

### Code Generator Processing

The code generator processes decorator configurations in multiple stages:

1. **Parse decorator field**: Extract decorator name and parameters
2. **Generate import statements**: Add decorator imports to generated class
3. **Generate properties**: Create property with decorator applied
4. **Generate serialize methods**: Use decorator metadata for correct serialization
5. **Generate deserialize methods**: Use decorator metadata for correct deserialization

### Generated Code Example

Given this JSON configuration:

```json
{
  "decorator": "ref_conditional:FIBEX-ELEMENTS"
}
```

The code generator generates:

```python
from armodel.serialization.decorators import ref_conditional

class System(ARElement):
    def __init__(self) -> None:
        self._fibex_element_refs: list[ARRef] = []

    @property
    @ref_conditional("FIBEX-ELEMENTS")
    def fibex_element_refs(self) -> list[ARRef]:
        """Get fibex_element_refs with ref_conditional wrapper."""
        return self._fibex_element_refs

    @fibex_element_refs.setter
    def fibex_element_refs(self, value: list[ARRef]) -> None:
        """Set fibex_element_refs with ref_conditional wrapper."""
        self._fibex_element_refs = value

    def serialize(self) -> ET.Element:
        """Serialize System to XML element."""
        # ... serialize code that uses FIBEX-ELEMENTS container
        # and wraps each ref in FIBEX-ELEMENT-REF-CONDITIONAL

    @classmethod
    def deserialize(cls, element: ET.Element) -> "System":
        """Deserialize XML element to System object."""
        # ... deserialize code that unwraps FIBEX-ELEMENT-REF-CONDITIONAL
```

## Decorator Detection and Processing

### How ARObject Detects Decorators

The serialization framework automatically detects decorators through marker attributes:

```python
# In ARObject.serialize()
def serialize(self, namespace: str = "") -> ET.Element:
    for attr_name, attr_value in vars(self).items():
        if attr_name.startswith('_'):
            continue  # Skip private attributes

        # Get the actual attribute (handle private backing fields)
        actual_attr = getattr(self.__class__, attr_name, None)

        # Check for @xml_attribute decorator
        if hasattr(actual_attr, '_is_xml_attribute'):
            elem.set(xml_tag, str(attr_value))
        else:
            # Serialize as child element
            child_elem = attr_value.serialize(namespace)
            elem.append(child_elem)
```

```python
# In ARObject.deserialize()
@classmethod
def deserialize(cls, element: ET.Element) -> ARObject:
    for attr_name, type_hint in get_type_hints(cls).items():
        # Handle private backing fields (_l1 -> l1)
        public_attr_name = attr_name[1:] if attr_name.startswith('_') else attr_name

        # Get the actual attribute (handle properties)
        actual_attr = getattr(cls, public_attr_name, None)

        # Check for @xml_attribute decorator
        if hasattr(actual_attr, '_is_xml_attribute'):
            value = element.get(xml_tag)
        else:
            # Find child element
            child = element.find(xml_tag)
            value = deserialize_child(child, type_hint)

        setattr(obj, attr_name, value)
```

### Marker Attributes

Each decorator sets specific marker attributes that the serialization framework checks:

| Decorator | Marker Attributes | Type |
|-----------|-------------------|------|
| `@xml_attribute` | `_is_xml_attribute`, `_xml_attr_name` | `bool`, `str` |
| `@atp_variant()` | `_atp_variant` | `bool` |
| `@lang_prefix(tag)` | `_lang_prefix`, `_lang_prefix_tag` | `bool`, `str` |
| `@language_abbr(attr)` | `_language_abbr`, `_xml_attr_name` | `bool`, `str` |
| `@xml_element_name(tag)` | `_xml_element_name`, `_xml_tag` | `bool`, `str` |
| `@ref_conditional(tag)` | `_is_ref_conditional`, `_xml_tag` | `bool`, `str` |

## Usage Guidelines

### When to Use Decorators

| Scenario | Decorator | Example |
|----------|-----------|---------|
| XML attribute needed | `@xml_attribute` | `<ELEMENT uuid="abc">` |
| AUTOSAR atpVariation pattern (class-level) | `@atp_variant()` | SwDataDefProps with VARIANTS/CONDITIONAL wrappers |
| AUTOSAR atpVariation pattern (reference lists) | `@ref_conditional("TAG")` | System.fibexElements with -REF-CONDITIONAL wrappers |
| Language-specific content | `@lang_prefix("L-N")` | MultiLanguagePlainText with L-10 wrapper |
| Language abbreviation attribute | `@language_abbr("L")` | LanguageSpecific with L attribute |
| Non-standard element name | `@xml_element_name("TAG")` | BswModuleDescription with PROVIDED-ENTRYS |
| Multi-level nesting | `@xml_element_name("TAG1/TAG2/TAG3")` | ExecutableEntity with nested containers |

### When NOT to Use Decorators

1. **Simple attributes**: Use default reflection-based serialization
2. **List attributes**: Automatically wrapped in plural element names
3. **Optional attributes**: Automatically skipped if `None`
4. **Nested objects**: Automatically recursively serialized
5. **Primitive types**: Automatically converted to text content

### Decorator Order

For property-based decorators, the order is critical:

```python
# CORRECT order
@xml_attribute  # 1. Mark as XML attribute
@property       # 2. Define as property
def schema_version(self) -> str:
    return self._schema_version

# WRONG order (will not work)
@property       # 1. Define as property
@xml_attribute  # 2. Mark as XML attribute (too late)
def schema_version(self) -> str:
    return self._schema_version
```

### Property Pattern

Property-based decorators require the full property pattern:

```python
class MyClass(ARObject):
    def __init__(self) -> None:
        self._uuid: str = ""  # Private backing field

    @xml_attribute
    @property
    def uuid(self) -> str:
        return self._uuid

    @uuid.setter
    def uuid(self, value: str) -> None:
        self._uuid = value
```

## Testing Decorators

### Unit Testing

```python
def test_xml_attribute():
    """Test @xml_attribute decorator."""
    obj = AUTOSAR()
    obj.schema_version = "4.5.0"
    elem = obj.serialize("")

    # Verify attribute is set (not an element)
    assert elem.get("SCHEMA-VERSION") == "4.5.0"
    assert elem.find("SCHEMA-VERSION") is None


def test_atp_variant():
    """Test @atp_variant decorator."""
    obj = SwDataDefProps()
    obj.base_type_ref = ARRef("...")
    elem = obj.serialize("")

    # Verify wrapper structure
    assert elem.tag == "SW-DATA-DEF-PROPS"
    variants = elem.find("SW-DATA-DEF-PROPS-VARIANTS")
    assert variants is not None
    conditional = variants.find("SW-DATA-DEF-PROPS-CONDITIONAL")
    assert conditional is not None


def test_lang_prefix():
    """Test @lang_prefix decorator."""
    obj = MultiLanguagePlainText()
    l10 = LPlainText()
    l10.value = "English text"
    obj.l10 = l10
    elem = obj.serialize("")

    # Verify language-specific wrapper
    l10_elem = elem.find("L-10")
    assert l10_elem is not None
    assert l10_elem.get("L") == "EN"


def test_language_abbr():
    """Test @language_abbr decorator."""
    obj = LanguageSpecific()
    obj.l = LEnum.EN
    elem = obj.serialize("")

    # Verify language abbreviation attribute
    assert elem.get("L") == "EN"


def test_xml_element_name():
    """Test @xml_element_name decorator."""
    obj = BswModuleDescription()
    entry = BswModuleClientServerEntry()
    entry.short_name = "MyEntry"
    obj.provided_client_server_entries = [entry]
    elem = obj.serialize("")

    # Verify custom element name
    provided = elem.find("PROVIDED-ENTRYS")
    assert provided is not None
    # Verify it's NOT the auto-generated name
    assert elem.find("PROVIDED-CLIENT-SERVER-ENTRYS") is None
```

## Troubleshooting

### Issue: Decorator Not Working

**Symptoms**: Decorator is ignored, default behavior occurs

**Solutions**:
1. Check decorator order: `@decorator` must come **before** `@property`
2. Verify property pattern: Must have both getter and setter
3. Check private backing field: Use underscore-prefixed private field
4. Verify import: Import from `armodel.serialization.decorators`

### Issue: Wrong XML Tag Name

**Symptoms**: XML tag doesn't match expected name

**Solutions**:
1. For `@xml_attribute`: Check that attribute name is correct in XML
2. For `@lang_prefix`: Verify the tag parameter matches XML (e.g., "L-10")
3. For `@language_abbr`: Verify the attr parameter matches XML (e.g., "L")
4. For `@xml_element_name`: Verify the tag parameter matches XML exactly

### Issue: Attribute Not Serializing

**Symptoms**: Expected XML element/attribute is missing

**Solutions**:
1. Check attribute is not private (doesn't start with `_`)
2. Check value is not `None`
3. Verify decorator is applied correctly
4. Check for typos in decorator parameters

## References

- **Implementation**: `src/armodel/serialization/decorators.py`
- **Base class**: `src/armodel/models/M2/.../ArObject/ar_object.py`
- **Serialization framework**: `docs/designs/serialization.md`
- **Design rules**: `docs/designs/design_rules.md`
- **Model design**: `docs/designs/model_design.md`