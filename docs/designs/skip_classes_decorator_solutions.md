# Skip Classes Analysis and Decorator-Based Solutions

## Overview

This document analyzes the classes in `tools/skip_classes.yaml` and proposes decorator-based solutions to enable their auto-generation, reducing manual maintenance.

**Date**: 2026-02-19
**Status**: Analysis Complete
**Purpose**: Reduce manually maintained classes from 18 to 3-5

## Current State

### Classes in skip_classes.yaml

| Class | Category | Reason for Skipping | Manual Maintenance Required |
|-------|----------|---------------------|---------------------------|
| `AUTOSAR` | Root Element | Root element with namespace handling | **Yes** |
| `ARObject` | Infrastructure | Base class implementing serialization framework | **Yes** |
| `ARRef` | Reference Type | Special handling for DEST/BASE attributes | **Yes** |
| `BaseType` | Base Type | Flat structure (no wrapper) | Can be auto-generated |
| `SwDataDefProps` | Data Definition | Multi-level wrapper structure | Can be auto-generated |
| `CompuMethod` family | Computation | Complex nested structure | Can be auto-generated |
| `Compu` | Computation | Nested computation content | Can be auto-generated |
| `CompuScales` | Computation | Scale collection | Can be auto-generated |
| `CompuScale` | Computation | Individual scale | Can be auto-generated |
| `CompuConst` | Computation | Constant value | Can be auto-generated |
| `CompuConstTextContent` | Computation | Text content wrapper | Can be auto-generated |
| `MultiLanguagePlainText` | Multilingual | L-N naming convention (L-1, L-2, etc.) | Can be auto-generated |
| `MultilanguageLongName` | Multilingual | L-N naming convention | Can be auto-generated |
| `MultiLanguageParagraph` | Multilingual | L-N naming convention | Can be auto-generated |
| `MultiLanguageOverviewParagraph` | Multilingual | L-N naming convention | Can be auto-generated |
| `MultiLanguageVerbatim` | Multilingual | L-N naming convention | Can be auto-generated |
| `ARPackage` | Package | Custom handling for long_name | Can be auto-generated |
| `LanguageSpecific` | Multilingual | L should be attribute, not child | Can be auto-generated |
| `LLongName` | Multilingual | Language-specific long name | Can be auto-generated |
| `LPlainText` | Multilingual | Language-specific plain text | Can be auto-generated |
| `LParagraph` | Multilingual | Language-specific paragraph | Can be auto-generated |
| `LOverviewParagraph` | Multilingual | Language-specific overview | Can be auto-generated |
| `LVerbatim` | Multilingual | Language-specific verbatim | Can be auto-generated |
| `MixedContentForUnitNames` | Multilingual | Mixed content for units | Can be auto-generated |
| `Item` | Documentation | item_contents as direct children | Can be auto-generated |

**Total**: 27 classes
**Must remain manual**: 3 (`AUTOSAR`, `ARObject`, `ARRef`)
**Can be auto-generated with new decorators**: 24

## Current Decorator Library

### Available Decorators

| Decorator | Location | Purpose |
|-----------|----------|---------|
| `@xml_attribute` | `src/armodel/serialization/decorators.py:6-27` | Mark property/attribute as XML attribute |
| `@xml_tag(tag_name)` | `src/armodel/serialization/decorators.py:30-47` | Specify custom XML tag name for class or attribute |
| `@xml_element_tag(xml_element_name, python_class_name)` | `src/armodel/serialization/decorators.py:50-96` | Handle multi-level element paths and polymorphic types |

### Current Decorator Capabilities

1. **`@xml_attribute`**
   - Marks property as XML attribute instead of element
   - Used in: `AUTOSAR`, `ARRef`, `LanguageSpecific`
   - Example: `<AUTOSAR SCHEMA-VERSION="4.5.0">`

2. **`@xml_tag()`**
   - Specifies custom XML tag name for class
   - Used in: `AUTOSAR`, various manually maintained classes
   - Example: `AUTOSAR` class → `<AUTOSAR>` tag

