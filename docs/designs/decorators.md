# Decorator Configuration Guide

## Introduction

The py-armodel2 project uses a **decorator-based XML serialization system** to handle AUTOSAR ARXML serialization edge cases. While 95% of model classes serialize correctly using the reflection-based framework, certain AUTOSAR XML patterns require special handling via decorators.

**When to use decorators:**
- The default reflection-based serialization produces incorrect XML structure
- AUTOSAR schema requires specific XML attributes instead of elements
- XML wrapper patterns need special handling (atpVariation, REF-CONDITIONAL, etc.)
- Element names don't follow standard naming conventions
- Language-specific elements require custom tags

**When NOT to use decorators:**
- Standard element serialization works correctly
- NameConverter handles snake_case to UPPER-CASE conversion properly
- The attribute follows normal list/container patterns

## Decorator Overview

| Decorator             | Purpose                              | Level     | Active Use  |
| --------------------- | ------------------------------------ | --------- | ----------- |
| `@xml_attribute`      | Serialize as XML attribute           | Attribute | 5 configs   |
| `@atp_variant()`      | AUTOSAR atpVariation wrapper pattern | Class     | 25+ classes |
| `@atp_mixed()`        | AUTOSAR atpMixed container pattern   | Class     | 54+ classes |
| `@lang_prefix()`      | Language-specific wrapper elements   | Attribute | 6 configs   |
| `@lang_abbr()`        | Language abbreviation XML attribute  | Attribute | 1 config    |
| `@xml_element_name()` | Custom XML element name              | Attribute | 11 configs  |
| `@ref_conditional()`  | REF-CONDITIONAL wrapper pattern      | Attribute | 2 configs   |
| `@instance_ref()`     | Instance reference pattern           | Attribute | 10 configs  |
| `@polymorphic()`      | Polymorphic deserialization          | Attribute | 14 configs  |

## Decorator Reference

### `@xml_attribute`

**Purpose:** Serialize a property/attribute as an XML attribute instead of a child element.

**Use Case:** When AUTOSAR schema defines metadata as XML attributes rather than elements (e.g., `SCHEMA-VERSION`, `T` for timestamp).

**JSON Configuration:**
```json
{
  "attributes": {
    "schema_version": {
      "decorator": "xml_attribute"
    },
    "timestamp": {
      "decorator": "xml_attribute:T"
    }
  }
}
```

**Generated Python Code:**
```python
# Without parameter (uses NameConverter for attribute name)
@xml_attribute
@property
def schema_version(self) -> str:
    return self._schema_version

# With custom attribute name
@xml_attribute("T")
@property
def timestamp(self) -> str:
    return self._timestamp
```

**Before/After ARXML:**
```xml
<!-- Without decorator (WRONG) -->
<AUTOSAR>
  <SCHEMA-VERSION>4.5.0</SCHEMA-VERSION>
</AUTOSAR>

<!-- With @xml_attribute (CORRECT) -->
<AUTOSAR SCHEMA-VERSION="4.5.0">
</AUTOSAR>
```

**Real-World Examples:**
- `AUTOSAR.schema_version` → `src/armodel2/models/M2/AUTOSARTemplates/AutosarTopLevelStructure/autosar.py`
- `ARObject.timestamp` → `src/armodel2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ArObject/ar_object.py`
- `Identifiable.gid` → Globally unique identifier

**Related Decorators:** None (standalone)

---

### `@atp_variant()`

**Purpose:** Mark a class as using the AUTOSAR atpVariation pattern, which wraps all class attributes in nested XML elements.

**Use Case:** AUTOSAR's conditional feature system where elements are wrapped in `<CLASS-TAG>-VARIANTS/<CLASS-TAG>-CONDITIONAL` structure.

**JSON Configuration:**
```json
{
  "classes": [{
    "name": "SwDataDefProps",
    "atp_type": "atpVariation"
  }]
}
```

Or explicitly:
```json
{
  "classes": [{
    "name": "SwDataDefProps",
    "decorator": "atp_variant"
  }]
}
```

**Generated Python Code:**
```python
from armodel2.serialization.decorators import atp_variant

@atp_variant()
class SwDataDefProps(ARObject):
    base_type_ref: Optional[ARRef] = None
    sw_calibration_access: Optional[SwCalibrationAccessEnum] = None
```

**Before/After ARXML:**
```xml
<!-- Without decorator (WRONG) -->
<SW-DATA-DEF-PROPS>
  <BASE-TYPE-REF DEST="...">/Package/Element</BASE-TYPE-REF>
</SW-DATA-DEF-PROPS>

<!-- With @atp_variant() (CORRECT) -->
<SW-DATA-DEF-PROPS>
  <SW-DATA-DEF-PROPS-VARIANTS>
    <SW-DATA-DEF-PROPS-CONDITIONAL>
      <BASE-TYPE-REF DEST="...">/Package/Element</BASE-TYPE-REF>
    </SW-DATA-DEF-PROPS-CONDITIONAL>
  </SW-DATA-DEF-PROPS-VARIANTS>
</SW-DATA-DEF-PROPS>
```

