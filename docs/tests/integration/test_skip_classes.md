# Skip Classes Integration Tests

## Overview

This document describes integration tests for manually maintained (skipped) classes listed in `tools/skip_classes.yaml`. These classes are not auto-generated and require manual testing to ensure they work correctly with the optimized serialization framework.

## Background

The code generator (`tools/generate_models.py`) automatically generates Python classes from AUTOSAR schema definitions. However, some classes are too complex or require special handling, so they are manually maintained and listed in `tools/skip_classes.yaml`.

## Skip Classes List

### Root and Base Classes

1. **AUTOSAR** - Root AUTOSAR element
2. **ARObject** - Base class with reflection-based serialization framework
3. **ARRef** - AUTOSAR references with DEST attribute

### Base Type Classes

4. **BaseType** - Abstract base class for SwBaseType

### Data Definition Properties

5. **SwDataDefProps** - SW-DATA-DEF-PROPS-VARIANTS/SW-DATA-DEF-PROPS-CONDITIONAL wrappers

### Computation Method Classes

6. **CompuMethod** - Computation method with custom wrappers
7. **Compu** - Base computation class
8. **CompuScales** - Computation scales
9. **CompuScale** - Single computation scale
10. **CompuConst** - Computation constant
11. **CompuConstTextContent** - Text content for computation constant

### Language-Specific Classes (L-1, L-2, L-4, L-5, L-10)

12. **MultiLanguagePlainText** - Plain text in multiple languages
13. **MultilanguageLongName** - Long names in multiple languages
14. **MultiLanguageParagraph** - Paragraphs in multiple languages
15. **MultiLanguageOverviewParagraph** - Overview paragraphs
16. **MultiLanguageVerbatim** - Verbatim text

### Package Classes

17. **ARPackage** - Package with long_name handling

### Language Attribute Classes

18. **LanguageSpecific** - Language-specific with L attribute
19. **LLongName** - Long name with language
20. **LPlainText** - Plain text with language
21. **LParagraph** - Paragraph with language
22. **LOverviewParagraph** - Overview paragraph with language
23. **LVerbatim** - Verbatim text with language

## Test Coverage

### Test Suite: TestCompuMethodClasses

**Test IDs**: SWITS-INT-0300 to SWITS-INT-0310

Tests the CompuMethod class and related computation classes that handle COMPU-INTERNAL-TO-PHYS and COMPU-PHYS-TO-INTERNAL wrapper elements.

**Tests**:
- `test_compu_method_deserialization` - Validates CompuMethod loads from ARXML
- `test_compu_method_serialization` - Validates CompuMethod round-trip serialization

**Test Files**:
- demos/arxml/AUTOSAR_Datatypes.arxml
- demos/arxml/AUTOSAR_MOD_AISpecification_CompuMethod_Blueprint.arxml

### Test Suite: TestLanguageSpecificClasses

**Test IDs**: SWITS-INT-0320 to SWITS-INT-0330

Tests language-specific classes that handle hyphenated XML tag names (L-1, L-2, L-4, L-5, L-10).

**Tests**:
- `test_multilanguage_elements_present` - Validates L-2 elements are present
- `test_language_specific_round_trip` - Validates language elements survive round-trip

**Test Files**:
- demos/arxml/AUTOSAR_MOD_AISpecification_ApplicationDataType_Blueprint.arxml

### Test Suite: TestARPackageClass

**Test IDs**: SWITS-INT-0340 to SWITS-INT-0345

Tests ARPackage class with custom long_name attribute handling.

**Tests**:
- `test_ar_package_long_name` - Validates long_name is preserved
- `test_ar_package_serialization` - Validates AR-PACKAGE serialization

**Test Files**:
- demos/arxml/AUTOSAR_Datatypes.arxml
- demos/arxml/AUTOSAR_MOD_AISpecification_CompuMethod_Blueprint.arxml

### Test Suite: TestArgumentDirectionEnum

**Test IDs**: SWITS-INT-0350 to SWITS-INT-0355

