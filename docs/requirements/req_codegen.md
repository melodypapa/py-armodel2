# Software Requirements - Code Generation
## py-armodel2 - AUTOSAR ARXML Processing Library

**Module**: `tools/generate_models.py`
**Version**: 1.0
**Date**: 2026-02-15

---

## 1. Module Overview

The code generation module provides automated generation of AUTOSAR model classes from type definitions.

### 1.1 Purpose
- Generate Python classes for AUTOSAR types
- Ensure code standards compliance
- Automate repetitive code writing
- Maintain consistency across model classes

### 1.2 Components
- `tools/generate_models.py`: Standalone code generator

### 1.3 Output
- 1,912 generated Python class files
- Located in `src/armodel2/models/M2/`

---

## 2. Functional Requirements

### SWR_CODEGEN_001: Generate Model Classes
**Description**: The system shall provide a code generator that creates Python classes for all AUTOSAR type definitions.

**Priority**: P0 (Critical)

**Input**: Type definitions (mapping data)

**Output**: Python class files with serialize/deserialize methods

---

### SWR_CODEGEN_002: Create Package Structure
**Description**: The generator shall create directory structure matching AUTOSAR package hierarchy.

**Priority**: P0 (Critical)

**Required Structure**:
```
src/armodel2/models/M2/
├── AUTOSARTemplates/
│   ├── autosar.py
│   ├── AbstractPlatform/
│   ├── AdaptivePlatform/
│   └── ...
└── MSR/
    ├── AsamHdo/
    └── ...
```

---

### SWR_CODEGEN_003: Generate Serialize Method
**Description**: Each generated class shall include a serialize() method that converts the object to xml.etree.ElementTree.Element.

**Priority**: P0 (Critical)

**Method Signature**: `def serialize(self) -> ET.Element`

---

### SWR_CODEGEN_004: Generate Deserialize Method
**Description**: Each generated class shall include a deserialize() classmethod that creates an object from XML.

**Priority**: P0 (Critical)

**Method Signature**: `@classmethod def deserialize(cls, element: ET.Element) -> Self`

---

### SWR_CODEGEN_005: Generate Builder Class
**Description**: Each generated class shall include a Builder class for fluent object construction.

**Priority**: P1 (High)

**Required Pattern**:
```python
class ClassNameBuilder:
    def with_attribute(self, value: type) -> "ClassNameBuilder"
    def build(self) -> ClassName
```

---

### SWR_CODEGEN_006: Add Type Hints
**Description**: All generated code shall include complete type hints for all attributes and methods.

**Priority**: P0 (Critical)

---

### SWR_CODEGEN_007: Add Docstrings
**Description**: All generated classes and methods shall have comprehensive docstrings.

**Priority**: P1 (High)

**Standard**: Google style docstrings

---

### SWR_CODEGEN_008: Create __init__.py Files
**Description**: The generator shall create __init__.py files in each package directory to export classes.

**Priority**: P1 (High)

**Content**: Export all classes in the package

---

### SWR_CODEGEN_009: Code Standards Compliance
**Description**: Generated code shall comply with all design rules in `docs/designs/design_rules.md`.

**Priority**: P0 (Critical)

**Standards**:
- Ruff linting compliance
- MyPy strict mode compliance
- Line length ≤ 100 characters
- PEP 8 style guide

---

### SWR_CODEGEN_010: Idempotent Generation
**Description**: Running the generator multiple times shall produce identical output (no duplicate content).

**Priority**: P1 (High)

**Behavior**:
- Overwrite existing files
- No accumulation of content
- Consistent output across runs

---

## 3. Data Requirements

### 3.1 Input Data

The generator requires type definition data including:
- Package path
- Class name
- Parent class
- Attributes with types
- Multiplicity information
- Documentation

### 3.2 Output Data

For each type definition, generate:
- Python class file
- serialize() method
- deserialize() classmethod
- Builder class
- __init__.py exports

---

## 4. Interface Requirements

### 4.1 Code Generator Script

**Location**: `tools/generate_models.py`

**Usage**: Command-line execution

**Exit Codes**:
- 0: Success
- 1: Error (missing input, invalid data, etc.)

---

## 5. Non-Functional Requirements

### SWR_CODEGEN_NFR_001: Performance
**Description**: Code generation shall complete within 60 seconds for 1,912 classes.

**Priority**: P1 (High)

**Metric**: Total generation time
**Target**: ≤ 60 seconds

---

### SWR_CODEGEN_NFR_002: Memory Efficiency
**Description**: Generator shall use memory efficiently when generating large numbers of classes.

**Priority**: P2 (Medium)

---

### SWR_CODEGEN_NFR_003: Error Handling
**Description**: Generator shall provide clear error messages when input data is invalid or missing.

**Priority**: P1 (High)

---

## 6. Dependencies

### 6.1 Internal Dependencies
- Design rules document: `docs/designs/design_rules.md`

### 6.2 External Dependencies
- `pathlib`: File and directory operations
- `typing`: Type hints

---

## 7. Requirements Summary

| Category | Total Requirements |
|----------|-------------------|
| Functional | 10 |
| Non-Functional | 3 |
| **Total** | **13** |

---

**Document History**:
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-02-15 | AI Assistant | Initial version |
| 1.1 | 2026-02-15 | AI Assistant | Removed verification methods and code |