**Real-World Examples:**
- `McGroupDataRefSet` → `src/armodel2/models/M2/AUTOSARTemplates/CommonStructure/McGroups/mc_group_data_ref_set.py`
- `DiagnosticCommonProps`
- `EcucFunctionNameDef`
- `EcucLinkerSymbolDef`

**Note:** Metadata elements (`SHORT-NAME`, `LONG-NAME`, `DESC`, `ADMIN-DATA`) are placed **outside** the wrapper.

**Related Decorators:** `@atp_mixed()` (similar pattern, different structure)

---

### `@atp_mixed()`

**Purpose:** Mark a class as using the AUTOSAR atpMixed pattern for container classes that hold multiple different child types.

**Use Case:** Container classes where children are serialized directly without wrapping.

**JSON Configuration:**
```json
{
  "classes": [{
    "name": "SwRecordLayoutGroupContent",
    "atp_type": "atpMixed"
  }]
}
```

Or explicitly:
```json
{
  "classes": [{
    "name": "SwRecordLayoutGroupContent",
    "decorator": "atp_mixed"
  }]
}
```

**Generated Python Code:**
```python
from armodel2.serialization.decorators import atp_mixed

@atp_mixed()
class SwRecordLayoutGroupContent(ARObject):
    sw_record_layout_ref: Optional[ARRef] = None
    sw_record_layout_group: Optional[SwRecordLayoutGroup] = None
    sw_record_layout_v: Optional[SwRecordLayoutV] = None
```

**Before/After ARXML:**
```xml
<!-- Without decorator - attributes would be wrapped -->
<SW-RECORD-LAYOUT-GROUP-CONTENT>
  <SW-RECORD-LAYOUT-REF DEST="...">...</SW-RECORD-LAYOUT-REF>
</SW-RECORD-LAYOUT-GROUP-CONTENT>

<!-- With @atp_mixed() - children serialized directly (same structure) -->
<!-- Note: atp_mixed mainly affects deserialization behavior -->
```

**Real-World Examples:**
- `RuleArguments`
- `ValueList`
- `SwDataDependencyArgs`
- `SwValues`
- `SdgContents`
- `SwRecordLayoutGroupContent`
- `HwPinGroupContent`

**Note:** Unlike `@atp_variant()`, `@atp_mixed()` classes serialize children directly. The decorator primarily affects **deserialization** by flattening container attributes.

**Related Decorators:** `@atp_variant()` (wrapper pattern variant)

---

### `@lang_prefix()`

**Purpose:** Mark an attribute as using the language-specific wrapper element pattern (e.g., `L-2`, `L-4`, `L-10`).

**Use Case:** MultiLanguage* classes where language-specific content is wrapped in numbered language elements.

**JSON Configuration:**
```json
{
  "attributes": {
    "l4": {
      "type": "LPlainText",
      "decorator": "lang_prefix:L-4"
    },
    "l10": {
      "type": "LPlainText",
      "decorator": "lang_prefix:L-10"
    }
  }
}
```

**Generated Python Code:**
```python
from armodel2.serialization.decorators import lang_prefix

class MultilanguageLongName(ARObject):
    @lang_prefix("L-4")
    l4: Optional[LPlainText] = None

    @lang_prefix("L-10")
    l10: Optional[LPlainText] = None
```

**Before/After ARXML:**
```xml
<!-- Without decorator (WRONG) -->
<MULTILANGUAGE-LONG-NAME>
  <L4>English text</L4>
</MULTILANGUAGE-LONG-NAME>

<!-- With @lang_prefix("L-4") (CORRECT) -->
<MULTILANGUAGE-LONG-NAME>
  <L-4 L="EN">English text</L-4>
</MULTILANGUAGE-LONG-NAME>
```

**Real-World Examples:**
- `MultilanguageLongName.l4` / `l10`
- `MultilanguagePlainText.l2`
- `MultilanguageParagraph.l1` / `l2` / `l3` / `l4` / `l5` / `l10`
- `MLFigure.l_graphic`

**Note:** Language number corresponds to AUTOSAR specification. See `MultilanguageLongName` class for mapping.

**Related Decorators:** `@lang_abbr()` (often used together)

---

### `@lang_abbr()`

**Purpose:** Mark an attribute as a language abbreviation XML attribute with a custom name.

**Use Case:** LanguageSpecific series classes where the language attribute should be serialized as `L` (not `LANG`).

