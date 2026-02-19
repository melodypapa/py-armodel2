# generate_models

AUTOSAR model code generator for the py-armodel2 project.

This package generates Python model classes, enums, and primitives from AUTOSAR JSON schema definitions.

## Overview

The generator reads JSON schema files and produces Python code with:
- **Classes**: AUTOSAR model classes with type hints, serialization/deserialization support
- **Enums**: Enumeration types inheriting from `AREnum`
- **Primitives**: Primitive types inheriting from `ARPrimitive`

Generated classes support:
- Reflection-based XML serialization via `ARObject.serialize()`
- XML deserialization via `ARObject.deserialize()`
- Builder pattern for object construction
- Circular import detection and handling with `TYPE_CHECKING`

## Package Structure

```
generate_models/
├── __init__.py       # Public API exports
├── __main__.py       # Module entry point (python -m generate_models)
├── _common.py        # Base utilities (no dependencies)
├── generators.py     # Code generation functions
├── main.py           # CLI entry point
├── parsers.py        # JSON/YAML parsing functions
├── type_utils.py     # Type-related utilities and circular import detection
└── utils.py          # Directory structure utilities
```

## Usage

### Command Line

```bash
# From the tools directory
python -m tools.generate_models [options]

# Example with defaults (uses default paths: docs/json/mapping.json, docs/json/hierarchy.json, src/armodel/models/M2)
python -m tools.generate_models --members

# Example with custom paths
python -m tools.generate_models --mapping-file custom/mapping.json --hierarchy-file custom/hierarchy.json --output-dir custom/output --members

# From project root (running from tools directory)
python generate_models --members
```

### Arguments

| Argument | Default | Description |
|----------|---------|-------------|
| `--mapping-file` | `docs/json/mapping.json` | Path to mapping.json file |
| `--hierarchy-file` | `docs/json/hierarchy.json` | Path to hierarchy.json file |
| `--output-dir` | `src/armodel/models/M2` | Output directory for generated files |

### Options

| Option | Default | Description |
|--------|---------|-------------|
| `--classes` | True | Generate class files |
| `--no-classes` | - | Skip class file generation |
| `--enums` | True | Generate enum files |
| `--no-enums` | - | Skip enum file generation |
| `--primitives` | True | Generate primitive files |
| `--no-primitives` | - | Skip primitive file generation |
| `--members` | False | Include member lists from package definitions |
| `--no-members` | - | Skip member list generation |
| `--skip-list` | tools/skip_classes.yaml | Path to skip_classes.yaml file |

### Programmatic Usage

```python
from generate_models import generate_all_models
from pathlib import Path

generate_all_models(
    mapping_file=Path("docs/json/mapping.json"),
    hierarchy_file=Path("docs/json/hierarchy.json"),
    output_dir=Path("src/armodel/models/M2"),
    generate_classes=True,
    generate_enums=True,
    generate_primitives=True,
    include_members=True,
)
```

## Input Files

### mapping.json

Contains type definitions with package paths:

```json
{
  "types": [
    {
      "name": "ARPackage",
      "type": "Class",
      "package_path": "M2::AUTOSARTemplates::GenericStructure::AbstractStructure"
    }
  ]
}
```

### hierarchy.json

Contains class hierarchy with parent relationships and abstract markers:

```
## Class Hierarchy
ARObject
    ARPackage
    Identifiable (abstract)
        Referrable
```

### packages/*.json

Package-specific JSON files with detailed class definitions:

- `*.classes.json` - Class attributes and inheritance
- `*.enums.json` - Enumeration literals
- `*.primitives.json` - Primitive type definitions

### skip_classes.yaml

YAML file specifying classes to skip during generation:

```yaml
skip_classes:
  - ARObject      # Manually maintained
  - AUTOSAR       # Manually maintained
  - BaseType      # Manually maintained

force_type_checking_imports:
  ClassName:       # Force TYPE_CHECKING for specific imports
    - CircularDependencyClass
  OtherClass: "*"  # Force TYPE_CHECKING for all imports
```

## Generated Code Features

### Reflection-Based Serialization

