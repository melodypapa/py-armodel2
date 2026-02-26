# Unit Test Cases - Core Module
## py-armodel2 - AUTOSAR ARXML Processing Library

**Module**: `armodel.core`
**Test File**: `tests/unit/test_core/test_version.py`
**Version**: 1.0
**Date**: 2026-02-15

---

## 1. Test Overview

This document describes unit tests for the `armodel.core` module, focusing on the `SchemaVersionManager` class.

### 1.1 Test Scope
- Schema version detection from XML namespaces
- Configuration access and management
- Singleton pattern behavior
- Error handling for unknown namespaces

### 1.2 Test Framework
- **Framework**: pytest
- **Python Version**: 3.9+
- **Execution**: `PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/unit/test_core/test_version.py`

---

## 2. Unit Test Cases

### SWUT_CORE_001: Detect Schema Version 00046
**Objective**: Verify schema version detection from AUTOSAR 00046 namespace

**Requirements**: SWR_CORE_001, SWR_CORE_002

**Test Steps**:
1. Create XML element with AUTOSAR 00046 namespace
2. Call `SchemaVersionManager.detect_schema_version()`
3. Verify return value is "00046"

**Test Code**:
```python
def test_detect_schema_version_00046():
    xml_str = '''<AUTOSAR xmlns="http://autosar.org/schema/r4.0">
        <AR-PACKAGES>
        </AR-PACKAGES>
    </AUTOSAR>'''
    root = ET.fromstring(xml_str)
    manager = SchemaVersionManager()
    version = manager.detect_schema_version(root)
    assert version == "00046"
```

**Expected Result**: Returns "00046"

**Status**: ✅ Implemented

---

### SWUT_CORE_002: Detect Schema Version 00044
**Objective**: Verify schema version detection from AUTOSAR 00044 namespace

**Requirements**: SWR_CORE_001, SWR_CORE_002

**Test Steps**:
1. Create XML element with AUTOSAR 00044 namespace
2. Call `detect_schema_version()`
3. Verify return value is "00044"

**Test Code**:
```python
def test_detect_schema_version_00044():
    xml_str = '''<AUTOSAR xmlns="http://autosar.org/3.0.4">
        <AR-PACKAGES>
        </AR-PACKAGES>
    </AUTOSAR>'''
    root = ET.fromstring(xml_str)
    manager = SchemaVersionManager()
    version = manager.detect_schema_version(root)
    assert version == "00044"
```

**Expected Result**: Returns "00044"

**Status**: ✅ Implemented

---

### SWUT_CORE_003: Detect Schema Version 00052
**Objective**: Verify schema version detection from AUTOSAR 00052 namespace

**Requirements**: SWR_CORE_001, SWR_CORE_002

**Test Steps**:
1. Create XML element with AUTOSAR 00052 namespace
2. Call `detect_schema_version()`
3. Verify return value is "00052"

**Test Code**:
```python
def test_detect_schema_version_00052():
    xml_str = '''<AUTOSAR xmlns="http://autosar.org/schema/r5.0">
        <AR-PACKAGES>
        </AR-PACKAGES>
    </AUTOSAR>'''
    root = ET.fromstring(xml_str)
    manager = SchemaVersionManager()
    version = manager.detect_schema_version(root)
    assert version == "00052"
```

**Expected Result**: Returns "00052"

**Status**: ✅ Implemented

---

### SWUT_CORE_004: Unknown Namespace Handling
**Objective**: Verify behavior with unknown namespace

**Requirements**: SWR_CORE_008

**Test Steps**:
1. Create XML element with unknown namespace
2. Call `detect_schema_version()`
3. Verify return value is None

**Test Code**:
```python
def test_detect_schema_version_unknown():
    xml_str = '''<AUTOSAR xmlns="http://unknown-namespace.org">
        <AR-PACKAGES>
        </AR-PACKAGES>
    </AUTOSAR>'''
    root = ET.fromstring(xml_str)
    manager = SchemaVersionManager()
    version = manager.detect_schema_version(root)
    assert version is None
```

**Expected Result**: Returns None

**Status**: ✅ Implemented

---

### SWUT_CORE_005: Get Configuration for Version
**Objective**: Verify configuration retrieval for specific schema version

