# py-armodel2 Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build a Python library for reading, writing, and analyzing AUTOSAR ARXML files with static Python objects generated from AUTOSAR type definitions.

**Architecture:** Static Python classes generated at build time from `mapping.json`, with independent reader/writer modules for ARXML parsing and serialization. Supports multiple AUTOSAR schema versions (00044, 00046, 00052) with optional validation.

**Tech Stack:** Python 3.8+, lxml for XML parsing, pytest for testing, mypy for type checking

---

## Phase 1: Project Setup and Base Infrastructure

### Task 1: Create project structure

**Files:**
- Create: `src/armodel/__init__.py`
- Create: `src/armodel/core/__init__.py`
- Create: `src/armodel/reader/__init__.py`
- Create: `src/armodel/writer/__init__.py`
- Create: `src/armodel/cli/__init__.py`
- Create: `src/armodel/models/__init__.py`
- Create: `cfg/schemas/__init__.py`
- Create: `src/armodel/utils/__init__.py`
- Create: `tests/__init__.py`
- Create: `tests/unit/__init__.py`
- Create: `tests/integration/__init__.py`
- Create: `tests/fixtures/__init__.py`
- Create: `tools/__init__.py`

**Step 1: Create all package directories and __init__.py files**

Run:
```bash
mkdir -p src/armodel/{core,reader,writer,cli,models,utils} cfg/schemas
mkdir -p tests/{unit,integration,fixtures}
touch src/armodel/{__init__.py,core/__init__.py,reader/__init__.py,writer/__init__.py,cli/__init__.py,models/__init__.py,utils/__init__.py}
touch tests/{__init__.py,unit/__init__.py,integration/__init__.py,fixtures/__init__.py}
touch tools/__init__.py
```

**Step 2: Create pyproject.toml**

Create: `pyproject.toml`
```toml
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "armodel"
version = "0.1.0"
description = "Python library for AUTOSAR ARXML models"
readme = "README.md"
requires-python = ">=3.8"
license = {text = "MIT"}
authors = [
    {name = "Your Name", email = "your.email@example.com"}
]
classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
]
dependencies = [
    "lxml>=4.9.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0",
    "pytest-cov>=4.0",
    "mypy>=1.0",
    "ruff>=0.1.0",
]

[project.scripts]
armodel = "armodel.cli.main:main"

[tool.setuptools.packages.find]
where = ["src"]

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]

[tool.mypy]
python_version = "3.8"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = false

[tool.ruff]
line-length = 100
target-version = "py38"
```

**Step 3: Create README.md**

Create: `README.md`
```markdown
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
```

**Step 4: Commit**

Run:
```bash
git add .
git commit -m "feat: create project structure and build configuration
- Add pyproject.toml with dependencies and tooling
- Create package directories with __init__.py files
- Add README.md with basic usage"
```

---

### Task 2: Create base ARObject class

**Files:**
- Create: `src/armodel/core/base.py`
- Create: `tests/unit/test_core/test_base.py`

**Step 1: Write failing test for base class**

Create: `tests/unit/test_core/test_base.py`
```python
import pytest

def test_ar_object_creation():
    """Test that ARObject can be instantiated"""
    from armodel.core.base import ARObject

    obj = ARObject()
    assert obj is not None

def test_ar_object_serialization_not_implemented():
    """Test that serialize raises NotImplementedError by default"""
    from armodel.core.base import ARObject

    obj = ARObject()
    with pytest.raises(NotImplementedError):
        obj.serialize()
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/unit/test_core/test_base.py -v`
Expected: FAIL with "cannot import 'ARObject'"

**Step 3: Write minimal implementation**

Create: `src/armodel/core/base.py`
```python
"""Base AUTOSAR object classes."""

from typing import Any
from lxml import etree


class ARObject:
    """Base class for all AUTOSAR objects.

    All generated AUTOSAR classes inherit from this base class.
    """

    def __init__(self):
        """Initialize ARObject."""
        self._attributes: dict[str, Any] = {}

    def serialize(self) -> etree.Element:
        """Convert object to XML element.

        Raises:
            NotImplementedError: Subclasses must implement this method
        """
        raise NotImplementedError(
            f"{self.__class__.__name__} must implement serialize() method"
        )

    @classmethod
    def deserialize(cls, element: etree.Element) -> "ARObject":
        """Create object from XML element.

        Args:
            element: XML element to deserialize from

        Raises:
            NotImplementedError: Subclasses must implement this method
        """
        raise NotImplementedError(
            f"{cls.__name__} must implement deserialize() classmethod"
        )
```

Update: `src/armodel/core/__init__.py`
```python
from armodel.core.base import ARObject

__all__ = ["ARObject"]
```

**Step 4: Run test to verify it passes**

Run: `pytest tests/unit/test_core/test_base.py -v`
Expected: PASS

**Step 5: Commit**

Run:
```bash
git add src/armodel/core/base.py tests/unit/test_core/test_base.py
git commit -m "feat: add ARObject base class
- Add ARObject with serialize/deserialize stub methods
- Raise NotImplementedError for methods to be implemented by subclasses
- Add unit tests for base class functionality"
```

---

### Task 3: Create AUTOSAR singleton class

**Files:**
- Create: `src/armodel/models/M2/AUTOSARTemplates/autosar.py`
- Create: `tests/unit/test_models/test_autosar.py`

**Step 1: Create directory structure**

Run:
```bash
mkdir -p src/armodel/models/M2/AUTOSARTemplates
touch src/armodel/models/M2/__init__.py
touch src/armodel/models/M2/AUTOSARTemplates/__init__.py
```