**JSON Configuration:**
```json
{
  "attributes": {
    "l": {
      "type": "LEnum",
      "decorator": "lang_abbr:L"
    }
  }
}
```

**Generated Python Code:**
```python
from armodel2.serialization.decorators import lang_abbr

class LanguageSpecific(ARObject):
    @lang_abbr("L")
    @property
    def l(self) -> LEnum:
        return self._l
```

**Manual Implementation Note:** `LanguageSpecific` is manually maintained and implements the decorator logic directly in `serialize()`/`deserialize()`:

```python
# Direct serialization (no decorator used in manual code)
def serialize(self) -> ET.Element:
    elem = ET.Element(self._XML_TAG)
    # ...
    if self.l is not None:
        elem.set("L", str(self.l))  # Manual serialization
    return elem
```

**Before/After ARXML:**
```xml
<!-- Without decorator - would use NameConverter (WRONG) -->
<L-LONG-NAME LANG="EN">Text</L-LONG-NAME>

<!-- With @lang_abbr("L") (CORRECT) -->
<L-LONG-NAME L="EN">Text</L-LONG-NAME>
```

**Real-World Examples:**
- `LanguageSpecific.l` → `src/armodel2/models/M2/MSR/Documentation/TextModel/LanguageDataModel/language_specific.py`
- `LLongName` (inherits from `LanguageSpecific`)
- `LPlainText`
- `LParagraph`

**Note:** Unlike `@xml_attribute` which uses `NameConverter` for conversion, `@lang_abbr()` allows specifying the **exact** XML attribute name.

**Related Decorators:** `@lang_prefix()` (language-specific elements)

---

### `@xml_element_name()`

**Purpose:** Specify a custom XML element name for attributes that don't follow standard naming conventions.

**Use Case:** When AUTOSAR XML element name differs from the auto-generated name (e.g., `PROVIDED-ENTRYS` instead of `PROVIDED-CLIENT-SERVER-ENTRIES`).

**JSON Configuration:**
```json
{
  "attributes": {
    "provided_client_server_entries": {
      "type": "BswModuleClientServerEntry",
      "multiplicity": "*",
      "decorator": "xml_element_name:PROVIDED-ENTRYS"
    },
    "data_receive_point_by_arguments": {
      "type": "DataReceivePointByArgument",
      "multiplicity": "*",
      "decorator": "xml_element_name:DATA-RECEIVE-POINT-BY-ARGUMENTS"
    }
  }
}
```

**Generated Python Code:**
```python
from armodel2.serialization.decorators import xml_element_name

class BswModuleDescription(ARElement):
    @xml_element_name("PROVIDED-ENTRYS")
    provided_client_server_entries: list[BswModuleClientServerEntry] = []

class RunnableEntity(ARElement):
    @xml_element_name("DATA-RECEIVE-POINT-BY-ARGUMENTS")
    data_receive_point_by_arguments: list[DataReceivePointByArgument] = []
```

**Before/After ARXML:**
```xml
<!-- Without decorator - NameConverter would produce (WRONG) -->
<BSW-MODULE-DESCRIPTION>
  <PROVIDED-CLIENT-SERVER-ENTRIES>
    <PROVIDED-CLIENT-SERVER-ENTRY>...</PROVIDED-CLIENT-SERVER-ENTRY>
  </PROVIDED-CLIENT-SERVER-ENTRIES>
</BSW-MODULE-DESCRIPTION>

<!-- With @xml_element_name("PROVIDED-ENTRYS") (CORRECT) -->
<BSW-MODULE-DESCRIPTION>
  <PROVIDED-ENTRYS>
    <PROVIDED-CLIENT-SERVER-ENTRY>...</PROVIDED-CLIENT-SERVER-ENTRY>
  </PROVIDED-ENTRYS>
</BSW-MODULE-DESCRIPTION>
```

**Nested Path Support:**
```python
# For nested container structures
@xml_element_name("ENTITIES/BSW-SCHEDULABLE-ENTITY")
bsw_schedulable_entities: list[BswSchedulableEntity] = []
```

**Auto-Detection:** The code generator automatically detects the **YS→IES pattern** for attributes ending in "ies" with "*" multiplicity:

```python
# JSON without explicit decorator - auto-detected
{
  "provided_client_server_entries": {
    "type": "...",
    "multiplicity": "*"  # Ends in "ies" with "*" → auto-adds xml_element_name
  }
}
```

**Real-World Examples:**
- `BswModuleDescription.provided_client_server_entries` → `PROVIDED-ENTRYS`
- `BswModuleDescription.required_client_server_entries` → `REQUIRED-ENTRYS`
- `RunnableEntity.data_receive_point_by_arguments`
- `BswInternalBehavior.bsw_schedulable_entities` → `ENTITIES/BSW-SCHEDULABLE-ENTITY`
- `ArList.items` → `ITEM`
- `CompuNominatorDenominator.v` → `V`

