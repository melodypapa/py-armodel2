# Unit Test Cases - Writer Module
## py-armodel2 - AUTOSAR ARXML Processing Library

**Module**: `armodel.writer`
**Test File**: `tests/unit/test_writer/test_writer.py`
**Version**: 1.0
**Date**: 2026-02-15

---

## 1. Test Overview

This document describes unit tests for the `armodel.writer` module, focusing on the `ARXMLWriter` class.

### 1.1 Test Scope
- Saving AUTOSAR objects to ARXML files
- XML serialization
- Pretty print formatting
- Custom encoding
- Automatic directory creation
- String conversion

### 1.2 Test Framework
- **Framework**: pytest
- **Python Version**: 3.9+
- **Execution**: `PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/unit/test_writer/test_writer.py`

---

## 2. Unit Test Cases

### SWUT_WRITER_001: Save Valid AUTOSAR Object
**Objective**: Verify saving AUTOSAR object to file

**Requirements**: SWR_WRITER_001, SWR_WRITER_008

**Test Steps**:
1. Create AUTOSAR object with packages
2. Call `save_arxml()` with output path
3. Verify file is created
4. Verify file contains valid XML

**Test Code**:
```python
def test_save_autosar_to_file():
    import tempfile
    import os
    from pathlib import Path
    from armodel.writer import ARXMLWriter
    from armodel.models.M2.AUTOSARTemplates.autosar import AUTOSAR

    autosar = AUTOSAR()

    with tempfile.TemporaryDirectory() as temp_dir:
        output_path = os.path.join(temp_dir, 'test_output.arxml')

        writer = ARXMLWriter()
        writer.save_arxml(autosar, output_path)

        assert Path(output_path).exists()

        # Verify file content
        with open(output_path, 'r') as f:
            content = f.read()
            assert '<?xml version=' in content
            assert '<AUTOSAR' in content
```

**Expected Result**: Valid ARXML file created

**Status**: ✅ Implemented

---

### SWUT_WRITER_002: Serialize Objects to XML
**Objective**: Verify XML serialization

**Requirements**: SWR_WRITER_002

**Test Steps**:
1. Create AUTOSAR object
2. Call internal `_serialize_to_xml()` method
3. Verify return type is ET.Element
4. Verify element tag is correct

**Test Code**:
```python
def test_serialize_to_xml():
    import xml.etree.ElementTree as ET
    from armodel.writer import ARXMLWriter
    from armodel.models.M2.AUTOSARTemplates.autosar import AUTOSAR

    autosar = AUTOSAR()
    writer = ARXMLWriter()
    root = writer._serialize_to_xml(autosar)

    assert isinstance(root, ET.Element)
    assert root.tag.endswith('AUTOSAR')
```

**Expected Result**: Valid XML element

**Status**: ✅ Implemented

---

### SWUT_WRITER_003: Pretty Print Formatting
**Objective**: Verify pretty print functionality

**Requirements**: SWR_WRITER_003

**Test Steps**:
1. Create ARXMLWriter with `pretty_print=True`
2. Save AUTOSAR object
3. Read output file
4. Verify proper indentation

**Test Code**:
```python
def test_pretty_print():
    import tempfile
    import os
    from armodel.writer import ARXMLWriter
    from armodel.models.M2.AUTOSARTemplates.autosar import AUTOSAR

    autosar = AUTOSAR()

    with tempfile.TemporaryDirectory() as temp_dir:
        output_path = os.path.join(temp_dir, 'test_output.arxml')

        writer = ARXMLWriter(pretty_print=True)
        writer.save_arxml(autosar, output_path)

        with open(output_path, 'r') as f:
            content = f.read()
            # Check for indentation (spaces after newlines)
            assert '\n  ' in content or '\n\t' in content
```

**Expected Result**: File is properly indented

**Status**: ✅ Implemented

---

### SWUT_WRITER_004: Custom Encoding
**Objective**: Verify custom encoding support

**Requirements**: SWR_WRITER_004

**Test Steps**:
1. Create ARXMLWriter with `encoding="UTF-8"`
2. Save AUTOSAR object
3. Verify file encoding is UTF-8

**Test Code**:
```python
def test_custom_encoding():
    import tempfile
    import os
    from armodel.writer import ARXMLWriter
    from armodel.models.M2.AUTOSARTemplates.autosar import AUTOSAR

    autosar = AUTOSAR()

    with tempfile.TemporaryDirectory() as temp_dir:
        output_path = os.path.join(temp_dir, 'test_output.arxml')

        writer = ARXMLWriter(encoding="UTF-8")
        writer.save_arxml(autosar, output_path)

        # Verify file can be read with UTF-8
        with open(output_path, 'r', encoding='UTF-8') as f:
            content = f.read()
            assert len(content) > 0
```

**Expected Result**: File uses specified encoding

**Status**: ✅ Implemented

---

### SWUT_WRITER_005: Auto-Create Directories
**Objective**: Verify automatic directory creation

**Requirements**: SWR_WRITER_005

**Test Steps**:
1. Create AUTOSAR object
2. Save to path with non-existent parent directories
3. Verify directories are created
4. Verify file is created

**Test Code**:
```python
def test_auto_create_directories():
    import tempfile
    import os
    from pathlib import Path
    from armodel.writer import ARXMLWriter
    from armodel.models.M2.AUTOSARTemplates.autosar import AUTOSAR

    autosar = AUTOSAR()

    with tempfile.TemporaryDirectory() as temp_dir:
        output_path = os.path.join(temp_dir, 'new', 'nested', 'dir', 'output.arxml')

        writer = ARXMLWriter()
        writer.save_arxml(autosar, output_path)

        assert Path(output_path).exists()
        assert Path(output_path).parent.exists()
```