**Step 2: Write failing test for AUTOSAR singleton**

Create: `tests/unit/test_models/test_autosar.py`
```python
import pytest

def test_autosar_singleton():
    """Test that AUTOSAR is a singleton"""
    from armodel.models.M2.AUTOSARTemplates.autosar import AUTOSAR

    obj1 = AUTOSAR()
    obj2 = AUTOSAR()
    assert obj1 is obj2

def test_autosar_get_splitable_elements():
    """Test getting splitable elements"""
    from armodel.models.M2.AUTOSARTemplates.autosar import AUTOSAR

    autosar = AUTOSAR()
    splitable = autosar.get_splitable_elements()
    assert isinstance(splitable, list)
```

**Step 3: Run test to verify it fails**

Run: `pytest tests/unit/test_models/test_autosar.py -v`
Expected: FAIL with "cannot import AUTOSAR"

**Step 4: Write minimal implementation**

Create: `src/armodel/models/M2/AUTOSARTemplates/autosar.py`
```python
"""AUTOSAR root element - singleton pattern."""

from armodel.core.base import ARObject


class AUTOSAR(ARObject):
    """AUTOSAR root element representing the entire ARXML document.

    This class implements the singleton pattern - there is only one
    AUTOSAR instance per document.
    """

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        """Initialize AUTOSAR singleton."""
        if hasattr(self, "_initialized"):
            return
        super().__init__()
        self._initialized = True
        # Splitable elements (top-level children)
        self.ar_packages: list = []
        self.administrative_data: list = []

    def get_splitable_elements(self) -> list:
        """Get all splitable child elements.

        Returns:
            List of splitable elements
        """
        splitable = []
        for elem in self.ar_packages:
            if getattr(elem, "is_splitable", False):
                splitable.append(elem)
        return splitable
```

Update: `src/armodel/models/M2/AUTOSARTemplates/__init__.py`
```python
from armodel.models.M2.AUTOSARTemplates.autosar import AUTOSAR

__all__ = ["AUTOSAR"]
```

**Step 5: Run test to verify it passes**

Run: `pytest tests/unit/test_models/test_autosar.py -v`
Expected: PASS

**Step 6: Commit**

Run:
```bash
git add src/armodel/models tests/unit/test_models
git commit -m "feat: add AUTOSAR singleton class
- Implement singleton pattern for AUTOSAR root element
- Add get_splitable_elements() method
- Add unit tests for singleton behavior"
```

---

### Task 4: Add schema version detection

**Files:**
- Create: `src/armodel/core/version.py`
- Create: `tests/unit/test_core/test_version.py`

**Step 1: Write failing test for version detection**

Create: `tests/unit/test_core/test_version.py`
```python
import pytest
from lxml import etree

def test_detect_schema_version_00046():
    """Test detection of AUTOSAR 00046 schema"""
    from armodel.core.version import detect_schema_version

    xml_content = '''<?xml version="1.0" encoding="UTF-8"?>
<AUTOSAR xmlns="http://autosar.org/schema/r4.0">
  <AR-PACKAGES>
    <AR-PACKAGE>
      <SHORT-NAME>Test</SHORT-NAME>
    </AR-PACKAGE>
  </AR-PACKAGES>
</AUTOSAR>'''

    # Parse to get root
    root = etree.fromstring(xml_content.encode())
    version = detect_schema_version(root)
    assert version == "00046"

def test_detect_schema_version_unknown():
    """Test handling of unknown schema versions"""
    from armodel.core.version import detect_schema_version

    xml_content = '''<?xml version="1.0" encoding="UTF-8"?>
<ROOT xmlns="http://unknown/schema">
</ROOT>'''

    root = etree.fromstring(xml_content.encode())
    version = detect_schema_version(root)
    assert version is None
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/unit/test_core/test_version.py -v`
Expected: FAIL with "cannot import detect_schema_version"

**Step 3: Write implementation**

Create: `src/armodel/core/version.py`
```python
"""Schema version detection for ARXML files."""

from typing import Optional
from lxml import etree


# Mapping of AUTOSAR namespaces to schema versions
NAMESPACE_TO_VERSION = {
    "http://autosar.org/3.0.4": "00044",
    "http://autosar.org/3.1.4": "00044",
    "http://autosar.org/schema/r4.0": "00046",
    "http://autosar.org/r4.0": "00046",
    "http://autosar.org/schema/r5.0": "00052",
    "http://autosar.org/r5.0": "00052",
}


def detect_schema_version(root: etree.Element) -> Optional[str]:
    """Detect AUTOSAR schema version from XML element namespace.

    Args:
        root: Root XML element from ARXML file

    Returns:
        Schema version string (e.g., "00046") or None if unknown
    """
    # Get the namespace
    namespace = root.nsmap.get(None, "")

    # Map to version
    return NAMESPACE_TO_VERSION.get(namespace)
```

Update: `src/armodel/core/__init__.py`
```python
from armodel.core.base import ARObject
from armodel.core.version import detect_schema_version

__all__ = ["ARObject", "detect_schema_version"]
```

**Step 4: Run test to verify it passes**

Run: `pytest tests/unit/test_core/test_version.py -v`
Expected: PASS

**Step 5: Commit**

Run:
```bash
git add src/armodel/core/version.py tests/unit/test_core/test_version.py
git commit -m "feat: add schema version detection
- Map AUTOSAR namespaces to schema versions
- Support versions 00044, 00046, 00052
- Add unit tests for version detection"
```

---

## Phase 2: Code Generator

### Task 5: Parse mapping.json

