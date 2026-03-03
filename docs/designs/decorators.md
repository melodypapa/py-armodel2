# XML Serialization Decorators

## Overview

Decorators in py-armodel2 provide a declarative way to handle edge cases in XML serialization that cannot be automatically handled by the reflection-based framework. They are used sparingly - only when the XML structure differs from the default behavior of the `ARObject.serialize()` and `ARObject.deserialize()` methods.

**Location**: `src/armodel2/serialization/decorators.py`

**Key Principles**:
- **Minimal usage**: 95% of classes need no decorators
- **Declarative**: Decorators mark what needs special handling
- **Automatic**: The serialization framework automatically detects and processes decorators
- **Type-safe**: Decorators work seamlessly with type hints and reflection

## Available Decorators

| Decorator | Purpose | Type | JSON Configuration |
|-----------|---------|------|-------------------|
| `@xml_attribute` | Mark property as XML attribute instead of element | Attribute-level | `"decorator": "xml_attribute"` or `"decorator": "xml_attribute:T"` |
| `@atp_variant()` | Mark class as using atpVariation pattern (nested wrappers) | Class-level | `"atp_type": "atpVariation"` |
| `@atp_mixed()` | Mark class as mixed content container (no wrapping) | Class-level | `"atp_type": "atpMixed"` |
| `@lang_prefix("L-N")` | Mark attribute as using language-specific L-N pattern | Attribute-level | `"decorator": "lang_prefix:L-N"` |
| `@lang_abbr("L")` | Mark attribute as language abbreviation XML attribute | Attribute-level | `"decorator": "lang_abbr:L"` |
| `@xml_element_name("TAG")` | Specify custom XML element name for attributes | Attribute-level | `"decorator": "xml_element_name:TAG"` or `"decorator": "xml_element_name:TAG1/TAG2/TAG3"` |
| `@ref_conditional("TAG")` | Mark attribute as using -REF-CONDITIONAL pattern | Attribute-level | `"decorator": "ref_conditional:TAG"` |
| `@instance_ref(flatten, list_type)` | Mark attribute as instance reference with flattening control | Attribute-level | `"decorator": "instance_ref:flatten=True,list_type=single"` |
| `@polymorphic({...})` | Mark attribute as polymorphic with wrapper-to-type mapping | Attribute-level | `"decorator": "polymorphic:TAG=BaseType"` |

---

## 1. `@xml_attribute`

Mark a property/attribute to be serialized as an **XML attribute** instead of a child element.

### Description

By default, all attributes are serialized as child elements. The `@xml_attribute` decorator changes this behavior to serialize the attribute as an XML attribute on the parent element.

### JSON Configuration

```json
{
  "name": "AUTOSAR",
  "attributes": {
    "schemaVersion": {
      "type": "String",
      "multiplicity": "1",
      "kind": "xml_attribute",
      "is_ref": false,
      "decorator": "xml_attribute",
      "note": "AUTOSAR schema version"
    }
  }
}
```

**JSON decorator format**:
- `"decorator": "xml_attribute"` - Auto-generates XML attribute name from property name
- `"decorator": "xml_attribute:T"` - Uses custom XML attribute name (e.g., "T")

### Usage

```python
from armodel2.serialization.decorators import xml_attribute

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

### Generated XML Structure

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

### Common Use Cases

- `schema_version` - AUTOSAR schema version attribute
- `uuid` - Unique identifiers
- `id` - Element IDs
- `version` - Version attributes
- `timestamp` - Timestamp with custom "T" attribute name

---

## 2. `@atp_variant()`

Mark a class as using the AUTOSAR **atpVariation** pattern, which wraps all class attributes in nested XML elements.

### Description

The atpVariation pattern is used in AUTOSAR schemas to support conditional variants. All attributes of a class marked with `@atp_variant()` are wrapped in a two-level nested structure: `<CLASS-TAG>-VARIANTS/<CLASS-TAG>-CONDITIONAL`.

### JSON Configuration

```json
{
  "name": "SwDataDefProps",
  "maturity": "draft",
  "package": "M2::AUTOSARTemplates::MSR::DataDictionary",
  "is_abstract": false,
  "atp_type": "atpVariation",
  "attributes": {
    "baseType": {
      "type": "DataTypeReference",
      "multiplicity": "0..1",
      "kind": "ref",
      "is_ref": true
    },
    "swCalibrationAccess": {
      "type": "SwCalibrationAccessEnum",
      "multiplicity": "0..1",
      "kind": "attribute",
      "is_ref": false
    }
  }
}
```

**Note**: The `@atp_variant()` decorator is applied by the code generator when `"atp_type": "atpVariation"` is present in the JSON class definition. It is not configured via the `decorator` field.

### Usage

```python
from armodel2.serialization.decorators import atp_variant

@atp_variant()
class SwDataDefProps(ARObject):
    base_type_ref: Optional[ARRef] = None
    sw_calibration_access: Optional[SwCalibrationAccessEnum] = None
```

### Generated XML Structure

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

### AUTOSAR atpVariation Pattern Structure

```
<Class-Tag>
  <Class-Tag-VARIANTS>
    <Class-Tag-CONDITIONAL>
      <!-- All class attributes go here -->
    </Class-Tag-CONDITIONAL>
  </Class-Tag-VARIANTS>