**Related Decorators:** None (standalone)

---

### `@ref_conditional()`

**Purpose:** Mark an attribute as using the AUTOSAR -REF-CONDITIONAL wrapper pattern for reference lists.

**Use Case:** AUTOSAR atpVariation for reference lists where each reference is wrapped in a `<TAG>-REF-CONDITIONAL` element.

**JSON Configuration:**
```json
{
  "attributes": {
    "fibex_element_refs": {
      "type": "ARRef",
      "multiplicity": "*",
      "decorator": "ref_conditional:FIBEX-ELEMENTS"
    }
  }
}
```

**Generated Python Code:**
```python
from armodel2.serialization.decorators import ref_conditional

class System(ARElement):
    @ref_conditional("FIBEX-ELEMENTS")
    @property
    def fibex_element_refs(self) -> list[ARRef]:
        return self._fibex_element_refs
```

**Before/After ARXML:**
```xml
<!-- Standard reference list pattern (WRONG for this case) -->
<SYSTEM>
  <FIBEX-ELEMENT-REFS>
    <FIBEX-ELEMENT-REF DEST="...">...</FIBEX-ELEMENT-REF>
  </FIBEX-ELEMENT-REFS>
</SYSTEM>

<!-- With @ref_conditional("FIBEX-ELEMENTS") (CORRECT) -->
<SYSTEM>
  <FIBEX-ELEMENTS>
    <FIBEX-ELEMENT-REF-CONDITIONAL>
      <FIBEX-ELEMENT-REF DEST="...">...</FIBEX-ELEMENT-REF>
    </FIBEX-ELEMENT-REF-CONDITIONAL>
  </FIBEX-ELEMENTS>
</SYSTEM>
```

**Real-World Examples:**
- `System.fibex_element_refs` → `src/armodel2/models/M2/AUTOSARTemplates/SystemTemplate/system.py`
- `PhysicalChannel.comm_connectors`

**Note:** This is different from standard reference lists which use `<TAG-REFS><TAG-REF>...` pattern.

**Related Decorators:** `@atp_variant()` (often used together in atpVariation classes)

---

### `@instance_ref()`

**Purpose:** Mark an attribute as an instance reference (iref) with configurable flattening and list behavior.

**Use Case:** AUTOSAR instance references where elements are wrapped in `<TAG>-IREF` with optional flattening.

**JSON Configuration:**
```json
{
  "attributes": {
    "provider_iref": {
      "type": "PPortInCompositionInstanceRef",
      "decorator": "instance_ref:flatten=True"
    },
    "inner_port_iref": {
      "type": "PortInCompositionTypeInstanceRef",
      "decorator": "instance_ref:flatten=False"
    },
    "component_irefs": {
      "type": "ComponentInSystemInstanceRef",
      "multiplicity": "*",
      "decorator": "instance_ref:flatten=True,list_type=multi"
    }
  }
}
```

**Generated Python Code:**
```python
from armodel2.serialization.decorators import instance_ref

# Flattened - AssemblySwConnector
class AssemblySwConnector(SwConnector):
    @instance_ref(flatten=True)
    @property
    def provider_iref(self) -> Optional[PPortInCompositionInstanceRef]:
        return self._provider_iref

# Non-flattened - DelegationSwConnector
class DelegationSwConnector(SwConnector):
    @instance_ref(flatten=False)
    @property
    def inner_port_iref(self) -> Optional[PortInCompositionTypeInstanceRef]:
        return self._inner_port_iref

# Multi-wrapper list - SwcToEcuMapping
class SwcToEcuMapping(ARObject):
    @instance_ref(flatten=True, list_type="multi")
    @property
    def component_irefs(self) -> list[ComponentInSystemInstanceRef]:
        return self._component_irefs
```

**Before/After ARXML:**

**Flattened (`flatten=True`):**
```xml
<ASSEMBLY-SW-CONNECTOR>
  <PROVIDER-IREF>
    <CONTEXT-COMPONENT-REF DEST="...">/Path/To/Component</CONTEXT-COMPONENT-REF>
    <TARGET-P-PORT-REF DEST="...">/Path/To/Port</TARGET-P-PORT-REF>
  </PROVIDER-IREF>
</ASSEMBLY-SW-CONNECTOR>
```

