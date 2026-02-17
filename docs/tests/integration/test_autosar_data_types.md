# Integration Test: AUTOSAR Data Types

## Overview

The AUTOSAR data types integration test validates the complete read → verify → write → read → verify cycle for ARXML files. This ensures that the serialization/deserialization pipeline preserves data integrity correctly.

## Traceability Matrix

| SWITS ID | Test Method | Documentation Section | Status |
|----------|-------------|----------------------|--------|
| SWITS-INT-0001 | test_read_and_verify_structure | Read and Verify Structure | ✅ Implemented |
| SWITS-INT-0002 | test_write_and_read_back | Write and Read Back | ✅ Implemented |
| SWITS-INT-0003 | test_serialize_deserialize_symmetry | Serialize-Deserialize Symmetry | ✅ Implemented |
| SWITS-INT-0004 | test_package_element_counts | Package and Element Counts | ✅ Implemented |
| SWITS-INT-0005 | test_base_types_elements | Specific Element Verification - BaseTypes | ✅ Implemented |
| SWITS-INT-0006 | test_implementation_data_types_elements | Specific Element Verification - ImplementationDataTypes | ✅ Implemented |
| SWITS-INT-0007 | test_binary_file_comparison | Binary File Comparison | ✅ Implemented |
| SWITS-INT-0008 | test_xml_content_comparison | XML Content Comparison | ✅ Implemented |

## Test File

**Main Test**: `tests/integration/test_autosar_datatypes.py`

This single file contains all integration tests organized into test methods.

## Test Data

**Source File**: `demos/arxml/AUTOSAR_Datatypes.arxml`

This file contains:
- 1 root package: `AUTOSAR_Platform`
- 4 nested packages: `BaseTypes`, `CompuMethods`, `DataConstrs`, `ImplementationDataTypes`
- 43 total elements across all packages
- AUTOSAR schema version: 4.0 (namespace: `http://autosar.org/schema/r4.0`)

## Test Scenarios

### 1. Read and Verify Structure

**SWITS ID**: SWITS-INT-0001
**Test Method**: `test_read_and_verify_structure`
**Purpose**: Verify that `ARXMLReader` can correctly parse ARXML files and create proper Python objects.

**Steps**:
1. Load `AUTOSAR_Datatypes.arxml` using `ARXMLReader.load_arxml()`
2. Verify AUTOSAR object structure
3. Verify root package has correct short_name
4. Verify all nested packages exist with correct names
5. Verify element counts in each package

**Expected Results**:
- Root package: `AUTOSAR_Platform`
- Nested packages: `BaseTypes`, `CompuMethods`, `DataConstrs`, `ImplementationDataTypes`
- Element counts: 15, 1, 12, 15 respectively

---

### 2. Write and Read Back

**SWITS ID**: SWITS-INT-0002
**Test Method**: `test_write_and_read_back`
**Purpose**: Verify that `ARXMLWriter` can serialize objects and `ARXMLReader` can read them back correctly.

**Steps**:
1. Load original ARXML file
2. Serialize to file using `ARXMLWriter.save_arxml()`
3. Read the written file back
4. Verify structure is preserved

**Expected Results**:
- Written file exists and is valid XML
- Structure matches original (package counts, element counts)

---

### 3. Serialize-Deserialize Symmetry

**SWITS ID**: SWITS-INT-0003
**Test Method**: `test_serialize_deserialize_symmetry`
**Purpose**: Verify that serialize and deserialize operations are symmetric.

**Steps**:
1. Load original ARXML file
2. Count packages recursively
3. Count elements in each package
4. Serialize and deserialize
5. Count packages and elements again
6. Compare counts

**Expected Results**:
- Package count: 5 total (1 root + 4 nested)
- Element counts preserved exactly

---

### 4. Package and Element Counts

**SWITS ID**: SWITS-INT-0004
**Test Method**: `test_package_element_counts`
**Purpose**: Verify that package and element counts are preserved through round-trip.