All generated classes inherit from `ARObject` and support:
- **Automatic serialization** via `serialize()` method
- **XML deserialization** via `deserialize()` classmethod
- **Automatic attribute discovery** using Python's `vars()` and `get_type_hints()`
- **Name conversion** via `NameConverter` (snake_case ↔ UPPER-CASE-WITH-HYPHENS)

### Abstract Classes

Abstract classes inherit from `ABC` and have an `is_abstract` property:

```python
from abc import ABC, abstractmethod

class AbstractClass(ARObject, ABC):
    @property
    def is_abstract(self) -> bool:
        return True
```

### Concrete Classes

Concrete classes have a non-abstract `is_abstract` property:

```python
class ConcreteClass(ARObject):
    @property
    def is_abstract(self) -> bool:
        return False
```

### Type Hints and Multiplicity

| AUTOSAR Multiplicity | Python Type | Initial Value |
|---------------------|-------------|---------------|
| `0..1` | `Optional[Type]` | `None` |
| `1` | `Type` | `None` |
| `*` | `list[Type]` | `[]` |

### Circular Import Handling

The generator automatically detects circular imports and places them in `TYPE_CHECKING` blocks:

```python
if TYPE_CHECKING:
    from armodel.models.M2.SomePackage.some_class import (
        SomeClass,
    )
```

This is controlled by:
- `force_type_checking_imports` in `skip_classes.yaml` for manual control
- Automatic dependency graph analysis for detection

### Builder Pattern

Each class has a corresponding builder for fluent construction:

```python
obj = (ClassNameBuilder()
       .with_attribute(value)
       .with_another_attribute(value)
       .build())
```

### Documentation

Generated classes include:
- **PDF references** - Links to source PDF documentation (when available)
- **JSON source** - Path to the JSON file containing the definition
- **Type hints** - Full type annotations for all attributes

## Module Reference

### `generate_all_models()`

Main entry point for code generation. Generates all model classes, enums, and primitives from JSON definitions with support for:

- Class generation with circular import handling
- Enum generation inheriting from `AREnum`
- Primitive type generation inheriting from `ARPrimitive`
- Member list inclusion from package definitions
- Skip list support via `skip_classes.yaml`

### `parsers` Module

**JSON Parsing:**
- `parse_mapping_json()` - Parse mapping.json file for type definitions
- `parse_hierarchy_json()` - Parse hierarchy.json for class relationships and abstract markers
- `parse_enum_json()` - Parse enum JSON files for enumeration literals
- `parse_primitive_json()` - Parse primitive JSON files for type definitions

**Configuration:**
- `load_skip_list()` - Load skip_classes.yaml with classes to skip and force TYPE_CHECKING imports

**Data Loading:**
- `load_all_package_data()` - Load all package JSON files (*.classes.json, *.enums.json, *.primitives.json)

### `generators` Module

**Code Generation:**
- `generate_class_code()` - Generate Python class code with full support for:
  - Abstract and concrete classes
  - Type hints with Optional, list, and Any types
  - Circular import detection via TYPE_CHECKING blocks
  - PDF source references in docstrings
  - JSON file path documentation
- `generate_builder_code()` - Generate builder class for fluent object construction
- `generate_enum_code()` - Generate enum code with literals
- `generate_primitive_code()` - Generate primitive type code

### `type_utils` Module

**Type Checking:**
- `is_primitive_type()` - Check if type is defined in primitives JSON files
- `is_enum_type()` - Check if type is defined in enums JSON files

**Type Conversion:**
- `get_python_type()` - Convert AUTOSAR type to Python type annotation:
  - Handles multiplicity (0..1 → Optional, * → list, 1 → direct)
  - Supports primitive types, class types, and Any for polymorphic types
- `get_type_import_path()` - Generate block import statement for class types
- `get_type_package_path()` - Get package path string for a class

**Circular Import Detection:**
- `build_complete_dependency_graph()` - Build complete dependency graph across all classes
- `detect_circular_import()` - Detect circular import dependencies using depth-first search

### `utils` Module

- `create_directory_structure()` - Create output directory structure from type definitions
- `to_snake_case()` - Convert CamelCase to snake_case for filenames

### `_common` Module

- `get_python_identifier()` - Convert AUTOSAR names to valid Python identifiers (handles keywords)

## Dependencies

- Python 3.9+
- PyYAML (optional, for skip_classes.yaml support)