**Non-flattened (`flatten=False`):**
```xml
<DELEGATION-SW-CONNECTOR>
  <INNER-PORT-IREF>
    <R-PORT-IN-COMPOSITION-INSTANCE-REF>
      <CONTEXT-COMPONENT-REF DEST="...">/Path/To/Component</CONTEXT-COMPONENT-REF>
      <TARGET-R-PORT-REF DEST="...">/Path/To/Port</TARGET-R-PORT-REF>
    </R-PORT-IN-COMPOSITION-INSTANCE-REF>
  </INNER-PORT-IREF>
</DELEGATION-SW-CONNECTOR>
```

**Multi-wrapper list (`list_type="multi"`):**
```xml
<SWC-TO-ECU-MAPPING>
  <COMPONENT-IREFS>
    <COMPONENT-IREF>
      <CONTEXT-COMPOSITION-REF DEST="...">...</CONTEXT-COMPOSITION-REF>
      <TARGET-COMPONENT-REF DEST="...">...</TARGET-COMPONENT-REF>
    </COMPONENT-IREF>
    <COMPONENT-IREF>
      <CONTEXT-COMPOSITION-REF DEST="...">...</CONTEXT-COMPOSITION-REF>
      <TARGET-COMPONENT-REF DEST="...">...</TARGET-COMPONENT-REF>
    </COMPONENT-IREF>
  </COMPONENT-IREFS>
</SWC-TO-ECU-MAPPING>
```

**Parameters:**
- `flatten` (bool): If `True`, children are flattened directly into wrapper. If `False`, wrapped in their own element. Default: `False`
- `list_type` (str): For list attributes only. `"single"` for single-wrapper, `"multi"` for multi-wrapper. Default: `"single"`

**Real-World Examples:**
- `AssemblySwConnector.provider_iref` / `requester_iref` (flattened)
- `DelegationSwConnector.inner_port_iref` (non-flattened)
- `SwcToEcuMapping.component_irefs` (multi-wrapper)
- `OperationInvokedEvent.data_receives` (instance ref list)

**Related Decorators:** `@ref_conditional()` (reference pattern variant)

---

### `@polymorphic()`

**Purpose:** Mark an attribute as polymorphic with wrapper element mapping for concrete implementations of abstract base classes.

**Use Case:** When an XML wrapper element contains a concrete implementation of an abstract base class.

**JSON Configuration:**
```json
{
  "attributes": {
    "value_spec": {
      "type": "ValueSpecification",
      "decorator": "polymorphic:{\"VALUE-SPEC\": \"ValueSpecification\"}"
    },
    "compu_internal_to_phys": {
      "type": "CompuContent",
      "decorator": "polymorphic:{\"COMPU-INTERNAL-TO-PHYS\": \"CompuContent\", \"COMPU-PHYS-TO-INTERNAL\": \"CompuContent\"}"
    }
  }
}
```

**Generated Python Code:**
```python
from armodel2.serialization.decorators import polymorphic

# Single mapping
class ConstantSpecification(ARElement):
    @polymorphic({"VALUE-SPEC": "ValueSpecification"})
    @property
    def value_spec(self) -> Optional[ValueSpecification]:
        return self._value_spec

# Multiple mappings
class CompuMethod(ARObject):
    @polymorphic({
        "COMPU-INTERNAL-TO-PHYS": "CompuContent",
        "COMPU-PHYS-TO-INTERNAL": "CompuContent"
    })
    compu_internal_to_phys: Optional[CompuContent] = None
```

**Before/After ARXML:**
```xml
<!-- Without polymorphic handling - would not know concrete type -->
<CONSTANT-SPECIFICATION>
  <VALUE-SPEC>
    <!-- Cannot determine which concrete class to deserialize -->
  </VALUE-SPEC>
</CONSTANT-SPECIFICATION>

<!-- With @polymorphic({"VALUE-SPEC": "ValueSpecification"}) -->
<CONSTANT-SPECIFICATION>
  <VALUE-SPEC>
    <NUMERICAL-VALUE-SPECIFICATION>
      <SHORT-LABEL>MyValue</SHORT-LABEL>
      <VALUE>42</VALUE>
    </NUMERICAL-VALUE-SPECIFICATION>
  </VALUE-SPEC>
</CONSTANT-SPECIFICATION>
```

**Deserialization Process:**
1. Find child element (`<NUMERICAL-VALUE-SPECIFICATION>`)
2. Resolve concrete class (`NumericalValueSpecification`)
3. Validate it's a subclass of `ValueSpecification` (from mapping)
4. Deserialize using concrete class

**Real-World Examples:**
- `ConstantSpecification.value_spec` → `src/armodel2/models/M2/AUTOSARTemplates/CommonStructure/Constants/constant_specification.py`
- `VariableDataPrototype.init_value`
- `CompuMethod.compu_internal_to_phys` / `compu_phys_to_internal`
- `DiagnosticCondition.condition`

**Related Decorators:** None (standalone)

---

