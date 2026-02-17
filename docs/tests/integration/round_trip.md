# Integration Test: Round-Trip Serialization

## Overview

The round-trip integration test validates the complete read → verify → write → read → verify cycle for ARXML files. This ensures that the serialization/deserialization pipeline preserves data integrity correctly.

## Test File

**Main Test**: `tests/integration/test_round_trip.py`

This single file contains all round-trip integration tests organized into test methods.

## Test Data

**Source File**: `demos/arxml/AUTOSAR_Datatypes.arxml`

This file contains:
- 1 root package: `AUTOSAR_Platform`
- 4 nested packages: `BaseTypes`, `CompuMethods`, `DataConstrs`, `ImplementationDataTypes`
- 43 total elements across all packages
- AUTOSAR schema version: 4.0 (namespace: `http://autosar.org/schema/r4.0`)

## Test Scenarios

### 1. Read and Verify Structure

**File**: `test_round_trip_read.py`

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

**File**: `test_round_trip_write.py`

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

### 3. Count Preservation

**File**: `test_round_trip_compare.py`

**Purpose**: Verify that package and element counts are preserved through round-trip.

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

### 4. Serialize-Deserialize Symmetry

**File**: `test_round_trip_symmetry.py`

**Purpose**: Verify that the serialize and deserialize operations are symmetric.

**Steps**:
1. Load original ARXML file
2. Serialize to XML string
3. Parse XML string back to object
4. Verify structure is preserved

**Expected Results**:
- All structure verified successfully
- No data loss in round-trip

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
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/integration/test_round_trip_read.py -v
```

### Run Specific Test Case

```bash
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/integration/test_round_trip_read.py::TestRoundTripRead::test_read_and_verify -v
```

## Test Coverage

The integration tests cover:

- ✅ Reading ARXML files with `ARXMLReader`
- ✅ Writing ARXML files with `ARXMLWriter`
- ✅ Structure preservation through round-trip
- ✅ Package count preservation
- ✅ Element count preservation
- ✅ Serialize-deserialize symmetry
- ⏸️ Exact XML match (blocked by tag name issue, documented above)

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