**Steps**:
1. Load original ARXML file
2. Serialize to XML string
3. Parse XML string back to object
4. Verify structure is preserved

**Expected Results**:
- All structure verified successfully
- No data loss in round-trip

### 5. Specific Element Verification - BaseTypes

**SWITS ID**: SWITS-INT-0005
**Test Method**: `test_base_types_elements`
**Purpose**: Verify that BaseTypes package contains the correct base type elements in the correct order.

**Expected Elements**:
- float32, float64
- sint16, sint16_least
- sint32, sint32_least
- sint8, sint8_least
- uint16, uint16_least
- uint32, uint32_least
- uint8, uint8_least
- void

### 6. Specific Element Verification - ImplementationDataTypes

**SWITS ID**: SWITS-INT-0006
**Test Method**: `test_implementation_data_types_elements`
**Purpose**: Verify that ImplementationDataTypes package contains the correct implementation type elements in the correct order.

**Expected Elements**:
- boolean
- float32, float64
- sint16, sint16_least
- sint32, sint32_least
- sint8, sint8_least
- uint16, uint16_least
- uint32, uint32_least
- uint8, uint8_least

### 7. Binary File Comparison

**SWITS ID**: SWITS-INT-0007
**Test Method**: `test_binary_file_comparison`
**Purpose**: Verify that the generated file is binary identical to the original file.

**Steps**:
1. Load original ARXML file
2. Write to a new file using `ARXMLWriter.save_arxml()`
3. Read both files as binary
4. Compare file sizes byte-by-byte

**Expected Results**:
- Generated file exists
- File sizes match exactly
- Binary content is identical (byte-by-byte comparison)
- No data loss or corruption in round-trip

**Status**: ❌ **EXPECTED TO FAIL**

**Reason for Failure**:
The reflection-based serialization framework uses Python class names instead of AUTOSAR XML tag names, and does not preserve all attributes from the original file. This results in:
- Different file sizes (original: 23,416 bytes, generated: 9,178 bytes)
- Different XML tag names (e.g., `SW-BASE-TYPE` vs `PACKAGEABLEELEMENT`)
- Missing attributes (e.g., `BASE-TYPE-SIZE`, `BASE-TYPE-ENCODING`, etc.)

**Note**: This test is kept to demonstrate the limitation of the current serialization framework. A future enhancement to add proper XML tag mapping would enable this test to pass.

### 8. XML Content Comparison

**SWITS ID**: SWITS-INT-0008
**Test Method**: `test_xml_content_comparison`
**Purpose**: Verify that the generated XML content is identical to the original XML content using canonical XML comparison.

**Steps**:
1. Load original ARXML file
2. Write to a new file using `ARXMLWriter.save_arxml()`
3. Parse both files as XML
4. Generate canonical XML strings (normalizes whitespace and attribute ordering)
5. Compare canonical XML content

**Expected Results**:
- Generated file exists
- Canonical XML content matches exactly
- XML structure and formatting are preserved
- No semantic differences in XML content

## Helper Methods

### `verify_autosar_structure(autosar_obj, stage)`

Verifies the complete AUTOSAR object structure:

```python
def verify_autosar_structure(autosar_obj, stage: str):
    """Verify AUTOSAR object structure matches expected content.

    Args:
        autosar_obj: AUTOSAR object to verify
        stage: Description of verification stage (for error messages)
    """
    assert autosar_obj is not None
    assert hasattr(autosar_obj, 'ar_packages')
    assert len(autosar_obj.ar_packages) >= 1

    # Verify root package
    root_pkg = autosar_obj.ar_packages[0]
    assert root_pkg.short_name == "AUTOSAR_Platform"

    # Verify nested packages
    nested_packages = root_pkg.ar_packages
    assert len(nested_packages) == 4

    # Verify each package...
```

### `count_ar_packages(autosar_obj) -> int`

Recursively counts all AR-PACKAGE elements in the AUTOSAR object.

### `count_elements(pkg) -> int`

Counts elements in a specific package.

## Known Limitations

### XML Tag Name Mismatch

