# AGENTS.md

This file provides guidance to AI agents working with the py-armodel2 codebase.

## Project Overview

**py-armodel2** is a Python library for processing AUTOSAR (Automotive Open System Architecture) ARXML models. The project uses a code generation architecture with **2,200+ generated AUTOSAR model classes** that support full reading, parsing, writing, and serialization of ARXML files across multiple AUTOSAR schema versions.

**Key Architecture:**
- **Reflection-based serialization** - Zero boilerplate, uses Python's `vars()` and `get_type_hints()`
- **Code generation** - All model classes auto-generated from AUTOSAR schema mappings
- **Multi-version support** - Handles AUTOSAR 00044, 00046, and 00052 schemas
- **Type-safe** - Strict type hints throughout with MyPy enforcement

## Development Commands

### Environment Setup
```bash
# Install in development mode with all dependencies
pip install -e ".[dev]"
```

### Running Tests
```bash
# Run all tests (requires PYTHONPATH)
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest

# Run specific test file
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/unit/core/test_version.py -v

# Run tests with coverage
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest --cov=src --cov-report=html --cov-report=term

# Run specific test methods
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/unit/core/test_version.py::TestSchemaVersionManager::test_singleton_pattern -v

# Run integration tests
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/integration/test_autosar_datatypes.py -v
```

### Linting and Formatting
```bash
# Lint code
ruff check src/ tools/

# Format code
ruff format src/ tools/

# Type checking (strict mode, excludes generated models)
mypy src/
```

### Code Generation
```bash
# Regenerate all model classes (after generator or mapping changes)
python tools/generate_models.py docs/json/mapping.json docs/json/hierarchy.json src/armodel/models/M2 --members --classes --enums --primitives

# Generate YAML model mappings (after model class changes)
python tools/generate_model_mappings.py
```

**Special Classes:**
- **AUTOSAR** and **ARObject** are manually maintained and **NOT** auto-generated
- The code generator will skip these classes with a warning message
- These classes contain critical serialization infrastructure that requires careful manual maintenance
- AUTOSAR is the root element for all ARXML files
- ARObject is the base class implementing reflection-based serialization

### Verification After Changes
```bash
# Full verification pipeline after code generation changes
ruff check src/
mypy src/
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest
```

## Code Style Guidelines

### File and Naming Conventions
- **Files**: snake_case (e.g., `schema_version_manager.py`)
- **Classes**: PascalCase (e.g., `SchemaVersionManager`) 
- **Functions/Variables**: snake_case
- **Constants**: UPPER_SNAKE_CASE
- **Generated model files**: One class per file, matching AUTOSAR package structure

### Import Style
```python
# Standard imports first
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import TYPE_CHECKING, Optional

# Third-party imports
from lxml import etree

# Internal imports with block format for multiple classes
from armodel.models.M2.SomePackage.some_module import (
    ClassA,
    ClassB,
)

# Use TYPE_CHECKING for circular imports
if TYPE_CHECKING:
    from armodel.models.M2.SomeModule import SomeClass
```

### Type Hints
- **All class attributes must have type hints** at class level (not just in `__init__`)
- Use `Optional[T]` for nullable attributes
- Use `from __future__ import annotations` for complex circular dependencies
- Strict typing enforced via MyPy with generated model exclusions

### Circular Import Handling
```python
from __future__ import annotations  # Must be first import
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from armodel.models.M2.SomeModule import SomeClass

class MyClass(ARObject):
    related: Optional[SomeClass] = None  # Type hint works, no runtime import
```

### Class Structure
Infrastructure classes follow dependency-injection pattern:
```python
class SomeClass:
    """Brief description following class name."""
    
    def __init__(self, dependency: Optional[DependencyType] = None):
        """Initialize with dependency injection for testability."""
        self._dependency = dependency or DefaultDependency()
    
    def method(self) -> ReturnType:
        """Method description with Args/Returns as needed."""
        # Implementation
        pass
```

### Error Handling
- Use specific exception types (`ValueError`, `FileNotFoundError`, etc.)
- Document exceptions in docstrings
- Validate inputs in `builder.build()` methods
- Use `raise ValueError("descriptive message")` for invalid input

### Testing Conventions
```python
import pytest

class TestClassName:
    """Unit tests for ClassName class."""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup test fixtures."""
        self.instance = ClassName()
    
    def test_descriptive_name(self):
        """Test specific functionality."""
        # Arrange, Act, Assert pattern
        assert self.instance.method() == expected_value
```