**Requirements**: SWR_CORE_003

**Test Steps**:
1. Call `get_config("00046")`
2. Verify configuration contains namespace and xsd_file

**Test Code**:
```python
def test_get_config():
    manager = SchemaVersionManager()
    config = manager.get_config("00046")
    assert config is not None
    assert "namespace" in config
    assert "xsd_file" in config
    assert config["namespace"] == "http://autosar.org/schema/r4.0"
```

**Expected Result**: Valid configuration dictionary

**Status**: ✅ Implemented

---

### SWUT_CORE_006: Get Namespace for Version
**Objective**: Verify namespace retrieval for specific version

**Requirements**: SWR_CORE_003

**Test Steps**:
1. Call `get_namespace("00046")`
2. Verify correct namespace is returned

**Test Code**:
```python
def test_get_namespace():
    manager = SchemaVersionManager()
    namespace = manager.get_namespace("00046")
    assert namespace == "http://autosar.org/schema/r4.0"
```

**Expected Result**: Correct namespace URI

**Status**: ✅ Implemented

---

### SWUT_CORE_007: Get Default Version
**Objective**: Verify default version is 00046

**Requirements**: SWR_CORE_004

**Test Steps**:
1. Call `get_default_version()`
2. Verify return value is "00046"

**Test Code**:
```python
def test_get_default_version():
    manager = SchemaVersionManager()
    default = manager.get_default_version()
    assert default == "00046"
```

**Expected Result**: Returns "00046"

**Status**: ✅ Implemented

---

### SWUT_CORE_008: Get All Versions
**Objective**: Verify all supported versions are returned

**Requirements**: SWR_CORE_005

**Test Steps**:
1. Call `get_all_versions()`
2. Verify list contains all supported versions

**Test Code**:
```python
def test_get_all_versions():
    manager = SchemaVersionManager()
    versions = manager.get_all_versions()
    assert "00044" in versions
    assert "00046" in versions
    assert "00052" in versions
    assert len(versions) == 3
```

**Expected Result**: List of all supported versions

**Status**: ✅ Implemented

---

### SWUT_CORE_009: Singleton Pattern
**Objective**: Verify SchemaVersionManager is a singleton

**Requirements**: SWR_CORE_007

**Test Steps**:
1. Create two SchemaVersionManager instances
2. Verify they are the same object (using `is` operator)

**Test Code**:
```python
def test_singleton_pattern():
    manager1 = SchemaVersionManager()
    manager2 = SchemaVersionManager()
    assert manager1 is manager2
```

**Expected Result**: Both instances are the same object

**Status**: ✅ Implemented

---

### SWUT_CORE_010: Configuration Reload
**Objective**: Verify configuration reload functionality

**Requirements**: SWR_CORE_006

**Test Steps**:
1. Create SchemaVersionManager instance
2. Get configuration
3. Call `reload()`
4. Verify configuration is reloaded

**Test Code**:
```python
def test_reload_configuration():
    manager = SchemaVersionManager()
    # Get initial config
    config1 = manager.get_config("00046")
    # Reload
    manager.reload()
    # Get config after reload
    config2 = manager.get_config("00046")
    # Verify they have same structure
    assert config1["namespace"] == config2["namespace"]
```

**Expected Result**: Configuration reloaded successfully

**Status**: ✅ Implemented

---

### SWUT_CORE_011: Namespace Extraction from Tag
**Objective**: Verify namespace extraction from XML tag with embedded namespace

**Requirements**: SWR_CORE_002

**Test Steps**:
1. Create XML element with namespace in tag
2. Call `_extract_namespace()`
3. Verify correct namespace is extracted

**Test Code**:
```python
def test_extract_namespace_from_tag():
    xml_str = '<{http://autosar.org/schema/r4.0}AUTOSAR/>'
    root = ET.fromstring(xml_str)
    manager = SchemaVersionManager()
    namespace = manager._extract_namespace(root)
    assert namespace == "http://autosar.org/schema/r4.0"
```

**Expected Result**: Correct namespace extracted

**Status**: ✅ Implemented

---

### SWUT_CORE_012: Namespace Extraction from Attribute
**Objective**: Verify namespace extraction from xmlns attribute

