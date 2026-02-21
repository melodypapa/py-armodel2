# ARObject Serialization Refactoring - Implementation Plan

**Date**: 2026-02-21
**Status**: In Progress
**Related**: docs/plans/todo.md

## Objectives

This refactoring aims to improve the maintainability and consistency of the ARObject serialization framework by:

1. **Simplifying ARObject** - ARObject should only handle `checksum` and `timestamp` serialization, not reflection-based serialization of all attributes
2. **Extracting Helper Methods** - Move all helper functions from ARObject to a dedicated `SerializationHelper` class
3. **Ensuring Proper Inheritance** - All inherited classes must call `super().serialize()` and `super().deserialize()` to properly inherit parent attributes
4. **Updating Skip Classes** - All classes in `tools/skip_classes.yaml` should follow the same inheritance pattern
5. **Maintaining Generated Code** - Ensure all modifications are done in the code generator, not in generated classes
6. **Passing All Tests** - Ensure all pytest test cases pass after refactoring

## Current State Analysis

### Issues with Current Implementation

#### 1. ARObject is Too Large
- **File**: `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ArObject/ar_object.py`
- **Size**: ~1375 lines of code
- **Problem**: ARObject contains both core serialization logic AND 20+ helper methods, violating Single Responsibility Principle

#### 2. Reflection-Based Serialization in ARObject
- **Problem**: ARObject.serialize() uses `vars(self)` to discover and serialize ALL attributes via reflection
- **Issue**: This means child classes don't need to call `super().serialize()`, which leads to inconsistent patterns
- **Expected**: ARObject should only serialize `checksum` and `timestamp`, child classes must call `super()`

#### 3. Inconsistent Inheritance Patterns
- **Good Pattern**: `Collection`, `ARPackage`, `CompuMethod` - Call `super().serialize()` and `super().deserialize()`
- **Bad Pattern**: `DocumentationBlock` - Does NOT call `super()`, misses checksum/timestamp
- **Special Case**: `ARRef` - Has custom serialization format, intentionally doesn't call `super()`

#### 4. Helper Methods Scattered
ARObject contains 20+ helper methods that should be in a separate utility class:
- `_get_xml_tag()`
- `_is_xml_attribute()`
- `_get_element_tag()`
- `_get_element_tag_path()`
- `_has_l_prefix()`
- `_get_l_prefix_tag()`
- `_serialize_l_prefix()`
- `_validate_deserialization()`
- `_is_xml_attribute_static()`
- `_import_class_by_name()`
- `_strip_namespace()`
- `_add_text_element()`
- `_extract_text()`
- `_unwrap_primitive()`
- `_extract_value()`
- `_find_child_element()`
- `_find_all_child_elements()`
- `_deserialize_by_tag()`
- `_deserialize_with_type()`
- `_serialize_item()`
- `_get_atp_variant_wrapper_path()`

### Classes in skip_classes.yaml

| Class | Current Pattern | Action Required |
|-------|----------------|-----------------|
| AUTOSAR | Root element, no parent | No change |
| ARObject | Base class, reflection-based | Simplify to only handle checksum/timestamp |
| ARRef | Custom serialization (DEST attribute) | No change - special case |
| BaseType | Need to verify | Add super() calls if needed |
| CompuMethod | Already calls super() | Verify and ensure correct |
| Compu, CompuScales, etc. | Need to verify | Add super() calls |
| ARPackage | Already calls super() | Verify and ensure correct |
| LanguageSpecific series | Need to verify | Add super() calls |
| LLongName, LPlainText, etc. | Need to verify | Add super() calls |
| Item | Already calls super() | Verify and ensure correct |
| DocumentationBlock | **Does NOT call super()** | **Add super() calls** |

## Proposed Solution

### Architecture Changes