### Documentation
- All classes and methods must have docstrings
- Use Google-style docstrings with Args/Returns sections
- Document complex logic with inline comments
- Maximum line length: **100 characters**

### Package Structure
- **infrastructure** (`core`, `reader`, `writer`, `cfg`, `serialization`, `utils`) - use class-based design with dependency injection
- **generated** (`models/M2/`) - 2,200+ files, do not edit manually
- **Singleton pattern** for shared state managers (e.g., `SchemaVersionManager`)

## Architecture Patterns

### Singleton Pattern
```python
class SomeManager:
    _instance: Optional["SomeManager"] = None
    _initialized: bool = False
    
    def __new__(cls) -> "SomeManager":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

### Builder Pattern
All generated classes include a Builder:
```python
obj = (ClassNameBuilder()
       .with_attribute(value)
       .with_another_attribute(value)
       .build())
```

## Reflection-Based Serialization Framework

### Overview

The project uses a reflection-based serialization framework that eliminates boilerplate code. The framework consists of:

- **Base class**: `ARObject` - provides `serialize()` and `deserialize()` methods
- **Name converter**: `NameConverter` - handles snake_case ↔ UPPER-CASE-WITH-HYPHENS conversion
- **Decorators**: Edge case handlers for special XML scenarios

### Key Components

#### 1. ARObject Base Class

Location: `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ArObject/ar_object.py`

```python
class ARObject:
    def serialize(self, namespace: str = "") -> ET.Element:
        """Serialize object to XML using reflection."""
        # Uses vars() to discover all attributes
        # Converts names via NameConverter
        # Handles objects, lists, and primitives
    
    @classmethod
    def deserialize(cls, element: ET.Element) -> Self:
        """Deserialize XML to Python object."""
        # Uses get_type_hints() for type information
        # Recursively deserializes child objects
```

#### 2. NameConverter

Location: `src/armodel/serialization/name_converter.py`

```python
class NameConverter:
    @staticmethod
    def to_xml_tag(name: str) -> str:
        """short_name → SHORT-NAME"""
        return name.upper().replace('_', '-')

    @staticmethod
    def to_python_name(tag: str) -> str:
        """SHORT-NAME → short_name"""
        return tag.lower().replace('-', '_')

    @staticmethod
    def tag_to_class_name(tag: str) -> str:
        """SW-BASE-TYPE → SwBaseType"""
        # Handles AR prefix and acronyms
```

#### 3. ModelFactory

Location: `src/armodel/serialization/model_factory.py`

The ModelFactory provides efficient class instantiation from XML tags with support for polymorphic type resolution.

```python
from armodel.serialization import ModelFactory

# Get singleton instance
factory = ModelFactory()

# Load mappings (automatic if not loaded)
if not factory.is_initialized():
    factory.load_mappings()

# Get class from XML tag
cls = factory.get_class("SW-BASE-TYPE")  # Returns SwBaseType class

# Resolve polymorphic type
concrete_cls = factory.resolve_polymorphic_type(
    "SW-BASE-TYPE",
    "PackageableElement"
)
```

**Features:**
- Singleton pattern for global access
- Cached class imports for performance
- Polymorphic type resolution using YAML mappings
- Automatic XML tag to class name conversion

**YAML Mappings File:** `src/armodel/cfg/model_mappings.yaml`

The YAML file is generated from JSON mapping data and contains:
- XML tag to class name mappings (1623+ classes)
- Polymorphic type mappings (233 base classes with concrete implementations)
- Class name to import path mappings

**Generating YAML Mappings:**
```bash
python tools/generate_model_mappings.py
```

#### 4. Decorators

Location: `src/armodel/serialization/decorators.py`

```python
@xml_attribute  # Mark property as XML attribute
@xml_tag("NAME")  # Specify custom XML tag name
```

### Serialization Behavior

**How serialize() works:**
1. Get XML tag name (from `@xml_tag` or auto-generate from class name)
2. Iterate attributes via `vars(self)`
3. Convert names via `NameConverter.to_xml_tag()`
4. Check for `@xml_attribute` decorator
5. Serialize objects, lists, or primitives

**How deserialize() works:**
1. Create instance using `cls.__new__(cls)`
2. Get type hints via `get_type_hints()`
3. For each attribute, find matching XML element/attribute
4. Parse value based on type hint
5. Recursively deserialize child objects

### Type Hints and Multiplicity

| AUTOSAR Multiplicity | Python Type | Initial Value |
|---------------------|-------------|---------------|
| `0..1` | `Optional[Type]` | `None` |
| `1` | `Type` | `None` |
| `*` | `list[Type]` | `[]` |
| `0..*` | `list[Type]` | `[]` |

### Common Patterns

**Pattern 1: Simple Class (No Decorators)**
```python
class ARPackage(ARObject):
    short_name: Optional[str] = None
    ar_packages: list[ARPackage] = []
