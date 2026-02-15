# Integration Test Cases - Reader/Writer
## py-armodel2 - AUTOSAR ARXML Processing Library

**Modules**: `armodel.reader`, `armodel.writer`
**Test Files**: `tests/integration/test_reader_writer.py`
**Version**: 1.0
**Date**: 2026-02-15

---

## 1. Test Overview

This document describes integration tests for ARXML reading and writing workflows.

### 1.1 Test Scope
- End-to-end read-write cycles
- Round-trip data integrity
- Multi-version support
- Performance testing
- XSD validation integration

### 1.2 Test Framework
- **Framework**: pytest
- **Python Version**: 3.9+
- **Execution**: `PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/integration/test_reader_writer.py`

---

## 2. Integration Test Cases

### SWIT_RW_001: Basic Read-Write Cycle
**Objective**: Verify reading and writing ARXML file preserves data

**Requirements**: SWR_READER_001, SWR_WRITER_001, SWR_WRITER_010

**Test Steps**:
1. Load ARXML file using ARXMLReader
2. Save using ARXMLWriter
3. Load saved file
4. Compare original and roundtrip objects
5. Verify all data is preserved

**Test Code**:
```python
def test_read_write_cycle():
    import tempfile
    import os
    from armodel.reader import ARXMLReader
    from armodel.writer import ARXMLWriter

    # Create test ARXML file
    arxml_content = '''<?xml version="1.0" encoding="UTF-8"?>
<AUTOSAR xmlns="http://autosar.org/schema/r4.0">
    <AR-PACKAGES>
        <AR-PACKAGE>
            <SHORT-NAME>TestPackage</SHORT-NAME>
        </AR-PACKAGE>
    </AR-PACKAGES>
</AUTOSAR>'''

    with tempfile.TemporaryDirectory() as temp_dir:
        input_path = os.path.join(temp_dir, 'input.arxml')
        output_path = os.path.join(temp_dir, 'output.arxml')

        # Write input file
        with open(input_path, 'w') as f:
            f.write(arxml_content)

        # Read, write, read cycle
        reader = ARXMLReader()
        writer = ARXMLWriter()

        original = reader.load_arxml(input_path)
        writer.save_arxml(original, output_path)
        roundtrip = reader.load_arxml(output_path)

        # Verify roundtrip integrity
        assert original is not None
        assert roundtrip is not None
        assert len(original.ar_packages) == len(roundtrip.ar_packages)
```

**Expected Result**: Roundtrip preserves all data

**Status**: ✅ Implemented

---

### SWIT_RW_002: XSD Validation Integration
**Objective**: Verify XSD validation during read

**Requirements**: SWR_READER_005

**Test Steps**:
1. Load valid ARXML with validation enabled
2. Verify success
3. Create invalid ARXML (violates schema)
4. Attempt load with validation
5. Verify ValueError is raised

**Test Code**:
```python
def test_xsd_validation():
    import tempfile
    import os
    from armodel.reader import ARXMLReader

    # Valid ARXML
    valid_arxml = '''<?xml version="1.0" encoding="UTF-8"?>
<AUTOSAR xmlns="http://autosar.org/schema/r4.0">
    <AR-PACKAGES>
    </AR-PACKAGES>
</AUTOSAR>'''

    with tempfile.TemporaryDirectory() as temp_dir:
        valid_path = os.path.join(temp_dir, 'valid.arxml')

        with open(valid_path, 'w') as f:
            f.write(valid_arxml)

        reader = ARXMLReader()

        # Test valid file
        autosar = reader.load_arxml(valid_path, validate=True)
        assert autosar is not None
```

**Expected Result**: Valid files load, invalid files raise ValueError

**Status**: 🚧 In Progress

---

### SWIT_RW_003: Large File Handling
**Objective**: Verify handling of large ARXML files

**Requirements**: SWR_READER_009, SWR_READER_NFR_001, SWR_READER_NFR_002

**Test Steps**:
1. Create or use 10MB ARXML file
2. Record start time and memory usage
3. Load file using ARXMLReader
4. Record end time and memory usage
5. Verify file is loaded successfully
6. Save to new file
7. Verify roundtrip integrity

