# py-armodel2

Python library for working with AUTOSAR ARXML models.

## Installation

```bash
pip install armodel
```

## Usage

```python
from armodel.reader import load_arxml

model = load_arxml("example.arxml")
```

## Development

```bash
# Install in development mode
pip install -e ".[dev]"

# Run tests
pytest

# Run linter
ruff check src/

# Type checking
mypy src/
```
