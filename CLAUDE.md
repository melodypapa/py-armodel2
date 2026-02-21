# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**py-armodel2** is a Python library for processing AUTOSAR (Automotive Open System Architecture) ARXML models. The project uses a code generation architecture where AUTOSAR model classes (~2,200 files) are automatically generated and support full reading, parsing, writing, and serialization of ARXML files across multiple AUTOSAR schema versions.

## Development Commands

### Installation
```bash
pip install -e ".[dev]"
```

### Testing (Critical: PYTHONPATH Required)
**IMPORTANT**: All pytest commands must set `PYTHONPATH` to include the `src` directory:

```bash
# Run all tests
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest

# Run specific test file
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/unit/test_core/test_version.py -v

# Run with coverage
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest --cov=src --cov-report=html --cov-report=term

# Binary comparison integration tests (verify read/write cycle produces identical XML)
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/integration/test_binary_comparison.py -v
```

**Note**: The project does not use pytest.ini or conftest to set PYTHONPATH. It must be set manually for each test run.

### Code Generation
```bash
# Regenerate all model classes (after generator or mapping changes)
python -m tools.generate_models --members

# Or from project root
python -m tools.generate_models --members
```

### Quality Checks
```bash
# Lint
ruff check src/ tools/

# Format
ruff format src/ tools/

# Type check (strict mode, excludes generated models)
mypy src/
```

## Architecture

### Code Generation

All AUTOSAR model classes in `src/armodel/models/M2/` are generated from mapping data in `docs/json/`:

**Generator**: `python -m tools.generate_models` (module in `tools/generate_models/`)

**Key Characteristics**:
- **~2,200 generated Python files** covering AUTOSAR M2 model definitions
- Each class has `serialize()` and `deserialize()` methods
- Each class includes a Builder for fluent API construction
- Generated classes follow AUTOSAR package structure exactly
- Uses reflection-based serialization with decorator system for edge cases

**When to Regenerate**:
- After modifying `tools/generate_models/` code
- After changing mapping JSON files in `docs/json/`
- After updating serialization framework

**⚠️ CRITICAL RULE: NEVER Edit Generated Code Directly**

If you find bugs, issues, or needed improvements in files under `src/armodel/models/M2/`:
- **DO NOT** edit the generated files directly - your changes will be lost on next regeneration
- **DO** fix the issue in `tools/generate_models/` (the generator)
- **THEN** regenerate by running: `python -m tools.generate_models --members`

**Exception**: Only classes listed in `tools/skip_classes.yaml` should be manually edited (AUTOSAR, ARObject, ARRef, ARPackage, CompuMethod*, Item, DocumentationBlock, LanguageSpecific*)

**Manually Maintained Classes** (defined in `tools/skip_classes.yaml`):
- `AUTOSAR` - Root element
- `ARObject` - Base class implementing reflection-based serialization
- `ARRef` - AUTOSAR reference type with DEST/BASE attributes
- `ARPackage` - Package with custom long_name handling
- `CompuMethod*` - Custom compu logic (CompuMethod, Compu, CompuScales, CompuScale, CompuConst, CompuConstTextContent)
- `Item` - Custom serialization for item_contents
- `DocumentationBlock` - Language-specific elements (L-1 through L-10)
- `LanguageSpecific*` - Language-specific classes (LLongName, LPlainText, LParagraph, etc.)

### Reflection-Based Serialization Framework

The project uses a reflection-based serialization framework that eliminates boilerplate code for 95% of classes:

**Key Components**:
- `ARObject.serialize()` - Uses `vars()` to discover all attributes automatically
- `ARObject.deserialize()` - Uses `get_type_hints()` for type information
- `NameConverter` - Handles snake_case ↔ UPPER-CASE-WITH-HYPHENS conversion
- `ModelFactory` - Factory for creating model instances from XML tags (supports polymorphic deserialization)
- `@xml_attribute` - Decorator for XML attributes
- `@atp_variant()` - Decorator for AUTOSAR atpVariation pattern (auto-wraps in VARIANTS/CONDITIONAL)
- `@l_prefix()` - Decorator for language-specific L-N naming pattern

**How It Works**:
```python
class AUTOSAR(ARObject):
    admin_data: Optional[AdminData]
    ar_packages: list[ARPackage]  # Automatically serialized as <AR-PACKAGES><AR-PACKAGE>...
    file_info: Optional[FileInfoComment]

# No manual serialization needed! ARObject automatically:
# 1. Discovers attributes via vars()
# 2. Converts names via NameConverter (ar_packages → AR-PACKAGES)
# 3. Serializes using type hints
```