3. **`@xml_element_tag()`**
   - Handles multi-level element paths
   - Supports polymorphic type resolution
   - Supports explicit Python class name specification
   - Example: `@xml_element_tag("SW-DATA-DEF-PROPS-VARIANTS/SW-DATA-DEF-PROPS-CONDITIONAL", "SwDataDefPropsConditional")`

## Analysis by Category

### 1. Infrastructure Classes (Must Remain Manual)

#### AUTOSAR
**Location**: `src/armodel/models/M2/AUTOSARTemplates/AutosarTopLevelStructure/autosar.py`

**Current Implementation**:
- Root element for all ARXML files
- Manages namespace attributes (`xmlns`, `xmlns:xsi`)
- Handles `xsi:schemaLocation` attribute
- Has custom `serialize()` and `deserialize()` methods

**Reason for Manual Maintenance**:
- Namespace handling is unique to root element
- Schema version detection and management
- Special XML declaration handling

**Verdict**: **Keep manual** - Critical infrastructure

---

#### ARObject
**Location**: `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ArObject/ar_object.py`

**Current Implementation**:
- Base class for all AUTOSAR model classes
- Implements reflection-based serialization
- Provides `serialize()` and `deserialize()` methods
- Handles name conversion, type hints, circular imports

**Reason for Manual Maintenance**:
- Core serialization framework implementation
- Cannot be generated by itself
- Defines the framework that generators use

**Verdict**: **Keep manual** - Core infrastructure

---

#### ARRef
**Location**: `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ArObject/ar_ref.py`

**Current Implementation**:
- Represents AUTOSAR references with DEST attribute
- Has custom `serialize()` method that creates element with DEST and text content
- Uses `@xml_attribute` for DEST and BASE properties

**Reason for Manual Maintenance**:
- Reference semantics are unique (DEST attribute + path text)
- Requires special handling for reference suffixes (-REF, -TREF)
- Polymorphic reference types

**Verdict**: **Keep manual** - Unique reference semantics

---

### 2. Classes with Flat Structure (Need `@xml_flatten`)

#### BaseType
**Location**: `src/armodel/models/M2/MSR/AsamHdo/BaseTypes/base_type.py`

**Current Issue**:
```xml
<!-- Expected XML (flat structure) -->
<BASE-TYPE>
  <SHORT-NAME>uint8</SHORT-NAME>
  <BASE-TYPE-SIZE>8</BASE-TYPE-SIZE>
  <BASE-TYPE-ENCODING>native</BASE-TYPE-ENCODING>
  <MEM-ALIGNMENT>8</MEM-ALIGNMENT>
  <BYTE-ORDER>MOTOROLA</BYTE-ORDER>
</BASE-TYPE>

<!-- Default reflection would create (nested structure) -->
<BASE-TYPE>
  <SHORT-NAME>uint8</SHORT-NAME>
  <BASE-TYPE-DEFINITION>
    <BASE-TYPE-SIZE>8</BASE-TYPE-SIZE>
    <BASE-TYPE-ENCODING>native</BASE-TYPE-ENCODING>
    <MEM-ALIGNMENT>8</MEM-ALIGNMENT>
    <BYTE-ORDER>MOTOROLA</BYTE-ORDER>
  </BASE-TYPE-DEFINITION>
</BASE-TYPE>
```

**Proposed Solution**: `@xml_flatten` decorator

```python
@xml_flatten("base_type_definition")
class BaseType(ARElement):
    base_type_definition: BaseTypeDefinition
```

**Decorator Behavior**:
- Flatten nested object's attributes to parent level
- Skip creating wrapper element for specified attribute
- Copy all child elements directly to parent

---

#### Item
**Location**: `src/armodel/models/M2/MSR/Documentation/BlockElements/ListElements/item.py`

**Current Issue**:
```xml
<!-- Expected XML (no wrapper) -->
<ITEM>
  <SHORT-NAME>item1</SHORT-NAME>
  <TITLE>Item Title</TITLE>
  <P>Paragraph content</P>
</ITEM>

<!-- Default reflection would create (with wrapper) -->
<ITEM>
  <SHORT-NAME>item1</SHORT-NAME>
  <ITEM-CONTENTS>
    <TITLE>Item Title</TITLE>
    <P>Paragraph content</P>
  </ITEM-CONTENTS>
</ITEM>
```