Tests ArgumentDirectionEnum enum values and serialization.

**Tests**:
- `test_enum_values_exist` - Validates enum values (IN, INOUT, OUT) exist
- `test_enum_serialization` - Validates enum serialization/deserialization

**Known Issues**:
- Enum values are lowercase ("in", "inout", "out") but may serialize as uppercase ("IN", "INOUT", "OUT")
- Deserialization normalizes to lowercase member values

### Test Suite: TestARRefClass

**Test IDs**: SWITS-INT-0360 to SWITS-INT-0365

Tests ARRef class for AUTOSAR references.

**Tests**:
- `test_ar_ref_basic_usage` - Validates ARRef creation and DEST attribute

### Test Suite: TestBaseTypeClass

**Test IDs**: SWITS-INT-0370 to SWITS-INT-0375

Tests BaseType abstract base class and SwBaseType subclasses.

**Tests**:
- `test_basetype_loading` - Validates SwBaseType objects load correctly

**Test Files**:
- demos/arxml/AUTOSAR_MOD_AISpecification_BaseTypes_Standard.arxml

### Test Suite: TestSwDataDefPropsClass

**Test IDs**: SWITS-INT-0380 to SWITS-INT-0385

Tests SwDataDefProps with SW-DATA-DEF-PROPS wrapper handling.

**Tests**:
- `test_sw_data_def_props_loading` - Validates SW-DATA-DEF-PROPS elements load

**Test Files**:
- demos/arxml/AUTOSAR_MOD_AISpecification_ApplicationDataType_Blueprint.arxml

### Test Suite: TestARObjectClass

**Test IDs**: SWITS-INT-0390 to SWITS-INT-0399

Tests ARObject base class and serialization framework helper methods.

**Tests**:
- `test_ar_object_helper_methods` - Validates _find_child_element, _find_all_child_elements, _strip_namespace
- `test_ar_object_inheritance_chain` - Validates inheritance-based deserialization

## Running Tests

### Run All Skip Classes Tests

```bash
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/integration/test_skip_classes.py -v
```

### Run Specific Test Suite

```bash
# CompuMethod tests
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/integration/test_skip_classes.py::TestCompuMethodClasses -v

# ArgumentDirectionEnum tests
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/integration/test_skip_classes.py::TestArgumentDirectionEnum -v

# ARObject helper methods
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/integration/test_skip_classes.py::TestARObjectClass::test_ar_object_helper_methods -v
```

## Test Results

### Latest Test Run

**Total**: 13 tests
- ✅ **Passed**: 12
- ⏭️ **Skipped**: 1
- ❌ **Failed**: 0

### Pass Rate

92% pass rate (12/13 tests, 1 skipped)

## Known Issues

### 1. ArgumentDirectionEnum Case Sensitivity

**Issue**: Enum values are defined as lowercase ("in", "inout", "out") but may serialize as uppercase ("IN", "INOUT", "OUT").

**Impact**: Binary comparison tests fail because serialized XML uses uppercase.

**Workaround**: The `AREnum.deserialize()` method normalizes both cases to member values.

**Future Fix**: Update `AREnum.serialize()` to use lowercase values matching member definitions.

### 2. Missing Classes

**Issue**: Some classes in skip_classes.yaml may not be tested yet.

**Impact**: Untested classes may have serialization issues.

**Workaround**: Tests focus on critical classes (CompuMethod, ARPackage, enums).

**Future Fix**: Add tests for remaining skip classes as needed.

## Related Tests

- `tests/integration/test_binary_comparison.py` - Binary comparison tests for all ARXML files
- `tests/integration/test_autosar_datatypes.py` - Structure validation tests
- `tests/unit/test_reader.py` - Reader unit tests
- `tests/unit/test_writer.py` - Writer unit tests

## References

- Skip Classes Config: `tools/skip_classes.yaml`
- Code Generator: `tools/generate_models.py`
- ARObject Implementation: `src/armodel2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ArObject/ar_object.py`
- AREnum Implementation: `src/armodel2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes/ar_enum.py`
