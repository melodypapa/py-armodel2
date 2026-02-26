# Software Requirements - Core Module
## py-armodel2 - AUTOSAR ARXML Processing Library

**Module**: `armodel.core`
**Version**: 1.0
**Date**: 2026-02-15

---

## 1. Module Overview

The `armodel.core` module provides core utilities for schema version detection and configuration management. It serves as the foundation for ARXML reading and writing operations.

### 1.1 Purpose
- Detect AUTOSAR schema versions from ARXML files
- Provide schema version configuration and mapping
- Manage schema-related metadata (namespaces, XSD paths)

### 1.2 Components
- `SchemaVersionManager`: Singleton class for schema version management

---

## 2. Functional Requirements

### SWR_CORE_001: Schema Version Detection
**Description**: The system shall provide functionality to detect AUTOSAR schema version from XML namespace declarations.

**Priority**: P0 (Critical)

**Input**: XML element with namespace declaration

**Output**: Schema version string ("00044", "00046", "00052") or None if unknown

---

### SWR_CORE_002: Namespace Extraction
**Description**: The system shall extract namespace URIs from XML elements, supporting both embedded namespaces in tags and xmlns attributes.

**Priority**: P0 (Critical)

**Input Formats**:
- Embedded namespace: `<{namespace}tagname>`
- Attribute namespace: `<tagname xmlns="namespace">`

**Output**: Namespace URI string

---

### SWR_CORE_003: Schema Configuration Access
**Description**: The system shall provide methods to retrieve configuration data for specific schema versions.

**Priority**: P0 (Critical)

**Required Methods**:
- `get_config(version)`: Get full configuration dict for version
- `get_namespace(version)`: Get namespace URI for version
- `get_xsd_path(version)`: Get XSD file path for version

**Output**: Configuration data (dict, string, or file path)

---

### SWR_CORE_004: Default Version Management
**Description**: The system shall provide a default schema version (00046) for operations when no version is specified.

**Priority**: P0 (Critical)

**Output**: Default version string "00046"

---

### SWR_CORE_005: List All Supported Versions
**Description**: The system shall provide a list of all supported AUTOSAR schema versions.

**Priority**: P1 (High)

**Output**: List containing "00044", "00046", "00052"

---

### SWR_CORE_006: Configuration Reload
**Description**: The system shall support reloading configuration from YAML files without restarting the application.

**Priority**: P1 (High)

**Use Case**: Testing environments where configuration changes during execution

---

### SWR_CORE_007: Singleton Pattern
**Description**: The SchemaVersionManager shall implement the singleton pattern to ensure only one instance exists.

**Priority**: P0 (Critical)

**Rationale**: Ensures consistent configuration across the application

---

### SWR_CORE_008: Unknown Namespace Handling
**Description**: The system shall return None when encountering unknown or unsupported namespace URIs.

**Priority**: P1 (High)

**Output**: None for unknown namespaces

---

## 3. Data Requirements

### 3.1 Schema Version Configuration

**Location**: `src/armodel2/cfg/schemas/config.yaml`

**Required Structure**:
- `default`: Default schema version
- `versions`: Mapping of version IDs to configuration
  - Each version must have `namespace` and `xsd_file` keys

### 3.2 Supported Schema Versions

| Version | Namespace | Description | XSD File |
|---------|-----------|-------------|----------|
| 00044 | http://autosar.org/3.0.4 | Classic Platform 4.3.1 (2017) | AUTOSAR_00044.xsd |
| 00046 | http://autosar.org/schema/r4.0 | CP 4.4.0 / AP 18-10 (2018) | AUTOSAR_00046_COMPACT.xsd |
| 00052 | http://autosar.org/schema/r5.0 | CP/AP 23-11 (2023) | AUTOSAR_00052.xsd |

---

## 4. Interface Requirements

### 4.1 SchemaVersionManager Class

**Location**: `src/armodel2/core/version.py`

**Required Public Interface**:

| Method | Input | Output |
|--------|-------|--------|
| `detect_schema_version(root)` | XML element | Version string or None |
| `get_config(version)` | Version string | Configuration dict or None |
| `get_namespace(version)` | Version string | Namespace URI or None |
| `get_xsd_path(version)` | Version string | XSD file path or None |
| `get_default_version()` | None | Default version string |
| `get_all_versions()` | None | List of version strings |
| `reload()` | None | None (void) |

---

## 5. Non-Functional Requirements

### SWR_CORE_NFR_001: Performance
**Description**: Schema version detection shall complete within 1 second for typical ARXML files.

**Priority**: P2 (Medium)

**Metric**: Time to detect version from XML element
**Target**: ≤ 1 second

---

### SWR_CORE_NFR_002: Thread Safety
**Description**: The singleton instance shall be thread-safe for concurrent access.

**Priority**: P1 (High)

---

### SWR_CORE_NFR_003: Type Safety
**Description**: All public methods shall have complete type hints and pass MyPy strict mode checking.

**Priority**: P0 (Critical)

---

## 6. Dependencies

### 6.1 Internal Dependencies
- `armodel.cfg.schemas.ConfigurationManager`: For loading YAML configuration

### 6.2 External Dependencies
- `xml.etree.ElementTree`: XML parsing (standard library)
- `typing`: Type hints (standard library)

---

## 7. Requirements Summary

| Category | Total Requirements |
|----------|-------------------|
| Functional | 8 |
| Non-Functional | 3 |
| **Total** | **11** |

---

**Document History**:
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-02-15 | AI Assistant | Initial version |
| 1.1 | 2026-02-15 | AI Assistant | Removed verification methods and code |
