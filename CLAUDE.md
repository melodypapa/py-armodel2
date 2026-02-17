# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**py-armodel2** is a Python library for processing AUTOSAR (Automotive Open System Architecture) ARXML models. The project uses a code generation architecture where AUTOSAR model classes (1,912 files) are automatically generated and support full reading, parsing, writing, and serialization of ARXML files across multiple AUTOSAR schema versions.

## Development Commands

```bash
# Installation
pip install -e ".[dev]"

# Regenerate all model classes (after generator or mapping changes)
python tools/generate_models.py

# Run tests (requires PYTHONPATH)
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest

# Run specific test file
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/unit/test_core/test_version.py -v

# Run tests with coverage
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest --cov=src --cov-report=html --cov-report=term

# Lint
ruff check src/ tools/

# Format
ruff format src/ tools/

# Type check (strict mode, excludes generated models)
mypy src/
```

## Architecture

### Code Generation

All AUTOSAR model classes in `src/armodel/models/M2/` are generated from mapping data. Key characteristics:
- **1,912 generated Python files** covering AUTOSAR M2 model definitions
- Each class has `serialize()` and `deserialize()` methods
- Each class includes a Builder for fluent API construction
- Generated classes follow AUTOSAR package structure
- Uses registry-based serialization framework with XMLMember metadata

**Generator**: `tools/generate_models.py` (standalone tool)

**Regenerate after**: Modifying the generator, changing mapping JSON files, or updating serialization framework

### Serialization Framework (Reflection-Based)

The project uses a reflection-based serialization framework that eliminates boilerplate:

**Key Components**:
- `ARObject.serialize()` - Base method that uses reflection to discover attributes
- `ARObject.deserialize()` - Class method that deserializes using type hints
- `NameConverter` - Utility for snake_case ↔ UPPER-CASE-WITH-HYPHENS conversion
- `@xml_attribute`, `@xml_tag()` - Decorators for edge cases

**Each class defines**:
- Type hints on class attributes (drive deserialization)
- Optional decorators for edge cases (XML attributes, custom tags)
- No `_xml_members` dict needed!

**The base class handles the rest**:
- Uses `vars()` to discover all attributes automatically
- Uses `get_type_hints()` for type information
- Converts names automatically via NameConverter
- Supports nested objects, lists, and primitives

**Example**:
```python
class AUTOSAR(ARObject):
    admin_data: Optional[AdminData]
    ar_packages: list[ARPackage]  # Automatically serialized as <AR-PACKAGES><AR-PACKAGE>...
    file_info: Optional[FileInfoComment]

# Automatically discovers these attributes via vars() and serializes!
```

### Class-Based Architecture

Infrastructure modules use class-based design (not module-based functions):

**Singletons** (shared state):
- `SchemaVersionManager` (`src/armodel/core/version.py`) - Schema version detection and config
- `AUTOSAR` (`src/armodel/models/M2/AUTOSARTemplates/autosar.py`) - Root AUTOSAR element

**Dependency Injection** (testable):
- `ARXMLReader` (`src/armodel/reader/__init__.py`) - ARXML file loading and parsing
- `ARXMLWriter` (`src/armodel/writer/__init__.py`) - ARXML serialization and file saving
- `ConfigurationManager` (`src/armodel/cfg/schemas/__init__.py`) - Configuration loading with caching

### Model Class Hierarchy

All generated classes inherit from `ARObject` base class:

```
ARObject
├── Referrable (short_name property)
│   ├── Identifiable (identifier properties)
│   │   ├── Describable (description properties)
│   │   └── ARElement (AUTOSAR-specific)
│   └── PackageableElement
│       └── ARPackage
```

Key classes:
- `AUTOSAR`: Root element (singleton), contains AR-PACKAGES
- `ARPackage`: Package container with elements and sub-packages
- `CompuMethod`, `SwBaseType`, `DataConstr`, `ImplementationDataType`: Core AUTOSAR types

### Schema Version Support

Multiple AUTOSAR versions supported via `src/armodel/cfg/schemas/config.yaml`:

| Version | Namespace                                    | XSD                          |
|---------|----------------------------------------------|------------------------------|
| 00044   | http://autosar.org/3.0.4                    | AUTOSAR_00044.xsd            |
| 00046   | http://autosar.org/schema/r4.0              | AUTOSAR_00046_COMPACT.xsd    |
| 00052   | http://autosar.org/schema/r5.0              | AUTOSAR_00052.xsd            |

**Default version**: 00046

Version detection automatically parses XML namespace declarations from ARXML files.

### Design Rules

Key rules from `docs/designs/design_rules.md`:
- **Naming**: snake_case files, PascalCase classes
- **Serialization**: `serialize(namespace, element)` returns `xml.etree.ElementTree.Element`
- **Deserialization**: `@classmethod deserialize(element)` accepts XML element
- **All infrastructure classes**: Class-based with dependency injection
- **Singletons**: Used for shared state managers
- **Circular imports**: Use `from __future__ import annotations` with `TYPE_CHECKING` for type hints only
- **Imports**: All imports at file beginning, use relative imports within same package