**Files:**
- Create: `tools/generate_models.py`
- Create: `tests/test_generate_models.py`

**Step 1: Write failing test for mapping parser**

Create: `tests/test_generate_models.py`
```python
import pytest
import json
from pathlib import Path

def test_parse_mapping_json():
    """Test parsing mapping.json file"""
    from tools.generate_models import parse_mapping_json

    # Create test mapping.json
    test_data = {
        "types": [
            {
                "name": "TestClass",
                "type": "Class",
                "package_path": "M2::Test"
            }
        ]
    }

    test_file = Path("test_mapping.json")
    test_file.write_text(json.dumps(test_data))

    result = parse_mapping_json(test_file)
    assert len(result["types"]) == 1
    assert result["types"][0]["name"] == "TestClass"

    # Cleanup
    test_file.unlink()
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_generate_models.py -v`
Expected: FAIL with "cannot import parse_mapping_json"

**Step 3: Write implementation**

Create: `tools/generate_models.py`
```python
#!/usr/bin/env python3
"""Code generator for AUTOSAR model classes."""

import json
from pathlib import Path
from typing import Any, Dict


def parse_mapping_json(mapping_file: Path) -> Dict[str, Any]:
    """Parse mapping.json file.

    Args:
        mapping_file: Path to mapping.json file

    Returns:
        Parsed JSON data as dictionary
    """
    with open(mapping_file, "r", encoding="utf-8") as f:
        return json.load(f)


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: generate_models.py <mapping.json> <output_dir>")
        sys.exit(1)

    mapping_file = Path(sys.argv[1])
    output_dir = Path(sys.argv[2])

    # Parse mapping
    data = parse_mapping_json(mapping_file)
    print(f"Loaded {len(data.get('types', []))} type definitions")
```

**Step 4: Run test to verify it passes**

Run: `pytest tests/test_generate_models.py -v`
Expected: PASS

**Step 5: Commit**

Run:
```bash
git add tools/generate_models.py tests/test_generate_models.py
git commit -m "feat: add mapping.json parser
- Parse AUTOSAR type definitions from mapping.json
- Add command-line interface for code generator
- Add unit test for mapping parser"
```

---

### Task 6: Generate directory structure from package paths

**Files:**
- Modify: `tools/generate_models.py`
- Modify: `tests/test_generate_models.py`

**Step 1: Write failing test**

Update: `tests/test_generate_models.py`
```python
def test_generate_directory_structure(tmp_path):
    """Test generating directory structure from package path"""
    from tools.generate_models import create_directory_structure

    types = [
        {"name": "TestClass", "package_path": "M2::Test::SubPackage"}
    ]

    output_dir = tmp_path / "output"
    output_dir.mkdir()

    create_directory_structure(types, output_dir)

    # Check directories were created
    assert (output_dir / "M2").exists()
    assert (output_dir / "M2" / "Test").exists()
    assert (output_dir / "M2" / "Test" / "SubPackage").exists()
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_generate_models.py::test_generate_directory_structure -v`
Expected: FAIL with "function not defined"

**Step 3: Write implementation**

Update: `tools/generate_models.py`
```python
def create_directory_structure(types: list, output_dir: Path):
    """Create directory structure from package paths.

    Args:
        types: List of type definitions with package_path
        output_dir: Base output directory
    """
    for type_def in types:
        package_path = type_def.get("package_path", "")
        if not package_path:
            continue

        # Convert package path to directory path
        dir_path = output_dir / package_path.replace("::", "/")

        # Create directory and __init__.py files
        dir_path.mkdir(parents=True, exist_ok=True)

        # Create __init__.py if it doesn't exist
        init_file = dir_path / "__init__.py"
        if not init_file.exists():
            init_file.write_text('"""AUTOSAR model classes."""\n')

    # Create __init__.py for each level
    for init_path in output_dir.rglob("__init__.py"):
        if init_path.parent != output_dir:
            # Ensure parent packages have __init__.py
            parent_init = init_path.parent.parent / "__init__.py"
            if not parent_init.exists():
                parent_init.write_text('"""AUTOSAR model package."""\n')
```

**Step 4: Run test to verify it passes**

Run: `pytest tests/test_generate_models.py::test_generate_directory_structure -v`
Expected: PASS

**Step 5: Commit**

Run:
```bash
git add tools/generate_models.py tests/test_generate_models.py
git commit -m "feat: add directory structure generation
- Create directory hierarchy from package paths
- Generate __init__.py files for all packages
- Add unit test for directory creation"
```

---

### Task 7: Generate Python class from type definition

**Files:**
- Modify: `tools/generate_models.py`
- Modify: `tests/test_generate_models.py`

**Step 1: Write failing test**

Update: `tests/test_generate_models.py`
```python
def test_generate_class_code():
    """Test generating Python class code"""
    from tools.generate_models import generate_class_code

    type_def = {
        "name": "TestInterface",
        "type": "Class",
        "package_path": "M2::Test"
    }

    code = generate_class_code(type_def)

    # Check that class is generated
    assert "class TestInterface(ARObject):" in code
    assert "def serialize(self):" in code
    assert "@classmethod" in code
    assert "def deserialize(cls, element):" in code
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_generate_models.py::test_generate_class_code -v`
Expected: FAIL with "function not defined"

**Step 3: Write implementation**