</Class-Tag>
```

### Common Use Cases

- `SwDataDefProps` - Data definition properties with variant support
- `J1939Cluster` - J1939 CAN cluster with conditional variants
- `AbstractCanCluster` - Abstract CAN cluster base class

---

## 3. `@atp_mixed()`

Mark a class as using the AUTOSAR **atpMixed** pattern, which allows mixed content without wrapper elements.

### Description

The atpMixed pattern is used for container classes that can hold multiple different child types. Unlike atpVariation, children are serialized directly without any wrapper elements.

### JSON Configuration

```json
{
  "name": "SwRecordLayoutGroupContent",
  "maturity": "draft",
  "package": "M2::AUTOSARTemplates::MSR::DataDictionary::RecordLayout",
  "is_abstract": false,
  "atp_type": "atpMixed",
  "attributes": {
    "swRecordLayoutRef": {
      "type": "SwRecordLayout",
      "multiplicity": "0..1",
      "kind": "ref",
      "is_ref": true
    },
    "swRecordLayoutGroup": {
      "type": "SwRecordLayoutGroup",
      "multiplicity": "0..1",
      "kind": "aggr",
      "is_ref": false
    },
    "swRecordLayoutV": {
      "type": "SwRecordLayoutV",
      "multiplicity": "0..1",
      "kind": "aggr",
      "is_ref": false
    }
  }
}
```

**Note**: The `@atp_mixed()` decorator is applied by the code generator when `"atp_type": "atpMixed"` is present in the JSON class definition. It is not configured via the `decorator` field.

### Usage

```python
from armodel2.serialization.decorators import atp_mixed

@atp_mixed()
class SwRecordLayoutGroupContent(ARObject):
    sw_record_layout_ref: Optional[ARRef] = None
    sw_record_layout_group: Optional[SwRecordLayoutGroup] = None
    sw_record_layout_v: Optional[SwRecordLayoutV] = None
```

### Generated XML Structure

```xml
<SW-RECORD-LAYOUT-GROUP-CONTENT>
  <SW-RECORD-LAYOUT-REF DEST="SW-RECORD-LAYOUT">/path/to/layout</SW-RECORD-LAYOUT-REF>
  <SW-RECORD-LAYOUT-GROUP>...</SW-RECORD-LAYOUT-GROUP>
  <SW-RECORD-LAYOUT-V>...</SW-RECORD-LAYOUT-V>
</SW-RECORD-LAYOUT-GROUP-CONTENT>
```

### Common Use Cases

- `SwRecordLayoutGroupContent` - Mixed content container for record layout elements
- Container classes that hold heterogeneous child elements

---

## 4. `@lang_prefix(xml_tag: str)`

Mark an attribute as using the **language-specific L-N** naming pattern for multilanguage text.

### Description

The lang_prefix pattern wraps child elements in language-specific XML tags (L-1, L-2, L-4, L-5, L-10, etc.). This is used for MultiLanguage* classes where content needs to be provided in multiple languages.

### JSON Configuration

```json
{
  "name": "MultiLanguagePlainText",
  "maturity": "draft",
  "package": "M2::MSR::Documentation::TextModel::MultilanguageData",
  "is_abstract": false,
  "attributes": {
    "l10": {
      "type": "LPlainText",
      "multiplicity": "*",
      "kind": "aggr",
      "is_ref": false,
      "decorator": "lang_prefix:L-10",
      "note": "Language-specific plain text content"
    },
    "l4": {
      "type": "LParagraph",
      "multiplicity": "*",
      "kind": "aggr",
      "is_ref": false,
      "decorator": "lang_prefix:L-4",
      "note": "Language-specific paragraph content"
    }
  }
}
```

**JSON decorator format**: `"decorator": "lang_prefix:L-N"` where N is the language slot number (1, 2, 4, 5, 10, etc.)

### Usage

```python
from armodel2.serialization.decorators import lang_prefix

class MultiLanguagePlainText(ARObject):
    def __init__(self) -> None:
        self._l10: LPlainText = None

    @lang_prefix("L-10")
    @property
    def l10(self) -> LPlainText:
        return self._l10

    @l10.setter
    def l10(self, value: LPlainText) -> None:
        self._l10 = value
```

**Note**: The `@lang_prefix` decorator must come AFTER `@property` (unlike `@xml_attribute`).

### Generated XML Structure

```xml
<L-10 L="EN">English text</L-10>
<L-4 L="DE">German paragraph</L-4>
```

### Language Tag Pattern

The lang_prefix pattern is used for AUTOSAR multilanguage support:

```xml
<L-1 L="EN">English text</L-1>
<L-2 L="DE">German text</L-2>
<L-4 L="FR">French text</L-4>
<L-5 L="ES">Spanish text</L-5>
<L-10 L="EN">Long English text</L-10>
<L-GRAPHIC L="EN">Graphic description</L-GRAPHIC>
```

### Common Use Cases

- `MultiLanguagePlainText.l10` - Long plain text content
- `MultiLanguageParagraph.l4` - Paragraph content
- `MultiLanguageLongName.l1` - Long name content
- `DocumentationBlock` - Language-specific documentation elements

---

## 5. `@lang_abbr(xml_attr_name: str)`

Mark an attribute as a language abbreviation XML attribute with exact control over the attribute name.

### Description

This decorator is used for LanguageSpecific series classes where the language abbreviation attribute (typically 'l') should be serialized as an XML attribute with a specific name (typically 'L'). Unlike `@xml_attribute` which uses NameConverter to auto-convert names, `@lang_abbr` allows specifying the exact XML attribute name.

### JSON Configuration

```json
{
  "name": "LanguageSpecific",
  "maturity": "draft",
  "package": "M2::MSR::Documentation::TextModel::MultilanguageData",
  "is_abstract": false,
  "attributes": {
    "l": {
      "type": "LEnum",
      "multiplicity": "1",
      "kind": "attribute",
      "is_ref": false,
      "decorator": "lang_abbr:L",
      "note": "Language abbreviation"
    }
  }
}
```

**JSON decorator format**: `"decorator": "lang_abbr:L"` where L is the exact XML attribute name to use.

### Usage

```python
from armodel2.serialization.decorators import lang_abbr

class LanguageSpecific(ARObject):
    def __init__(self) -> None:
        self._l: LEnum = LEnum.EN

    @lang_abbr("L")
    @property
    def l(self) -> LEnum:
        return self._l

    @l.setter
    def l(self, value: LEnum) -> None:
        self._l = value
