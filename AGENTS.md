# py-armodel2 Project Guide

This document provides comprehensive context about this Python project for AI agents to guide subsequent development and maintenance work.

## Project Overview

**py-armodel2** is a Python library for processing AUTOSAR (AUTomotive Open System ARchitecture) ARXML models. The project adopts a code generation architecture, automatically generating static Python classes to represent AUTOSAR type definitions.

**Project Status**: Core infrastructure is complete and functional. The library can read, parse, write, and serialize ARXML files with full support for AUTOSAR schema versions 00044, 00046, and 00052.

### Core Features

- **Code Generation Driven**: AUTOSAR model classes are automatically generated from JSON metadata files
- **Multi-Version Support**: Supports three AUTOSAR schema versions: 00044, 00046, and 00052
- **Static Type Safety**: Uses Python type hints and MyPy strict type checking
- **Complete Test Coverage**: Unit tests and integration tests
- **Modern Toolchain**: Uses Ruff for code formatting and linting, Pytest for testing
- **Class-Based Architecture**: All infrastructure modules use class-based design with dependency injection and singleton patterns
- **Full ARXML Support**: Read, parse, validate, write, and serialize ARXML files
- **Builder Pattern**: All model classes include Builder classes for fluent API
- **Automatic Hierarchy Handling**: Base class automatically handles serialize/deserialize for entire class hierarchy via `_xml_members` pattern

### Development Environment Requirements

- **Operating System**: macOS, Linux, Windows
- **Python Version**: 3.9, 3.10, 3.11
- **Package Manager**: pip
- **Optional Tools**: git, GitHub CLI (gh)

### Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/melodypapa/py-armodel2.git
cd py-armodel2

# 2. Install dependencies
pip install -e ".[dev]"

# 3. Run tests to verify installation
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest

# 4. Read an ARXML file
python -c "
from armodel.reader import ARXMLReader
reader = ARXMLReader()
autosar = reader.load_arxml('demos/arxml/AUTOSAR_Datatypes.arxml')
print(f'Loaded AUTOSAR with {len(autosar.ar_packages)} packages')
"
```

## Tech Stack

### Core Dependencies
- **Python 3.9+**: Minimum Python version requirement
- **lxml 4.9.0+**: XML parsing (used in reader module)
- **xml.etree.ElementTree**: XML parsing (standard library, used in writer module)
- **PyYAML 6.0+**: Configuration file parsing

### Development Tools
- **pytest 7.0+**: Testing framework
- **pytest-cov 4.0+**: Code coverage
- **mypy 1.0+**: Static type checking (strict mode enabled)
- **ruff 0.1.0+**: Code lint and formatting
- **lxml-stubs 0.4.0+**: Type stubs for lxml (added for better type checking)
- **types-PyYAML 6.0+**: Type stubs for PyYAML (added for better type checking)

### MyPy Configuration
- **Strict mode**: Enabled for all source code
- **Line length**: 100 characters
- **Target Python**: 3.9
- **Special override**: Generated model files (`armodel.models.M2.*`) are excluded from strict type checking requirements (`disallow_untyped_defs = false`, `disallow_untyped_calls = false`)
- **Project scripts**: `armodel` CLI command configured (main.py to be implemented)

### Code Generation Tools
- **JSON Metadata Files** (located in `docs/json/`):
  - `hierarchy.json`: Class inheritance hierarchy
  - `mapping.json`: Package and class name mappings
  - `index.json`: Class index for quick lookup
  - `packages/*.classes.json`: Detailed class definitions with attributes and types
  - `packages/*.enums.json`: Enum definitions
  - `packages/*.json`: Package metadata

## Project Structure

```
py-armodel2/
├── src/armodel/              # Source code
│   ├── cfg/                 # Configuration files
│   │   ├── __init__.py    # Module initialization (ConfigurationManager class)
│   │   ├── config.yaml    # Configuration entry point
│   │   └── schemas/       # Schema version configuration
│   │       ├── __init__.py # Module initialization
│   │       └── config.yaml # Version mapping configuration
│   ├── core/               # Core utilities
│   │   ├── __init__.py    # Module initialization
│   │   └── version.py     # SchemaVersionManager class (singleton)
│   ├── models/             # Generated AUTOSAR model classes
│   │   ├── __init__.py    # Module initialization
│   │   └── M2/            # AUTOSAR M2 model definitions (1,900+ files)
│   │       ├── __init__.py # Module initialization
│   │       ├── AUTOSARTemplates/ # AUTOSAR template classes
│   │       │   ├── autosar.py # AUTOSAR root element (singleton)
│   │       │   ├── AbstractPlatform/ # Abstract platform elements
│   │       │   ├── AdaptivePlatform/ # Adaptive platform elements
│   │       │   ├── AutosarTopLevelStructure/ # Top-level structure
│   │       │   ├── BswModuleTemplate/ # BSW module templates
│   │       │   ├── CommonStructure/ # Common structure classes
│   │       │   ├── DiagnosticExtract/ # Diagnostic extract elements
│   │       │   ├── ECUCDescriptionTemplate/ # ECUC description templates
│   │       │   ├── ECUCParameterDefTemplate/ # ECUC parameter definitions
│   │       │   ├── EcuResourceTemplate/ # ECU resource templates
│   │       │   ├── FeatureModelTemplate/ # Feature model templates
│   │       │   ├── GenericStructure/ # Generic structure classes
│   │       │   │   ├── GeneralTemplateClasses/ # Base classes
│   │       │   │   │   ├── ArObject/ # ARObject base class
│   │       │   │   │   ├── Identifiable/ # Identifiable hierarchy
│   │       │   │   │   ├── PrimitiveTypes/ # AUTOSAR primitive types
│   │       │   │   │   └── ... # Other generic classes
│   │       │   ├── LogAndTraceExtract/ # Log and trace elements
│   │       │   ├── SecurityExtractTemplate/ # Security extract templates
│   │       │   ├── SWComponentTemplate/ # Software component templates
│   │       │   └── SystemTemplate/ # System template elements
│   │       └── MSR/       # MSR (Measurement, Systems, Requirements) classes
│   │           ├── AsamHdo/ # ASAM HDO elements
│   │           ├── CalibrationData/ # Calibration data elements
│   │           ├── DataDictionary/ # Data dictionary elements
│   │           └── Documentation/ # Documentation elements
│   ├── reader/             # ARXML reading module
│   │   └── __init__.py    # ARXMLReader class (class-based architecture)
│   ├── writer/             # ARXML writing module
│   │   └── __init__.py    # ARXMLWriter class (class-based architecture)
│   ├── cli/                # Command line interface
│   │   └── __init__.py    # Module initialization (main.py to be implemented)
│   └── utils/              # Utility tools (placeholder)
│       └── __init__.py    # Module initialization
├── tests/                  # Test suite
│   ├── unit/              # Unit tests (mirrors src structure)
│   │   ├── test_core/     # Core module tests
│   │   ├── test_models/   # Model class tests
│   │   ├── test_reader/   # Reader module tests
│   │   ├── test_writer/   # Writer module tests
│   │   └── test_tools/    # Tools tests
│   ├── integration/       # Integration tests
│   │   ├── test_read_arxml.py        # ARXML reading tests
│   │   ├── test_write_arxml.py       # ARXML writing tests
│   │   ├── test_read_write_cycle.py  # Read-write cycle tests
│   │   └── test_application_data_type_blueprint.py  # Application data type tests
│   ├── fixtures/          # Test data
│   │   └── arxml/         # ARXML test files
│   └── test_generate_models.py # Code generator tests
├── tools/                  # Code generation tools
│   └── generate_models.py # Model class generator
├── scripts/                # Development scripts
│   └── setup.sh           # Development environment setup script
├── demos/                  # AUTOSAR schema and example files
│   ├── xsd/               # XSD schema files
│   │   ├── AUTOSAR_00044/
│   │   ├── AUTOSAR_00046/
│   │   └── AUTOSAR_00052/
│   └── arxml/             # ARXML example files
├── docs/                   # Documentation
│   ├── json/              # JSON metadata for code generation
│   │   ├── hierarchy.json # Class inheritance hierarchy
│   │   ├── mapping.json   # Package and class mappings
│   │   ├── index.json     # Class index
│   │   └── packages/      # Package definitions
│   │       ├── *.classes.json  # Class attribute definitions
│   │       └── *.enums.json    # Enum definitions
│   ├── plans/             # Implementation plans
│   │   ├── class-todo.md   # Class generation TODO
│   │   └── todo.md         # General TODO
│   ├── reports/           # Project reports
│   │   └── class-todo-items.md  # Class generation items
│   ├── designs/           # Design documents
│   │   └── design_rules.md # Design rules (12 categories, 40 rules)
│   ├── requirements/      # Requirements documents
│   │   ├── req_cfg.md     # Configuration requirements
│   │   ├── req_codegen.md # Code generation requirements
│   │   ├── req_core.md    # Core module requirements
│   │   ├── req_element_mapping.md  # Element mapping requirements
│   │   ├── req_models.md  # Model requirements
│   │   ├── req_reader.md  # Reader requirements
│   │   └── req_writer.md  # Writer requirements
│   └── tests/             # Test documentation
│       ├── integration/   # Integration test plans
│       └── unit/          # Unit test plans
├── .claude/                # Claude AI configuration
│   └── commands/          # Custom slash commands
│       ├── gen-class.md   # Class generation command
│       ├── gh-workflow.md # GitHub workflow command
│       ├── merge-pr.md    # PR merge command
│       ├── quality.md     # Quality check command
│       ├── req.md         # Requirements command
│       ├── test.md        # Test command
│       └── README.md      # Commands documentation
├── pyproject.toml         # Project configuration
├── .github/workflows/     # CI/CD configuration
│   └── ci.yml            # GitHub Actions workflows
├── .gitignore             # Git ignore rules
├── README.md              # Project description
├── AGENTS.md              # AI agent guide (this document)
└── CLAUDE.md              # Claude AI configuration
```

## Building and Running

### Installation and Setup

```bash
# Using setup script (recommended)
./scripts/setup.sh

# Or manual installation
pip install -e ".[dev]"
```

### Running Tests

```bash
# Set PYTHONPATH and run tests
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest

# Run tests with coverage
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest --cov=armodel --cov-report=html --cov-report=term

# Run specific test file
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/unit/test_core/test_version.py -v
```

### Code Quality Checks

```bash
# Lint check
ruff check src/ tools/

# Code formatting
ruff format src/ tools/

# Type checking
mypy src/
```

### Command Line Tools (To Be Implemented)

```bash
# View help
armodel --help

# Check ARXML file
armodel check path/to/file.arxml

# Convert ARXML file
armodel convert input.arxml output.arxml --version 00046
```

### Custom Claude Commands

The project includes custom slash commands for AI agents:

- `/gen-class`: Generate or update classes from ARXML files using JSON metadata
- `/gh-workflow`: Manage GitHub workflows and actions
- `/merge-pr`: Merge pull requests with validation
- `/quality`: Run quality checks (lint, format, type check)
- `/req`: View and manage requirements
- `/test`: Run tests with various options

See `.claude/commands/README.md` for detailed usage.

## Development Conventions

### Coding Standards

The project follows these coding rules (defined in `docs/designs/design_rules.md` and `docs/requirements/req_element_mapping.md`):

#### Naming Conventions
- **File names**: Use snake_case (e.g., `test_version.py`)
- **Class names**: Use PascalCase (e.g., `ApplicationInterface`)
- **Function/Variable names**: Use snake_case

#### XML Tag/Attribute to Python Name Mapping
- **XML Tags**: AUTOSAR kebab-case → Python PascalCase
  - `SW-BASE-TYPE` → `SwBaseType`
  - `IMPLEMENTATION-DATA-TYPE` → `ImplementationDataType`
- **XML Attributes**: AUTOSAR kebab-case → Python snake_case
  - `SHORT-NAME` → `short_name`
  - `BASE-TYPE-SIZE` → `base_type_size`

#### Class Structure
- All generated classes must inherit from `ARObject` (FULLY IMPLEMENTED)
- Each class must include `serialize()` and `deserialize()` methods (FULLY IMPLEMENTED)
- Each class must include a builder class for instantiation (FULLY IMPLEMENTED)
- Builder classes are named `<ClassName>Builder` (FULLY IMPLEMENTED)
- Builder classes use fluent API pattern (FULLY IMPLEMENTED)

#### _xml_members Pattern (CRITICAL)
- Each class defines `_xml_members` for its own attributes only (not inherited)
- Format: `(member_name, xml_tag_name, is_attribute, is_list, element_class)`
- ARObject base class automatically handles entire class hierarchy
- XML tag names are auto-converted from member names when `xml_tag_name` is `None`

#### Serialization/Deserialization
- `serialize()` accepts `namespace: str` parameter (FULLY IMPLEMENTED)
- `serialize()` returns `xml.etree.ElementTree.Element` (FULLY IMPLEMENTED)
- `deserialize()` is a `@classmethod` that accepts an element parameter (FULLY IMPLEMENTED)
- All child elements must be serialized using their `serialize()` method (FULLY IMPLEMENTED)
- All child elements must be deserialized using their `deserialize()` method (FULLY IMPLEMENTED)
- Namespace handling in XML tags (FULLY IMPLEMENTED)
- Automatic hierarchy handling via `_xml_members` pattern (FULLY IMPLEMENTED)

#### Package Structure
- Package hierarchy follows AUTOSAR namespace structure
- Each class has its own file in the matching directory
- `__init__.py` exports all classes in the package

#### Type Safety
- Use type hints for all class attributes
- Use `Optional[T]` for nullable attributes (multiplicity 0..1)
- Use `list[T]` for multiple attributes (multiplicity *)
- Use `str` for string representations of numeric values
- Use `typing.Any` for AUTOSAR "any (...)" types
- Document complex types with docstrings

#### Initialization Rules
- Single objects (multiplicity 1 or 0..1): Initialize to `None`
- Lists (multiplicity * or 0..*): Initialize to `[]` (never `None`)
- Required primitives: Can initialize to `0`, `""`, `False` or use `None`
- Never use Optional for lists

#### Validation
- All attributes must be validated in the `builder.build()` method
- Raise `ValueError` for invalid attribute values
- Validate that required attributes exist

#### Documentation
- Each class must have a docstring
- Each method must have a docstring
- Document complex logic with inline comments

#### Testing
- Each class must have unit tests
- Tests must cover serialize/deserialize
- Tests must verify builder functionality

#### Architecture (DESIGN_RULE_032-035)
- Use class-based architecture instead of module-based (FULLY IMPLEMENTED)
- All infrastructure modules (core, reader, writer, cfg) use class-based design (FULLY IMPLEMENTED)
- Infrastructure classes use dependency injection for testability (FULLY IMPLEMENTED)
- Singleton pattern is used for shared state managers (FULLY IMPLEMENTED)

#### Infrastructure Classes (DESIGN_RULE_036-039)
- **SchemaVersionManager**: Manages schema version detection and configuration (singleton) - FULLY IMPLEMENTED
- **ConfigurationManager**: Provides configuration loading with caching - FULLY IMPLEMENTED
- **ARXMLReader**: Handles ARXML file loading and mapping to objects - FULLY IMPLEMENTED
- **ARXMLWriter**: Handles object serialization and ARXML file saving - FULLY IMPLEMENTED

#### Code Quality
- No hardcoded values (use config where appropriate)
- Follow PEP 8 style guide
- Maximum line length of 100 characters
- Full type hints on all public APIs
- Comprehensive docstrings for all classes and methods
- All import statements must be defined at the beginning of the file

### Git Workflow

- **Main branch**: `main`
- **Feature branches**: `feature/**`
- **Current branch**: `main`
- **Remote branch**: `origin/main` (default HEAD)

### CI/CD

GitHub Actions configuration (`.github/workflows/ci.yml`) includes:
- **Lint**: Code checking with Ruff (on Ubuntu, Python 3.9)
- **Type Check**: Type checking with MyPy strict mode (on Ubuntu, Python 3.9)
- **Test**: Run tests on Python 3.9, 3.10, 3.11 with coverage
- **Coverage**: Upload coverage reports to Codecov (from Python 3.9 job)

Trigger conditions:
- **Push**: main, feature/** branches
- **Pull Request**: main, develop branches

**Note**: MyPy strict mode is enabled but generated model files (`armodel.models.M2.*`) are excluded from strict type checking requirements.

## AUTOSAR Schema Versions

The project supports multiple AUTOSAR standard versions:

### Version Mapping (config.yaml)

| Version | Namespace                               | XSD File(s)                                      | Features                          |
|---------|-----------------------------------------|--------------------------------------------------|-----------------------------------|
| 00044   | http://autosar.org/3.0.4               | AUTOSAR_00044.xsd                                 | Classic Platform 4.3.1 (2017)    |
| 00046   | http://autosar.org/schema/r4.0         | AUTOSAR_00046_COMPACT.xsd, AUTOSAR_STRICT_COMPACT.xsd | CP 4.4.0 / AP 18-10 (2018)       |
| 00052   | http://autosar.org/schema/r5.0         | AUTOSAR_00052.xsd                                 | CP/AP 23-11 (2023)                |

**Default version**: 00046

### Schema Variants and Validation Modes

Different versions support different validation modes and features:

| Version | Validation Mode   | Features                          |
|---------|-------------------|-----------------------------------|
| 00044   | strict            | Strict validation                 |
| 00046   | standard          | Standard validation + compact_schema (supports both COMPACT and STRICT_COMPACT schemas) |
| 00052   | strict            | Strict validation + compact_schema + strict_compact |

**Default version**: 00046

## Core Architecture

### Model Generation

AUTOSAR model classes are automatically generated from JSON metadata files:
- **1,900+ generated Python files** covering AUTOSAR M2 model definitions
- Generated classes are placed in `src/armodel/models/`, following package paths
- Each class includes serialize/deserialize methods
- Includes builder classes for fluent API
- Full type hints for all attributes and methods
- Comprehensive docstrings for classes and methods
- Automatic hierarchy handling via `_xml_members` pattern

**Code Generator**: `tools/generate_models.py`
- Standalone tool for generating model classes
- Reads JSON metadata from `docs/json/` directory
- Automatically creates directory structure
- Generates Python class files for each type
- Includes class definitions and Builder classes
- Follows all coding standards defined in `docs/designs/design_rules.md`
- Uses `_xml_members` pattern for XML mapping

**JSON Metadata Files**:
- `docs/json/hierarchy.json`: Class inheritance hierarchy
- `docs/json/mapping.json`: Package and class name mappings
- `docs/json/index.json`: Class index for quick lookup
- `docs/json/packages/*.classes.json`: Detailed class definitions with attributes and types
- `docs/json/packages/*.enums.json`: Enum definitions

### Class-Based Architecture (DESIGN_RULE_032-039)

The project uses a class-based architecture for infrastructure modules:

**Core Infrastructure Classes:**
- **SchemaVersionManager** (`src/armodel/core/version.py`): Singleton class for schema version detection and configuration management (FULLY IMPLEMENTED)
- **ConfigurationManager** (`src/armodel/cfg/schemas/__init__.py`): Provides configuration loading with caching (FULLY IMPLEMENTED)
- **ARXMLReader** (`src/armodel/reader/__init__.py`): Handles ARXML file loading and mapping to objects using dependency injection (FULLY IMPLEMENTED)
- **ARXMLWriter** (`src/armodel/writer/__init__.py`): Handles object serialization and ARXML file saving using dependency injection (FULLY IMPLEMENTED)

**Design Principles:**
- Singleton pattern for shared state managers (SchemaVersionManager, AUTOSAR)
- Dependency injection for testability (ARXMLReader, ARXMLWriter)
- Class-based design instead of module-based functions
- Clear separation of concerns
- Full type safety with comprehensive type hints

### _xml_members Pattern (Automatic Hierarchy Handling)

**CRITICAL ARCHITECTURAL PATTERN**: The project uses a unique `_xml_members` pattern for automatic XML serialization/deserialization hierarchy handling.

**Key Features:**
1. Each class defines `_xml_members` for its own attributes only
2. Base class automatically collects `_xml_members` from entire hierarchy
3. XML tag names are auto-converted from member names
4. Serialize/deserialize methods delegate to base class

**Example:**
```python
class Referrable(ARObject):
    # Only define members for this class, not inherited ones
    _xml_members = [
        ("short_name", None, False, False, None),  # Primitive child element
        ("short_name_fragments", None, False, True, ShortNameFragment),  # List of objects
    ]

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        # Base class handles entire hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Referrable":
        # Base class handles entire hierarchy automatically
        obj = super().deserialize(element)
        return cast("Referrable", obj)
```

**_xml_members Format:**
```python
_xml_members = [
    (member_name, xml_tag_name, is_attribute, is_list, element_class)
]
```

**Parameters:**
- `member_name`: Python attribute name (snake_case)
- `xml_tag_name`: XML tag/attribute name (or `None` to auto-convert)
- `is_attribute`: `True` = XML attribute, `False` = child element
- `is_list`: `True` = member is a list, `False` = single value
- `element_class`: For child elements, the class to deserialize (or `None` for primitives)

**XML Tag Inference:**
When `xml_tag_name` is `None`, tags are automatically converted:
- `short_name` → `SHORT-NAME`
- `category` → `CATEGORY`
- `data_type` → `DATA-TYPE`

### Reader Module

ARXML file reading and parsing:
- **ARXMLReader** (`src/armodel/reader/__init__.py`): Main class-based reader with dependency injection
  - `load_arxml(filepath, validate=False)`: Load ARXML and return AUTOSAR object
  - `get_schema_version(filepath)`: Detect schema version without loading entire file
  - Automatic schema version detection from namespace
  - Optional XSD schema validation
  - Support for all three schema versions (00044, 00046, 00052)
  - All functionality consolidated in single class (no separate loader.py or mapper.py)

### Writer Module

ARXML file writing and serialization:
- **ARXMLWriter** (`src/armodel/writer/__init__.py`): Main class-based writer with dependency injection
  - `save_arxml(autosar, filepath)`: Save AUTOSAR object to ARXML file
  - `to_string(autosar)`: Convert AUTOSAR object to XML string
  - `configure(pretty_print, encoding)`: Update writer configuration
  - Configurable pretty printing
  - Custom encoding support
  - Automatic directory creation
  - Namespace registration for proper XML output
  - All functionality consolidated in single class (no separate saver.py or serializer.py)

### Schema Version Support

Multiple AUTOSAR schema versions are supported through `cfg/schemas/config.yaml`:
- Version detection from ARXML namespace declarations
- Version-specific parsing and validation
- Backward compatibility for old ARXML files
- Forward compatibility considerations for new versions

**Version Detection**: `src/armodel/core/version.py` - `SchemaVersionManager` class (singleton)
- `detect_schema_version(root)`: Detects schema version from XML element
- `get_default_version()`: Gets default version (00046)
- `get_config(version)`: Gets configuration for specific schema version
- `get_namespace(version)`: Gets namespace URI for specific schema version
- `get_xsd_path(version)`: Gets XSD file path for specific schema version
- `get_all_versions()`: Gets list of all available schema versions
- `reload()`: Reloads configuration from file

### Model Class Hierarchy

All generated model classes follow a strict inheritance hierarchy:

```
ARObject (base class)
├── Referrable (adds short_name)
│   ├── Identifiable (adds identifier properties)
│   │   ├── Describable (adds description properties)
│   │   └── ARElement (AUTOSAR-specific element)
│   └── PackageableElement (can be in packages)
│       └── CollectableElement (can be in collections)
│           └── ARPackage (package container)
└── [Generated AUTOSAR Classes]
```

**Key Model Classes:**
- **AUTOSAR**: Root element (singleton), contains AR-PACKAGES
- **ARPackage**: Package container, contains elements and sub-packages
- **CompuMethod**: Computation method for data conversion
- **SwBaseType**: Base type definition
- **DataConstr**: Data constraint definition
- **ImplementationDataType**: Implementation data type

Each generated class includes:
- Full serialize() implementation with namespace support
- Full deserialize() implementation with namespace handling
- Builder class for fluent API
- Type hints for all attributes
- Comprehensive docstrings
- `_xml_members` for automatic hierarchy handling

## Important File Descriptions

### Configuration Files
- `pyproject.toml`: Project configuration, dependencies, and tool settings (includes MyPy strict mode)
- `.github/workflows/ci.yml`: CI/CD configuration
- `src/armodel/cfg/config.yaml`: Configuration file loading entry point
- `src/armodel/cfg/schemas/config.yaml`: Schema version configuration

### Code Generation Metadata
- `docs/json/hierarchy.json`: Class inheritance hierarchy (used by code generator)
- `docs/json/mapping.json`: Package and class name mappings (used by code generator)
- `docs/json/index.json`: Class index for quick lookup (used by code generator)
- `docs/json/packages/*.classes.json`: Detailed class definitions (used by code generator)
- `docs/json/packages/*.enums.json`: Enum definitions (used by code generator)

### Code Generation Tools
- `tools/generate_models.py`: Model class generator (reads JSON metadata from `docs/json/`)
- `.claude/commands/gen-class.md`: Custom command for class generation

### Core Modules
- `src/armodel/core/version.py`: SchemaVersionManager class (singleton pattern) - Fully implemented
- `src/armodel/core/__init__.py`: Module initialization, exports core classes

### Reader Module
- `src/armodel/reader/__init__.py`: ARXMLReader class (class-based architecture, dependency injection)

**ARXMLReader Features:**
- Load ARXML files and convert to AUTOSAR objects
- Automatic schema version detection
- Optional XSD schema validation
- Support for all three schema versions

### Writer Module
- `src/armodel/writer/__init__.py`: ARXMLWriter class (class-based architecture, dependency injection)

**ARXMLWriter Features:**
- Serialize AUTOSAR objects to ARXML files
- Configurable pretty printing
- Custom encoding support
- XML string conversion
- Namespace registration for proper XML output

### CLI Module
- `src/armodel/cli/__init__.py`: CLI module initialization (main.py to be implemented)
- Entry point configured: `armodel = "armodel.cli.main:main"`

### Testing
- `tests/unit/`: Unit tests (mirrors src structure)
- `tests/integration/`: Integration tests (read, write, read-write cycle)
- `tests/fixtures/`: Test data (AUTOSAR ARXML files)
- `tests/test_generate_models.py`: Code generator tests

**Current Integration Tests:**
- `test_read_arxml.py`: ARXML reading tests
- `test_write_arxml.py`: ARXML writing tests
- `test_read_write_cycle.py`: Read-write cycle tests
- `test_application_data_type_blueprint.py`: Application data type blueprint tests

### Documentation
- `docs/designs/design_rules.md`: Design rules (12 categories, 40 rules)
- `docs/requirements/req_element_mapping.md`: Element mapping requirements (12 requirements)
- `docs/plans/class-todo.md`: Class generation TODO list
- `docs/reports/class-todo-items.md`: Class generation items report
- `README.md`: Project overview and quick start
- `AGENTS.md`: AI agent guide (this document)
- `CLAUDE.md`: Claude AI configuration

## Common Tasks

### Reading ARXML Files

```python
from armodel.reader import ARXMLReader

# Create reader instance
reader = ARXMLReader()

# Load ARXML file
autosar = reader.load_arxml('path/to/file.arxml')

# Load with validation
autosar = reader.load_arxml('path/to/file.arxml', validate=True)

# Get schema version without loading
version = reader.get_schema_version('path/to/file.arxml')
print(f"Schema version: {version}")

# Access loaded data
print(f"Number of packages: {len(autosar.ar_packages)}")
for pkg in autosar.ar_packages:
    print(f"Package: {pkg.short_name}")
```

### Writing ARXML Files

```python
from armodel.writer import ARXMLWriter
from armodel.models.M2.AUTOSARTemplates.autosar import AUTOSAR

# Create writer instance
writer = ARXMLWriter(pretty_print=True, encoding="UTF-8")

# Write AUTOSAR object to file
writer.save_arxml(autosar, 'path/to/output.arxml')

# Convert to XML string
xml_string = writer.to_string(autosar)

# Update configuration
writer.configure(pretty_print=False, encoding="ASCII")
```

### Creating AUTOSAR Objects Programmatically

```python
from armodel.models.M2.AUTOSARTemplates.autosar import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_package import ARPackage, ARPackageBuilder
from armodel.models.M2.MSR.AsamHdo.BaseTypes.sw_base_type import SwBaseType, SwBaseTypeBuilder

# Create AUTOSAR root
autosar = AUTOSAR()

# Create package using builder
pkg = (ARPackageBuilder()
       .with_short_name("MyPackage")
       .with_category("DataTypes")
       .build())

# Create data type using builder
base_type = (SwBaseTypeBuilder()
             .with_short_name("MyType")
             .with_category("FIXED")
             .with_base_type_size("32")
             .build())

# Add to package
pkg.elements.append(base_type)

# Add to AUTOSAR
autosar.ar_packages.append(pkg)

# Save to file
from armodel.writer import ARXMLWriter
writer = ARXMLWriter()
writer.save_arxml(autosar, 'output.arxml')
```

### Generating Classes from ARXML

Use the `/gen-class` custom command to generate or update classes:

1. Analyze ARXML file structure
2. Query JSON metadata (`docs/json/hierarchy.json`, `docs/json/packages/*.classes.json`)
3. Generate or update classes with correct inheritance and attributes
4. Use `_xml_members` pattern for XML mapping

See `.claude/commands/gen-class.md` for detailed instructions.

### Adding a New AUTOSAR Type

1. Define the new AUTOSAR type structure
2. Add to JSON metadata files in `docs/json/`
3. Generate the model class using `/gen-class` command
4. Add unit tests for the new type
5. Update container classes' TAG_CLASS_MAP if needed

### Fixing Bugs

1. Add or update test cases in `tests/`
2. Fix the code
3. Run tests to verify fix: `PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest`
4. Run lint and type checks: `ruff check src/ && mypy src/`

### Updating Dependencies

1. Update versions in `pyproject.toml`
2. Run `pip install -e ".[dev]"`
3. Run tests to ensure compatibility

## Testing Strategy

### Unit Tests
- Mirror `src/` directory structure
- Each module has a corresponding test file
- Use pytest framework
- Current test modules:
  - `test_core/`: Core functionality tests
  - `test_models/`: Model class tests
  - `test_reader/`: Reader module tests
  - `test_writer/`: Writer module tests
  - `test_tools/`: Tools tests

### Integration Tests
- Test complete ARXML read/write workflows
- Use actual AUTOSAR files from `tests/fixtures/`
- Current integration tests:
  - `test_read_arxml.py`: ARXML reading tests
  - `test_write_arxml.py`: ARXML writing tests
  - `test_read_write_cycle.py`: Read-write cycle tests
  - `test_application_data_type_blueprint.py`: Application data type blueprint tests

### Code Generation Tests
- `tests/test_generate_models.py`: Tests code generator
- Verifies generated code complies with coding rules

## Performance Considerations

- Use compact schema for validation to reduce overhead
- Consider caching mechanisms for large ARXML files
- Use batch processing for frequent operations
- `_xml_members` pattern reduces serialization overhead

## Security Considerations

- Validate all user-input ARXML files
- Use schema validation to prevent XML injection
- Limit file size to prevent DoS attacks
- Proper namespace handling prevents XML parsing attacks

## AUTOSAR References

- Official AUTOSAR specifications: https://www.autosar.org
- Schema version numbering follows AUTOSAR document identifiers (e.g., AUTOSAR_00052)
- Each schema version corresponds to specific AUTOSAR Classic Platform and Adaptive Platform versions

## Project Information

- **Project Author**: Your Name (your.email@example.com)
- **License**: MIT
- **Current Version**: 0.1.0
- **Development Status**: Alpha (Core infrastructure complete, working towards beta)
- **Target Users**: AUTOSAR tool developers, automotive software engineers
- **Generated Model Files**: 1,900+ Python files covering AUTOSAR M2 model definitions
- **Code Coverage**: Comprehensive unit and integration tests

## CLI Configuration

The project includes a CLI entry point configured in `pyproject.toml`:

```toml
[project.scripts]
armodel = "armodel.cli.main:main"
```

**Current Status**: CLI module structure exists but `main.py` is not yet implemented.

**Planned Commands** (from design documents):
```bash
# View help
armodel --help

# Check ARXML file
armodel check path/to/file.arxml

# Convert ARXML file
armodel convert input.arxml output.arxml --version 00046
```

## Known Limitations

- CLI module (main.py) not yet implemented
- Utils module not yet implemented (placeholder only)
- Some model classes may have incomplete deserialize() implementations for complex nested structures
- Performance optimization for very large ARXML files (100MB+) could be improved
- Schema validation is implemented but may have edge cases with custom XSD files
- Full support for all AUTOSAR types is ongoing (1,900+ files currently generated)

## Future Plans

**Priority Areas for Future Development:**
1. Complete CLI implementation (main.py)
2. Enhance deserialize() implementations for complex types
3. Add more comprehensive integration tests
4. Performance optimization for large files
5. Add utility functions for common operations
6. Complete documentation and examples
7. Add support for ARXML modification and transformation
8. Improve code generation tool with better error handling
9. Add support for validation rules beyond schema validation

## Implementation Status

### Completed Features ✅
- Project structure and configuration
- Schema version detection and management (SchemaVersionManager singleton)
- Model code generation framework (1,900+ files generated)
- Basic model class generation with serialize/deserialize
- Builder pattern implementation for all generated classes
- `_xml_members` pattern for automatic hierarchy handling
- Test framework setup
- CI/CD pipeline configuration
- Type checking configuration with MyPy strict mode
- ARXMLReader class with dependency injection
- ARXMLWriter class with dependency injection
- AUTOSAR root element (singleton pattern)
- ARPackage model with element handling
- Core AUTOSAR types (CompuMethod, SwBaseType, DataConstr, ImplementationDataType)
- XSD schema validation support
- Integration tests for read/write cycles
- Full type hints on all public APIs
- Comprehensive docstrings for all classes
- JSON metadata files for code generation
- Custom Claude commands for AI agents
- Element mapping requirements documentation

### In Progress 🚧
- Complete deserialize() implementations for complex nested structures
- Full support for all AUTOSAR types (1,900+ files currently generated)
- Advanced model operations and transformations
- Performance optimization for large files
- Class generation TODO items (see `docs/plans/class-todo.md`)

### Planned 📋
- CLI implementation (main.py)
- Utility functions for common operations
- Advanced model operations
- Performance optimization
- Complete documentation and examples
- Additional integration tests
- ARXML modification and transformation tools
- Enhanced code generation tool with validation