Update: `tools/generate_models.py`
```python
def generate_class_code(type_def: dict) -> str:
    """Generate Python class code from type definition.

    Args:
        type_def: Type definition from mapping.json

    Returns:
        Generated Python code as string
    """
    class_name = type_def["name"]
    package_path = type_def.get("package_path", "")
    is_splitable = type_def.get("splitable", False)
    split_file_name = type_def.get("split_file_name", "")

    # Generate class code
    code = f'''"""{class_name} AUTOSAR element."""

from armodel.core.base import ARObject
from lxml import etree
from typing import Optional


class {class_name}(ARObject):
    """AUTOSAR {class_name}."""

'''

    if is_splitable:
        code += f'''    is_splitable = True
    split_file_name = "{split_file_name}"

'''

    code += f'''    def __init__(self):
        """Initialize {class_name}."""
        super().__init__()
'''

    # Add serialize method
    code += f'''
    def serialize(self) -> etree.Element:
        """Convert {class_name} to XML element.

        Returns:
            XML element representing this object
        """
        element = etree.Element("{class_name.upper()}")
        # TODO: Add serialization logic
        return element

    @classmethod
    def deserialize(cls, element: etree.Element) -> "{class_name}":
        """Create {class_name} from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            {class_name} instance
        """
        obj = cls()
        # TODO: Add deserialization logic
        return obj
'''

    return code
```

**Step 4: Run test to verify it passes**

Run: `pytest tests/test_generate_models.py::test_generate_class_code -v`
Expected: PASS

**Step 5: Commit**

Run:
```bash
git add tools/generate_models.py tests/test_generate_models.py
git commit -m "feat: add class code generation
- Generate Python class from type definition
- Add serialize/deserialize method stubs
- Handle splitable element metadata
- Add unit test for code generation"
```

---

### Task 8: Generate builder class

**Files:**
- Modify: `tools/generate_models.py`
- Modify: `tests/test_generate_models.py`

**Step 1: Write failing test**

Update: `tests/test_generate_models.py`
```python
def test_generate_builder_code():
    """Test generating builder class code"""
    from tools.generate_models import generate_builder_code

    type_def = {
        "name": "TestInterface",
        "type": "Class",
        "package_path": "M2::Test"
    }

    code = generate_builder_code(type_def)

    # Check that builder is generated
    assert "class TestInterfaceBuilder:" in code
    assert "def set_name(self" in code
    assert "def build(self)" in code
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_generate_models.py::test_generate_builder_code -v`
Expected: FAIL with "function not defined"

**Step 3: Write implementation**

Update: `tools/generate_models.py`
```python
def generate_builder_code(type_def: dict) -> str:
    """Generate builder class code from type definition.

    Args:
        type_def: Type definition from mapping.json

    Returns:
        Generated builder code as string
    """
    class_name = type_def["name"]
    builder_name = f"{class_name}Builder"

    code = f'''class {builder_name}:
    """Builder for {class_name}."""

    def __init__(self):
        """Initialize builder."""
        self._obj = {class_name}()

    def build(self) -> {class_name}:
        """Build and return the {class_name} object.

        Returns:
            {class_name} instance
        """
        # TODO: Add validation
        return self._obj
'''

    return code
```

**Step 4: Run test to verify it passes**

Run: `pytest tests/test_generate_models.py::test_generate_builder_code -v`
Expected: PASS

**Step 5: Commit**

Run:
```bash
git add tools/generate_models.py tests/test_generate_models.py
git commit -m "feat: add builder class generation
- Generate builder class for each AUTOSAR type
- Add build() method to construct objects
- Add unit test for builder generation"
```

---

### Task 9: Integrate code generator

**Files:**
- Modify: `tools/generate_models.py`
- Modify: `tests/test_generate_models.py`

**Step 1: Write failing test for full generation**

Update: `tests/test_generate_models.py`
```python
def test_full_generation(tmp_path):
    """Test full code generation process"""
    from tools.generate_models import generate_all_models

    # Create test mapping
    test_data = {
        "types": [
            {
                "name": "TestClass",
                "type": "Class",
                "package_path": "M2::TestPackage"
            }
        ]
    }

    mapping_file = tmp_path / "mapping.json"
    mapping_file.write_text(json.dumps(test_data))

    output_dir = tmp_path / "output"

    generate_all_models(mapping_file, output_dir)

    # Check files were created
    assert (output_dir / "M2" / "TestPackage" / "test_class.py").exists()
    assert (output_dir / "M2" / "__init__.py").exists()

    # Check file content
    content = (output_dir / "M2" / "TestPackage" / "test_class.py").read_text()
    assert "class TestClass(ARObject):" in content
    assert "class TestClassBuilder:" in content
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_generate_models.py::test_full_generation -v`
Expected: FAIL with "function not defined"

**Step 3: Write implementation**

Update: `tools/generate_models.py`
```python
def generate_all_models(mapping_file: Path, output_dir: Path):
    """Generate all model classes from mapping.json.

    Args:
        mapping_file: Path to mapping.json
        output_dir: Output directory for generated files
    """
    # Parse mapping
    data = parse_mapping_json(mapping_file)
    types = data.get("types", [])

    # Create directory structure
    create_directory_structure(types, output_dir)

    # Generate each class
    for type_def in types:
        if type_def.get("type") != "Class":
            continue

        class_name = type_def["name"]
        package_path = type_def.get("package_path", "")

        # Convert package path to file path
        dir_path = output_dir / package_path.replace("::", "/")
        filename = dir_path / f"{to_snake_case(class_name)}.py"

        # Generate class code
        class_code = generate_class_code(type_def)
        builder_code = generate_builder_code(type_def)

        # Write to file
        full_code = class_code + "\n\n" + builder_code
        filename.write_text(full_code)

    print(f"Generated {len(types)} model classes in {output_dir}")


def to_snake_case(name: str) -> str:
    """Convert CamelCase to snake_case.

    Args:
        name: CamelCase string

    Returns:
        snake_case string
    """
    import re
    s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower()
```