```

**Note**: The `@lang_abbr` decorator must come AFTER `@property` (unlike `@xml_attribute`).

### Generated XML Structure

```xml
<L-LONG-NAME L="EN">Long Name</L-LONG-NAME>
<L-PLAIN-TEXT L="DE">Plain text in German</L-PLAIN-TEXT>
```

### Difference from @xml_attribute

| Decorator | Name Conversion | Use Case |
|-----------|----------------|----------|
| `@xml_attribute` | Auto-converted via NameConverter | General XML attributes (e.g., SCHEMA-VERSION) |
| `@lang_abbr` | Exact attribute name specified | Language abbreviation attributes (always "L") |

### Common Use Cases

- `LanguageSpecific.l` - Language abbreviation for all language-specific elements
- Used in combination with `@lang_prefix` for multilanguage content

---

## 6. `@xml_element_name(xml_tag: str)`

Specify a custom XML element name for attributes when the auto-generated name differs from the schema, or when multi-level nesting is required.

### Description

This decorator is used when the XML element name differs from the auto-generated name via NameConverter. It supports both single-level override and multi-level path nesting.

### JSON Configuration

**Single parameter** (override container tag):
```json
{
  "name": "BswModuleDescription",
  "maturity": "draft",
  "package": "M2::AUTOSARTemplates::BswModuleTemplate::BswOverview",
  "is_abstract": false,
  "attributes": {
    "providedClientServerEntries": {
      "type": "BswModuleClientServerEntry",
      "multiplicity": "*",
      "kind": "aggr",
      "is_ref": false,
      "decorator": "xml_element_name:PROVIDED-ENTRYS",
      "note": "Provided client/server entries"
    },
    "requiredClientServerEntries": {
      "type": "BswModuleClientServerEntry",
      "multiplicity": "*",
      "kind": "aggr",
      "is_ref": false,
      "decorator": "xml_element_name:REQUIRED-ENTRYS",
      "note": "Required client/server entries"
    }
  }
}
```

**Multi-level path** (nested containers):
```json
{
  "name": "ExecutableEntity",
  "maturity": "draft",
  "package": "M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses",
  "is_abstract": false,
  "attributes": {
    "canEnterRefs": {
      "type": "ARRef",
      "multiplicity": "*",
      "kind": "ref",
      "is_ref": true,
      "decorator": "xml_element_name:CAN-ENTER-EXCLUSIVE-AREA-REFS/CAN-ENTER-EXCLUSIVE-AREA/CAN-ENTER-EXCLUSIVE-AREA-REF",
      "note": "References to exclusive areas that can be entered"
    }
  }
}
```

**JSON decorator format**:
- Single level: `"decorator": "xml_element_name:TAG"` - Override container element name
- Multi-level: `"decorator": "xml_element_name:TAG1/TAG2/TAG3"` - Nested container path

### Usage

**Single parameter** (override container tag):
```python
from armodel2.serialization.decorators import xml_element_name

class BswModuleDescription(ARElement):
    _provided_client_server_entries: list[BswModuleClientServerEntry] = []
    _required_client_server_entries: list[BswModuleClientServerEntry] = []

    @property
    @xml_element_name("PROVIDED-ENTRYS")
    def provided_client_server_entries(self) -> list[BswModuleClientServerEntry]:
        return self._provided_client_server_entries

    @provided_client_server_entries.setter
    def provided_client_server_entries(self, value: list[BswModuleClientServerEntry]) -> None:
        self._provided_client_server_entries = value

    @property
    @xml_element_name("REQUIRED-ENTRYS")
    def required_client_server_entries(self) -> list[BswModuleClientServerEntry]:
        return self._required_client_server_entries

    @required_client_server_entries.setter
    def required_client_server_entries(self, value: list[BswModuleClientServerEntry]) -> None:
        self._required_client_server_entries = value
```

**Multi-level path** (nested containers):
```python
from armodel2.serialization.decorators import xml_element_name

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

**Note**: The `@xml_element_name` decorator must come AFTER `@property`.

### Generated XML Structure

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

### Common Use Cases

- `BswModuleDescription.provided_client_server_entries` - Custom "PROVIDED-ENTRYS" instead of auto-generated name
- `ExecutableEntity.can_enter_refs` - Multi-level nested container structure
- Legacy schema compatibility where element names don't follow standard conventions

---

## 7. `@ref_conditional(xml_tag: str)`

Mark an attribute as using the AUTOSAR **-REF-CONDITIONAL** pattern for reference lists in atpVariation scenarios.

### Description

The -REF-CONDITIONAL pattern is used in AUTOSAR atpVariation for reference lists where each reference is wrapped in a `<TAG>-REF-CONDITIONAL` element containing the actual `<TAG>-REF` element. This is different from the standard reference list pattern.

### JSON Configuration

```json
{
  "name": "System",
  "maturity": "draft",
  "package": "M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Can::CanTopology",
  "is_abstract": false,
  "attributes": {
    "fibexElements": {
      "type": "FibexElement",
      "multiplicity": "*",
      "kind": "ref",
      "is_ref": true,
      "decorator": "ref_conditional:FIBEX-ELEMENTS",
      "note": "Reference to ASAM FIBEX elements specifying Topology"
    }
  }
}
```

**JSON decorator format**: `"decorator": "ref_conditional:CONTAINER-TAG"` where CONTAINER-TAG is the container element name (e.g., "FIBEX-ELEMENTS", "COMM-CONNECTORS").

### Usage

```python
from armodel2.serialization.decorators import ref_conditional

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

**Note**: The `@ref_conditional` decorator must come AFTER `@property`.

### Generated XML Structure

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

### XML Structure Breakdown

```
<CONTAINER-TAG>
  <TYPE-TAG>-REF-CONDITIONAL>
    <TYPE-TAG>-REF DEST="...">...</TYPE-TAG>-REF>
  </TYPE-TAG>-REF-CONDITIONAL>