#### Before (Current)
```
ARObject (1375 lines)
├── serialize() - Reflection-based, handles ALL attributes
├── deserialize() - Reflection-based, handles ALL attributes
└── 20+ helper methods

Child Classes
├── Some call super().serialize() ✅
├── Some don't call super().serialize() ❌
└── Inconsistent inheritance patterns
```

#### After (Refactored)
```
ARObject (simplified, ~200 lines)
├── serialize() - Only handles checksum and timestamp
├── deserialize() - Only handles checksum and timestamp
└── No helper methods

SerializationHelper (new file)
└── 20+ static helper methods

Child Classes
├── ALL must call super().serialize() ✅
├── ALL must call super().deserialize() ✅
└── Consistent inheritance patterns
```

### Design Decisions

#### 1. SerializationHelper Design
- **Location**: `src/armodel/serialization/serialization_helper.py`
- **Type**: All methods are `@staticmethod`
- **Rationale**: Helper methods don't need instance state, static methods are simpler to use

#### 2. ARObject Simplification
- `serialize()` only serializes `checksum` (child element) and `timestamp` (XML attribute)
- `deserialize()` only deserializes `checksum` and `timestamp`
- All other serialization logic moved to child classes via `super()` calls

#### 3. Inheritance Pattern
All child classes (except special cases like ARRef) must follow this pattern:

```python
def serialize(self) -> ET.Element:
    tag = SerializationHelper.get_xml_tag(self.__class__)
    elem = ET.Element(tag)

    # 1. Call parent's serialize to handle inherited attributes
    parent_elem = super(ClassName, self).serialize()
    elem.attrib.update(parent_elem.attrib)
    for child in parent_elem:
        elem.append(child)

    # 2. Serialize own attributes
    # ...

    return elem

@classmethod
def deserialize(cls, element: ET.Element) -> "ClassName":
    # 1. Call parent's deserialize to handle inherited attributes
    obj = super(ClassName, cls).deserialize(element)

    # 2. Parse own attributes
    # ...

    return obj
```

#### 4. Special Cases
- **ARRef**: Keep as-is - has custom serialization format (DEST attribute + text content)
- **AUTOSAR**: Keep as-is - root element with no parent

## Detailed Implementation Steps

### Step 1: Create SerializationHelper Class

**File**: `src/armodel/serialization/serialization_helper.py` (NEW)

Extract all helper methods from ARObject:

```python
"""Serialization helper utilities for ARObject.

This module provides static utility methods for XML serialization and deserialization
of AUTOSAR model objects. These methods were extracted from ARObject to improve
code organization and maintainability.
"""

import xml.etree.ElementTree as ET
from typing import TYPE_CHECKING, Any, Optional, Union, get_type_hints

from armodel.serialization.decorators import atp_variant, l_prefix, xml_attribute
from armodel.serialization.model_factory import ModelFactory
from armodel.serialization.name_converter import NameConverter

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import (
        ARObject,
    )


class SerializationHelper:
    """Static utility methods for XML serialization and deserialization."""

    @staticmethod
    def get_atp_variant_wrapper_path(class_name: str) -> str:
        """Derive wrapper path for atpVariation classes from class name.

        Examples:
            SwDataDefProps → "SW-DATA-DEF-PROPS-VARIANTS/SW-DATA-DEF-PROPS-CONDITIONAL"
        """
        class_tag = NameConverter.to_xml_tag(class_name)
        return f"{class_tag}-VARIANTS/{class_tag}-CONDITIONAL"

    @staticmethod
    def get_xml_tag(cls: type) -> str:
        """Get XML tag name for a class."""
        return NameConverter.to_xml_tag(cls.__name__)

    @staticmethod
    def is_xml_attribute(obj: Any, attr_name: str) -> bool:
        """Check if a property has @xml_attribute decorator."""
        prop = getattr(type(obj), attr_name, None)
        return hasattr(prop, '_xml_attribute') and prop._xml_attribute

    # ... all other helper methods ...
```