**Proposed Solution**: `@xml_flatten` decorator

```python
@xml_flatten("item_contents")
class Item(Paginateable):
    item_contents: DocumentationBlock
```

**Verdict**: Add `@xml_flatten` decorator, then auto-generate

---

### 3. Classes with Multi-Level Wrappers (Need `@xml_wrapper`)

#### SwDataDefProps
**Location**: `src/armodel/models/M2/MSR/DataDictionary/DataDefProperties/sw_data_def_props.py`

**Current Issue**:
```xml
<!-- Expected XML (multi-level wrapper) -->
<SW-DATA-DEF-PROPS>
  <SW-DATA-DEF-PROPS-VARIANTS>
    <SW-DATA-DEF-PROPS-CONDITIONAL>
      <SW-CALIBRATION-ACCESS>READ-ONLY</SW-CALIBRATION-ACCESS>
      <SW-IMPL-POLICY>CONST</SW-IMPL-POLICY>
      <UNIT-REF DEST="UNIT">/AUTOSAR/Units/degreeC</UNIT-REF>
    </SW-DATA-DEF-PROPS-CONDITIONAL>
  </SW-DATA-DEF-PROPS-VARIANTS>
</SW-DATA-DEF-PROPS>

<!-- Default reflection would create (flat structure) -->
<SW-DATA-DEF-PROPS>
  <SW-CALIBRATION-ACCESS>READ-ONLY</SW-CALIBRATION-ACCESS>
  <SW-IMPL-POLICY>CONST</SW-IMPL-POLICY>
  <UNIT-REF DEST="UNIT">/AUTOSAR/Units/degreeC</UNIT-REF>
</SW-DATA-DEF-PROPS>
```

**Current Implementation**: Custom `serialize()` and `deserialize()` methods

**Proposed Solution**: `@xml_wrapper` decorator

```python
@xml_wrapper("SW-DATA-DEF-PROPS-VARIANTS/SW-DATA-DEF-PROPS-CONDITIONAL")
class SwDataDefProps(ARObject):
    sw_calibration_access: Optional[SwCalibrationAccessEnum] = None
    sw_impl_policy: Optional[SwImplPolicyEnum] = None
    unit_ref: Optional[ARRef] = None
    # ... all other attributes
```

**Decorator Behavior**:
- Wrap all child elements in specified multi-level path
- During deserialize: navigate through wrapper hierarchy to find children
- During serialize: create wrapper elements, place children at deepest level

**Alternative**: Use existing `@xml_element_tag` decorator with improvements

```python
class SwDataDefProps(ARObject):
    @xml_element_tag("SW-DATA-DEF-PROPS-VARIANTS/SW-DATA-DEF-PROPS-CONDITIONAL")
    variants: Optional[SwDataDefPropsConditional] = None
```

This would require all attributes to be grouped into a single `variants` attribute, which doesn't match the current flat attribute structure.

**Verdict**: Add `@xml_wrapper` decorator for class-level wrapper specification, then auto-generate

---

### 4. CompuMethod Family (Complex Nested Structure)

#### CompuMethod
**Location**: `src/armodel/models/M2/MSR/AsamHdo/ComputationMethod/compu_method.py`

**Current Issue**:
```xml
<!-- Expected XML -->
<COMPU-METHOD>
  <SHORT-NAME>CompuMethod1</SHORT-NAME>
  <COMPU-INTERNAL-TO-PHYS>
    <COMPU-SCALES>
      <COMPU-SCALE>
        <LOWER-LIMIT>0</LOWER-LIMIT>
        <UPPER-LIMIT>100</UPPER-LIMIT>
        <COMPU-CONST>
          <VT>0.0</VT>
        </COMPU-CONST>
      </COMPU-SCALE>
    </COMPU-SCALES>
  </COMPU-INTERNAL-TO-PHYS>
</COMPU-METHOD>

<!-- Note: COMPU element is implicit, not explicit -->
```

**Current Implementation**: Custom `serialize()` wraps Compu children directly