## Decorator Processing

### How the Generator Reads Decorator Configurations

The code generator (`tools/generate_models/generators.py`) processes decorator configurations from JSON metadata files:

**Parsing Decorator Specifications:**
```python
# From generators.py lines 79-100
if "decorator" in attr_info:
    decorator_spec = attr_info["decorator"]
    if ":" in decorator_spec:
        decorator_name, params = decorator_spec.split(":", 1)
        attr_meta["decorator_name"] = decorator_name
        attr_meta["decorator_params"] = params
    else:
        decorator_name = decorator_spec
        attr_meta["decorator_name"] = decorator_spec
        attr_meta["decorator_params"] = None
```

**Auto-Detection of YS→IES Pattern:**
```python
# Auto-detect attributes ending in "ies" with "*" multiplicity
if (
    attr_name.lower().endswith("ies")
    and attr_info.get("multiplicity") == "*"
):
    snake_name = to_snake_case(attr_name)
    xml_tag = snake_name.upper().replace("_", "-")
    legacy_tag = f"{xml_tag[:-3]}YS"
    attr_meta["decorator_name"] = "xml_element_name"
    attr_meta["decorator_params"] = legacy_tag
```

**Class-Level Decorator Detection:**
```python
# ATP type detection from JSON
atp_type = class_info.get("atp_type")
if atp_type == "atpVariation":
    # Generate @atp_variant()
elif atp_type == "atpMixed":
    # Generate @atp_mixed()
```

### Decorator Parameter Parsing

Different decorators use different parameter formats:

| Decorator           | Parameter Format      | Example                                                                         |
| ------------------- | --------------------- | ------------------------------------------------------------------------------- |
| `@xml_attribute`    | Optional custom name  | `"xml_attribute:T"`                                                             |
| `@xml_element_name` | Single XML tag        | `"xml_element_name:PROVIDED-ENTRYS"`                                            |
| `@ref_conditional`  | Single XML tag        | `"ref_conditional:FIBEX-ELEMENTS"`                                              |
| `@lang_prefix`      | Single XML tag        | `"lang_prefix:L-4"`                                                             |
| `@lang_abbr`        | Single attribute name | `"lang_abbr:L"`                                                                 |
| `@instance_ref`     | Key=value pairs       | `"instance_ref:flatten=True"` or `"instance_ref:flatten=False,list_type=multi"` |
| `@polymorphic`      | JSON dictionary       | `"polymorphic:{\"VALUE-SPEC\": \"ValueSpecification\"}"`                        |
| `@atp_variant`      | No parameters         | Class-level only                                                                |
| `@atp_mixed`        | No parameters         | Class-level only                                                                |

### Code Generation Patterns

The generator produces different code patterns based on decorator type:

**Simple Attribute Decorators:**
```python
@decorator_name("params")
@property
def attribute_name(self) -> Type:
    return self._attribute_name
```

**Class-Level Decorators:**
```python
@decorator_name()
class ClassName(ParentClass):
    ...
```

**Property with Setter:**
```python
@decorator_name("params")
@property
def attribute_name(self) -> Type:
    return self._attribute_name

@attribute_name.setter
def attribute_name(self, value: Type) -> None:
    self._attribute_name = value
```

---

## Best Practices

### When to Use Each Decorator

**Decision Tree:**

```
Is the attribute an XML attribute instead of element?
├─ Yes → Use @xml_attribute
└─ No
   └─ Is it a class-level wrapper pattern?
      ├─ Yes → Use @atp_variant() or @atp_mixed()
      └─ No
         └─ Does XML use non-standard element name?
            ├─ Yes → Use @xml_element_name()
            └─ No
               └─ Is it a reference with special wrapper?
                  ├─ Yes → Use @ref_conditional() or @instance_ref()
                  └─ No
                     └─ Is it polymorphic (abstract base class)?
                        ├─ Yes → Use @polymorphic()
                        └─ No
                           └─ Is it language-specific?
                              ├─ Yes → Use @lang_prefix() or @lang_abbr()
                              └─ No → Use default serialization
```

**Use Case Mapping:**

| Scenario                    | Decorator           | Example                            |
| --------------------------- | ------------------- | ---------------------------------- |
| XML attribute               | `@xml_attribute`    | `<AUTOSAR SCHEMA-VERSION="4.5.0">` |
| Non-standard plural         | `@xml_element_name` | `entries` → `<ENTRYS>`             |
| atpVariation wrapper        | `@atp_variant()`    | `<SW-DATA-DEF-PROPS-VARIANTS>`     |
| atpMixed container          | `@atp_mixed()`      | `SwRecordLayoutGroupContent`       |
| REF-CONDITIONAL pattern     | `@ref_conditional`  | `<FIBEX-ELEMENT-REF-CONDITIONAL>`  |
| Instance reference          | `@instance_ref`     | `<PROVIDER-IREF>`                  |
| Language-specific element   | `@lang_prefix`      | `<L-4>`                            |
| Language abbreviation       | `@lang_abbr`        | `L="EN"`                           |
| Polymorphic deserialization | `@polymorphic`      | `<VALUE-SPEC>` wrapper             |