**Methods to extract**:
1. `get_atp_variant_wrapper_path()` - Derive atpVariant wrapper path
2. `get_xml_tag()` - Get XML tag from class name
3. `is_xml_attribute()` - Check for @xml_attribute decorator
4. `get_element_tag()` - Get element tag for attribute
5. `get_element_tag_path()` - Get full element tag path
6. `has_l_prefix()` - Check for @l_prefix decorator
7. `get_l_prefix_tag()` - Get l_prefix tag name
8. `serialize_l_prefix()` - Serialize l_prefix wrapped elements
9. `validate_deserialization()` - Validate deserialization
10. `is_xml_attribute_static()` - Static version of attribute check
11. `import_class_by_name()` - Import class by qualified name
12. `strip_namespace()` - Remove namespace from XML tag
13. `add_text_element()` - Add text element to parent
14. `extract_text()` - Extract text content
15. `unwrap_primitive()` - Unwrap primitive type
16. `extract_value()` - Extract value from element
17. `find_child_element()` - Find single child element
18. `find_all_child_elements()` - Find all child elements
19. `deserialize_by_tag()` - Deserialize by XML tag
20. `deserialize_with_type()` - Deserialize by type hint
21. `serialize_item()` - Serialize single item

### Step 2: Refactor ARObject

**File**: `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ArObject/ar_object.py`

#### Simplified serialize() method

```python
def serialize(self) -> ET.Element:
    """Serialize object to XML element.

    Only serializes checksum and timestamp attributes.
    Child classes must call super().serialize() to inherit these attributes.

    Returns:
        xml.etree.ElementTree.Element representing this object
    """
    from armodel.serialization.serialization_helper import SerializationHelper

    tag = SerializationHelper.get_xml_tag(self.__class__)
    elem = ET.Element(tag)

    # Serialize timestamp (XML attribute)
    if self._timestamp is not None:
        elem.set("T", str(self._timestamp))

    # Serialize checksum (child element)
    if self._checksum is not None:
        checksum_elem = ET.Element("CHECKSUM")
        checksum_elem.text = str(self._checksum)
        elem.append(checksum_elem)

    return elem
```

#### Simplified deserialize() method

```python
@classmethod
def deserialize(cls, element: ET.Element) -> "ARObject":
    """Deserialize XML element to ARObject.

    Only deserializes checksum and timestamp attributes.
    Child classes must call super().deserialize() to inherit these attributes.

    Args:
        element: XML element to deserialize from

    Returns:
        Deserialized ARObject object
    """
    from armodel.serialization.serialization_helper import SerializationHelper

    obj = cls.__new__(cls)
    obj.__init__()

    # Deserialize timestamp (XML attribute)
    timestamp_str = element.get("T")
    if timestamp_str is not None:
        obj.timestamp = timestamp_str

    # Deserialize checksum (child element)
    from armodel.serialization.serialization_helper import SerializationHelper
    checksum_elem = SerializationHelper.find_child_element(element, "CHECKSUM")
    if checksum_elem is not None and checksum_elem.text:
        obj.checksum = checksum_elem.text

    return obj
```

#### Remove all helper methods
Delete all methods starting with `_` (helper methods) from ARObject.

### Step 3: Update DocumentationBlock

**File**: `src/armodel/models/M2/MSR/Documentation/BlockElements/documentation_block.py`

#### Add super().serialize() call

```python
def serialize(self) -> ET.Element:
    """Serialize DocumentationBlock to XML element.

    Returns:
        xml.etree.ElementTree.Element representing this object
    """
    from armodel.serialization.serialization_helper import SerializationHelper

    # Get XML tag name for this class
    tag = SerializationHelper.get_xml_tag(self.__class__)
    elem = ET.Element(tag)

    # NEW: Call parent's serialize to handle inherited attributes (checksum, timestamp)
    parent_elem = super(DocumentationBlock, self).serialize()
    elem.attrib.update(parent_elem.attrib)
    for child in parent_elem:
        elem.append(child)

    # Serialize def_list_ref
    # ... rest of existing serialization code ...
```