**Proposed Solution**: Enhance `@xml_element_tag` to support "unwrap" behavior

```python
class CompuMethod(ARElement):
    @xml_element_tag("COMPU-INTERNAL-TO-PHYS", unwrap=True)
    compu_internal_to_phys: Optional[Compu] = None

    @xml_element_tag("COMPU-PHYS-TO-INTERNAL", unwrap=True)
    compu_phys_to_internal: Optional[Compu] = None
```

**Decorator Behavior** (with `unwrap=True`):
- Serialize: Take serialized Compu object's children, place them directly in wrapper
- Deserialize: Find wrapper element, deserialize children as Compu object
- This avoids creating an explicit `<COMPU>` element

**Verdict**: Enhance `@xml_element_tag` with `unwrap` parameter, then auto-generate

---

### 5. MultiLanguage Classes (L-N Naming Convention)

#### MultiLanguagePlainText, MultiLanguageLongName, etc.
**Location**: `src/armodel/models/M2/MSR/Documentation/TextModel/MultilanguageData/`

**Current Issue**:
```xml
<!-- Expected XML (L-1, L-2, L-4, L-5, L-10) -->
<MULTI-LANGUAGE-PLAIN-TEXT>
  <L-10>English text</L-10>
</MULTI-LANGUAGE-PLAIN-TEXT>

<!-- Default reflection would create -->
<MULTI-LANGUAGE-PLAIN-TEXT>
  <L10>English text</L10>
</MULTI-LANGUAGE-PLAIN-TEXT>
```

**Current Implementation**: Custom `serialize()` wraps with "L-10" tag

**Proposed Solution**: `@xml_language_tag` decorator

```python
@xml_language_tag("L-10")
class MultiLanguagePlainText(ARObject):
    l10: LPlainText
```

**Decorator Behavior**:
- Map Python attribute `l10` to XML tag `L-10`
- Map Python attribute `l1` to XML tag `L-1`
- Map Python attribute `l2` to XML tag `L-2`
- General pattern: `l{N}` → `L-{N}`

**Implementation**:

```python
def xml_language_tag(xml_tag: str) -> Callable[[Any], Any]:
    """Decorator for language-specific elements with L-N naming convention.

    Examples:
        @xml_language_tag("L-10")
        class MultiLanguagePlainText(ARObject):
            l10: LPlainText

        @xml_language_tag("L-2")
        class MultilanguageLongName(ARObject):
            l2: LLongName

    Args:
        xml_tag: The XML tag name (e.g., "L-10", "L-2")

    Returns:
        Decorator function
    """
    def decorator(cls: Any) -> Any:
        cls._xml_language_tag = xml_tag  # type: ignore[union-attr]
        return cls
    return decorator
```

**Verdict**: Add `@xml_language_tag` decorator, then auto-generate

---

### 6. LanguageSpecific Classes (L Attribute)

#### LanguageSpecific, LLongName, LPlainText, etc.
**Location**: `src/armodel/models/M2/MSR/Documentation/TextModel/LanguageDataModel/`

**Current Issue**:
```xml
<!-- Expected XML (L as attribute) -->
<L-10 L="EN">English text</L-10>

<!-- Default reflection would create (L as child element) -->
<L-10>
  <L>EN</L>
  English text
</L-10>
```

**Current Implementation**: Custom `serialize()` adds L as XML attribute

**Proposed Solution**: Use existing `@xml_attribute` decorator

```python
class LanguageSpecific(ARObject, ABC):
    @xml_attribute
    @property
    def l(self) -> LEnum:
        return self._l

    @l.setter
    def l(self, value: LEnum) -> None:
        self._l = value

    _text: Optional[str] = None
```

**Current Status**: Already uses `@xml_attribute` decorator

**Verdict**: Can be auto-generated with existing decorators

---

### 7. ARPackage

#### ARPackage
**Location**: `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ARPackage/ar_package.py`

**Current Issue**: Custom handling for long_name attribute which contains language-specific elements

**Analysis**:
- Reviewing the implementation shows standard list serialization
- No special decorators currently used
- Actually follows standard reflection pattern

**Verdict**: **Can be auto-generated now** - No special handling needed