### Common Pitfalls

**1. Forgetting @xml_attribute for metadata:**
```python
# WRONG - Schema version serializes as element
@property
def schema_version(self) -> str:
    return self._schema_version
# Result: <AUTOSAR><SCHEMA-VERSION>4.5.0</SCHEMA-VERSION></AUTOSAR>

# CORRECT
@xml_attribute
@property
def schema_version(self) -> str:
    return self._schema_version
# Result: <AUTOSAR SCHEMA-VERSION="4.5.0"></AUTOSAR>
```

**2. Using @xml_element_name for standard plurals:**
```python
# WRONG - Unnecessary decorator
@xml_element_name("DATA-TYPOSE")  # Standard plural works fine
data_types: list[DataType] = []

# CORRECT - Let NameConverter handle it
data_types: list[DataType] = []
# Result: <DATA-TYPES> (auto-generated)
```

**3. Confusing @atp_variant with @atp_mixed:**
```python
# @atp_variant - Adds wrapper structure
@atp_variant()
class SwDataDefProps:
    # Result: <SW-DATA-DEF-PROPS><SW-DATA-DEF-PROPS-VARIANTS>...

# @atp_mixed - Direct serialization (no wrapper)
@atp_mixed()
class SwRecordLayoutGroupContent:
    # Result: <SW-RECORD-LAYOUT-GROUP-CONTENT> (no wrapper)
```

**4. Wrong instance_ref parameters:**
```python
# WRONG - Missing list_type for lists
@instance_ref(flatten=True)
component_irefs: list[ComponentInSystemInstanceRef] = []

# CORRECT - Specify list_type for lists
@instance_ref(flatten=True, list_type="multi")
component_irefs: list[ComponentInSystemInstanceRef] = []
```

**5. Incorrect polymorphic mapping format:**
```json
// WRONG - Invalid JSON format
"decorator": "polymorphic:{VALUE-SPEC: ValueSpecification}"

// CORRECT - Proper JSON escaping
"decorator": "polymorphic:{\"VALUE-SPEC\": \"ValueSpecification\"}"
```

### Testing Guidelines

**Testing Decorator Behavior:**

1. **Write ARXML round-trip tests:**
```python
def test_atp_variant_roundtrip():
    # Create object
    obj = SwDataDefPropsBuilder().with_short_name("Test").build()

    # Serialize
    elem = obj.serialize()

    # Deserialize
    restored = SwDataDefProps.deserialize(elem)

    # Verify
    assert restored.short_name == obj.short_name
```

2. **Verify XML structure:**
```python
def test_xml_attribute():
    obj = AUTOSAR()
    obj.schema_version = "4.5.0"
    elem = obj.serialize()
    assert elem.get("SCHEMA-VERSION") == "4.5.0"  # Attribute, not element
    assert elem.find("SCHEMA-VERSION") is None  # No child element
```

3. **Test decorator combinations:**
```python
def test_ref_conditional_in_atp_variant():
    # Reference conditional inside atp_variant wrapper
    obj = SystemBuilder().with_short_name("Test").build()
    elem = obj.serialize()
    # Verify nested structure
    assert elem.find("FIBEX-ELEMENTS") is not None
    assert elem.find("FIBEX-ELEMENTS/FIBEX-ELEMENT-REF-CONDITIONAL") is not None
```

**Binary Comparison Tests:**
Use `PYTHONPATH=./src python -m pytest tests/integration/test_binary_comparison.py` to verify read/write cycles produce identical XML.

---

## Migration Guide

### Adding New Decorators

**1. Define Decorator in `decorators.py`:**
```python
def new_decorator(param: str) -> Callable[[Any], Any]:
    """Decorator documentation with usage examples.

    Args:
        param: Parameter description

    Returns:
        Decorator function
    """
    def decorator(attr_or_func: Any) -> Any:
        attr_or_func._marker_name = True  # type: ignore
        attr_or_func._param_value = param  # type: ignore
        return attr_or_func
    return decorator
```

**2. Update Generator in `generators.py`:**
```python
# Add to decorator parsing logic
if attr_meta.get("decorator_name") == "new_decorator":
    params = attr_meta.get("decorator_params")
    # Generate appropriate code
```

**3. Add JSON Configuration:**
```json
{
  "attributes": {
    "my_attribute": {
      "type": "MyType",
      "decorator": "new_decorator:param_value"
    }
  }
}
```