```

**Pattern 2: XML Attribute**
```python
class AUTOSAR(ARObject):
    def __init__(self) -> None:
        self._schema_version: str = "4.5.0"
    
    @xml_attribute
    @property
    def schema_version(self) -> str:
        return self._schema_version
```

**Pattern 3: Custom Tag Name**
```python
@xml_tag("AUTOSAR")
class AUTOSAR(ARObject):
    pass
```

## Key Files and Modules

### Core Infrastructure
- **SchemaVersionManager** (`src/armodel/core/version.py`) - Schema version detection
- **NameConverter** (`src/armodel/serialization/name_converter.py`) - Name conversion utility
- **ModelFactory** (`src/armodel/serialization/model_factory.py`) - Factory for creating AUTOSAR model instances from XML tags with polymorphic type resolution
- **Decorators** (`src/armodel/serialization/decorators.py`) - XML serialization decorators
- **ARObject** (`src/armodel/models/M2/.../ArObject/ar_object.py`) - Base class with serialize/deserialize

### Reader/Writer
- **ARXMLReader** (`src/armodel/reader/__init__.py`) - ARXML file loading with merge support
- **ARXMLWriter** (`src/armodel/writer/__init__.py`) - ARXML serialization with formatting

### Configuration
- **ConfigurationManager** (`src/armodel/cfg/schemas/__init__.py`) - Config loading
- **Schema configs** (`src/armodel/cfg/config.yaml`) - Version-specific settings

### Code Generation
- **Code Generator** (`tools/generate_models.py`) - Regenerate all model classes
- **Mapping files** (`docs/json/mapping.json`, `docs/json/hierarchy.json`) - AUTOSAR schema mappings

### CLI Module
- **Main Entry** (`src/armodel/cli/main.py`) - CLI entry point with argparse router
- **Common Utilities** (`src/armodel/cli/common.py`) - Exit codes and file validation helpers
- **Commands** (`src/armodel/cli/commands/`) - Subcommand implementations
  - `format.py` - ARXML formatting command

## New API Usage

### Reader API (Load Multiple Files)

```python
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.autosar import AUTOSAR
from armodel.reader import ARXMLReader

# Create AUTOSAR instance
autosar = AUTOSAR()

# Load multiple files into same instance
reader = ARXMLReader()
reader.load_arxml(autosar, "demos/arxml/AUTOSAR_Datatypes.arxml")
reader.load_arxml(autosar, "demos/arxml/another_file.arxml")

# Packages from multiple files are merged into autosar.ar_packages
print(f"Total packages: {len(autosar.ar_packages)}")
```

### Writer API (Save to File)

```python
from armodel.writer import ARXMLWriter

writer = ARXMLWriter(pretty_print=True, encoding="UTF-8")
writer.save_arxml(autosar, "output.arxml")
```

### CLI Tool

The CLI uses a multi-command architecture (similar to `git` or `docker`):

```bash
# Install to get CLI tool
pip install -e ".[dev]"

# Show version
armodel --version

# Show help
armodel --help

# Format ARXML files
armodel format INPUT.arxml -o OUTPUT.arxml
```

#### `armodel format` - Format ARXML Files

Reads, parses, and reformats ARXML files with pretty-printing:

```bash
# Basic formatting
armodel format unformatted.arxml -o formatted.arxml

# Strict validation mode (fail on errors)
armodel format input.arxml -o output.arxml --strict

# Permissive mode (continue on warnings)
armodel format input.arxml -o output.arxml --permissive

# Custom encoding
armodel format input.arxml -o output.arxml --encoding UTF-8

# Verbose output for debugging
armodel format input.arxml -o output.arxml -v