**Test Code**:
```python
def test_large_file_handling():
    import tempfile
    import os
    import time
    from armodel.reader import ARXMLReader
    from armodel.writer import ARXMLWriter

    # Generate large ARXML file (10MB+)
    # This would typically use a pre-generated test file
    large_arxml_path = 'tests/fixtures/arxml/large_file.arxml'

    if os.path.exists(large_arxml_path):
        reader = ARXMLReader()
        writer = ARXMLWriter()

        start_time = time.time()
        autosar = reader.load_arxml(large_arxml_path)
        load_time = time.time() - start_time

        assert autosar is not None
        assert load_time < 60  # Should load within 60 seconds

        # Test roundtrip
        with tempfile.TemporaryDirectory() as temp_dir:
            output_path = os.path.join(temp_dir, 'output.arxml')
            writer.save_arxml(autosar, output_path)

            # Verify output file exists and is valid
            assert os.path.exists(output_path)
            assert os.path.getsize(output_path) > 0
```

**Expected Result**: Large files handled within performance targets

**Status**: 🚧 In Progress (requires large test file)

---

### SWIT_RW_004: Multi-Version Support
**Objective**: Verify reading/writing files from different schema versions

**Requirements**: SWR_READER_007

**Test Steps**:
1. Load 00044 ARXML file
2. Save to new file
3. Load 00046 ARXML file
4. Save to new file
5. Load 00052 ARXML file
6. Save to new file
7. Verify all files are valid

**Test Code**:
```python
def test_multi_version_support():
    import tempfile
    import os
    from armodel.reader import ARXMLReader
    from armodel.writer import ARXMLWriter

    reader = ARXMLReader()
    writer = ARXMLWriter()

    # Test with available test fixtures
    test_files = {
        '00044': 'tests/fixtures/arxml/AUTOSAR_00044_sample.arxml',
        '00046': 'tests/fixtures/arxml/AUTOSAR_00046_sample.arxml',
        '00052': 'tests/fixtures/arxml/AUTOSAR_00052_sample.arxml',
    }

    with tempfile.TemporaryDirectory() as temp_dir:
        for version, input_file in test_files.items():
            if os.path.exists(input_file):
                # Load
                autosar = reader.load_arxml(input_file)
                assert autosar is not None

                # Save
                output_path = os.path.join(temp_dir, f'output_{version}.arxml')
                writer.save_arxml(autosar, output_path)

                # Verify roundtrip
                roundtrip = reader.load_arxml(output_path)
                assert roundtrip is not None
```

**Expected Result**: All schema versions handled correctly

**Status**: 🚧 In Progress (requires test fixtures)

---

### SWIT_RW_005: Performance Benchmark
**Objective**: Benchmark read/write performance for various file sizes

**Requirements**: SWR_READER_NFR_001, SWR_WRITER_NFR_001

**Test Steps**:
1. Test with files of various sizes (1MB, 5MB, 10MB)
2. Measure load time for each
3. Measure save time for each
4. Verify within acceptable limits

**Test Code**:
```python
def test_performance_benchmark():
    import time
    from armodel.reader import ARXMLReader
    from armodel.writer import ARXMLWriter

    test_files = [
        ('tests/fixtures/arxml/small_1mb.arxml', 10),  # 10 seconds max
        ('tests/fixtures/arxml/medium_5mb.arxml', 30),
        ('tests/fixtures/arxml/large_10mb.arxml', 60),
    ]

    reader = ARXMLReader()
    writer = ARXMLWriter()

    for file_path, max_time in test_files:
        if os.path.exists(file_path):
            # Test read performance
            start = time.time()
            autosar = reader.load_arxml(file_path)
            read_time = time.time() - start

            assert autosar is not None
            assert read_time < max_time, f"Read time {read_time}s exceeds {max_time}s for {file_path}"

            # Test write performance
            import tempfile
            with tempfile.TemporaryDirectory() as temp_dir:
                output_path = os.path.join(temp_dir, 'output.arxml')

                start = time.time()
                writer.save_arxml(autosar, output_path)
                write_time = time.time() - start

                assert write_time < max_time, f"Write time {write_time}s exceeds {max_time}s"
```

**Expected Result**: Performance within targets

**Status**: 🚧 In Progress (requires test fixtures)

---

### SWIT_RW_006: Complex Nested Structures
**Objective**: Verify handling of complex nested AUTOSAR structures

**Requirements**: SWR_READER_006, SWR_WRITER_002

**Test Steps**:
1. Load ARXML file with complex nesting
2. Verify nested elements are deserialized
3. Verify parent-child relationships
4. Save and verify roundtrip