**4. Update This Documentation:**
- Add entry to Decorator Overview table
- Add complete reference section
- Update decision tree
- Add examples

### Modifying Existing Decorator Configurations

**To change decorator parameters:**
```json
// Before
"decorator": "instance_ref:flatten=True"

// After
"decorator": "instance_ref:flatten=False"
```

Then regenerate:
```bash
python -m tools.generate_models --members
```

**To add decorator to existing attribute:**
```json
{
  "attributes": {
    "existing_attr": {
      "type": "SomeType",
      "multiplicity": "*",
      "decorator": "xml_element_name:CUSTOM-NAME"  // Add this line
    }
  }
}
```

**To remove decorator:**
Delete the `"decorator"` key from JSON configuration and regenerate.

### When to Regenerate

Regenerate model classes after:
- Adding/modifying decorator configurations in JSON
- Modifying decorator implementation in `decorators.py`
- Changing decorator generation logic in `generators.py`

**Regeneration Command:**
```bash
python -m tools.generate_models --members --classes --enums --primitives
```

**Verification:**
```bash
# Lint
ruff check src/

# Type check
mypy src/

# Test
PYTHONPATH=./src python -m pytest
```

---

## Critical Files Reference

### Decorator Implementation

**File:** `src/armodel2/serialization/decorators.py`

All 9 decorators are implemented in this file with comprehensive docstrings.

### Code Generator

**File:** `tools/generate_models/generators.py`

**Lines 79-100:** Decorator parsing logic
**Lines 142-180:** Dispatch table generation for deserialization

### Real-World Examples

| Decorator           | Example File                                                                                                     | Line           |
| ------------------- | ---------------------------------------------------------------------------------------------------------------- | -------------- |
| `@xml_attribute`    | `src/armodel2/models/M2/AUTOSARTemplates/AutosarTopLevelStructure/autosar.py`                                    | ~45            |
| `@atp_variant`      | `src/armodel2/models/M2/AUTOSARTemplates/CommonStructure/McGroups/mc_group_data_ref_set.py`                      | 26             |
| `@lang_prefix`      | `src/armodel2/models/M2/MSR/Documentation/TextModel/MultilanguageData/multilanguage_long_name.py`                | ~40            |
| `@lang_abbr`        | `src/armodel2/models/M2/MSR/Documentation/TextModel/LanguageDataModel/language_specific.py`                      | 64-65 (manual) |
| `@xml_element_name` | `src/armodel2/models/M2/AUTOSARTemplates/BswModuleTemplate/BswOverview/bsw_module_description.py`                | 123, 134       |
| `@ref_conditional`  | `src/armodel2/models/M2/AUTOSARTemplates/SystemTemplate/system.py`                                               | 125            |
| `@instance_ref`     | `src/armodel2/models/M2/AUTOSARTemplates/SWComponentTemplate/Composition/assembly_sw_connector.py`               | 62, 73         |
| `@polymorphic`      | `src/armodel2/models/M2/AUTOSARTemplates/SWComponentTemplate/Datatype/DataPrototypes/variable_data_prototype.py` | 59             |

### JSON Configuration Files

**Location:** `docs/json/packages/*.classes.json`

Key files:
- `M2_AUTOSARTemplates_BswModuleTemplate_BswOverview.classes.json` - `@xml_element_name`, `@atp_variant`
- `M2_AUTOSARTemplates_SystemTemplate.classes.json` - `@ref_conditional`
- `M2_AUTOSARTemplates_SWComponentTemplate_Composition.classes.json` - `@instance_ref`
- `M2_MSR_Documentation_TextModel_MultilanguageData.classes.json` - `@lang_prefix`
- `M2_MSR_Documentation_TextModel_LanguageDataModel.classes.json` - `@lang_abbr`

### ARXML Test Fixtures

**Location:** `demos/validated/` and `tests/fixtures/arxml/`

Use these files to verify decorator behavior produces correct XML output.

---

## Summary

The decorator system is a powerful mechanism for handling AUTOSAR XML serialization edge cases. By understanding when and how to use each decorator, you can:

1. **Configure decorators correctly** in JSON metadata files
2. **Debug serialization issues** by identifying missing or incorrect decorators
3. **Add new decorators** or modify existing configurations
4. **Generate correct ARXML** that complies with AUTOSAR schema specifications

Remember:
- **95% of classes don't need decorators** - use reflection-based serialization
- **Decorators are for edge cases** - XML attributes, special wrappers, non-standard naming
- **Always verify ARXML output** - use binary comparison tests
- **Never edit generated code** - fix the generator and regenerate

For questions or issues, refer to the implementation files listed in Critical Files Reference.
