# py-armodel2 Project Guide

This document provides comprehensive context about this Python project for AI agents to guide subsequent development and maintenance work.

## Project Overview

**py-armodel2** is a Python library for processing AUTOSAR (AUTomotive Open System ARchitecture) ARXML models. The project adopts a code generation architecture, automatically generating static Python classes from mapping files to represent AUTOSAR type definitions.

**Project Status**: Early development stage, core infrastructure is in place, implementing core features.

### Core Features

- **Code Generation Driven**: All AUTOSAR model classes are automatically generated from `docs/requirements/mapping.json`
- **Multi-Version Support**: Supports three AUTOSAR schema versions: 00044, 00046, and 00052
- **Static Type Safety**: Uses Python type hints and MyPy type checking
- **Complete Test Coverage**: Unit tests and integration tests
- **Modern Toolchain**: Uses Ruff for code formatting and linting, Pytest for testing

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

# 4. Generate model classes (if needed)
python tools/generate_models.py docs/requirements/mapping.json src/armodel/models/
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
- **mypy 1.0+**: Static type checking
- **ruff 0.1.0+**: Code lint and formatting

## Project Structure

```
py-armodel2/
├── src/armodel/              # Source code
│   ├── cfg/                 # Configuration files
│   │   └── schemas/        # Schema version configuration
│   │       └── config.yaml # Version mapping configuration
│   ├── core/               # Core utilities
│   │   ├── __init__.py    # Module initialization
│   │   └── version.py     # Schema version detection
│   ├── models/             # Generated AUTOSAR model classes
│   │   └── M2/            # AUTOSAR M2 model definitions
│   ├── reader/             # ARXML reading module
│   │   ├── __init__.py    # Module initialization
│   │   ├── loader.py      # ARXML file loader
│   │   └── mapper.py      # Element mapper
│   ├── writer/             # ARXML writing module
│   │   ├── __init__.py    # Module initialization
│   │   ├── saver.py       # ARXML file saver
│   │   └── serializer.py  # Serializer
│   ├── cli/                # Command line interface (to be implemented)
│   │   └── __init__.py    # Module initialization
│   └── utils/              # Utility tools (to be implemented)
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
│   │   └── test_read_write_cycle.py  # Read-write cycle tests
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
│   ├── plans/             # Implementation plans
│   │   ├── CODING_RULES.md # Coding rules
│   │   ├── design-rules.md # Design rules
│   │   ├── AGENTS.md      # AI agent guide (this document)
│   │   └── *.md           # Other planning documents
│   ├── designs/           # Design documents
│   └── requirements/      # Requirements documents
│       └── mapping.json   # Type definition mapping (1,937 types)
├── pyproject.toml         # Project configuration
├── .github/workflows/     # CI/CD configuration
│   └── ci.yml            # GitHub Actions workflows
├── .gitignore             # Git ignore rules
├── README.md              # Project description
├── AGENTS.md              # AI agent guide (root directory copy)
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
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest --cov=src --cov-report=html

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

### Code Generation

```bash
# Generate all model classes from mapping.json
python tools/generate_models.py docs/requirements/mapping.json src/armodel/models/
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

## Development Conventions

### Coding Standards

The project follows these coding rules (defined in `docs/plans/CODING_RULES.md`):

#### Naming Conventions
- **File names**: Use snake_case (e.g., `test_version.py`)
- **Class names**: Use PascalCase (e.g., `ApplicationInterface`)
- **Function/Variable names**: Use snake_case

#### Class Structure
- All generated classes must inherit from `ARObject`
- Each class must include `serialize()` and `deserialize()` methods
- Each class must include a builder class for instantiation
- Builder classes are named `<ClassName>Builder`

#### Serialization/Deserialization
- `serialize()` returns `xml.etree.ElementTree.Element`
- `deserialize()` is a `@classmethod` that accepts an element parameter
- All child elements must be serialized using their `serialize()` method
- All child elements must be deserialized using their `deserialize()` method

#### Package Structure
- Package hierarchy must exactly match the `package_path` in `mapping.json`
- Each class has its own file in the matching directory
- `__init__.py` exports all classes in the package

#### Type Safety
- Use type hints for all class attributes
- Use `Optional[T]` for nullable attributes
- Document complex types with docstrings

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

#### Code Quality
- No hardcoded values (use configuration where appropriate)
- Follow PEP 8 style guide
- Maximum line length of 100 characters

### Git Workflow

- **Main branch**: `main`
- **Development branch**: `develop` (to be enabled)
- **Feature branches**: `feature/**`
- **Current branch**: `main`
- **Remote branch**: `origin/main` (default HEAD)

### CI/CD

GitHub Actions configuration (`.github/workflows/ci.yml`) includes:
- **Lint**: Code checking with Ruff
- **Type Check**: Type checking with MyPy
- **Test**: Run tests on Python 3.9-3.11
- **Coverage**: Upload coverage reports to Codecov