**Polymorphic Deserialization**: When an attribute is `Optional[BaseType]` and XML contains a concrete implementation tag (e.g., `COMPU-SCALES` instead of `COMPU-CONTENT`), the framework uses `ModelFactory` to find and deserialize the concrete class.

**Custom serialize/deserialize**: Override only when child element tag must differ from parent attribute name:
- **CompuMethod**: `compu_internal_to_phys` → `<COMPU-INTERNAL-TO-PHYS>`, `compu_phys_to_internal` → `<COMPU-PHYS-TO-INTERNAL>`
- **Item**: `item_contents` (DocumentationBlock) serializes as direct children of ITEM, not wrapped in ITEM-CONTENTS
- **Language-specific classes**: Handle L-N naming (L-1, L-2, L-4, L-5, L-10) with inheritance-based parsing

### Decorator System

The codebase uses decorators for XML serialization edge cases:

```python
# @xml_attribute - Serialize as XML attribute instead of element
@xml_attribute
@property
def schema_version(self) -> str:
    return self._schema_version
# Result: <AUTOSAR SCHEMA-VERSION="4.5.0">...</AUTOSAR>

# @atp_variant() - AUTOSAR atpVariation pattern
@atp_variant()
class SwDataDefProps(ARObject):
    base_type_ref: Optional[ARRef] = None
# Result: Wrapped in SW-DATA-DEF-PROPS-VARIANTS/SW-DATA-DEF-PROPS-CONDITIONAL

# @l_prefix("L-N") - Language-specific naming
@l_prefix("L-2")
def l_2(self) -> str:
    return self._l_2
# Result: <L-2>text</L-2> within multilanguage elements
```

### Class-Based Architecture

Infrastructure modules use class-based design (not module-based functions):

**Singletons** (shared state):
- `SchemaVersionManager` (`src/armodel/core/version.py`) - Schema version detection and config
- `AUTOSAR` (`src/armodel/models/M2/AUTOSARTemplates/autosar.py`) - Root AUTOSAR element
- `GlobalSettingsManager` (`src/armodel/core/settings.py`) - Application-wide settings (strict_validation, warn_on_unrecognized)

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

### Schema Version Support

Multiple AUTOSAR versions supported via `src/armodel/cfg/schemas/config.yaml`:

| Version | Namespace                                    | XSD                          |
|---------|----------------------------------------------|------------------------------|
| 00044   | http://autosar.org/3.0.4                    | AUTOSAR_00044.xsd            |
| 00046   | http://autosar.org/schema/r4.0              | AUTOSAR_00046_COMPACT.xsd    |
| 00052   | http://autosar.org/schema/r5.0              | AUTOSAR_00052.xsd            |

**Default version**: 00046

Version detection automatically parses XML namespace declarations from ARXML files.

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

**How ARObject.deserialize() handles circular dependencies**:
1. First tries `get_type_hints()` for actual types
2. Falls back to `__annotations__` (strings) if `get_type_hints()` fails
3. Dynamically imports classes by name using `_import_class_by_name()`

**Force TYPE_CHECKING**: `tools/skip_classes.yaml` defines types that always need TYPE_CHECKING:
- `AbstractImplementationDataType`, `SwDataDefProps`, `ApplicationPrimitiveDataType`, `ValueSpecification`

### Primitive and Enum Type Wrappers

**ARPrimitive**: Wraps primitive values (int, float, str, bool) with AUTOSAR type information
- Automatically unwrapped to native Python types during deserialization
- Transparently compares with native types: `ARPrimitive(5) == 5` returns `True`

**AREnum**: Wraps enumeration values
- Transparently compares with string values: `AREnum("VALUE") == "VALUE"` returns `True`
- All enum values use UPPER_SNAKE_CASE formatting (enforced by code generator)

```python
# During deserialization, ARPrimitive is automatically unwrapped
value = ar_object.some_int  # Returns int 42, not ARPrimitive(42)

# Enum comparisons work transparently
if ar_object.some_enum == "EXPECTED_VALUE":  # Works even if some_enum is AREnum
    ...
```

### ARRef Reference Type

`ARRef` represents AUTOSAR references with DEST/BASE attributes:

**XML Format**:
```xml
<SW-ADDR-METHOD-REF DEST="SW-ADDR-METHOD" BASE="DataTypes">/Package/Element</SW-ADDR-METHOD-REF>
```

**Python Usage**:
```python
ref = ARRef(dest="SW-ADDR-METHOD", value="/Package/Element", base="DataTypes")
```

