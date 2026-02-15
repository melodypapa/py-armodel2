# py-armodel2 Design Document

**Date:** 2026-02-15
**Status:** Draft
**Author:** Claude Code Brainstorming Session

## Overview

py-armodel2 is a Python library for working with AUTOSAR (Automotive Open System Architecture) ARXML models. The library provides:

- **Read and write** ARXML files
- **Analysis and reporting** capabilities
- **Multi-version support** (AUTOSAR 00044, 00046, 00052)
- **Optional validation** against XSD schemas
- **Static Python object model** generated from AUTOSAR type definitions

## Project Goals

- **Primary use case:** Analysis and reporting of AUTOSAR models
- **API style:** Full AUTOSAR object model based on `mapping.json` (1,937 types)
- **Performance:** Fast parsing with optional validation
- **Developer experience:** Static Python classes with IDE autocomplete support

## Architecture

### Project Structure

```
py-armodel2/
├── src/
│   └── armodel/
│       ├── __init__.py
│       ├── core/
│       │   ├── __init__.py
│       │   ├── base.py              # BaseAutosarObject, ModelElement
│       │   ├── version.py           # Schema version detection
│       │   └── validation.py        # Optional XSD validation
│       ├── reader/                   # ARXML reading (independent)
│       │   ├── __init__.py
│       │   ├── parser.py            # lxml-based parsing logic
│       │   ├── loader.py            # File loading and preprocessing
│       │   └── mapper.py            # XML → Python object mapping
│       ├── writer/                   # ARXML writing (independent)
│       │   ├── __init__.py
│       │   ├── serializer.py        # Python object → XML
│       │   ├── formatter.py         # XML formatting/pretty-print
│       │   └── saver.py             # File writing
│       ├── cli/
│       │   ├── __init__.py
│       │   ├── main.py              # CLI entry point
│       │   └── commands/            # Individual command files (TBD)
│       │       ├── __init__.py
│       │       └── ...
│       ├── models/                   # Generated from mapping.json
│       │   ├── __init__.py
│       │   ├── M2/
│       │   │   ├── __init__.py
│       │   │   └── AUTOSARTemplates/
│       │   │       ├── __init__.py
│       │   │       ├── AbstractPlatform/
│       │   │       ├── AdaptivePlatform/
│       │   │       └── ...
│       ├── schemas/                  # XSD schema references
│       └── utils/                    # Helpers for analysis/reporting
├── tools/
│   └── generate_models.py           # Code generator from mapping.json
├── tests/
│   ├── unit/                         # Unit tests (mirror src structure)
│   │   ├── test_core/
│   │   ├── test_reader/
│   │   ├── test_writer/
│   │   ├── test_cli/
│   │   └── test_models/
│   ├── integration/                  # Integration tests
│   │   ├── test_read_write_cycle.py
│   │   ├── test_merge_split.py
│   │   └── test_schema_validation.py
│   └── fixtures/                     # Test data
│       ├── arxml/
│       └── expected/
├── pyproject.toml
└── setup.py
```

### Key Design Decisions

1. **Static Python objects** - Generated at build time, not runtime
2. **Directory structure mirrors AUTOSAR packages** - e.g., `M2::AUTOSARTemplates::AbstractPlatform` → `models/M2/AUTOSARTemplates/AbstractPlatform/`
3. **Reader and Writer as independent modules** - Clean separation of concerns
4. **CLI with flexible command structure** - Commands to be decided later
5. **Tests mirror source structure** - Easy to find tests for specific modules

## Code Generation

### Generation Pipeline

The `tools/generate_models.py` script generates all Python classes from `docs/requirements/mapping.json`:

1. **Parse mapping.json**
   - Load 1,937 type definitions
   - Identify the base `ARObject` type
   - Build inheritance hierarchy

2. **Create directory structure**
   - Convert package paths to directory structure
   - Create all intermediate directories
   - Generate `__init__.py` files

3. **Generate Python classes**
   - One file per type
   - Classes include:
     - Pure Python attributes (no XML element references)
     - `serialize()` method for XML conversion
     - `deserialize()` class method for XML parsing
     - Builder class for easy object creation