#### Add super().deserialize() call

```python
@classmethod
def deserialize(cls, element: ET.Element) -> "DocumentationBlock":
    """Deserialize XML element to DocumentationBlock object.

    Args:
        element: XML element to deserialize from

    Returns:
        Deserialized DocumentationBlock object
    """
    # NEW: Call parent's deserialize first to handle inherited attributes
    obj = super(DocumentationBlock, cls).deserialize(element)

    # Parse def_list_ref
    # ... rest of existing deserialization code ...
```

### Step 4: Update Other Skip Classes

For each class in `tools/skip_classes.yaml` (except AUTOSAR, ARObject, ARRef):

1. **Verify** if the class already calls `super().serialize()` and `super().deserialize()`
2. **Add** super() calls if missing
3. **Update** imports to use `SerializationHelper` instead of `ARObject._method()`

#### Priority Order
1. **High Priority**: DocumentationBlock (currently missing super() calls)
2. **Medium Priority**: LanguageSpecific series, Compu series, BaseType
3. **Low Priority**: ARPackage, Item, CompuMethod (verify existing super() calls)

### Step 5: Update Imports Across Codebase

Search and replace all calls to `ARObject._helper_method()` with `SerializationHelper.helper_method()`:

```bash
# Search for usage
rg "ARObject\._" src/

# Update imports in affected files
# Add: from armodel.serialization.serialization_helper import SerializationHelper
# Replace: ARObject._method() with SerializationHelper.method()
```

### Step 6: Update Code Generator (if needed)

**File**: `tools/generate_models/generators.py`

Verify that:
1. `_generate_ar_object_methods()` generates simplified ARObject (no reflection)
2. Generated code uses `SerializationHelper` static methods
3. No changes needed for generated classes (they already call super() correctly)

### Step 7: Verification Pipeline

After implementation, run the full verification pipeline:

```bash
# 1. Regenerate models (if code generator changed)
python -m tools.generate_models --members --classes --enums --primitives

# 2. Regenerate YAML mappings (if model structure changed)
python tools/generate_model_mappings.py

# 3. Run linting
ruff check src/ tools/

# 4. Run type checking
mypy src/

# 5. Run all tests
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest

# 6. Run binary comparison tests (critical for serialization verification)
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/integration/test_binary_comparison.py -v

# 7. Run integration tests
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/integration/test_autosar_datatypes.py -v
```

## Files to Modify

### New Files
1. `src/armodel/serialization/serialization_helper.py` - NEW

### Modified Files
1. `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ArObject/ar_object.py`
2. `src/armodel/models/M2/MSR/Documentation/BlockElements/documentation_block.py`
3. `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/StandardizationTemplate/compu_method.py`
4. All other skip classes in `tools/skip_classes.yaml`:
   - `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ARPackage/ar_package.py`
   - `src/armodel/models/M2/MSR/AsamHdo/ComputationMethod/compu.py`
   - `src/armodel/models/M2/MSR/AsamHdo/ComputationMethod/compu_scales.py`
   - `src/armodel/models/M2/MSR/AsamHdo/ComputationMethod/compu_scale.py`
   - `src/armodel/models/M2/MSR/AsamHdo/ComputationMethod/compu_const.py`
   - `src/armodel/models/M2/MSR/AsamHdo/ComputationMethod/compu_const_text_content.py`
   - `src/armodel/models/M2/MSR/Documentation/TextModel/MultilanguageData/language_specific.py`
   - `src/armodel/models/M2/MSR/Documentation/TextModel/LanguageDataModel/l_long_name.py`
   - `src/armodel/models/M2/MSR/Documentation/TextModel/LanguageDataModel/l_plain_text.py`
   - `src/armodel/models/M2/MSR/Documentation/TextModel/LanguageDataModel/l_paragraph.py`
   - `src/armodel/models/M2/MSR/Documentation/TextModel/LanguageDataModel/l_overview_paragraph.py`
   - `src/armodel/models/M2/MSR/Documentation/TextModel/LanguageDataModel/l_verbatim.py`
   - `src/armodel/models/M2/MSR/Documentation/TextModel/LanguageDataModel/mixed_content_for_unit_names.py`
   - `src/armodel/models/M2/MSR/Documentation/BlockElements/ListElements/item.py`