</CONTAINER-TAG>
```

Where:
- **CONTAINER-TAG**: The container element name from decorator params (e.g., "FIBEX-ELEMENTS", "COMM-CONNECTORS")
- **TYPE-TAG**: The XML tag derived from the attribute's type name via `NameConverter.to_xml_tag()` (e.g., "FIBEX-ELEMENT", "COMMUNICATION-CONNECTOR")
- **-REF-CONDITIONAL**: The atpVariation wrapper
- **-REF**: The actual reference element with DEST attribute

**Important**: The `TYPE-TAG` is derived from the **attribute's type name** (e.g., `CommunicationConnector` → `COMMUNICATION-CONNECTOR`), not from the container tag via simple string truncation. This ensures correct tag generation for abbreviated container names like `COMM-CONNECTORS` → `COMMUNICATION-CONNECTOR-REF-CONDITIONAL` (not `COMM-CONNECTOR-REF-CONDITIONAL`).

### Real-world Example - PhysicalChannel.comm_connector_refs

**JSON Configuration**:
```json
{
  "name": "PhysicalChannel",
  "attributes": {
    "commConnectors": {
      "type": "CommunicationConnector",
      "multiplicity": "*",
      "kind": "ref",
      "is_ref": true,
      "decorator": "ref_conditional:COMM-CONNECTORS"
    }
  }
}
```

**Generated XML**:
```xml
<COMM-CONNECTORS>
  <COMMUNICATION-CONNECTOR-REF-CONDITIONAL>
    <COMMUNICATION-CONNECTOR-REF DEST="CAN-COMMUNICATION-CONNECTOR">/CanSystem/ECUINSTANCES/DebugNode/Conn_DebugNode</COMMUNICATION-CONNECTOR-REF>
  </COMMUNICATION-CONNECTOR-REF-CONDITIONAL>
  <COMMUNICATION-CONNECTOR-REF-CONDITIONAL>
    <COMMUNICATION-CONNECTOR-REF DEST="CAN-COMMUNICATION-CONNECTOR">/CanSystem/ECUINSTANCES/EcuTestNode/Conn_EcuTestNode</COMMUNICATION-CONNECTOR-REF>
  </COMMUNICATION-CONNECTOR-REF-CONDITIONAL>
</COMM-CONNECTORS>
```

### Difference from Standard Reference Lists

| Pattern | Container | Child Wrapper | Reference |
|---------|-----------|---------------|-----------|
| Standard (no decorator) | `<TAG>-REFS` | None | `<TAG>-REF` |
| ref_conditional | `<TAG>S` | `<TAG>-REF-CONDITIONAL` | `<TAG>-REF` |

### Common Use Cases

- `System.fibexElements` - References to FIBEX topology elements
- `PhysicalChannel.comm_connector_refs` - CAN communication connectors
- `EcuInstance.managed_refs` - Managed references in ECU instances

---

## 8. `@instance_ref(flatten: bool = False, list_type: str = 'single')`

Mark an attribute as an **instance reference (iref)**. Instance references are wrapped in a `<TAG>-IREF` element. The `flatten` parameter controls whether children are flattened directly into the wrapper or wrapped in their own element.

### Description

Instance references are used in AUTOSAR connector classes (AssemblySwConnector, DelegationSwConnector) where the XML structure requires a `<TAG>-IREF` wrapper. The `flatten` parameter controls the internal structure, and `list_type` controls how list attributes are wrapped.

### JSON Configuration

**Flattened structure** (AssemblySwConnector):
```json
{
  "name": "AssemblySwConnector",
  "maturity": "draft",
  "package": "M2::AUTOSARTemplates::SWComponentTemplate::Composition",
  "is_abstract": false,
  "attributes": {
    "provider": {
      "type": "PPortInCompositionInstanceRef",
      "multiplicity": "0..1",
      "kind": "iref",
      "is_ref": true,
      "decorator": "instance_ref:flatten=True",
      "note": "Provider instance reference"
    },
    "requester": {
      "type": "RPortInCompositionInstanceRef",
      "multiplicity": "0..1",
      "kind": "iref",
      "is_ref": true,
      "decorator": "instance_ref:flatten=True",
      "note": "Requester instance reference"
    }
  }
}
```

**Non-flattened structure** (DelegationSwConnector):
```json
{
  "name": "DelegationSwConnector",
  "maturity": "draft",
  "package": "M2::AUTOSARTemplates::SWComponentTemplate::Composition",
  "is_abstract": false,
  "attributes": {
    "innerPort": {
      "type": "PortInCompositionTypeInstanceRef",
      "multiplicity": "0..1",
      "kind": "iref",
      "is_ref": true,
      "decorator": "instance_ref:flatten=False",
      "note": "Inner port instance reference"
    }
  }
}
```

**Multi-wrapper list pattern**:
```json
{
  "name": "SwcToEcuMapping",
  "attributes": {
    "components": {
      "type": "ComponentInSystemInstanceRef",
      "multiplicity": "*",
      "kind": "iref",
      "is_ref": true,
      "decorator": "instance_ref:flatten=True,list_type=multi",
      "note": "Component instance references"
    }
  }
}
```

**JSON decorator format**: `"decorator": "instance_ref:flatten=True,list_type=single"`
- `flatten=True/False` - Controls whether children are flattened into wrapper
- `list_type=single/multi` - For lists, controls single vs multi-wrapper pattern

### Usage

**Flattened structure** (AssemblySwConnector):
```python
from armodel2.serialization.decorators import instance_ref