Update: `tools/generate_models.py` main section:
```python
if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("Usage: generate_models.py <mapping.json> <output_dir>")
        sys.exit(1)

    mapping_file = Path(sys.argv[1])
    output_dir = Path(sys.argv[2])

    # Generate all models
    generate_all_models(mapping_file, output_dir)
```

**Step 4: Run test to verify it passes**

Run: `pytest tests/test_generate_models.py::test_full_generation -v`
Expected: PASS

**Step 5: Commit**

Run:
```bash
git add tools/generate_models.py tests/test_generate_models.py
git commit -m "feat: integrate full code generation
- Combine directory creation and class generation
- Generate model files with class and builder
- Add to_snake_case helper for filenames
- Add integration test for full generation"
```

---

## Phase 3: Reader Module

### Task 10: Implement ARXML file loading

**Files:**
- Create: `src/armodel/reader/loader.py`
- Create: `tests/unit/test_reader/test_loader.py`

**Step 1: Write failing test**

Create: `tests/unit/test_reader/test_loader.py`
```python
import pytest
from pathlib import Path

def test_load_arxml_file(tmp_path):
    """Test loading ARXML file"""
    from armodel.reader.loader import load_arxml_file

    # Create test ARXML file
    arxml_content = '''<?xml version="1.0" encoding="UTF-8"?>
<AUTOSAR xmlns="http://autosar.org/schema/r4.0">
  <AR-PACKAGES>
    <AR-PACKAGE>
      <SHORT-NAME>TestPackage</SHORT-NAME>
    </AR-PACKAGE>
  </AR-PACKAGES>
</AUTOSAR>'''

    test_file = tmp_path / "test.arxml"
    test_file.write_text(arxml_content)

    # Load file
    root = load_arxml_file(test_file)

    assert root is not None
    assert root.tag == "AUTOSAR"
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/unit/test_reader/test_loader.py -v`
Expected: FAIL with "cannot import load_arxml_file"

**Step 3: Write implementation**

Create: `src/armodel/reader/loader.py`
```python
"""ARXML file loading."""

from pathlib import Path
from lxml import etree
from typing import Union


def load_arxml_file(filepath: Union[str, Path]) -> etree.Element:
    """Load ARXML file and return root element.

    Args:
        filepath: Path to ARXML file

    Returns:
        Root XML element

    Raises:
        FileNotFoundError: If file doesn't exist
        etree.XMLSyntaxError: If XML is malformed
    """
    filepath = Path(filepath)

    if not filepath.exists():
        raise FileNotFoundError(f"ARXML file not found: {filepath}")

    # Parse XML file
    tree = etree.parse(str(filepath))
    return tree.getroot()
```

Update: `src/armodel/reader/__init__.py`
```python
from armodel.reader.loader import load_arxml_file

__all__ = ["load_arxml_file"]
```

**Step 4: Run test to verify it passes**

Run: `pytest tests/unit/test_reader/test_loader.py -v`
Expected: PASS

**Step 5: Commit**

Run:
```bash
git add src/armodel/reader/loader.py tests/unit/test_reader/test_loader.py
git commit -m "feat: add ARXML file loading
- Parse ARXML files using lxml
- Return root XML element
- Handle file not found errors
- Add unit tests for loader"
```

---

### Task 11: Implement XML to Python object mapping

**Files:**
- Create: `src/armodel/reader/mapper.py`
- Create: `tests/unit/test_reader/test_mapper.py`

**Step 1: Write failing test**

Create: `tests/unit/test_reader/test_mapper.py`
```python
import pytest
from lxml import etree

def test_map_xml_to_autosar():
    """Test mapping XML to AUTOSAR object"""
    from armodel.reader.mapper import map_xml_to_autosar

    xml_string = '''<?xml version="1.0" encoding="UTF-8"?>
<AUTOSAR xmlns="http://autosar.org/schema/r4.0">
  <AR-PACKAGES>
    <AR-PACKAGE>
      <SHORT-NAME>TestPackage</SHORT-NAME>
    </AR-PACKAGE>
  </AR-PACKAGES>
</AUTOSAR>'''

    root = etree.fromstring(xml_string.encode())
    autosar = map_xml_to_autosar(root)

    assert autosar is not None
    from armodel.models.M2.AUTOSARTemplates.autosar import AUTOSAR
    assert isinstance(autosar, AUTOSAR)
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/unit/test_reader/test_mapper.py -v`
Expected: FAIL with "cannot import map_xml_to_autosar"

**Step 3: Write implementation**

Create: `src/armodel/reader/mapper.py`
```python
"""XML to Python object mapping."""

from lxml import etree
from armodels.models.M2.AUTOSARTemplates.autosar import AUTOSAR


def map_xml_to_autosar(root: etree.Element) -> AUTOSAR:
    """Map XML element to AUTOSAR object.

    Args:
        root: Root XML element

    Returns:
        AUTOSAR object instance
    """
    # Get or create AUTOSAR singleton
    autosar = AUTOSAR()

    # TODO: Parse child elements and populate AUTOSAR
    # For now, just return the singleton

    return autosar
```

Update: `src/armodel/reader/__init__.py`
```python
from armodel.reader.loader import load_arxml_file
from armodel.reader.mapper import map_xml_to_autosar

__all__ = ["load_arxml_file", "map_xml_to_autosar"]
```

**Step 4: Run test to verify it passes**

Run: `pytest tests/unit/test_reader/test_mapper.py -v`
Expected: PASS