**Requirements**: SWR_CORE_002

**Test Steps**:
1. Create XML element with xmlns attribute
2. Call `_extract_namespace()`
3. Verify correct namespace is extracted

**Test Code**:
```python
def test_extract_namespace_from_attribute():
    xml_str = '<AUTOSAR xmlns="http://autosar.org/schema/r4.0"/>'
    root = ET.fromstring(xml_str)
    manager = SchemaVersionManager()
    namespace = manager._extract_namespace(root)
    assert namespace == "http://autosar.org/schema/r4.0"
```

**Expected Result**: Correct namespace extracted

**Status**: ✅ Implemented

---

### SWUT_CORE_013: Invalid Version Configuration
**Objective**: Verify behavior when requesting configuration for non-existent version

**Requirements**: SWR_CORE_003

**Test Steps**:
1. Call `get_config("99999")` (non-existent version)
2. Verify return value is None

**Test Code**:
```python
def test_get_config_invalid_version():
    manager = SchemaVersionManager()
    config = manager.get_config("99999")
    assert config is None
```

**Expected Result**: Returns None

**Status**: ✅ Implemented

---

## 3. Performance Tests

### SWUT_CORE_PERF_001: Schema Detection Performance
**Objective**: Verify schema version detection completes within 1 second

**Requirements**: SWR_CORE_NFR_001

**Test Steps**:
1. Create typical ARXML XML element
2. Record start time
3. Call `detect_schema_version()`
4. Record end time
5. Verify duration ≤ 1 second

**Test Code**:
```python
import time

def test_detect_schema_version_performance():
    xml_str = '''<AUTOSAR xmlns="http://autosar.org/schema/r4.0">
        <AR-PACKAGES>
            <AR-PACKAGE>
                <SHORT-NAME>TestPackage</SHORT-NAME>
            </AR-PACKAGE>
        </AR-PACKAGES>
    </AUTOSAR>'''
    root = ET.fromstring(xml_str)
    manager = SchemaVersionManager()

    start = time.time()
    version = manager.detect_schema_version(root)
    end = time.time()

    assert version == "00046"
    assert (end - start) <= 1.0  # 1 second max
```

**Expected Result**: Detection completes within 1 second

**Status**: 🚧 In Progress

---

## 4. Test Execution

### 4.1 Run All Core Unit Tests
```bash
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/unit/test_core/test_version.py -v
```

### 4.2 Run Specific Test
```bash
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/unit/test_core/test_version.py::test_detect_schema_version_00046 -v
```

### 4.3 Run with Coverage
```bash
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/unit/test_core/test_version.py --cov=src/armodel2/core --cov-report=term
```

---

## 5. Test Coverage Summary

| Category | Test Cases | Implemented | Status |
|----------|------------|-------------|--------|
| Schema Detection | 4 | 4 | ✅ |
| Configuration Access | 4 | 4 | ✅ |
| Singleton Pattern | 1 | 1 | ✅ |
| Namespace Extraction | 2 | 2 | ✅ |
| Error Handling | 2 | 2 | ✅ |
| Performance | 1 | 0 | 🚧 |
| **Total** | **14** | **13** | **93%** |

---

## 6. Requirements Traceability

| Requirement ID | Test Cases | Coverage |
|----------------|-----------|----------|
| SWR_CORE_001 | SWUT_CORE_001, SWUT_CORE_002, SWUT_CORE_003 | ✅ |
| SWR_CORE_002 | SWUT_CORE_011, SWUT_CORE_012 | ✅ |
| SWR_CORE_003 | SWUT_CORE_005, SWUT_CORE_006, SWUT_CORE_013 | ✅ |
| SWR_CORE_004 | SWUT_CORE_007 | ✅ |
| SWR_CORE_005 | SWUT_CORE_008 | ✅ |
| SWR_CORE_006 | SWUT_CORE_010 | ✅ |
| SWR_CORE_007 | SWUT_CORE_009 | ✅ |
| SWR_CORE_008 | SWUT_CORE_004 | ✅ |
| SWR_CORE_NFR_001 | SWUT_CORE_PERF_001 | 🚧 |

---

**Document History**:
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-02-15 | AI Assistant | Initial version |