4. **Preserve AUTOSAR inheritance**
   - Mirror AUTOSAR type hierarchy
   - Base class: `ARObject`

### Generated Class Structure

```python
from armodel.models.M2.AUTOSARTemplates.AbstractPlatform.ar_object import ARObject
from lxml import etree

class ApplicationInterface(ARObject):
    """AUTOSAR ApplicationInterface"""

    def __init__(self):
        super().__init__()
        # Pure Python attributes
        self.name: str = None
        self.category: str = None
        # ... other properties

    @classmethod
    def deserialize(cls, element: etree.Element) -> 'ApplicationInterface':
        """Create object from XML element"""
        obj = cls()
        obj.name = element.get('name')
        obj.category = element.get('category')
        # ... parse other attributes
        return obj

    def serialize(self) -> etree.Element:
        """Convert object to XML element"""
        element = etree.Element('APPLICATION-INTERFACE')
        element.set('name', self.name)
        element.set('category', self.category)
        # ... set other attributes
        return element
```

### Builder Pattern

Each generated class includes a builder for easy object creation:

```python
class ApplicationInterfaceBuilder:
    """Builder for ApplicationInterface"""

    def __init__(self):
        self._obj = ApplicationInterface()

    def set_name(self, name: str) -> 'ApplicationInterfaceBuilder':
        self._obj.name = name
        return self

    def set_category(self, category: str) -> 'ApplicationInterfaceBuilder':
        self._obj.category = category
        return self

    def add_port(self, port) -> 'ApplicationInterfaceBuilder':
        self._obj.ports.append(port)
        return self

    def build(self) -> ApplicationInterface:
        """Build and validate the object"""
        return self._obj
```

**Usage:**
```python
interface = (ApplicationInterface.builder()
    .set_name("SensorInterface")
    .set_category("SENDER_RECEIVER")
    .build())
```

### Build Integration

- Run during `python -m build`
- Skip if models/ is up-to-date (timestamp check)
- Optional pre-commit hook for development

## AUTOSAR Document Model

### AUTOSAR Class (Singleton Root)

The `AUTOSAR` class represents the entire ARXML document as a singleton:

```python
class AUTOSAR(ARObject):
    """AUTOSAR root element - represents the entire document"""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if hasattr(self, '_initialized'):
            return
        super().__init__()
        self._initialized = True
        # Splitable elements (top-level children)
        self.ar_packages: list = []
        # ... other splitable elements

    def get_splitable_elements(self) -> list:
        """Get all splitable child elements"""
        splitable = []
        for elem in self.ar_packages:
            if elem.is_splitable:
                splitable.append(elem)
        return splitable
```

### Splitable Elements

**Splitable element metadata in mapping.json:**

```json
{
  "name": "ARPackage",
  "type": "Class",
  "package_path": "M2::AUTOSARTemplates::...",
  "splitable": true,
  "split_file_name": "ar_package_{short_name}.arxml"
}
```

**Generated class includes:**

```python
class ARPackage(ARObject):
    """Splitable AUTOSAR element"""

    is_splitable = True
    split_file_name = "ar_package_{short_name}.arxml"

    def get_split_filename(self) -> str:
        """Get the ARXML filename for this splitable element"""
        return self.split_file_name.format(short_name=self.short_name)
```

## Reader/Writer Architecture

### Reader Module

**Components:**
- `loader.py` - File loading, encoding detection, XML parsing
- `parser.py` - Schema version detection, XML preprocessing
- `mapper.py` - Traverses XML tree, calls `deserialize()` methods

**Key functions:**
```python
def load_arxml(filename: str, validate: bool = False) -> AUTOSAR:
    """Load single ARXML file"""

def merge_arxml_files(filenames: list[str]) -> AUTOSAR:
    """Merge multiple ARXML files into one AUTOSAR document

    Each file contains: AUTOSAR root + one splitable child element
    Result: AUTOSAR root with all splitable children combined
    """
```