5. Any generated or manually maintained files that call `ARObject._helper_method()`
6. `tools/generate_models/generators.py` (if needed)

### Files NOT to Modify
1. `src/armodel/models/M2/AUTOSARTemplates/AutosarTopLevelStructure/autosar.py` - Root element, keep as-is
2. `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ArObject/ar_ref.py` - Special case, keep as-is
3. All generated model files in `src/armodel/models/M2/` (except the manually maintained ones above)

## Expected Outcomes

### Before Refactoring
- ARObject: ~1375 lines with reflection-based serialization
- DocumentationBlock: Missing super() calls, checksum/timestamp not serialized
- Inconsistent inheritance patterns across skip classes
- 20+ helper methods mixed with core logic in ARObject

### After Refactoring
- ARObject: ~200 lines, only handles checksum/timestamp
- SerializationHelper: New utility class with 20+ static methods
- All skip classes properly call super().serialize() and super().deserialize()
- Consistent inheritance patterns across codebase
- All tests pass including binary comparison tests

## Risk Assessment

### High Risk
- **DocumentationBlock super() calls**: This is currently broken (checksum/timestamp not serialized), so fixing it should be safe
- **SerializationHelper extraction**: Must ensure all helper methods are correctly moved

### Medium Risk
- **Skip classes updates**: Must verify each class's parent and ensure correct super() pattern
- **Import updates**: Must find all uses of `ARObject._method()` and replace correctly

### Low Risk
- **Generated classes**: Already call super() correctly, no changes needed
- **ARRef and AUTOSAR**: Special cases confirmed to keep as-is

## Rollback Plan

If issues arise during implementation:

1. **Git revert**: Each major change can be reverted individually:
   ```bash
   git revert <commit-hash>
   ```

2. **Feature branches**: Create a feature branch for this work:
   ```bash
   git checkout -b feat/arobject-serialization-refactoring
   ```

3. **Incremental testing**: Test after each major step to catch issues early

## Success Criteria

The refactoring is considered successful when:

1. ✅ ARObject.serialize() and deserialize() only handle checksum and timestamp
2. ✅ All helper methods are in SerializationHelper class
3. ✅ All skip classes (except special cases) call super().serialize() and super().deserialize()
4. ✅ No code in generated model files is manually edited
5. ✅ All pytest tests pass:
   - Unit tests
   - Integration tests
   - Binary comparison tests (critical for serialization verification)
6. ✅ Linting passes: `ruff check src/ tools/`
7. ✅ Type checking passes: `mypy src/`
8. ✅ Round-trip serialization produces identical binary output for all ARXML files

## Timeline Estimate

- Step 1: Create SerializationHelper - 2-3 hours
- Step 2: Refactor ARObject - 1-2 hours
- Step 3: Update DocumentationBlock - 30 minutes
- Step 4: Update other skip classes - 2-3 hours
- Step 5: Update imports - 1-2 hours
- Step 6: Update code generator (if needed) - 1 hour
- Step 7: Verification and debugging - 2-4 hours

**Total Estimated Time**: 10-16 hours

## References

- Original todo: `docs/plans/todo.md`
- AGENTS.md: Project architecture and conventions
- Current implementation: `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ArObject/ar_object.py`
- Skip classes: `tools/skip_classes.yaml`
- Binary comparison tests: `tests/integration/test_binary_comparison.py`