## Important Implementation Details

### Circular Import Handling

The codebase uses `from __future__ import annotations` combined with `TYPE_CHECKING` to avoid circular import issues:

```python
from __future__ import annotations  # Must be first import
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from armodel.models.M2.SomeModule import SomeClass

class MyClass(ARObject):
    related: Optional[SomeClass] = None  # Type hint works, no runtime import
```

The `ARObject.deserialize()` method uses dynamic class importing to handle circular dependencies:
- First tries `get_type_hints()` for actual types
- Falls back to `__annotations__` (strings) if `get_type_hints()` fails
- Dynamically imports classes by name using `_import_class_by_name()`

This allows seamless deserialization even with complex circular dependencies.

## Important Implementation Details

### Reader/Writer Architecture

- **ARXMLReader**: Uses `lxml` for parsing, converts to `xml.etree.ElementTree` for model deserialization
- **ARXMLWriter**: Uses `xml.etree.ElementTree` for serialization (not lxml)
- Both accept optional `SchemaVersionManager` injection for testability
- `ARXMLReader.get_schema_version()` detects version without full file load
- **Namespace handling**: All serialize() methods accept namespace parameter; deserialize() strips namespaces from tags

### Type Checking

MyPy runs in **strict mode** (`strict = true`) with one override:
```toml
[[tool.mypy.overrides]]
module = "armodel.models.M2.*"
disallow_untyped_defs = false
disallow_untyped_calls = false
```
Generated model files are excluded from strict requirements.

### XML Handling

- **lxml** (`>=4.9.0`): Used in reader for parsing and XSD validation
- **xml.etree.ElementTree** (stdlib): Used in writer and models for serialization
- Reader converts lxml elements to ElementTree elements before model deserialization

## Common Tasks

### Read ARXML file

```python
from armodel.reader import ARXMLReader

reader = ARXMLReader()
autosar = reader.load_arxml('path/to/file.arxml')
# With validation:
autosar = reader.load_arxml('path/to/file.arxml', validate=True)
```

### Write ARXML file

```python
from armodel.writer import ARXMLWriter

writer = ARXMLWriter(pretty_print=True, encoding="UTF-8")
writer.save_arxml(autosar, 'path/to/output.arxml')
```

### Detect schema version

```python
from armodel.reader import ARXMLReader

reader = ARXMLReader()
version = reader.get_schema_version('path/to/file.arxml')
```

### Create AUTOSAR objects

```python
from armodel.models.M2.AUTOSARTemplates.autosar import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_package import ARPackageBuilder

autosar = AUTOSAR()
pkg = (ARPackageBuilder()
       .with_short_name("MyPackage")
       .with_category("DataTypes")
       .build())
autosar.ar_packages.append(pkg)
```

### After modifying generator

When you modify `tools/generate_models.py` or the mapping JSON files, regenerate all classes:

```bash
python tools/generate_models.py
```

Then verify:
```bash
ruff check src/
mypy src/
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest
```

## Project Structure

```
src/armodel/
├── cfg/                 # Configuration (ConfigurationManager class)
├── core/                # Core utilities (SchemaVersionManager singleton)
├── models/M2/           # Generated AUTOSAR classes (1,912 files)
│   ├── AUTOSARTemplates/  # AUTOSAR template classes
│   └── MSR/              # MSR documentation classes
├── reader/              # ARXML reading (ARXMLReader class)
├── writer/              # ARXML writing (ARXMLWriter class)
├── serialization/       # Serialization framework (registry, strategies, metadata)
├── cli/                 # CLI (main.py not yet implemented)
└── utils/               # Utilities (not yet implemented)

tests/
├── unit/                # Unit tests (mirrors src structure)
├── integration/         # Integration tests (read, write, cycles)
└── fixtures/arxml/      # Test ARXML files

tools/
└── generate_models.py   # Code generator for AUTOSAR classes

demos/
├── xsd/                 # AUTOSAR XSD schema files
└── arxml/               # Sample ARXML files

docs/
├── designs/             # Design rules and architecture
├── json/                # Type mapping metadata for generator
├── requirements/        # Software requirements
└── tests/               # Test documentation
```

## Known Limitations

- CLI module (`main.py`) not implemented
- Utils module not implemented
- Some complex nested structures may have incomplete `deserialize()` implementations
- Performance optimization for very large files (100MB+) could be improved
- Generator has known issues with import path resolution for certain types (e.g., TableSeparatorString, enums in OasisExchangeTable) requiring manual fixes

## Key Reference Documents

- **Design Rules**: `docs/designs/design_rules.md` - Complete list of design rules including naming, structure, and import patterns
- **Generator Skill**: `.claude/commands/gen-class.md` - Interactive command for generating classes from ARXML files
- **Requirements**: `docs/requirements/` - Detailed functional and non-functional requirements for each module