**Step 5: Commit**

Run:
```bash
git add src/armodel/reader/mapper.py tests/unit/test_reader/test_mapper.py
git commit -m "feat: add XML to object mapping
- Map XML root element to AUTOSAR singleton
- Basic mapper structure (full parsing to be added)
- Add unit tests for mapper"
```

---

### Task 12: Integrate load_arxml function

**Files:**
- Create: `src/armodel/reader/__init__.py` (modify)
- Create: `tests/integration/test_read_arxml.py`

**Step 1: Write failing test**

Create: `tests/integration/test_read_arxml.py`
```python
import pytest
from pathlib import Path

def test_load_arxml_integration(tmp_path):
    """Test full ARXML loading flow"""
    from armodel.reader import load_arxml

    # Create test ARXML file
    arxml_content = '''<?xml version="1.0" encoding="UTF-8"?>
<AUTOSAR xmlns="http://autosar.org/schema/r4.0">
  <AR-PACKAGES>
    <AR-PACKAGE>
      <SHORT-NAME>TestPackage</SHORT-NAME>
    </AR-PACKAGE>
  </AR-PACKAGES>
</AUTOSAR>'''

    test_file = tmp_path / "test.arxml"
    test_file.write_text(arxml_content)

    # Load file
    autosar = load_arxml(test_file)

    # Verify
    from armodel.models.M2.AUTOSARTemplates.autosar import AUTOSAR
    assert isinstance(autosar, AUTOSAR)
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/integration/test_read_arxml.py -v`
Expected: FAIL with "cannot import load_arxml"

**Step 3: Write implementation**

Update: `src/armodel/reader/__init__.py`
```python
"""ARXML reading functionality."""

from pathlib import Path
from typing import Union
from lxml import etree

from armodel.reader.loader import load_arxml_file
from armodel.reader.mapper import map_xml_to_autosar


def load_arxml(filepath: Union[str, Path], validate: bool = False):
    """Load ARXML file and return AUTOSAR object.

    Args:
        filepath: Path to ARXML file
        validate: Whether to validate against XSD schema (not yet implemented)

    Returns:
        AUTOSAR object representing the document

    Raises:
        FileNotFoundError: If file doesn't exist
        etree.XMLSyntaxError: If XML is malformed
    """
    # Load XML
    root = load_arxml_file(filepath)

    # Map to Python object
    autosar = map_xml_to_autosar(root)

    # TODO: Add validation if requested

    return autosar


__all__ = ["load_arxml", "load_arxml_file", "map_xml_to_autosar"]
```

**Step 4: Run test to verify it passes**

Run: `pytest tests/integration/test_read_arxml.py -v`
Expected: PASS

**Step 5: Commit**

Run:
```bash
git add src/armodel/reader/__init__.py tests/integration/test_read_arxml.py
git commit -m "feat: add high-level load_arxml function
- Combine loader and mapper for easy file loading
- Add validate parameter (for future validation)
- Add integration test for full loading flow"
```

---

## Phase 4: Writer Module

### Task 13: Implement XML serialization

**Files:**
- Create: `src/armodel/writer/serializer.py`
- Create: `tests/unit/test_writer/test_serializer.py`

**Step 1: Write failing test**

Create: `tests/unit/test_writer/test_serializer.py`
```python
import pytest
from lxml import etree

def test_serialize_autosar_to_xml():
    """Test serializing AUTOSAR object to XML"""
    from armodel.writer.serializer import serialize_autosar_to_xml
    from armodel.models.M2.AUTOSARTemplates.autosar import AUTOSAR

    autosar = AUTOSAR()

    root = serialize_autosar_to_xml(autosar)

    assert root is not None
    assert root.tag == "AUTOSAR"
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/unit/test_writer/test_serializer.py -v`
Expected: FAIL with "cannot import serialize_autosar_to_xml"

**Step 3: Write implementation**

Create: `src/armodel/writer/serializer.py`
```python
"""Python object to XML serialization."""

from lxml import etree
from armodel.models.M2.AUTOSARTemplates.autosar import AUTOSAR


def serialize_autosar_to_xml(autosar: AUTOSAR) -> etree.Element:
    """Serialize AUTOSAR object to XML element.

    Args:
        autosar: AUTOSAR object to serialize

    Returns:
        Root XML element
    """
    # Call the object's serialize method
    root = autosar.serialize()
    return root
```

Update: `src/armodel/writer/__init__.py`
```python
from armodel.writer.serializer import serialize_autosar_to_xml

__all__ = ["serialize_autosar_to_xml"]
```

**Step 4: Run test to verify it passes**

Run: `pytest tests/unit/test_writer/test_serializer.py -v`
Expected: PASS (Note: serialize() on AUTOSAR needs to be implemented first)

**Step 5: Implement AUTOSAR.serialize()**

Update: `src/armodel/models/M2/AUTOSARTemplates/autosar.py` (add to class):
```python
    def serialize(self) -> etree.Element:
        """Convert AUTOSAR to XML element.

        Returns:
            XML element representing this document
        """
        element = etree.Element("AUTOSAR")
        element.set("xmlns", "http://autosar.org/schema/r4.0")

        # TODO: Serialize child elements

        return element
```

Run: `pytest tests/unit/test_writer/test_serializer.py -v`
Expected: PASS

**Step 6: Commit**

Run:
```bash
git add src/armodel/writer/serializer.py tests/unit/test_writer/test_serializer.py
git add src/armodel/models/M2/AUTOSARTemplates/autosar.py
git commit -m "feat: add XML serialization
- Serialize AUTOSAR object to XML element
- Implement AUTOSAR.serialize() method
- Add unit tests for serializer"
```