# Quiet mode (for scripts/CI)
armodel format input.arxml -o output.arxml -q
```

**Arguments:**
| Argument | Description |
|----------|-------------|
| `INPUT` | Input ARXML file path (required) |
| `-o, --output` | Output ARXML file path (required) |
| `--strict` | Enable strict validation (fail on errors) |
| `--permissive` | Enable permissive mode (continue on warnings) |
| `--encoding` | Output encoding (default: UTF-8) |
| `--no-pretty-print` | Disable pretty-printing |
| `-v, --verbose` | Show detailed error messages |
| `-q, --quiet` | Suppress output messages |

**Exit Codes:**
| Code | Constant | Description |
|------|----------|-------------|
| 0 | `EXIT_SUCCESS` | Success |
| 1 | `EXIT_FILE_NOT_FOUND` | Input file not found |
| 2 | `EXIT_PARSE_ERROR` | ARXML parsing error |
| 3 | `EXIT_WRITE_ERROR` | File write error |
| 4 | `EXIT_UNHANDLED_ERROR` | Unhandled exception |

## Generated Code Notes

- **Do not edit** files in `src/armodel/models/M2/` - they are auto-generated
  - **Exception**: AUTOSAR and ARObject are manually maintained - see below
- Each class has `serialize()`, `deserialize()`, and corresponding Builder
- Uses reflection-based serialization with automatic attribute discovery
- Follows AUTOSAR package structure exactly
- No `_xml_members` dict needed - type hints drive serialization
- MSR Documentation models (2,200+ files) included

### Manually Maintained Classes

The following classes are **NOT** auto-generated and must be maintained manually:

1. **AUTOSAR** (`src/armodel/models/M2/AUTOSARTemplates/AutosarTopLevelStructure/autosar.py`)
   - Root element for all ARXML files
   - Contains `@xml_tag("AUTOSAR")` decorator for proper XML serialization
   - May have special attributes like `schema_version` with `@xml_attribute` decorator

2. **ARObject** (`src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ArObject/ar_object.py`)
   - Base class for all AUTOSAR model classes
   - Implements `serialize()` and `deserialize()` methods using reflection
   - Contains the core serialization infrastructure
   - Uses `vars()` and `get_type_hints()` for automatic attribute discovery
   - Provides `NameConverter` integration for snake_case ↔ UPPER-CASE conversion

**Why manual maintenance?**
- These classes contain critical infrastructure that requires careful implementation
- They define the serialization framework that all other classes inherit from
- Changes to these classes affect the entire codebase
- The code generator explicitly skips these classes to prevent accidental overwrites

## Python Version Support

- **Minimum**: Python 3.9
- **Tested**: 3.9, 3.10, 3.11
- **Target**: py39 in pyproject.toml

## Special Considerations

- Always specify `PYTHONPATH=/Users/ray/Workspace/py-armodel2/src` when running pytest
- Generated model files are excluded from MyPy strict checking
- Use `lxml` for parsing XML, `xml.etree.ElementTree` for serialization
- Schema versions: 00044, 00046 (default), 00052
- AUTOSAR namespace detection via XML parsing
- The same AUTOSAR instance can be reused for multiple `load_arxml()` operations
- Round-trip serialization tested with `AUTOSAR_Datatypes.arxml`

## Documentation

### Design Documents
- **Serialization Framework**: `docs/designs/serialization.md`
- **Design Rules**: `docs/designs/design_rules.md`
- **Model Design**: `docs/designs/model_design.md`

### Test Documentation
- **Integration Tests**: `docs/tests/integration/test_autosar_data_types.md`
- **Unit Tests**: `docs/tests/unit/` (various modules)

### CLI Documentation
- **CLI Design**: `docs/plans/2026-02-18-cli-arxml-formatter-design.md`
- **CLI Implementation**: `docs/plans/2026-02-18-cli-arxml-formatter.md`

### Examples
- **New API Example**: `examples/new_api_example.py`

## Dependencies

### Core Dependencies
- `lxml>=4.9.0` - XML parsing
- `pyyaml>=6.0` - Configuration loading

### Development Dependencies
- `pytest>=7.0` - Testing framework
- `pytest-cov>=4.0` - Code coverage
- `mypy>=1.0` - Type checking
- `ruff>=0.1.0` - Linting and formatting
- `lxml-stubs>=0.4.0` - Type stubs for lxml
- `types-PyYAML>=6.0` - Type stubs for PyYAML

## Testing Strategy

### Unit Tests
- Located in `tests/unit/`
- Mirror the `src/` directory structure
- Test individual components in isolation
- CLI tests in `tests/unit/cli/` (main entry point, command handlers)

### Integration Tests
- Located in `tests/integration/`
- Test complete workflows (read → process → write)
- Main test: `test_autosar_datatypes.py` validates round-trip with real ARXML file
- CLI integration tests in `tests/integration/cli/` (end-to-end command testing)

### Test Data
- ARXML files: `demos/arxml/`
- XSD schemas: `demos/xsd/`
- Test fixtures: `tests/fixtures/`