**Usage:**
```python
from armodel.reader import load_arxml, merge_arxml_files

# Load single file
model = load_arxml("file.arxml", validate=False)

# Merge multiple files
autosar = merge_arxml_files([
    "interfaces.arxml",
    "components.arxml",
    "datatypes.arxml"
])
```

### Writer Module

**Components:**
- `serializer.py` - Traverses object tree, calls `serialize()` methods
- `formatter.py` - XML formatting, indentation, namespace handling
- `saver.py` - File writing, encoding, pretty-print options

**Key functions:**
```python
def save_arxml(autosar: AUTOSAR, filename: str, pretty_print: bool = True):
    """Save AUTOSAR document to ARXML file"""

def split_arxml(autosar: AUTOSAR, output_dir: str):
    """Split AUTOSAR document into multiple ARXML files

    Each file contains:
    - Parent: AUTOSAR root (regenerated)
    - Children: Only one splitable element
    """
```

**Usage:**
```python
from armodel.writer import save_arxml, split_arxml

# Save complete document
save_arxml(autosar, "output.arxml", pretty_print=True)

# Split into multiple files
split_arxml(autosar, "output/")
# Creates based on element.split_file_name:
#   - output/ar_package_Interfaces.arxml
#   - output/ar_package_Components.arxml
```

## Validation Strategy

**Optional validation** - user controlled via flags:

```python
# core/version.py
def detect_schema_version(arxml_file: str) -> str:
    """Detect AUTOSAR schema version from ARXML file namespace"""

# core/validation.py
def validate_against_schema(arxml_file: str, schema_version: str = None):
    """Validate ARXML file against XSD schema"""
```

**Usage:**
```python
# Fast loading without validation
model = load_arxml("file.arxml", validate=False)

# Safe loading with validation
model = load_arxml("file.arxml", validate=True)
```

## Testing Strategy

### Unit Tests

Mirror src structure:
```
tests/unit/
├── test_core/         # Base classes, version detection, validation
├── test_reader/       # Parsing, loading, mapping
├── test_writer/       # Serialization, formatting, saving
├── test_cli/          # Command-line interface
└── test_models/       # Generated model classes
```

### Integration Tests

```
tests/integration/
├── test_read_write_cycle.py    # Read ARXML → Write → Verify matches
├── test_merge_split.py         # Merge files → Split → Verify
├── test_schema_validation.py   # Validate against XSD
└── test_version_compat.py      # Cross-version compatibility
```

### Fixtures

```
tests/fixtures/
├── arxml/                      # Sample ARXML files
│   ├── AUTOSAR_00044_sample.arxml
│   ├── AUTOSAR_00046_sample.arxml
│   └── AUTOSAR_00052_sample.arxml
└── expected/                   # Expected outputs
```

## Dependencies

**Runtime:**
- `lxml>=4.9.0` - XML parsing and serialization
- Python >= 3.8

**Development:**
- `pytest>=7.0` - Testing framework
- `pytest-cov` - Coverage reporting
- `mypy` - Static type checking
- `ruff` - Fast Python linter

## CLI

CLI structure with flexible command organization (commands to be decided):

```
cli/
├── main.py              # CLI entry point
└── commands/            # Individual command files (TBD)
```

**Entry point:** `armodel` command (configured in pyproject.toml)

## Open Questions / Risks

1. **Split logic placement** - Should be in reader/writer, not in model classes (current design)
2. **Mapping.json completeness** - Assumes 1,937 types cover all needed AUTOSAR elements
3. **Builder generation complexity** - Need to determine which methods to generate for each builder
4. **Cross-file references** - Merge/split must preserve references correctly
5. **Performance** - Large ARXML files may need lazy loading or streaming

## Next Steps

1. Review and approve this design
2. Create detailed implementation plan using writing-plans skill
3. Implement in phases:
   - Phase 1: Code generator + base classes
   - Phase 2: Reader module
   - Phase 3: Writer module
   - Phase 4: Testing
   - Phase 5: CLI (commands TBD)