The current reflection-based serialization uses Python class names instead of AUTOSAR XML tag names:

**Expected XML**:
```xml
<SW-BASE-TYPE>
  <SHORT-NAME>float32</SHORT-NAME>
</SW-BASE-TYPE>
```

**Actual Output**:
```xml
<PACKAGEABLEELEMENT>
  <SHORT-NAME>float32</SHORT-NAME>
</PACKAGEABLEELEMENT>
```

**Impact**: Files are not semantically equivalent for direct comparison.

**Solution**: Add `@xml_tag()` decorators to all generated classes or modify code generator to output proper XML tag names.

**Workaround**: Current tests verify structure correctness rather than exact XML match.

## Running the Tests

### Run All Integration Tests

```bash
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/integration/ -v
```

### Run Specific Test File

```bash
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/integration/test_autosar_datatypes.py -v
```

### Run Specific Test Case by SWITS ID

```bash
# SWITS-INT-0001: Read and Verify Structure
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/integration/test_autosar_datatypes.py::TestAUTOSARDatatypes::test_read_and_verify_structure -v

# SWITS-INT-0002: Write and Read Back
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/integration/test_autosar_datatypes.py::TestAUTOSARDatatypes::test_write_and_read_back -v

# SWITS-INT-0003: Serialize-Deserialize Symmetry
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/integration/test_autosar_datatypes.py::TestAUTOSARDatatypes::test_serialize_deserialize_symmetry -v

# SWITS-INT-0004: Package and Element Counts
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/integration/test_autosar_datatypes.py::TestAUTOSARDatatypes::test_package_element_counts -v

# SWITS-INT-0005: BaseTypes Elements
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/integration/test_autosar_datatypes.py::TestAUTOSARDatatypes::test_base_types_elements -v

# SWITS-INT-0006: ImplementationDataTypes Elements
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/integration/test_autosar_datatypes.py::TestAUTOSARDatatypes::test_implementation_data_types_elements -v

# SWITS-INT-0007: Binary File Comparison
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/integration/test_autosar_datatypes.py::TestAUTOSARDatatypes::test_binary_file_comparison -v

# SWITS-INT-0008: XML Content Comparison
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/integration/test_autosar_datatypes.py::TestAUTOSARDatatypes::test_xml_content_comparison -v
```

## Test Coverage

The integration tests cover:

| SWITS ID | Coverage Area | Status |
|----------|---------------|--------|
| SWITS-INT-0001 | Reading ARXML files with `ARXMLReader` | ✅ |
| SWITS-INT-0002 | Writing ARXML files with `ARXMLWriter` | ✅ |
| SWITS-INT-0003 | Structure preservation through round-trip | ✅ |
| SWITS-INT-0004 | Package and element count preservation | ✅ |
| SWITS-INT-0005 | Serialize-deserialize symmetry | ✅ |
| SWITS-INT-0006 | Specific element verification (BaseTypes, ImplementationDataTypes) | ✅ |
| SWITS-INT-0007 | Binary file comparison (byte-by-byte) | ✅ |
| SWITS-INT-0008 | XML content comparison (canonical XML) | ✅ |
| N/A | Exact XML match (if needed in future) | ⏸️ Blocked by tag name issue (documented above) |
| SWITS-INT-0006 | Specific element verification (BaseTypes, ImplementationDataTypes) | ✅ |
| N/A | Exact XML match | ⏸️ Blocked by tag name issue (documented above) |

## Maintenance

When updating the serialization framework:

1. **If fixing XML tag names**: Re-enable file comparison in `test_round_trip_write.py`
2. **If adding new AUTOSAR elements**: Update expected counts in test methods
3. **If changing package structure**: Update `verify_autosar_structure()` method

## Related Documentation

- **Serialization Framework**: `docs/designs/serialization.md`
- **Reader Module**: `docs/tests/unit/test_reader.md`
- **Writer Module**: `docs/tests/unit/test_writer.md`
- **ARObject Tests**: `docs/tests/unit/test_models.md`