class AssemblySwConnector(SwConnector):
    def __init__(self) -> None:
        self._provider_iref: Optional[PPortInCompositionInstanceRef] = None
        self._requester_iref: Optional[RPortInCompositionInstanceRef] = None

    @property
    @instance_ref(flatten=True)
    def provider_iref(self) -> Optional[PPortInCompositionInstanceRef]:
        """Get provider_iref instance reference."""
        return self._provider_iref

    @provider_iref.setter
    def provider_iref(self, value: Optional[PPortInCompositionInstanceRef]) -> None:
        """Set provider_iref instance reference."""
        self._provider_iref = value

    @property
    @instance_ref(flatten=True)
    def requester_iref(self) -> Optional[RPortInCompositionInstanceRef]:
        """Get requester_iref instance reference."""
        return self._requester_iref

    @requester_iref.setter
    def requester_iref(self, value: Optional[RPortInCompositionInstanceRef]) -> None:
        """Set requester_iref instance reference."""
        self._requester_iref = value
```

**Non-flattened structure** (DelegationSwConnector):
```python
from armodel2.serialization.decorators import instance_ref

class DelegationSwConnector(SwConnector):
    def __init__(self) -> None:
        self._inner_port_iref: Optional[PortInCompositionTypeInstanceRef] = None

    @property
    @instance_ref(flatten=False)
    def inner_port_iref(self) -> Optional[PortInCompositionTypeInstanceRef]:
        """Get inner_port_iref instance reference."""
        return self._inner_port_iref

    @inner_port_iref.setter
    def inner_port_iref(self, value: Optional[PortInCompositionTypeInstanceRef]) -> None:
        """Set inner_port_iref instance reference."""
        self._inner_port_iref = value
```

**Note**: The `@instance_ref` decorator must come AFTER `@property`.

### Generated XML Structure

**Flattened structure** (`flatten=True`):
```xml
<!-- AssemblySwConnector with @instance_ref(flatten=True) -->
<PROVIDER-IREF>
  <CONTEXT-COMPONENT-REF DEST="SW-COMPONENT-PROTOTYPE">/path/to/component</CONTEXT-COMPONENT-REF>
  <TARGET-P-PORT-REF DEST="P-PORT-PROTOTYPE">/path/to/port</TARGET-P-PORT-REF>
</PROVIDER-IREF>

<REQUESTER-IREF>
  <CONTEXT-COMPONENT-REF DEST="SW-COMPONENT-PROTOTYPE">/path/to/component</CONTEXT-COMPONENT-REF>
  <TARGET-R-PORT-REF DEST="R-PORT-PROTOTYPE">/path/to/port</TARGET-R-PORT-REF>
</REQUESTER-IREF>
```

**Non-flattened structure** (`flatten=False`):
```xml
<!-- DelegationSwConnector with @instance_ref(flatten=False) -->
<INNER-PORT-IREF>
  <R-PORT-IN-COMPOSITION-INSTANCE-REF>
    <CONTEXT-COMPONENT-REF DEST="SW-COMPONENT-PROTOTYPE">/path/to/component</CONTEXT-COMPONENT-REF>
    <TARGET-R-PORT-REF DEST="R-PORT-PROTOTYPE">/path/to/port</TARGET-R-PORT-REF>
  </R-PORT-IN-COMPOSITION-INSTANCE-REF>
</INNER-PORT-IREF>
```

**Multi-wrapper list** (`flatten=True, list_type='multi'`):
```xml
<COMPONENT-IREFS>
  <COMPONENT-IREF>
    <CONTEXT-COMPOSITION-REF DEST="SW-COMPONENT-PROTOTYPE">/path/to/component1</CONTEXT-COMPOSITION-REF>
    <TARGET-COMPONENT-REF DEST="SW-COMPONENT-PROTOTYPE">/path/to/component1</TARGET-COMPONENT-REF>
  </COMPONENT-IREF>
  <COMPONENT-IREF>
    <CONTEXT-COMPOSITION-REF DEST="SW-COMPONENT-PROTOTYPE">/path/to/component2</CONTEXT-COMPOSITION-REF>
    <TARGET-COMPONENT-REF DEST="SW-COMPONENT-PROTOTYPE">/path/to/component2</TARGET-COMPONENT-REF>
  </COMPONENT-IREF>
</COMPONENT-IREFS>
```

**Single-wrapper list** (`flatten=True, list_type='single'`):
```xml
<COMPONENTS-IREF>
  <CONTEXT-COMPOSITION-REF DEST="SW-COMPONENT-PROTOTYPE">/path/to/component1</CONTEXT-COMPOSITION-REF>
  <TARGET-COMPONENT-REF DEST="SW-COMPONENT-PROTOTYPE">/path/to/component1</TARGET-COMPONENT-REF>
  <CONTEXT-COMPOSITION-REF DEST="SW-COMPONENT-PROTOTYPE">/path/to/component2</CONTEXT-COMPOSITION-REF>
  <TARGET-COMPONENT-REF DEST="SW-COMPONENT-PROTOTYPE">/path/to/component2</TARGET-COMPONENT-REF>