Trigger conditions:
- **Push**: main, develop, feature/** branches
- **Pull Request**: main, develop branches

## AUTOSAR Schema Versions

The project supports multiple AUTOSAR standard versions:

### Version Mapping (config.yaml)

| Version | Namespace                               | XSD File              | Features                          |
|---------|-----------------------------------------|-----------------------|-----------------------------------|
| 00044   | http://autosar.org/3.0.4               | AUTOSAR_00044.xsd     | Classic Platform 4.3.1 (2017)    |
| 00046   | http://autosar.org/schema/r4.0         | AUTOSAR_00046.xsd     | CP 4.4.0 / AP 18-10 (2018)       |
| 00052   | http://autosar.org/schema/r5.0         | AUTOSAR_00052.xsd     | CP/AP 23-11 (2023)                |

**Default version**: 00046

### Schema Variants and Validation Modes

Different versions support different validation modes and features:

| Version | Validation Mode   | Features                          |
|---------|-------------------|-----------------------------------|
| 00044   | strict            | Strict validation                 |
| 00046   | standard          | Standard validation + compact_schema |
| 00052   | strict            | Strict validation + compact_schema + strict_compact |

**Default version**: 00046

## Core Architecture

### Model Generation

All AUTOSAR model classes are generated from `docs/requirements/mapping.json`:
- **1,937 type definitions**
- Generated classes are placed in `src/armodel/models/`, following package paths
- Each class includes serialize/deserialize methods
- Includes builder classes for easy object creation

**Code Generator**: `tools/generate_models.py`
- Automatically creates directory structure
- Generates Python class files for each type
- Includes class definitions and Builder classes

### Reader Module

ARXML file reading and parsing:
- **loader.py**: Loads ARXML files using lxml
- **mapper.py**: Element mapper (to be completed)
- Supports loading from file paths
- Automatically handles XML syntax errors

### Writer Module

ARXML file writing and serialization:
- **saver.py**: Saves ARXML files using xml.etree.ElementTree
- **serializer.py**: Serializer (to be completed)
- Supports formatted output
- Automatically creates parent directories

### Schema Version Support

Multiple AUTOSAR schema versions are supported through `cfg/schemas/config.yaml`:
- Version detection from ARXML namespace declarations
- Version-specific parsing and validation
- Backward compatibility for old ARXML files
- Forward compatibility considerations for new versions

**Version Detection**: `src/armodel/core/version.py`
- `detect_schema_version()`: Detects schema version from XML element
- `get_default_version()`: Gets default version (00046)

## Important File Descriptions

### Configuration Files
- `pyproject.toml`: Project configuration, dependencies, and tool settings
- `.github/workflows/ci.yml`: CI/CD configuration
- `src/armodel/cfg/config.yaml`: Configuration file loading entry point
- `src/armodel/cfg/schemas/config.yaml`: Schema version configuration

### Code Generation
- `tools/generate_models.py`: Model class generator
- `docs/requirements/mapping.json`: Type definition mapping (317KB, 1,937 types)

### Core Modules
- `src/armodel/core/version.py`: Schema version detection

### Reader Module
- `src/armodel/reader/loader.py`: ARXML file loader (uses lxml)
- `src/armodel/reader/mapper.py`: Element mapper

### Writer Module
- `src/armodel/writer/saver.py`: ARXML file saver (uses ElementTree)
- `src/armodel/writer/serializer.py`: Serializer

### Testing
- `tests/unit/`: Unit tests (mirrors src structure)
- `tests/integration/`: Integration tests
- `tests/fixtures/`: Test data (AUTOSAR ARXML files)
- `tests/test_generate_models.py`: Code generator tests

### Documentation
- `docs/plans/CODING_RULES.md`: Coding rules
- `docs/plans/design-rules.md`: Design rules
- `docs/plans/AGENTS.md`: AI agent guide (this document)
- `README.md`: Project overview and quick start
- `AGENTS.md`: AI agent guide copy in root directory
- `CLAUDE.md`: Claude AI configuration

## Common Tasks

### Adding a New AUTOSAR Type

1. Add type definition in `docs/requirements/mapping.json`
2. Run code generator: `python tools/generate_models.py docs/requirements/mapping.json src/armodel/models/`
3. Add unit tests for the new type

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

### Code Generation Tests
- `tests/test_generate_models.py`: Tests code generator
- Verifies generated code complies with coding rules

## Performance Considerations

- Use compact schema for validation to reduce overhead
- Consider caching mechanisms for large ARXML files
- Use batch processing for frequent operations

## Security Considerations

- Validate all user-input ARXML files
- Use schema validation to prevent XML injection
- Limit file size to prevent DoS attacks

## AUTOSAR References

- Official AUTOSAR specifications: https://www.autosar.org
- Schema version numbering follows AUTOSAR document identifiers (e.g., AUTOSAR_00052)
- Each schema version corresponds to specific AUTOSAR Classic Platform and Adaptive Platform versions

## Project Information

- **Project Author**: Your Name (your.email@example.com)
- **License**: MIT
- **Current Version**: 0.1.0
- **Development Status**: Alpha (Early development)
- **Target Users**: AUTOSAR tool developers, automotive software engineers

## Known Limitations

- CLI module not yet implemented
- Utils module not yet implemented
- Model class serialization/deserialization logic needs completion
- Performance optimization for large ARXML files pending
- Schema validation functionality pending

## Future Plans

See implementation plan documents in `docs/plans/` directory:
- `2026-02-15-armodel2-implementation.md`: Detailed implementation plan
- `2026-02-15-class-based-refactoring.md`: Class refactoring plan