---

### Task 14: Implement ARXML file saving

**Files:**
- Create: `src/armodel/writer/saver.py`
- Create: `tests/unit/test_writer/test_saver.py`

**Step 1: Write failing test**

Create: `tests/unit/test_writer/test_saver.py`
```python
import pytest
from pathlib import Path

def test_save_arxml_file(tmp_path):
    """Test saving AUTOSAR to ARXML file"""
    from armodel.writer.saver import save_arxml_file
    from armodel.models.M2.AUTOSARTemplates.autosar import AUTOSAR
    from lxml import etree

    autosar = AUTOSAR()
    output_file = tmp_path / "output.arxml"

    # Serialize to XML
    from armodel.writer.serializer import serialize_autosar_to_xml
    root = serialize_autosar_to_xml(autosar)

    # Save to file
    save_arxml_file(root, output_file, pretty_print=True)

    # Verify file was created and contains XML
    assert output_file.exists()
    content = output_file.read_text()
    assert "<?xml" in content
    assert "<AUTOSAR" in content
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/unit/test_writer/test_saver.py -v`
Expected: FAIL with "cannot import save_arxml_file"

**Step 3: Write implementation**

Create: `src/armodel/writer/saver.py`
```python
"""ARXML file saving."""

from pathlib import Path
from typing import Union
from lxml import etree


def save_arxml_file(
    root: etree.Element,
    filepath: Union[str, Path],
    pretty_print: bool = True,
    encoding: str = "UTF-8"
):
    """Save XML element to ARXML file.

    Args:
        root: Root XML element
        filepath: Output file path
        pretty_print: Whether to format XML with indentation
        encoding: File encoding
    """
    filepath = Path(filepath)

    # Ensure parent directory exists
    filepath.parent.mkdir(parents=True, exist_ok=True)

    # Create tree and write
    tree = etree.ElementTree(root)
    tree.write(
        str(filepath),
        pretty_print=pretty_print,
        xml_declaration=True,
        encoding=encoding
    )
```

Update: `src/armodel/writer/__init__.py`
```python
from armodel.writer.serializer import serialize_autosar_to_xml
from armodel.writer.saver import save_arxml_file

__all__ = ["serialize_autosar_to_xml", "save_arxml_file"]
```

**Step 4: Run test to verify it passes**

Run: `pytest tests/unit/test_writer/test_saver.py -v`
Expected: PASS

**Step 5: Commit**

Run:
```bash
git add src/armodel/writer/saver.py tests/unit/test_writer/test_saver.py
git commit -m "feat: add ARXML file saving
- Write XML element to ARXML file
- Support pretty printing and encoding options
- Create parent directories as needed
- Add unit tests for saver"
```

---

### Task 15: Integrate save_arxml function

**Files:**
- Modify: `src/armodel/writer/__init__.py`
- Create: `tests/integration/test_write_arxml.py`

**Step 1: Write failing test**

Create: `tests/integration/test_write_arxml.py`
```python
import pytest
from pathlib import Path

def test_save_arxml_integration(tmp_path):
    """Test full ARXML saving flow"""
    from armodel.writer import save_arxml
    from armodel.models.M2.AUTOSARTemplates.autosar import AUTOSAR

    autosar = AUTOSAR()
    output_file = tmp_path / "output.arxml"

    # Save
    save_arxml(autosar, output_file, pretty_print=True)

    # Verify
    assert output_file.exists()
    content = output_file.read_text()
    assert "<?xml" in content
    assert "<AUTOSAR" in content
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/integration/test_write_arxml.py -v`
Expected: FAIL with "cannot import save_arxml"

**Step 3: Write implementation**

Update: `src/armodel/writer/__init__.py`
```python
"""ARXML writing functionality."""

from pathlib import Path
from typing import Union
from lxml import etree

from armodel.writer.serializer import serialize_autosar_to_xml
from armodel.writer.saver import save_arxml_file


def save_arxml(
    autosar,
    filepath: Union[str, Path],
    pretty_print: bool = True
):
    """Save AUTOSAR object to ARXML file.

    Args:
        autosar: AUTOSAR object to save
        filepath: Output file path
        pretty_print: Whether to format XML with indentation
    """
    # Serialize to XML
    root = serialize_autosar_to_xml(autosar)

    # Save to file
    save_arxml_file(root, filepath, pretty_print=pretty_print)


__all__ = ["save_arxml", "serialize_autosar_to_xml", "save_arxml_file"]
```

**Step 4: Run test to verify it passes**

Run: `pytest tests/integration/test_write_arxml.py -v`
Expected: PASS

**Step 5: Commit**

Run:
```bash
git add src/armodel/writer/__init__.py tests/integration/test_write_arxml.py
git commit -m "feat: add high-level save_arxml function
- Combine serializer and saver for easy file saving
- Add pretty_print parameter
- Add integration test for full saving flow"
```

---

## Phase 5: Integration Tests and Fixtures

### Task 16: Add test fixtures

**Files:**
- Create: `tests/fixtures/arxml/AUTOSAR_00046_sample.arxml`

**Step 1: Create sample ARXML fixture**

Run:
```bash
mkdir -p tests/fixtures/arxml
```

Create: `tests/fixtures/arxml/AUTOSAR_00046_sample.arxml`
```xml
<?xml version="1.0" encoding="UTF-8"?>
<AUTOSAR xmlns="http://autosar.org/schema/r4.0">
  <AR-PACKAGES>
    <AR-PACKAGE>
      <SHORT-NAME>TestPackage</SHORT-NAME>
      <AR-PACKAGES>
        <AR-PACKAGE>
          <SHORT-NAME>SubPackage</SHORT-NAME>
        </AR-PACKAGE>
      </AR-PACKAGES>
    </AR-PACKAGE>
  </AR-PACKAGES>
</AUTOSAR>
```

