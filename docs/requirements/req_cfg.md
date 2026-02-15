# Software Requirements - Configuration Module
## py-armodel2 - AUTOSAR ARXML Processing Library

**Module**: `armodel.cfg`
**Version**: 1.0
**Date**: 2026-02-15

---

## 1. Module Overview

The `armodel.cfg` module provides configuration management for schema versions and library settings.

### 1.1 Purpose
- Load YAML configuration files
- Cache configuration in memory
- Support configuration reload
- Provide configuration access to other modules

### 1.2 Components
- `ConfigurationManager`: Singleton class for configuration management
- `config.yaml`: Main configuration entry point
- `schemas/config.yaml`: Schema version mappings

---

## 2. Functional Requirements

### SWR_CFG_001: Load Configuration File
**Description**: The system shall provide functionality to load YAML configuration files.

**Priority**: P0 (Critical)

**Input**: YAML file path

**Output**: Configuration dictionary

---

### SWR_CFG_002: Configuration Caching
**Description**: The system shall cache configuration in memory after first load to avoid repeated file I/O.

**Priority**: P1 (High)

**Behavior**:
- Load file once on initialization
- Subsequent accesses use cached data
- Reload method to force reload

---

### SWR_CFG_003: Configuration Reload
**Description**: The system shall support reloading configuration from file without restarting.

**Priority**: P1 (High)

**Use Case**: Testing environments where configuration changes during execution

---

### SWR_CFG_004: Schema Version Mapping
**Description**: The configuration shall include mappings for AUTOSAR schema versions to namespace URIs and XSD files.

**Priority**: P0 (Critical)

**Required Configuration Structure**:
```yaml
default: "00046"
versions:
  "00044":
    namespace: "http://autosar.org/3.0.4"
    xsd_file: "AUTOSAR_00044.xsd"
  "00046":
    namespace: "http://autosar.org/schema/r4.0"
    xsd_file: "AUTOSAR_00046_COMPACT.xsd"
  "00052":
    namespace: "http://autosar.org/schema/r5.0"
    xsd_file: "AUTOSAR_00052.xsd"
```

---

### SWR_CFG_005: Error Handling
**Description**: The system shall raise appropriate exceptions when configuration files are missing or malformed.

**Priority**: P1 (High)

**Exception Types**:
- `FileNotFoundError`: Config file doesn't exist
- `ValueError`: YAML parsing error or invalid structure

---

### SWR_CFG_006: Thread Safety
**Description**: Configuration access shall be thread-safe for concurrent reads.

**Priority**: P2 (Medium)

---

## 3. Data Requirements

### 3.1 Configuration Files

**Main Config**: `src/armodel/cfg/config.yaml`
- Entry point for configuration loading

**Schema Config**: `src/armodel/cfg/schemas/config.yaml`
- Schema version mappings
- Default version setting
- Namespace URIs
- XSD file paths

### 3.2 Configuration Structure

Required keys:
- `default`: Default schema version
- `versions`: Dictionary of version configurations
- Each version must have `namespace` and `xsd_file`

---

## 4. Interface Requirements

### 4.1 ConfigurationManager Class

**Location**: `src/armodel/cfg/schemas/__init__.py`

**Required Public Interface**:

| Method/Property | Input | Output |
|-----------------|-------|--------|
| `config` (property) | None | Configuration dict |
| `reload()` | None | None (void) |

**Constructor**:
- `__init__(config_path=None)`: Accepts optional config file path

---

## 5. Non-Functional Requirements

### SWR_CFG_NFR_001: Performance
**Description**: Configuration loading shall complete within 100ms.

**Priority**: P2 (Medium)

**Metric**: Time to load config file
**Target**: ≤ 100ms

---

### SWR_CFG_NFR_002: Type Safety
**Description**: All public methods shall have complete type hints and pass MyPy strict mode checking.

**Priority**: P0 (Critical)

---

### SWR_CFG_NFR_003: Validation
**Description**: Configuration shall be validated for required keys and correct structure.

**Priority**: P1 (High)

**Validation Rules**:
- "default" key must exist
- "versions" key must exist
- Each version must have "namespace" and "xsd_file"

---

## 6. Dependencies

### 6.1 Internal Dependencies
- None (base module)

### 6.2 External Dependencies
- `yaml`: YAML file parsing (PyYAML)
- `pathlib`: File path handling
- `typing`: Type hints

---

## 7. Requirements Summary

| Category | Total Requirements |
|----------|-------------------|
| Functional | 6 |
| Non-Functional | 3 |
| **Total** | **9** |

---

**Document History**:
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-02-15 | AI Assistant | Initial version |
| 1.1 | 2026-02-15 | AI Assistant | Removed verification methods and code |