</COMPONENTS-IREF>
```

### When to Use Flattened vs Non-Flattened

| Mode | Use Case | Type | Example |
|------|----------|------|---------|
| `flatten=True` | Concrete instance reference types where XML structure is flattened | `PPortInCompositionInstanceRef`, `RPortInCompositionInstanceRef` | AssemblySwConnector |
| `flatten=False` | Abstract instance reference types where concrete type is determined at runtime | `PortInCompositionTypeInstanceRef` | DelegationSwConnector |

### List Handling with `list_type` Parameter

| list_type | Pattern | XML Structure |
|-----------|---------|---------------|
| `'single'` (default) | Single wrapper | All items in one `<TAG>-IREF` container |
| `'multi'` | Multi-wrapper | Each item in its own `<TAG>-IREF`, wrapped in `<TAG>-IREFS` |

### Common Use Cases

- `AssemblySwConnector.provider` - PPortInCompositionInstanceRef with flattened structure
- `AssemblySwConnector.requester` - RPortInCompositionInstanceRef with flattened structure
- `DelegationSwConnector.innerPort` - PortInCompositionTypeInstanceRef with non-flattened structure
- `Collection.collectedInstance` - AnyInstanceRef with flattened structure
- `SwcToEcuMapping.components` - ComponentInSystemInstanceRef list with multi-wrapper pattern

---

## 9. `@polymorphic(mapping: dict[str, str])`

Mark an attribute as polymorphic with wrapper element mapping. Used when an XML wrapper element contains a concrete implementation of an abstract base class.

### Description

The polymorphic pattern is used when an XML wrapper element contains a concrete implementation of an abstract base class. The decorator accepts a dictionary mapping wrapper XML tags to base class names, enabling the deserialization framework to correctly resolve and instantiate the concrete type.

### JSON Configuration

**Single mapping**:
```json
{
  "name": "ConstantSpecification",
  "maturity": "draft",
  "package": "M2::AUTOSARTemplates::CommonStructure::Constants",
  "is_abstract": false,
  "attributes": {
    "valueSpec": {
      "type": "ValueSpecification",
      "multiplicity": "0..1",
      "kind": "attribute",
      "is_ref": false,
      "decorator": "polymorphic:VALUE-SPEC=ValueSpecification",
      "note": "Value specification for the constant"
    }
  }
}
```

**Multiple mappings** (same base type):
```json
{
  "name": "CompuMethod",
  "maturity": "draft",
  "package": "M2::MSR::ComputationMethod",
  "is_abstract": false,
  "attributes": {
    "compuInternalToPhys": {
      "type": "CompuContent",
      "multiplicity": "0..1",
      "kind": "attribute",
      "is_ref": false,
      "decorator": "polymorphic:COMPU-INTERNAL-TO-PHYS=CompuContent",
      "note": "Computation from internal to physical"
    },
    "compuPhysToInternal": {
      "type": "CompuContent",
      "multiplicity": "0..1",
      "kind": "attribute",
      "is_ref": false,
      "decorator": "polymorphic:COMPU-PHYS-TO-INTERNAL=CompuContent",
      "note": "Computation from physical to internal"
    }
  }
}
```

**JSON decorator format**: `"decorator": "polymorphic:TAG=BaseType"` where TAG is the XML wrapper tag and BaseType is the expected base class.

### Usage

**Single mapping**:
```python
from armodel2.serialization.decorators import polymorphic

class ConstantSpecification(ARElement):
    _value_spec: Optional[ValueSpecification] = None

    @property
    @polymorphic({"VALUE-SPEC": "ValueSpecification"})
    def value_spec(self) -> Optional[ValueSpecification]:
        return self._value_spec

    @value_spec.setter
    def value_spec(self, value: Optional[ValueSpecification]) -> None:
        self._value_spec = value
```

**Multiple mappings** (for attribute with multiple possible wrapper tags):
```python
from armodel2.serialization.decorators import polymorphic

class CompuMethod(ARObject):
    _compu_internal_to_phys: Optional[CompuContent] = None

    @property
    @polymorphic({
        "COMPU-INTERNAL-TO-PHYS": "CompuContent",
        "COMPU-PHYS-TO-INTERNAL": "CompuContent"
    })
    def compu_internal_to_phys(self) -> Optional[CompuContent]:
        return self._compu_internal_to_phys

    @compu_internal_to_phys.setter
    def compu_internal_to_phys(self, value: Optional[CompuContent]) -> None:
        self._compu_internal_to_phys = value
```

**Note**: The `@polymorphic` decorator must come AFTER `@property`.

### Generated XML Structure

**Single mapping example**:
```xml
<CONSTANT-SPECIFICATION>
  <SHORT-NAME>MyConstant</SHORT-NAME>
  <VALUE-SPEC>
    <NUMERICAL-VALUE-SPECIFICATION>
      <SHORT-LABEL>MyValue</SHORT-LABEL>
      <VALUE>42</VALUE>
    </NUMERICAL-VALUE-SPECIFICATION>
  </VALUE-SPEC>
</CONSTANT-SPECIFICATION>
```

**Multiple mappings example**:
```xml
<COMPU-METHOD>
  <SHORT-NAME>MyCompuMethod</SHORT-NAME>
  <COMPU-INTERNAL-TO-PHYS>
    <COMPU-SCALES>
      <COMPU-SCALE>
        <LOWER-LIMIT INTERVAL-TYPE="CLOSED">0</LOWER-LIMIT>
        <UPPER-LIMIT INTERVAL-TYPE="CLOSED">100</UPPER-LIMIT>
        <COMPU-CONST>
          <VALUE>0.0</VALUE>
        </COMPU-CONST>
      </COMPU-SCALE>
    </COMPU-SCALES>
  </COMPU-INTERNAL-TO-PHYS>
