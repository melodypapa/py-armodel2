# generate_models

AUTOSAR model code generator for the py-armodel2 project.

This package generates Python model classes, enums, and primitives from AUTOSAR JSON schema definitions.

## Overview

The generator reads JSON schema files and produces Python code with:
- **Classes**: AUTOSAR model classes with type hints, serialization/deserialization support
- **Enums**: Enumeration types inheriting from `EnumerationType`
- **Primitives**: Primitive types inheriting from `PrimitiveType`

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
├── type_utils.py     # Type-related utilities
└── utils.py          # Directory structure utilities
```

## Usage

### Command Line

```bash
# From the tools directory
cd tools
python -m generate_models <mapping.json> <hierarchy.json> <output_dir> [options]

# Example
python -m generate_models ../docs/json/mapping.json ../docs/json/hierarchy.json ../src/armodel/models/ --members
```

### Arguments

| Argument | Description |
|----------|-------------|
| `mapping_file` | Path to mapping.json file (required) |
| `hierarchy_file` | Path to hierarchy.json file (required) |
| `output_dir` | Output directory for generated files (required) |

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

### Abstract Classes

Abstract classes inherit from `ABC` and have an abstract `is_abstract()` method:

```python
from abc import ABC, abstractmethod

class AbstractClass(ARObject, ABC):
    @abstractmethod
    def is_abstract(self) -> bool:
        return True
```

### Concrete Classes

Concrete classes have a non-abstract `is_abstract()` method:

```python
class ConcreteClass(ARObject):
    def is_abstract(self) -> bool:
        return False
```

### Builder Pattern

Each class has a corresponding builder:

```python
obj = (ClassNameBuilder()
       .with_attribute(value)
       .with_another_attribute(value)
       .build())
```

## Module Reference

### `generate_all_models()`

Main entry point for code generation.

### `parsers` Module

- `parse_mapping_json()` - Parse mapping.json file
- `parse_hierarchy_json()` - Parse hierarchy.json for class relationships
- `parse_enum_json()` - Parse enum JSON files
- `parse_primitive_json()` - Parse primitive JSON files
- `load_skip_list()` - Load skip_classes.yaml configuration
- `load_all_package_data()` - Load all package JSON files

### `generators` Module

- `generate_class_code()` - Generate Python class code
- `generate_builder_code()` - Generate builder class code
- `generate_enum_code()` - Generate enum code
- `generate_primitive_code()` - Generate primitive type code
- `generate_primitive_type_base()` - Generate PrimitiveType base class
- `generate_enumeration_type_base()` - Generate EnumerationType base class

### `type_utils` Module

- `is_primitive_type()` - Check if type is primitive
- `is_enum_type()` - Check if type is enum
- `get_python_type()` - Get Python type annotation for AUTOSAR type
- `get_type_import_path()` - Get import path for a class
- `build_complete_dependency_graph()` - Build dependency graph for circular import detection
- `detect_circular_import()` - Detect circular import dependencies

### `utils` Module

- `create_directory_structure()` - Create output directory structure
- `to_snake_case()` - Convert CamelCase to snake_case
- `get_python_identifier()` - Convert name to valid Python identifier

## Dependencies

- Python 3.9+
- PyYAML (optional, for skip_classes.yaml support)
