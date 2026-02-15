# py-armodel2

Python library for working with AUTOSAR (Automotive Open System Architecture) ARXML models.

## Current Status

🚧 **Early Development** - This library is under active development. Only basic infrastructure is in place.

## Installation

```bash
# Install in development mode
pip install -e ".[dev]"
```

## Project Structure

```
py-armodel2/
├── src/armodel/           # Source code
│   ├── cfg/              # Configuration files
│   │   └── schemas/     # Schema version configs
│   ├── core/          # Core utilities (version detection, validation)
│   ├── models/        # Generated AUTOSAR model classes
│   ├── reader/        # ARXML reading
│   ├── writer/        # ARXML writing
│   ├── cli/           # Command-line interface
│   └── utils/         # Helper utilities
├── tests/              # Test suite
│   ├── unit/          # Unit tests (mirrors src structure)
│   ├── integration/     # Integration tests
│   └── fixtures/       # Test data
├── tools/              # Code generation tools
├── demos/              # AUTOSAR schema and sample files
└── docs/               # Documentation
```

## Development

```bash
# Install in development mode
pip install -e ".[dev]"

# Run tests
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest

# Run with coverage
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest --cov=armodel --cov-report=html

# Run linter
ruff check src/

# Format code
ruff format src/

# Type checking
mypy src/
```

## Architecture

### Model Generation

All AUTOSAR model classes are generated from `docs/requirements/mapping.json` using the code generator in `tools/generate_models.py`.

- **1,937 type definitions** in mapping.json
- Generated classes placed in `src/armodel/models/` following package paths
- Each class includes serialize/deserialize methods
- Builder classes for easy object creation

### Reader/Writer Modules

- **Reader**: Loads ARXML files, creates Python objects using deserialize methods
- **Writer**: Serializes Python objects to ARXML using serialize methods

### Schema Version Support

Multiple AUTOSAR schema versions supported via `cfg/schemas/config.yaml`:

- **00044** (Classic Platform 4.3.1, 2017)
- **00046** (CP 4.4.0 / AP 18-10, 2018) - Default
- **00052** (CP/AP 23-11, 2023)

## License

MIT