**Step 2: Commit**

Run:
```bash
git add tests/fixtures/arxml/AUTOSAR_00046_sample.arxml
git commit -m "test: add AUTOSAR 00046 sample fixture
- Provide test data for integration tests
- Contains nested AR-PACKAGE structure"
```

---

### Task 17: Add read-write cycle test

**Files:**
- Create: `tests/integration/test_read_write_cycle.py`

**Step 1: Write test**

Create: `tests/integration/test_read_write_cycle.py`
```python
import pytest
from pathlib import Path

def test_read_write_cycle(tmp_path):
    """Test reading and writing ARXML preserves structure"""
    from armodel.reader import load_arxml
    from armodel.writer import save_arxml

    # Load fixture
    fixture = Path("tests/fixtures/arxml/AUTOSAR_00046_sample.arxml")
    autosar = load_arxml(fixture)

    # Write to temp file
    output = tmp_path / "output.arxml"
    save_arxml(autosar, output, pretty_print=True)

    # Read back
    autosar2 = load_arxml(output)

    # Verify both are AUTOSAR instances
    from armodel.models.M2.AUTOSARTemplates.autosar import AUTOSAR
    assert isinstance(autosar, AUTOSAR)
    assert isinstance(autosar2, AUTOSAR)

    # TODO: Add deeper comparison when parsing is implemented
```

**Step 2: Run test**

Run: `pytest tests/integration/test_read_write_cycle.py -v`
Expected: PASS

**Step 3: Commit**

Run:
```bash
git add tests/integration/test_read_write_cycle.py
git commit -m "test: add read-write cycle integration test
- Load fixture, write to temp, read back
- Verify AUTOSAR instance is preserved
- Foundation for deeper comparison tests"
```

---

## Phase 6: Documentation and Polish

### Task 18: Update README with usage examples

**Files:**
- Modify: `README.md`

**Step 1: Update README**

Update: `README.md`
```markdown
# py-armodel2

Python library for working with AUTOSAR ARXML models.

## Features

- Read and write ARXML files
- Static Python objects for all AUTOSAR types
- Multi-version support (AUTOSAR 00044, 00046, 00052)
- Optional validation against XSD schemas
- Builder pattern for easy object creation
- Merge and split ARXML documents

## Installation

```bash
pip install armodel
```

## Usage

### Reading ARXML Files

```python
from armodel.reader import load_arxml

# Load an ARXML file
autosar = load_arxml("model.arxml")

# Access the AUTOSAR document
print(f"Loaded {len(autosar.ar_packages)} packages")
```

### Writing ARXML Files

```python
from armodel.writer import save_arxml
from armodel.models.M2.AUTOSARTemplates.autosar import AUTOSAR

# Create AUTOSAR document
autosar = AUTOSAR()

# Save to file
save_arxml(autosar, "output.arxml", pretty_print=True)
```

### Creating Objects with Builders

```python
from armodel.models.M2.AUTOSARTemplates.AbstractPlatform import ApplicationInterface

# Create object using builder
interface = (ApplicationInterface.builder()
    .set_name("SensorInterface")
    .set_category("SENDER_RECEIVER")
    .build())
```

## Development

```bash
# Install in development mode
pip install -e ".[dev]"

# Run tests
pytest

# Run with coverage
pytest --cov=armodel --cov-report=html

# Run linter
ruff check src/

# Format code
ruff format src/

# Type checking
mypy src/
```

## Project Structure

- `src/armodel/core/` - Base classes and utilities
- `src/armodel/reader/` - ARXML reading functionality
- `src/armodel/writer/` - ARXML writing functionality
- `src/armodel/models/` - Generated AUTOSAR model classes
- `src/armodel/cli/` - Command-line interface
- `tools/generate_models.py` - Code generator

## License

MIT
```

**Step 2: Commit**

Run:
```bash
git add README.md
git commit -m "docs: update README with usage examples
- Add reading and writing examples
- Add builder pattern usage
- Add development instructions
- Document project structure"
```

---

### Task 19: Add setup script for development

**Files:**
- Create: `scripts/setup.sh`

**Step 1: Create setup script**

Create: `scripts/setup.sh`
```bash
#!/bin/bash
set -e

echo "Installing py-armodel2 in development mode..."

# Install in development mode
pip install -e ".[dev]"

# Run tests to verify
pytest

echo "Setup complete!"
```

Make executable:
```bash
chmod +x scripts/setup.sh
```

**Step 2: Commit**

Run:
```bash
git add scripts/setup.sh
git commit -m "chore: add development setup script
- Automated installation and test verification
- Make development onboarding easier"
```

---

## Summary

This implementation plan builds py-armodel2 in phases:

1. **Phase 1: Base Infrastructure** - Project setup, base classes, singleton
2. **Phase 2: Code Generator** - Generate Python classes from mapping.json
3. **Phase 3: Reader Module** - Load and parse ARXML files
4. **Phase 4: Writer Module** - Serialize and save ARXML files
5. **Phase 5: Integration Tests** - End-to-end testing
6. **Phase 6: Documentation** - Usage examples and polish

Each task follows TDD principles with bite-sized steps (2-5 minutes each).

**Next Steps:**

1. Review this plan
2. Adjust if needed
3. Execute using superpowers:executing-plans or superpowers:subagent-driven-development