**Key Points**:
- DEST attribute specifies the target type (required for most references)
- BASE attribute specifies the base package/type (optional)
- Text content contains the reference path
- Serialized with `-REF` or `-TREF` suffix based on JSON "kind" field in mappings

### Reader/Writer Architecture

- **ARXMLReader**: Uses `lxml` for parsing, converts to `xml.etree.ElementTree` for model deserialization
- **ARXMLWriter**: Uses `xml.etree.ElementTree` for serialization (not lxml)
- Both accept optional `SchemaVersionManager` injection for testability
- `ARXMLReader.get_schema_version()` detects version without full file load
- **Namespace handling**: All serialize() methods accept namespace parameter; deserialize() strips namespaces from tags

### Type Checking

MyPy runs in **strict mode** (`strict = true`) with overrides for generated files:

```toml
[[tool.mypy.overrides]]
module = "armodel.models.M2.*"
disallow_untyped_defs = false
disallow_untyped_calls = false
ignore_errors = true
```

Generated model files are excluded from strict requirements.

## Common Tasks

### Format ARXML Files (CLI)
```bash
# Basic formatting
armodel format input.arxml -o output.arxml

# With validation
armodel format input.arxml -o output.arxml --strict

# Verbose output for debugging
armodel format input.arxml -o output.arxml -v

# Quiet mode (suppress output)
armodel format input.arxml -o output.arxml -q
```

**CLI Exit Codes**:
- 0: Success
- 1: Input file not found
- 2: ARXML parsing error
- 3: File write error
- 4: Unhandled exception

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

### After Modifying Generator

When you modify `tools/generate_models/` or the mapping JSON files, regenerate all classes:

```bash
python -m tools.generate_models --members
```

**Remember**: Never manually edit generated files in `src/armodel/models/M2/` (except those in `tools/skip_classes.yaml`). Always fix the generator and regenerate.

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
├── core/                # Core utilities (SchemaVersionManager, GlobalSettingsManager)
├── models/M2/           # Generated AUTOSAR classes (~2,200 files)
│   ├── AUTOSARTemplates/  # AUTOSAR template classes
│   └── MSR/              # MSR documentation classes
├── reader/              # ARXML reading (ARXMLReader class)
├── writer/              # ARXML writing (ARXMLWriter class)
├── serialization/       # Serialization framework (decorators, name_converter)
├── cli/                 # CLI (armodel format command)
└── utils/               # Utilities (not yet implemented)

tests/
├── unit/                # Unit tests (mirrors src structure)
├── integration/         # Integration tests (read, write, cycles)
└── fixtures/arxml/      # Test ARXML files

tools/
├── generate_models/     # Code generator package (run with `python -m tools.generate_models`)
├── skip_classes.yaml    # Classes to skip during generation
└── generate_*.py        # Utility scripts

demos/
├── xsd/                 # AUTOSAR XSD schema files
└── arxml/               # Sample ARXML files

docs/
├── designs/             # Design rules and architecture
├── json/                # Type mapping metadata for generator (mapping.json, hierarchy.json)
└── requirements/        # Software requirements
```

## Design Rules

Key rules from `docs/designs/design_rules.md`:
- **Naming**: snake_case files, PascalCase classes
- **Serialization**: `serialize(namespace, element)` returns `xml.etree.ElementTree.Element`
- **Deserialization**: `@classmethod deserialize(element)` accepts XML element
- **All infrastructure classes**: Class-based with dependency injection
- **Singletons**: Used for shared state managers
- **Circular imports**: Use `from __future__ import annotations` with `TYPE_CHECKING` for type hints only
- **Imports**: All imports at file beginning, use relative imports within same package
- **Block imports**: Use multi-line block format with parentheses, define `__all__` in `__init__.py`

## Known Limitations

- Utils module not implemented
- Some complex nested structures may have incomplete `deserialize()` implementations
- Performance optimization for very large files (100MB+) could be improved
- Generator has known issues with import path resolution for certain types (e.g., TableSeparatorString, enums in OasisExchangeTable) - these should be fixed in `tools/generate_models/`, not manually in generated code

## Key Reference Documents

- **Design Rules**: `docs/designs/design_rules.md` - Complete list of design rules including naming, structure, and import patterns
- **Serialization**: `docs/designs/serialization.md` - Reflection-based serialization framework documentation
- **Skip Classes**: `tools/skip_classes.yaml` - List of manually maintained classes excluded from code generation
- **Generator README**: `tools/generate_models/README.md` - Code generator usage and options