</COMPU-METHOD>
```

### Deserialization Flow

1. The framework finds the child element inside the wrapper (e.g., `<NUMERICAL-VALUE-SPECIFICATION>` inside `<VALUE-SPEC>`)
2. Uses the mapping to verify the concrete type is a subclass of the expected base type
3. Deserializes using the concrete class based on the XML tag

### Common Use Cases

- `ConstantSpecification.valueSpec` - ValueSpecification with VALUE-SPEC wrapper
- `CompuMethod.compuInternalToPhys` - CompuContent with COMPU-INTERNAL-TO-PHYS wrapper
- `CompuMethod.compuPhysToInternal` - CompuContent with COMPU-PHYS-TO-INTERNAL wrapper
- `InitValue` - ValueSpecification with INIT-VALUE wrapper

---

## JSON Configuration for Decorators

Decorators are configured via JSON mapping data in the AUTOSAR class definitions. This allows the code generator to automatically generate the correct decorator usage.

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
- **decorator_params**: Parameters passed to the decorator (e.g., `FIBEX-ELEMENTS`, `L-10`, `flatten=True`)

### Decorator Types in JSON

| Decorator | JSON Example | When to Use |
|-----------|--------------|-------------|
| `xml_element_name` | `"decorator": "xml_element_name:PROVIDED-ENTRYS"` | Custom element name |
| `xml_element_name` | `"decorator": "xml_element_name:TAG1/TAG2/TAG3"` | Multi-level nesting |
| `ref_conditional` | `"decorator": "ref_conditional:FIBEX-ELEMENTS"` | -REF-CONDITIONAL pattern |
| `instance_ref` | `"decorator": "instance_ref:flatten=True"` | Instance reference (flattened) |
| `instance_ref` | `"decorator": "instance_ref:flatten=False"` | Instance reference (non-flattened) |
| `instance_ref` | `"decorator": "instance_ref:flatten=True,list_type=multi"` | Instance reference list (multi-wrapper) |
| `lang_prefix` | `"decorator": "lang_prefix:L-10"` | Language-specific content |
| `lang_abbr` | `"decorator": "lang_abbr:L"` | Language abbreviation attribute |
| `xml_attribute` | `"decorator": "xml_attribute"` | XML attribute (auto-generated name) |
| `xml_attribute` | `"decorator": "xml_attribute:T"` | XML attribute (custom name) |
| `polymorphic` | `"decorator": "polymorphic:VALUE-SPEC=ValueSpecification"` | Polymorphic type handling |

**Note**: Class-level decorators (`@atp_variant()` and `@atp_mixed()`) are not configured via the `decorator` field. Instead, they are applied by the code generator when `"atp_type": "atpVariation"` or `"atp_type": "atpMixed"` is present in the JSON class definition.

### Special Cases

**Attribute-level decorators** (ref_conditional, xml_element_name, xml_attribute, lang_prefix, lang_abbr, instance_ref, polymorphic):
- Use the `decorator` field with format `"name:params"`
- The code generator applies the decorator to the generated property
- For xml_attribute, lang_prefix, lang_abbr, instance_ref, and polymorphic, params are required

**Class-level decorators** (atp_variant, atp_mixed):
- Applied at the class level by the code generator
- Triggered by `"atp_type": "atpVariation"` or `"atp_type": "atpMixed"` in JSON
- Not configured via the `decorator` field

---

## Code Generator Processing

The code generator processes decorator configurations in multiple stages:

1. **Parse decorator field**: Extract decorator name and parameters from JSON
2. **Generate import statements**: Add decorator imports to generated class
3. **Generate properties**: Create property with decorator applied
4. **Generate serialize methods**: Use decorator metadata for correct serialization
5. **Generate deserialize methods**: Use decorator metadata for correct deserialization
6. **Generate dispatch tables**: For polymorphic types, generate if-elif-else chains

### Generated Code Example

Given this JSON configuration:

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

The code generator generates:

```python
from armodel2.serialization.decorators import ref_conditional

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

---

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

| Decorator | Marker Attributes | Type | Decorator Order |
|-----------|-------------------|------|-----------------|
| `@xml_attribute` | `_is_xml_attribute`, `_xml_attr_name` | `bool`, `str` | Before `@property` |
| `@atp_variant()` | `_atp_variant` | `bool` | Class-level (N/A) |
| `@atp_mixed()` | `_atp_mixed` | `bool` | Class-level (N/A) |
| `@lang_prefix(tag)` | `_lang_prefix`, `_lang_prefix_tag` | `bool`, `str` | After `@property` |
| `@lang_abbr(attr)` | `_language_abbr`, `_xml_attr_name` | `bool`, `str` | After `@property` |
| `@xml_element_name(tag)` | `_xml_element_name`, `_xml_tag` | `bool`, `str` | After `@property` |
| `@ref_conditional(tag)` | `_is_ref_conditional`, `_xml_tag` | `bool`, `str` | After `@property` |
| `@instance_ref(flatten, list_type)` | `_is_instance_ref`, `_flatten`, `_list_type` | `bool`, `bool`, `str` | After `@property` |
| `@polymorphic(mapping)` | `_is_polymorphic`, `_polymorphic_mapping` | `bool`, `dict` | After `@property` |

---

## Usage Guidelines

### When to Use Decorators

| Scenario | Decorator | Example |
|----------|-----------|---------|
| XML attribute needed | `@xml_attribute` | `<ELEMENT uuid="abc">` |
| AUTOSAR atpVariation pattern (class-level) | `@atp_variant()` | SwDataDefProps with VARIANTS/CONDITIONAL wrappers |
| AUTOSAR atpMixed pattern (class-level) | `@atp_mixed()` | SwRecordLayoutGroupContent with direct children |
| AUTOSAR atpVariation pattern (reference lists) | `@ref_conditional("TAG")` | System.fibexElements with -REF-CONDITIONAL wrappers |
| Instance reference (flattened) | `@instance_ref(flatten=True)` | AssemblySwConnector with <PROVIDER-IREF> |
| Instance reference (non-flattened) | `@instance_ref(flatten=False)` | DelegationSwConnector with <INNER-PORT-IREF> |
| Instance reference list (multi-wrapper) | `@instance_ref(flatten=True, list_type='multi')` | SwcToEcuMapping with multiple COMPONENT-IREF |
| Language-specific content | `@lang_prefix("L-N")` | MultiLanguagePlainText with L-10 wrapper |
| Language abbreviation attribute | `@lang_abbr("L")` | LanguageSpecific with L attribute |
| Non-standard element name | `@xml_element_name("TAG")` | BswModuleDescription with PROVIDED-ENTRYS |
| Multi-level nesting | `@xml_element_name("TAG1/TAG2/TAG3")` | ExecutableEntity with nested containers |
| Polymorphic type with wrapper | `@polymorphic({"TAG": "BaseType"})` | ConstantSpecification with VALUE-SPEC wrapper |

### When NOT to Use Decorators

1. **Simple attributes**: Use default reflection-based serialization
2. **List attributes**: Automatically wrapped in plural element names
3. **Optional attributes**: Automatically skipped if `None`
4. **Nested objects**: Automatically recursively serialized
5. **Primitive types**: Automatically converted to text content