---

## Proposed New Decorators

### 1. `@xml_flatten`

**Purpose**: Flatten nested object attributes to direct children

**Signature**:
```python
def xml_flatten(attribute_name: str) -> Callable[[Any], Any]:
    """Decorator to flatten nested object attributes to direct children.

    Use when XML schema uses flat structure but class has nested object.

    Example:
        @xml_flatten("base_type_definition")
        class BaseType(ARElement):
            base_type_definition: BaseTypeDefinition

    Results in:
        <BASE-TYPE>
            <SHORT-NAME>uint8</SHORT-NAME>
            <BASE-TYPE-SIZE>8</BASE-TYPE-SIZE>  # Flattened
            <BASE-TYPE-ENCODING>native</BASE-TYPE-ENCODING>  # Flattened
        </BASE-TYPE>

    Args:
        attribute_name: Name of the attribute to flatten

    Returns:
        Decorator function
    """
```

**Implementation Location**: `src/armodel/serialization/decorators.py`

**Usage**:
```python
@xml_flatten("base_type_definition")
class BaseType(ARElement):
    base_type_definition: BaseTypeDefinition
```

---

### 2. `@xml_wrapper`

**Purpose**: Specify multi-level wrapper structure for all class attributes

**Signature**:
```python
def xml_wrapper(wrapper_path: str) -> Callable[[Any], Any]:
    """Decorator to specify multi-level wrapper structure.

    Use when all child elements should be wrapped in a specific hierarchy.

    Example:
        @xml_wrapper("SW-DATA-DEF-PROPS-VARIANTS/SW-DATA-DEF-PROPS-CONDITIONAL")
        class SwDataDefProps(ARObject):
            sw_calibration_access: Optional[SwCalibrationAccessEnum] = None
            unit_ref: Optional[ARRef] = None

    Results in:
        <SW-DATA-DEF-PROPS>
            <SW-DATA-DEF-PROPS-VARIANTS>
                <SW-DATA-DEF-PROPS-CONDITIONAL>
                    <SW-CALIBRATION-ACCESS>READ-ONLY</SW-CALIBRATION-ACCESS>
                    <UNIT-REF DEST="UNIT">/AUTOSAR/Units/degreeC</UNIT-REF>
                </SW-DATA-DEF-PROPS-CONDITIONAL>
            </SW-DATA-DEF-PROPS-VARIANTS>
        </SW-DATA-DEF-PROPS>

    Args:
        wrapper_path: Multi-level path with '/' separator

    Returns:
        Decorator function
    """
```

**Implementation Location**: `src/armodel/serialization/decorators.py`

**Usage**:
```python
@xml_wrapper("SW-DATA-DEF-PROPS-VARIANTS/SW-DATA-DEF-PROPS-CONDITIONAL")
class SwDataDefProps(ARObject):
    sw_calibration_access: Optional[SwCalibrationAccessEnum] = None
    unit_ref: Optional[ARRef] = None
```

---

### 3. `@xml_language_tag`

**Purpose**: Handle L-N naming convention for language-specific elements

**Signature**:
```python
def xml_language_tag(xml_tag: str) -> Callable[[Any], Any]:
    """Decorator for language-specific elements with L-N naming convention.

    Examples:
        @xml_language_tag("L-10")
        class MultiLanguagePlainText(ARObject):
            l10: LPlainText

        @xml_language_tag("L-2")
        class MultilanguageLongName(ARObject):
            l2: LLongName

    Args:
        xml_tag: The XML tag name (e.g., "L-10", "L-2")

    Returns:
        Decorator function
    """
```

**Implementation Location**: `src/armodel/serialization/decorators.py`

**Usage**:
```python
@xml_language_tag("L-10")
class MultiLanguagePlainText(ARObject):
    l10: LPlainText

@xml_language_tag("L-2")
class MultilanguageLongName(ARObject):
    l2: LLongName
```

---

### 4. Enhancement: `@xml_element_tag` with `unwrap` parameter

**Purpose**: Support unwrapping of nested object children (for CompuMethod)