**Expected Result**: Parent directories created automatically

**Status**: ✅ Implemented

---

### SWUT_WRITER_006: Convert to String
**Objective**: Verify XML string conversion

**Requirements**: SWR_WRITER_006

**Test Steps**:
1. Create AUTOSAR object
2. Call `to_string()`
3. Verify return value is string
4. Verify string contains valid XML

**Test Code**:
```python
def test_to_string():
    from armodel.writer import ARXMLWriter
    from armodel.models.M2.AUTOSARTemplates.autosar import AUTOSAR

    autosar = AUTOSAR()

    writer = ARXMLWriter()
    xml_string = writer.to_string(autosar)

    assert isinstance(xml_string, str)
    assert '<?xml version=' in xml_string
    assert '<AUTOSAR' in xml_string
```

**Expected Result**: Valid XML string returned

**Status**: ✅ Implemented

---

### SWUT_WRITER_007: Configure Method
**Objective**: Verify runtime configuration update

**Requirements**: SWR_WRITER_007

**Test Steps**:
1. Create ARXMLWriter with default settings
2. Call `configure()` with new settings
3. Verify configuration is updated

**Test Code**:
```python
def test_configure():
    from armodel.writer import ARXMLWriter

    writer = ARXMLWriter(pretty_print=True, encoding="UTF-8")

    # Update configuration
    writer.configure(pretty_print=False, encoding="ASCII")

    assert writer._pretty_print == False
    assert writer._encoding == "ASCII"
```

**Expected Result**: Configuration updated successfully

**Status**: ✅ Implemented

---

### SWUT_WRITER_008: Dependency Injection
**Objective**: Verify SchemaVersionManager dependency injection

**Requirements**: SWR_WRITER_009

**Test Steps**:
1. Create mock SchemaVersionManager
2. Initialize ARXMLWriter with mock manager
3. Verify writer uses injected manager

**Test Code**:
```python
def test_dependency_injection():
    from unittest.mock import Mock
    from armodel.core import SchemaVersionManager
    from armodel.writer import ARXMLWriter

    mock_manager = Mock(spec=SchemaVersionManager)
    writer = ARXMLWriter(version_manager=mock_manager)

    assert writer._version_manager is mock_manager
```

**Expected Result**: Writer uses injected manager

**Status**: ✅ Implemented

---

### SWUT_WRITER_009: No Pretty Print
**Objective**: Verify output without pretty printing

**Requirements**: SWR_WRITER_003

**Test Steps**:
1. Create ARXMLWriter with `pretty_print=False`
2. Save AUTOSAR object
3. Verify output has no indentation

**Test Code**:
```python
def test_no_pretty_print():
    import tempfile
    import os
    from armodel.writer import ARXMLWriter
    from armodel.models.M2.AUTOSARTemplates.autosar import AUTOSAR

    autosar = AUTOSAR()

    with tempfile.TemporaryDirectory() as temp_dir:
        output_path = os.path.join(temp_dir, 'test_output.arxml')

        writer = ARXMLWriter(pretty_print=False)
        writer.save_arxml(autosar, output_path)

        with open(output_path, 'r') as f:
            content = f.read()
            # Should have minimal formatting
            assert content.count('\n') < 10 or '\n  ' not in content
```

**Expected Result**: Output without pretty formatting

**Status**: ✅ Implemented

---

## 3. Test Execution

### 3.1 Run All Writer Unit Tests
```bash
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/unit/test_writer/test_writer.py -v
```

### 3.2 Run Specific Test
```bash
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/unit/test_writer/test_writer.py::test_save_autosar_to_file -v
```

### 3.3 Run with Coverage
```bash
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/unit/test_writer/test_writer.py --cov=src/armodel/writer --cov-report=term
```

---

## 4. Test Coverage Summary

| Category | Test Cases | Implemented | Status |
|----------|------------|-------------|--------|
| Save to File | 1 | 1 | ✅ |
| XML Serialization | 1 | 1 | ✅ |
| Pretty Print | 2 | 2 | ✅ |
| Encoding | 1 | 1 | ✅ |
| Directory Creation | 1 | 1 | ✅ |
| String Conversion | 1 | 1 | ✅ |
| Configuration | 1 | 1 | ✅ |
| Dependency Injection | 1 | 1 | ✅ |
| **Total** | **9** | **9** | **100%** |

---

## 5. Requirements Traceability

| Requirement ID | Test Cases | Coverage |
|----------------|-----------|----------|
| SWR_WRITER_001 | SWUT_WRITER_001 | ✅ |
| SWR_WRITER_002 | SWUT_WRITER_002 | ✅ |
| SWR_WRITER_003 | SWUT_WRITER_003, SWUT_WRITER_009 | ✅ |
| SWR_WRITER_004 | SWUT_WRITER_004 | ✅ |
| SWR_WRITER_005 | SWUT_WRITER_005 | ✅ |
| SWR_WRITER_006 | SWUT_WRITER_006 | ✅ |
| SWR_WRITER_007 | SWUT_WRITER_007 | ✅ |
| SWR_WRITER_008 | SWUT_WRITER_001 | ✅ |
| SWR_WRITER_009 | SWUT_WRITER_008 | ✅ |
| SWR_WRITER_010 | - | (Integration test) |
| SWR_WRITER_NFR_001 | - | (Integration test) |
| SWR_WRITER_NFR_002 | - | (Integration test) |

---

**Document History**:
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-02-15 | AI Assistant | Initial version |