### Decorator Order

For property-based decorators, the order is critical and varies by decorator:

**Decorators that come BEFORE `@property`**:
- `@xml_attribute` - Must be first

```python
# CORRECT order for @xml_attribute
@xml_attribute  # 1. Mark as XML attribute (before @property)
@property       # 2. Define as property
def schema_version(self) -> str:
    return self._schema_version
```

**Decorators that come AFTER `@property`**:
- `@lang_prefix`
- `@lang_abbr`
- `@xml_element_name`
- `@ref_conditional`
- `@instance_ref`
- `@polymorphic`

```python
# CORRECT order for other decorators
@property
@lang_prefix("L-10")  # After @property
def l10(self) -> LPlainText:
    return self._l10

@property
@ref_conditional("FIBEX-ELEMENTS")  # After @property
def fibex_element_refs(self) -> list[ARRef]:
    return self._fibex_element_refs
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

---

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


def test_atp_mixed():
    """Test @atp_mixed decorator."""
    obj = SwRecordLayoutGroupContent()
    obj.sw_record_layout_ref = ARRef("...")
    elem = obj.serialize("")

    # Verify no wrapper - direct child
    ref = elem.find("SW-RECORD-LAYOUT-REF")
    assert ref is not None
    # Should NOT have any wrapper element


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


def test_lang_abbr():
    """Test @lang_abbr decorator."""
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


def test_ref_conditional():
    """Test @ref_conditional decorator."""
    obj = System()
    ref = ARRef(dest="CAN-CLUSTER", value="/CanSystem/Network")
    obj.fibex_element_refs = [ref]
    elem = obj.serialize("")

    # Verify container
    container = elem.find("FIBEX-ELEMENTS")
    assert container is not None
    # Verify -REF-CONDITIONAL wrapper
    conditional = container.find("FIBEX-ELEMENT-REF-CONDITIONAL")
    assert conditional is not None
    # Verify actual ref
    fibex_ref = conditional.find("FIBEX-ELEMENT-REF")
    assert fibex_ref is not None
    assert fibex_ref.get("DEST") == "CAN-CLUSTER"


def test_instance_ref_flattened():
    """Test @instance_ref(flatten=True) decorator."""
    obj = AssemblySwConnector()
    obj.provider_iref = PPortInCompositionInstanceRef(...)
    elem = obj.serialize("")

    # Verify -IREF wrapper
    iref = elem.find("PROVIDER-IREF")
    assert iref is not None
    # Verify children are flattened directly (no additional wrapper)
    context = iref.find("CONTEXT-COMPONENT-REF")
    assert context is not None


def test_instance_ref_non_flattened():
    """Test @instance_ref(flatten=False) decorator."""
    obj = DelegationSwConnector()
    obj.inner_port_iref = PortInCompositionTypeInstanceRef(...)
    elem = obj.serialize("")

    # Verify -IREF wrapper
    iref = elem.find("INNER-PORT-IREF")
    assert iref is not None
    # Verify element is wrapped in its own tag
    wrapped = iref.find("R-PORT-IN-COMPOSITION-INSTANCE-REF")
    assert wrapped is not None


def test_polymorphic():
    """Test @polymorphic decorator."""
    obj = ConstantSpecification()
    obj.value_spec = NumericalValueSpecification()
    elem = obj.serialize("")

    # Verify wrapper
    wrapper = elem.find("VALUE-SPEC")
    assert wrapper is not None
    # Verify concrete type inside wrapper
    concrete = wrapper.find("NUMERICAL-VALUE-SPECIFICATION")
    assert concrete is not None
```

---

## Troubleshooting

### Issue: Decorator Not Working

**Symptoms**: Decorator is ignored, default behavior occurs

**Solutions**:
1. Check decorator order:
   - `@xml_attribute` must come **before** `@property`
   - `@lang_prefix`, `@lang_abbr`, `@xml_element_name`, `@ref_conditional`, `@instance_ref`, `@polymorphic` must come **after** `@property`
2. Verify property pattern: Must have both getter and setter
3. Check private backing field: Use underscore-prefixed private field
4. Verify import: Import from `armodel2.serialization.decorators`
5. Check JSON configuration: Ensure decorator format is correct (`"decorator": "name:params"`)

### Issue: Wrong XML Tag Name

**Symptoms**: XML tag doesn't match expected name

**Solutions**:
1. For `@xml_attribute`: Check that attribute name is correct in XML
2. For `@lang_prefix`: Verify the tag parameter matches XML (e.g., "L-10")
3. For `@lang_abbr`: Verify the attr parameter matches XML (e.g., "L")
4. For `@xml_element_name`: Verify the tag parameter matches XML exactly
5. For multi-level paths: Verify each level is separated by `/`

### Issue: Attribute Not Serializing

**Symptoms**: Expected XML element/attribute is missing

**Solutions**:
1. Check attribute is not private (doesn't start with `_` in the property name)
2. Check value is not `None`
3. Verify decorator is applied correctly
4. Check for typos in decorator parameters
5. Verify the JSON `kind` field is correct (e.g., "attribute" vs "ref" vs "iref")

### Issue: Polymorphic Type Not Resolving

**Symptoms**: Polymorphic attribute deserializes as None or wrong type

**Solutions**:
1. Verify the polymorphic mapping includes the correct wrapper tag
2. Ensure the concrete type is registered in the ModelFactory
3. Check that the concrete type is a subclass of the base type in the mapping
4. Verify the JSON decorator format: `"polymorphic:TAG=BaseType"`

---

## References

- **Implementation**: `src/armodel2/serialization/decorators.py`
- **Base class**: `src/armodel2/models/M2/.../ArObject/ar_object.py`
- **Serialization framework**: `docs/designs/serialization.md`
- **Design rules**: `docs/designs/design_rules.md`
- **Model design**: `docs/designs/model_design.md`
- **JSON mappings**: `docs/json/packages/*.classes.json`