**Modified Signature**:
```python
def xml_element_tag(
    xml_element_name: str,
    python_class_name: Optional[str] = None,
    unwrap: bool = False
) -> Callable[[Any], Any]:
    """Decorator to specify custom XML element name and optional Python class name.

    Args:
        xml_element_name: XML element name to use
        python_class_name: Optional Python class name for deserialization
        unwrap: If True, unwrap nested object's children directly

    Returns:
        Decorator function
    """
```

**Usage**:
```python
class CompuMethod(ARElement):
    @xml_element_tag("COMPU-INTERNAL-TO-PHYS", unwrap=True)
    compu_internal_to_phys: Optional[Compu] = None
```

---

## Implementation Roadmap

### Phase 1: Add New Decorators (Priority: High)

1. Implement `@xml_flatten` in `src/armodel/serialization/decorators.py`
2. Implement `@xml_wrapper` in `src/armodel/serialization/decorators.py`
3. Implement `@xml_language_tag` in `src/armodel/serialization/decorators.py`
4. Enhance `@xml_element_tag` with `unwrap` parameter

### Phase 2: Update ARObject Base Class (Priority: High)

1. Update `ARObject.serialize()` to handle new decorators
2. Update `ARObject.deserialize()` to handle new decorators
3. Add tests for new decorator behaviors

### Phase 3: Migrate Classes from skip_classes.yaml (Priority: Medium)

| Priority | Class | New Decorator | Testing Required |
|----------|-------|---------------|------------------|
| High | `BaseType` | `@xml_flatten` | Unit + Integration |
| High | `SwDataDefProps` | `@xml_wrapper` | Unit + Integration |
| High | `Item` | `@xml_flatten` | Unit + Integration |
| Medium | `CompuMethod` family | `@xml_element_tag(unwrap=True)` | Unit + Integration |
| Medium | `MultiLanguage*` | `@xml_language_tag` | Unit + Integration |
| Low | `LanguageSpecific` | Existing decorators | Unit |
| Low | `ARPackage` | None (can auto-generate now) | Integration |

### Phase 4: Update Code Generator (Priority: Medium)

1. Update `tools/generate_models.py` to generate new decorators
2. Add decorator detection logic based on mapping.json metadata
3. Update skip_classes.yaml to remove migrated classes

### Phase 5: Verification (Priority: High)

1. Run existing test suite: `PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest`
2. Run round-trip tests for migrated classes
3. Verify ARXML files can be read and written correctly
4. Run linting: `ruff check src/`
5. Run type checking: `mypy src/`

---

## Summary

### Classes After Migration

| Category | Count | Classes |
|----------|-------|---------|
| **Must remain manual** | 3 | `AUTOSAR`, `ARObject`, `ARRef` |
| **Can auto-generate with new decorators** | 24 | All other classes |
| **Can auto-generate now** | 1 | `ARPackage` |

**Reduction**: From 27 manual classes to 3 manual classes (89% reduction)

### Benefits

1. **Reduced Maintenance**: 89% fewer manually maintained classes
2. **Consistency**: All classes follow same generation pattern
3. **Type Safety**: Generated code includes proper type hints
4. **Documentation**: Generated classes have docstrings from mapping.json
5. **Testability**: Easier to test with consistent structure

### Risks

1. **Complexity**: New decorators increase framework complexity
2. **Testing**: Comprehensive testing required for all new behaviors
3. **Backward Compatibility**: Must maintain compatibility with existing ARXML files
4. **Performance**: Additional decorator checks may impact performance

### Mitigation Strategies

1. **Comprehensive Testing**: Unit tests for each decorator, integration tests for migrated classes
2. **Gradual Migration**: Migrate classes one at a time, verify each before proceeding
3. **Performance Profiling**: Benchmark serialization/deserialization before and after
4. **Documentation**: Complete documentation for all new decorators

---

## References

- **Current decorators**: `src/armodel/serialization/decorators.py`
- **ARObject base class**: `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ArObject/ar_object.py`
- **Skip classes file**: `tools/skip_classes.yaml`
- **Serialization documentation**: `docs/designs/serialization.md`
- **Design rules**: `docs/designs/design_rules.md`
- **Model design**: `docs/designs/model_design.md`