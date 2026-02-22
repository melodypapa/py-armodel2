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
```

#### Implementation Details

1. **Decorator order**: `@xml_attribute` must come **before** `@property`
2. **Property pattern**: Requires property getter/setter pattern with private backing field
3. **Marker**: Sets `_is_xml_attribute = True` on the property's `fget` function

#### Example Output

```xml
<!-- With @xml_attribute decorator -->
<AUTOSAR SCHEMA-VERSION="4.5.0">
    <AR-PACKAGES>...</AR-PACKAGES>
</AUTOSAR>

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

### 3. `@l_prefix(xml_tag: str)`

Mark an attribute as using the **language-specific L-N** naming pattern for multilanguage text.

**When to use**:
- For MultiLanguage* classes where content is wrapped in language tags (e.g., L-1, L-2, L-4, L-5, L-10)
- Automatically applied by code generator based on JSON `kind: "l_prefix"` mapping

**Location**: `decorators.py:71-102`

#### Syntax

```python
from armodel.serialization.decorators import l_prefix

class MultiLanguagePlainText(ARObject):
    def __init__(self) -> None:
        self._l10: LPlainText = None

    @property
    @l_prefix("L-10")
    def l10(self) -> LPlainText:
        return self._l10

    @l10.setter
    def l10(self, value: LPlainText) -> None:
        self._l10 = value
```

#### Implementation Details

1. **Decorator order**: `@l_prefix("L-N")` must come **before** `@property`
2. **Parameter**: Accepts the exact XML tag name (e.g., "L-10", "L-4", "L-2")
3. **Markers**: Sets `_l_prefix = True` and `_l_prefix_tag = xml_tag` on the attribute
4. **Property pattern**: Requires property getter/setter with private backing field

#### Example Output

```xml
<L-10 L="EN">English text</L-10>
```

#### Language Tag Pattern

The l_prefix pattern is used for AUTOSAR multilanguage support:

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

### 5. `@xml_element_name(xml_tag: str)`

Specify a custom XML element name for attributes when the auto-generated name differs from the schema.

**When to use**:
- When the XML element name differs from the auto-generated name via NameConverter
- When AUTOSAR schema uses non-standard naming (e.g., "PROVIDED-ENTRYS" instead of "PROVIDED-CLIENT-SERVER-ENTRIES")

**Location**: `decorators.py:140-167`

#### Syntax

```python
from armodel.serialization.decorators import xml_element_name

class BswModuleDescription(ARElement):
    @xml_element_name("PROVIDED-ENTRYS")
    provided_client_server_entries: list[BswModuleClientServerEntry] = []

    @xml_element_name("REQUIRED-ENTRYS")
    required_client_server_entries: list[BswModuleClientServerEntry] = []
```

#### Implementation Details

1. **Attribute-level decorator**: Applied to individual attributes
2. **Parameter**: Accepts the exact XML element name (e.g., "PROVIDED-ENTRYS")
3. **Markers**: Sets `_xml_element_name = True` and `_xml_tag = xml_tag` on the attribute
4. **Overrides NameConverter**: The specified tag is used instead of auto-conversion

#### Example Output

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

#### When to Use

- AUTOSAR schema irregularities where element names don't follow standard conventions
- Legacy schema versions with non-standard naming
- Compatibility with existing ARXML files that use older naming

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
| `@xml_attribute` | `_is_xml_attribute` | `bool` |
| `@atp_variant()` | `_atp_variant` | `bool` |
| `@l_prefix(tag)` | `_l_prefix`, `_l_prefix_tag` | `bool`, `str` |
| `@language_abbr(attr)` | `_language_abbr`, `_xml_attr_name` | `bool`, `str` |
| `@xml_element_name(tag)` | `_xml_element_name`, `_xml_tag` | `bool`, `str` |

## Usage Guidelines

### When to Use Decorators

| Scenario | Decorator | Example |
|----------|-----------|---------|
| XML attribute needed | `@xml_attribute` | `<ELEMENT uuid="abc">` |
| AUTOSAR atpVariation pattern | `@atp_variant()` | SwDataDefProps with VARIANTS/CONDITIONAL wrappers |
| Language-specific content | `@l_prefix("L-N")` | MultiLanguagePlainText with L-10 wrapper |
| Language abbreviation attribute | `@language_abbr("L")` | LanguageSpecific with L attribute |
| Non-standard element name | `@xml_element_name("TAG")` | BswModuleDescription with PROVIDED-ENTRYS |

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


def test_l_prefix():
    """Test @l_prefix decorator."""
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
2. For `@l_prefix`: Verify the tag parameter matches XML (e.g., "L-10")
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