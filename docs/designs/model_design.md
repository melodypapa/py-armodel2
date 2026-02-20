# Model Design Documentation

## Overview

The AUTOSAR model layer (`src/armodel/models/`) provides a complete Python implementation of the AUTOSAR meta-model, supporting reading, writing, and manipulation of ARXML files across multiple AUTOSAR schema versions.

### Key Statistics

| Metric                     | Count                  |
| -------------------------- | ---------------------- |
| **Total Python Files**     | 2,223                  |
| **AUTOSARTemplates Files** | 1,998                  |
| **MSR Files**              | 225                    |
| **Enum Classes**           | 215+                   |
| **Top-level Packages**     | 17 (AUTOSAR) + 5 (MSR) |

## Architecture

### Directory Structure

```
src/armodel/models/
└── M2/                              # AUTOSAR M2 model definitions
    ├── AUTOSARTemplates/            # AUTOSAR standard templates (1,998 files)
    │   ├── AbstractPlatform/        # Abstract platform definitions
    │   ├── AdaptivePlatform/        # Adaptive AUTOSAR platform
    │   ├── AutosarTopLevelStructure/ # Root AUTOSAR element
    │   ├── BswModuleTemplate/       # Basic software module templates
    │   ├── CommonStructure/         # Common AUTOSAR structures
    │   │   ├── StandardizationTemplate/  # Blueprinting and tailoring
    │   │   ├── Timing/              # Timing specifications
    │   │   └── ...
    │   ├── DiagnosticExtract/       # Diagnostic extraction
    │   ├── ECUCDescriptionTemplate/ # ECU configuration description
    │   ├── ECUCParameterDefTemplate/# ECU parameter definitions
    │   ├── FeatureModelTemplate/    # Feature model templates
    │   ├── GenericStructure/        # Generic AUTOSAR structures
    │   │   └── GeneralTemplateClasses/
    │   │       ├── ArObject/        # Base ARObject class
    │   │       ├── Identifiable/    # Identifiable elements
    │   │       ├── ARPackage/       # Package structure
    │   │       └── PrimitiveTypes/  # AUTOSAR primitive types
    │   ├── LogAndTraceExtract/      # Log and trace extraction
    │   ├── SWComponentTemplate/     # Software component templates
    │   ├── SecurityExtractTemplate/ # Security extraction
    │   └── SystemTemplate/          # System-level templates
    └── MSR/                         # MSR documentation models (225 files)
        ├── AsamHdo/                 # ASAM HDO base types
        │   ├── AdminData/           # Administrative data
        │   ├── BaseTypes/           # Base data types
        │   ├── Units/               # Unit specifications
        │   └── ...
        ├── CalibrationData/         # Calibration data models
        ├── DataDictionary/          # Data dictionary structures
        └── Documentation/           # Documentation models
            ├── TextModel/           # Text content models
            ├── BlockElements/       # Block-level elements
            └── Chapters/            # Chapter organization
```

### Base Class Hierarchy

All model classes inherit from a common base class hierarchy:

```
ARObject (root base class)
├── Referrable (short_name property)
│   ├── Identifiable (identifier properties)
│   │   ├── Describable (description properties)
│   │   └── ARElement (AUTOSAR-specific elements)
│   └── PackageableElement
│       └── ARPackage (package container)
└── ...
```

**ARObject Location**: `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ArObject/ar_object.py`

**AUTOSAR Root Element**: `src/armodel/models/M2/AUTOSARTemplates/AutosarTopLevelStructure/autosar.py`

## Class Design Patterns

### 1. Reflection-Based Serialization

Model classes use type hints and automatic reflection for serialization:

```python
class ARPackage(ARObject):
    short_name: Optional[str] = None
    category: Optional[str] = None
    ar_packages: list[ARPackage] = []

    # No _xml_members dict needed!
    # Serialization is automatic via ARObject base class
```