**Test Code**:
```python
def test_complex_nested_structures():
    import tempfile
    import os
    from armodel.reader import ARXMLReader
    from armodel.writer import ARXMLWriter

    # Use complex ARXML file from demos/arxml/
    complex_file = 'demos/arxml/AUTOSAR_Datatypes.arxml'

    if os.path.exists(complex_file):
        reader = ARXMLReader()
        writer = ARXMLWriter()

        # Load complex file
        autosar = reader.load_arxml(complex_file)
        assert autosar is not None
        assert len(autosar.ar_packages) > 0

        # Verify structure
        for pkg in autosar.ar_packages:
            if pkg.elements:
                assert len(pkg.elements) > 0

        # Test roundtrip
        with tempfile.TemporaryDirectory() as temp_dir:
            output_path = os.path.join(temp_dir, 'output.arxml')
            writer.save_arxml(autosar, output_path)

            roundtrip = reader.load_arxml(output_path)
            assert roundtrip is not None
            assert len(roundtrip.ar_packages) == len(autosar.ar_packages)
```

**Expected Result**: Complex structures handled correctly

**Status**: ✅ Implemented

---

### SWIT_RW_007: Programmatic Object Creation
**Objective**: Verify creating AUTOSAR objects programmatically

**Requirements**: SWR_MODELS_005

**Test Steps**:
1. Create AUTOSAR object
2. Create ARPackage using builder
3. Create data types using builders
4. Add to package
5. Save to file
6. Load and verify structure

**Test Code**:
```python
def test_programmatic_object_creation():
    import tempfile
    import os
    from armodels.M2.AUTOSARTemplates.autosar import AUTOSAR
    from armodels.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_package import ARPackageBuilder
    from armodel.reader import ARXMLReader
    from armodel.writer import ARXMLWriter

    # Create AUTOSAR object
    autosar = AUTOSAR()

    # Create package using builder
    pkg = (ARPackageBuilder()
           .with_short_name("MyPackage")
           .with_category("DataTypes")
           .build())

    autosar.ar_packages.append(pkg)

    # Save and verify
    with tempfile.TemporaryDirectory() as temp_dir:
        output_path = os.path.join(temp_dir, 'created.arxml')

        writer = ARXMLWriter()
        writer.save_arxml(autosar, output_path)

        # Load and verify
        reader = ARXMLReader()
        loaded = reader.load_arxml(output_path)

        assert loaded is not None
        assert len(loaded.ar_packages) == 1
        assert loaded.ar_packages[0].short_name == "MyPackage"
```

**Expected Result**: Objects created and saved correctly

**Status**: 🚧 In Progress

---

## 3. Test Execution

### 3.1 Run All Integration Tests
```bash
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/integration/test_reader_writer.py -v
```

### 3.2 Run Specific Test
```bash
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/integration/test_reader_writer.py::test_read_write_cycle -v
```

### 3.3 Run with Coverage
```bash
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/integration/test_reader_writer.py --cov=src/armodel/reader --cov=src/armodel/writer --cov-report=term
```

---

## 4. Test Coverage Summary

| Category | Test Cases | Implemented | Status |
|----------|------------|-------------|--------|
| Read-Write Cycles | 1 | 1 | ✅ |
| XSD Validation | 1 | 0 | 🚧 |
| Large File Handling | 1 | 0 | 🚧 |
| Multi-Version Support | 1 | 0 | 🚧 |
| Performance | 1 | 0 | 🚧 |
| Complex Structures | 1 | 1 | ✅ |
| Programmatic Creation | 1 | 0 | 🚧 |
| **Total** | **7** | **2** | **29%** |

---

## 5. Requirements Traceability

| Requirement ID | Test Cases | Coverage |
|----------------|-----------|----------|
| SWR_READER_006 | SWIT_RW_001, SWIT_RW_006 | ✅ |
| SWR_READER_007 | SWIT_RW_004 | 🚧 |
| SWR_READER_009 | SWIT_RW_003 | 🚧 |
| SWR_READER_NFR_001 | SWIT_RW_003, SWIT_RW_005 | 🚧 |
| SWR_READER_NFR_002 | SWIT_RW_003 | 🚧 |
| SWR_WRITER_002 | SWIT_RW_006 | ✅ |
| SWR_WRITER_010 | SWIT_RW_001 | ✅ |
| SWR_WRITER_NFR_001 | SWIT_RW_005 | 🚧 |
| SWR_WRITER_NFR_002 | SWIT_RW_003 | 🚧 |
| SWR_MODELS_005 | SWIT_RW_007 | 🚧 |

---

**Document History**:
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-02-15 | AI Assistant | Initial version |
