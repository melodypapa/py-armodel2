# py-armodel2

Python library for processing AUTOSAR (Automotive Open System Architecture) ARXML models.

## Features

- **Reflection-based serialization** - Zero boilerplate, uses Python's `vars()` and `get_type_hints()`
- **Code generation** - 2,200+ model classes auto-generated from AUTOSAR schema mappings
- **Multi-version support** - Handles AUTOSAR 00044, 00046, and 00052 schemas
- **Type-safe** - Strict type hints throughout with MyPy enforcement
- **CLI tool** - Command-line interface for ARXML formatting and processing

## Installation

```bash
# Install in development mode
pip install -e ".[dev]"
```

## Quick Start

### Python API

```python
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.autosar import AUTOSAR
from armodel.reader import ARXMLReader
from armodel.writer import ARXMLWriter

# Load ARXML files
autosar = AUTOSAR()
reader = ARXMLReader()
reader.load_arxml(autosar, "input.arxml")

# Process the model
print(f"Total packages: {len(autosar.ar_packages)}")

# Save to file
writer = ARXMLWriter(pretty_print=True)
writer.save_arxml(autosar, "output.arxml")
```

### CLI Tool

```bash
# Format ARXML files
armodel format input.arxml -o output.arxml

# Strict validation mode
armodel format input.arxml -o output.arxml --strict

# Verbose output for debugging
armodel format input.arxml -o output.arxml -v
```

## Project Structure

```
py-armodel2/
├── src/armodel/           # Source code
│   ├── cfg/              # Configuration files
│   ├── core/             # Core utilities (version detection, validation)
│   ├── models/           # Generated AUTOSAR model classes (2,200+)
│   ├── reader/           # ARXML reading
│   ├── writer/           # ARXML writing
│   ├── serialization/    # Reflection-based serialization framework
│   ├── cli/              # Command-line interface
│   └── utils/            # Helper utilities
├── tests/                # Test suite
│   ├── unit/             # Unit tests (mirrors src structure)
│   ├── integration/      # Integration tests
│   └── fixtures/         # Test data
├── tools/                # Code generation tools
├── demos/                # AUTOSAR schema and sample files
└── docs/                 # Documentation
```

## Development

```bash
# Install in development mode
pip install -e ".[dev]"

# Run tests
PYTHONPATH=src python -m pytest

# Run with coverage
PYTHONPATH=src python -m pytest --cov=src --cov-report=html

# Run linter
ruff check src/ tools/

# Format code
ruff format src/ tools/

# Type checking
mypy src/

# Regenerate model classes
python -m tools.generate_models docs/json/mapping.json docs/json/hierarchy.json src/armodel/models/M2 --members --classes --enums --primitives
```

## Architecture

### Reflection-Based Serialization

The project uses a reflection-based serialization framework that eliminates boilerplate code:

- **ARObject** - Base class with `serialize()` and `deserialize()` methods
- **NameConverter** - Handles snake_case ↔ UPPER-CASE-WITH-HYPHENS conversion
- **ModelFactory** - Factory for creating model instances from XML tags

```python
class ARObject:
    def serialize(self, namespace: str = "") -> ET.Element:
        """Serialize object to XML using reflection."""
        # Uses vars() to discover all attributes
        # Converts names via NameConverter
    
    @classmethod
    def deserialize(cls, element: ET.Element) -> Self:
        """Deserialize XML to Python object."""
        # Uses get_type_hints() for type information
        # Recursively deserializes child objects
```

### Model Generation

All AUTOSAR model classes are generated from schema mappings:

- Generated classes placed in `src/armodel/models/M2/`
- Each class includes `serialize()`, `deserialize()`, and Builder
- Follows AUTOSAR package structure exactly
- **Exception**: `AUTOSAR` and `ARObject` are manually maintained

### Schema Version Support

| Version | Platform | Year |
|---------|----------|------|
| 00044 | Classic Platform 4.3.1 | 2017 |
| 00046 | CP 4.4.0 / AP 18-10 | 2018 (default) |
| 00052 | CP/AP 23-11 | 2023 |

## CLI Reference

### `armodel format` - Format ARXML Files

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

| Code | Description |
|------|-------------|
| 0 | Success |
| 1 | Input file not found |
| 2 | ARXML parsing error |
| 3 | File write error |
| 4 | Unhandled exception |

## Python Version Support

- **Minimum**: Python 3.9
- **Tested**: 3.9, 3.10, 3.11

## Dependencies

### Core
- `lxml>=4.9.0` - XML parsing
- `pyyaml>=6.0` - Configuration loading

### Development
- `pytest>=7.0` - Testing framework
- `pytest-cov>=4.0` - Code coverage
- `mypy>=1.0` - Type checking
- `ruff>=0.1.0` - Linting and formatting

## Documentation

- [Serialization Framework](docs/designs/serialization.md)
- [Design Rules](docs/designs/design_rules.md)
- [Model Design](docs/designs/model_design.md)
- [API Example](examples/new_api_example.py)

## License

MIT