**Special cases use decorators**:
```python
class AUTOSAR(ARObject):
    def __init__(self) -> None:
        self._schema_version: str = "4.5.0"

    @xml_attribute
    @property
    def schema_version(self) -> str:
        return self._schema_version
```

### 2. Multiplicity Mapping

| AUTOSAR Multiplicity | Python Type      | Initial Value                   |
| -------------------- | ---------------- | ------------------------------- |
| `0..1`               | `Optional[Type]` | `None`                          |
| `1`                  | `Type`           | `None` (set during deserialize) |
| `*`                  | `list[Type]`     | `[]`                            |
| `0..*`               | `list[Type]`     | `[]`                            |

### 3. Builder Pattern

Every model class includes a builder for fluent construction:

```python
class MyClassBuilder:
    def with_short_name(self, value: str) -> "MyClassBuilder":
        self._short_name = value
        return self

    def with_category(self, value: str) -> "MyClassBuilder":
        self._category = value
        return self

    def build(self) -> MyClass:
        obj = MyClass()
        obj.short_name = self._short_name
        obj.category = self._category
        return obj
```

### 4. Serialization/Deserialization

All classes inherit serialize/deserialize from `ARObject` base class:

```python
# Inherited from ARObject - no implementation needed
obj.serialize(namespace)  # Returns xml.etree.ElementTree.Element
MyClass.deserialize(element)  # @classmethod - returns MyClass instance
```

The base class automatically:
- Discovers attributes via `vars(self)` and `get_type_hints()`
- Converts names using `NameConverter` (snake_case ↔ UPPER-CASE-WITH-HYPHENS)
- Handles XML attributes vs child elements
- Manages nested objects, lists, and primitives
- Supports optional fields and circular imports

## AUTOSARTemplates Packages

### AbstractPlatform
- Application deferred data types
- Application interfaces

### AdaptivePlatform
- Application design (ports, interfaces)
- Platform module deployment
- Crypto, firewall, IDS configurations

### CommonStructure
- **StandardizationTemplate**: Blueprinting, tailoring, data exchange
- **Timing**: Execution time, stack/heap usage
- **Constants**: Value specifications (numerical, text, record, array)
- **DataTypes**: Implementation data types
- **PortInterface**: Server ports, provided/required interfaces
- **ModeDeclaration**: Mode switching, mode groups
- **SWC_BswMapping**: Software component to BSW mapping
- **ServiceNeeds**: Diagnostic, communication, security needs

### GenericStructure

**GeneralTemplateClasses**:
- `ArObject`: Root base class
- `Identifiable`: Elements with identifiers
- `Referrable`: Referencable elements
- `ARPackage`: Package containers
- `PrimitiveTypes`: 50+ AUTOSAR primitive types

### SWComponentTemplate
- Application software components
- Runnable entities
- Data type mappings
- Port prototypes
- Connector configurations

### SystemTemplate
- Ethernet, CAN, FlexRay, LIN transport
- Network management
- Diagnostic connections
- FIBEX integration

### DiagnosticExtract
- DCM (Diagnostic Communication Manager)
- DEM (Diagnostic Event Manager)
- OBD services

### ECUCDescriptionTemplate
- ECU configuration values
- Container definitions
- References and constraints

### BswModuleTemplate
- BSW module descriptions
- Internal behavior
- Schedulable entities
- BSW module entries

## MSR (Measurement, Calibration & Diagnostics)

### AsamHdo
- **AdminData**: Administrative data
- **BaseTypes**: Base data types
- **Units**: Unit and unit group specifications
- **Constraints**: Global constraints
- **ComputationMethod**: Computation methods

### CalibrationData
- **CalibrationValue**: Calibration value definitions

### DataDictionary
- **Axis**: Axis specifications
- **RecordLayout**: Record layout definitions
- **CalibrationParameter**: Calibration parameters
- **SystemConstant**: System constants
- **DataDefProperties**: Data definition properties

### Documentation
- **TextModel**:
  - LanguageDataModel: Single-language text
  - MultilanguageData: Multi-language support
  - InlineTextModel: Inline text elements
