# Binary Comparison Integration Tests

## Overview

This document describes the integration tests for binary comparison of ARXML round-trip serialization. These tests validate that the optimized serialization framework preserves all data correctly during read/write operations.

## Test Purpose

Ensure that:
1. All ARXML files can be read correctly with the optimized deserialization framework
2. All ARXML files can be written back identically
3. No data is lost or corrupted during round-trip serialization
4. The optimized framework produces binary-exact output

## Test Files

- **Test Module**: `tests/integration/test_binary_comparison.py`
- **SWITS IDs**: SWITS-INT-0100 through SWITS-INT-0299
- **Test Data**: All ARXML files in `demos/arxml/` (24 files)

## Test Coverage

### Test Suite: TestBinaryComparison

#### Test: `test_all_arxml_files_binary_comparison` (SWITS-INT-0100)

**Purpose**: Test all ARXML files for binary exact round-trip serialization.

**Process**:
1. Load each ARXML file from `demos/arxml/`
2. Deserialize to Python objects using optimized framework
3. Serialize back to XML
4. Perform binary comparison with original file
5. Report any differences with detailed diagnostics

**Assertions**:
- All 24 ARXML files must pass binary comparison
- Original bytes must equal serialized bytes

**Expected Result**: ✅ All files produce identical binary output

#### Test: `test_autosar_datatypes_detailed` (SWITS-INT-0101)

**Purpose**: Detailed test for AUTOSAR_Datatypes.arxml with comprehensive diagnostics.

**Process**:
1. Load AUTOSAR_Datatypes.arxml
2. Deserialize and count packages/elements
3. Serialize back to XML
4. Perform detailed line-by-line comparison
5. Show differences with context

**Assertions**:
- Binary comparison must succeed
- No line differences allowed

**Expected Result**: ✅ Binary exact match

### Test Suite: TestIndividualFiles

#### Test: `test_critical_files_binary_comparison` (SWITS-INT-0200)

**Purpose**: Test critical ARXML files with parameterized testing.

**Test Files**:
- AUTOSAR_Datatypes.arxml
- AUTOSAR_MOD_AISpecification_CompuMethod_Blueprint.arxml
- AUTOSAR_MOD_AISpecification_DataConstr_Blueprint.arxml
- AUTOSAR_MOD_AISpecification_Unit_Standard.arxml

**Assertions**: Each file must produce binary exact output

## Test Data

### ARXML Files Tested

1. AUTOSAR_Datatypes.arxml
2. AUTOSAR_MOD_AISpecification_ApplicationDataType_Blueprint.arxml
3. AUTOSAR_MOD_AISpecification_ApplicationDataType_LifeCycle_Standard.arxml
4. AUTOSAR_MOD_AISpecification_BaseTypes_Standard.arxml
5. AUTOSAR_MOD_AISpecification_Collection_Body_Blueprint.arxml
6. AUTOSAR_MOD_AISpecification_Collection_Chassis_Blueprint.arxml
7. AUTOSAR_MOD_AISpecification_Collection_MmedTelmHmi_Blueprint.arxml
8. AUTOSAR_MOD_AISpecification_Collection_OccptPedSfty_Blueprint.arxml
9. AUTOSAR_MOD_AISpecification_Collection_Pt_Blueprint.arxml
10. AUTOSAR_MOD_AISpecification_CompuMethod_Blueprint.arxml
11. AUTOSAR_MOD_AISpecification_CompuMethod_LifeCycle_Standard.arxml
12. AUTOSAR_MOD_AISpecification_DataConstr_Blueprint.arxml
13. AUTOSAR_MOD_AISpecification_DataConstr_LifeCycle_Standard.arxml
14. AUTOSAR_MOD_AISpecification_KeywordSet_Blueprint.arxml
15. AUTOSAR_MOD_AISpecification_Keyword_LifeCycle_Standard.arxml
16. AUTOSAR_MOD_AISpecification_PhysicalDimension_LifeCycle_Standard.arxml
17. AUTOSAR_MOD_AISpecification_PhysicalDimension_Standard.arxml
18. AUTOSAR_MOD_AISpecification_PortInterface_Blueprint.arxml
19. AUTOSAR_MOD_AISpecification_PortInterface_LifeCycle_Standard.arxml
20. AUTOSAR_MOD_AISpecification_PortPrototypeBlueprint_Blueprint.arxml
21. AUTOSAR_MOD_AISpecification_PortPrototypeBlueprint_LifeCycle_Standard.arxml
22. AUTOSAR_MOD_AISpecification_SwComponentTypes_Blueprint.arxml
23. AUTOSAR_MOD_AISpecification_Unit_LifeCycle_Standard.arxml
24. AUTOSAR_MOD_AISpecification_Unit_Standard.arxml

## Running Tests

### Run All Binary Comparison Tests

```bash
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/integration/test_binary_comparison.py -v
```

### Run Specific Test

```bash
# Test all files
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/integration/test_binary_comparison.py::TestBinaryComparison::test_all_arxml_files_binary_comparison -v

# Test AUTOSAR_Datatypes detailed
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/integration/test_binary_comparison.py::TestBinaryComparison::test_autosar_datatypes_detailed -v

# Test critical files
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/integration/test_binary_comparison.py::TestIndividualFiles -v
```

### Run with Detailed Output

```bash
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/integration/test_binary_comparison.py -v -s
```

## Success Criteria

- ✅ All 24 ARXML files pass binary comparison
- ✅ Original bytes == Serialized bytes for all files
- ✅ No data loss or corruption
- ✅ Line-by-line comparison shows no differences

## Troubleshooting

### Test Failures

If a test fails:

1. **Check file size differences**:
   - Original vs Serialized size
   - Large differences indicate structural issues

2. **Review line differences**:
   - Test output shows first 10 differences
   - Check for formatting, ordering, or content issues

3. **Validate XML structure**:
   ```bash
   xmllint --format demos/arxml/FILENAME.arxml > /tmp/original.xml
   xmllint --format /tmp/FILENAME_output.arxml > /tmp/serialized.xml
   diff /tmp/original.xml /tmp/serialized.xml
   ```

4. **Check specific elements**:
   - Compare element counts
   - Verify attribute preservation
   - Check text content

### Common Issues

1. **Whitespace differences**: Pretty-printing may cause differences
2. **Attribute ordering**: XML attributes may be in different order
3. **Namespace declarations**: May appear in different locations
4. **Text encoding**: Ensure UTF-8 encoding consistency

## Related Tests

- `tests/integration/test_autosar_datatypes.py` - Structure validation tests
- `tests/unit/test_reader.py` - Reader unit tests
- `tests/unit/test_writer.py` - Writer unit tests

## References

- AUTOSAR XML Schema: `demos/xsd/AUTOSAR_00046.xsd`
- Reader Implementation: `src/armodel/reader/__init__.py`
- Writer Implementation: `src/armodel/writer/__init__.py`
- Serialization Framework: `src/armodel/serialization/`