- **BlockElements**:
  - Chapters, Lists, Tables
  - Figures, Formulas
  - Pagination and view control
  - Requirements tracing

## Code Generation

### Generator Tool
- **Location**: `tools/generate_models.py`
- **Input**: `docs/json/` mapping metadata
- **Output**: All Python model files

### Generation Triggers
Regenerate models when:
1. Modifying `tools/generate_models.py`
2. Changing `docs/json/mapping.json` metadata
3. Updating serialization framework

### Regeneration Command
```bash
python tools/generate_models.py
```

### Verification
```bash
ruff check src/
mypy src/
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest
```

## Design Rules Compliance

All model classes follow `docs/designs/design_rules.md`:

- ✅ **DESIGN_RULE_001**: snake_case file names
- ✅ **DESIGN_RULE_002**: PascalCase class names
- ✅ **DESIGN_RULE_004**: Inherit from ARObject
- ✅ **DESIGN_RULE_005**: serialize/deserialize methods (inherited)
- ✅ **DESIGN_RULE_006**: Builder classes
- ✅ **DESIGN_RULE_042**: Circular import handling (TYPE_CHECKING)
- ✅ **DESIGN_RULE_040**: All imports at file beginning

## Serialization Framework

### Reflection-Based Architecture

Model classes use a reflection-based serialization framework that eliminates boilerplate:

**Key Components**:
- `ARObject.serialize()` - Base method using `vars()` and `get_type_hints()`
- `ARObject.deserialize()` - Class method for XML deserialization
- `NameConverter` - Utility for snake_case ↔ UPPER-CASE-WITH-HYPHENS conversion
- `@xml_attribute`, `@atp_variant()`, `@l_prefix()` - Decorators for edge cases only

**No XMLMember, No Registry, No Strategies!**

### Automatic Behavior

The framework automatically:
- Discovers all non-private attributes via `vars(self)`
- Converts Python names to XML tags using `NameConverter`
- Uses type hints for deserialization
- Handles nested objects, lists, and primitives
- Supports optional fields and circular imports

### Decorator Usage

Use decorators only when XML structure doesn't match default behavior:

```python
from armodel.serialization.decorators import xml_attribute

class AUTOSAR(ARObject):
    def __init__(self) -> None:
        self._schema_version: str = "4.5.0"
        # XML tag name is auto-generated as AUTOSAR
        self.ar_packages: list[ARPackage] = []

    @xml_attribute  # Serialize as XML attribute
    @property
    def schema_version(self) -> str:
        return self._schema_version
```

### Circular Import Handling

For classes with circular dependencies, use `TYPE_CHECKING`:

```python
from __future__ import annotations
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from armodel.models.M2.SomeModule import SomeClass

class MyClass(ARObject):
    related: Optional[SomeClass] = None  # Type hint works, no runtime import
```

The `ARObject.deserialize()` method handles this automatically by falling back to string annotations and dynamic imports.

### Documentation

See `docs/designs/serialization.md` for complete serialization framework documentation including:
- Decorator usage and examples
- Name conversion rules
- Common patterns
- Troubleshooting guide

## Known Limitations

### Generator Issues
- Import path resolution for certain types requires manual fixes
- Examples: `TableSeparatorString`, OasisExchangeTable enums

### Complex Structures
- Some nested structures may have incomplete deserialize() implementations
- Performance optimization for very large files (100MB+) needed

### Testing
- Round-trip tests (read → serialize → deserialize → compare) needed for all classes
- Integration tests for complex nested structures

## Future Improvements

1. **Performance**: Optimize for very large ARXML files (100MB+)
2. **Validation**: Add XSD validation support
3. **Type Safety**: Improve enum type handling
4. **Generator**: Fix import path resolution issues
5. **Testing**: Comprehensive round-trip test coverage

## References

- **Design Rules**: `docs/designs/design_rules.md`
- **Generator**: `tools/generate_models.py`
- **Requirements**: `docs/requirements/req_models.md`
- **Metadata**: `docs/json/` mapping files
