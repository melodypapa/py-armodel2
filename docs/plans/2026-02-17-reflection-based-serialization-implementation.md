# Reflection-Based Serialization Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Redesign ARXML reader/writer to use Python reflection instead of registry/strategies pattern, eliminating ~800 lines of complex abstraction.

**Architecture:** ARObject.serialize() and deserialize() use `vars()` and `get_type_hints()` for automatic serialization. NameConverter handles snake_case ↔ UPPER-CASE conversion. Decorators (@xml_attribute, @xml_tag) handle edge cases.

**Tech Stack:** Python 3.12+, xml.etree.ElementTree, lxml, pytest

---

## Task 1: Create NameConverter Utility

**Files:**
- Create: `src/armodel/serialization/name_converter.py`
- Test: `tests/unit/serialization/test_name_converter.py`

**Step 1: Write the failing test**

```python
# tests/unit/serialization/test_name_converter.py
from armodel.serialization.name_converter import NameConverter

def test_short_name_to_xml_tag():
    result = NameConverter.to_xml_tag("short_name")
    assert result == "SHORT-NAME"

def test_xml_tag_to_python_name():
    result = NameConverter.to_python_name("SHORT-NAME")
    assert result == "short_name"

def test_complex_conversion():
    result = NameConverter.to_xml_tag("sw_data_def_props")
    assert result == "SW-DATA-DEF-PROPS"

def test_private_attribute_stripped():
    result = NameConverter.to_xml_tag("_private_attr")
    assert result == "PRIVATE-ATTR"
```

**Step 2: Run test to verify it fails**

```bash
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/unit/serialization/test_name_converter.py -v
```
Expected: FAIL with "module 'armodel.serialization.name_converter' not found"

**Step 3: Write minimal implementation**

```python
# src/armodel/serialization/name_converter.py
"""Name conversion utility for Python ↔ AUTOSAR XML naming conventions."""


class NameConverter:
    """Convert between Python snake_case and AUTOSAR UPPER-CASE-WITH-HYPHENS naming."""

    @staticmethod
    def to_xml_tag(name: str) -> str:
        """Convert Python attribute name to XML tag name.

        Args:
            name: Python attribute name (snake_case)

        Returns:
            XML tag name (UPPER-CASE-WITH-HYPHENS)

        Examples:
            short_name → SHORT-NAME
            sw_data_def_props → SW-DATA-DEF-PROPS
        """
        # Remove private prefix
        if name.startswith('_'):
            name = name[1:]
        # Convert to uppercase and replace underscores with hyphens
        return name.upper().replace('_', '-')

    @staticmethod
    def to_python_name(tag: str) -> str:
        """Convert XML tag name to Python attribute name.

        Args:
            tag: XML tag name (UPPER-CASE-WITH-HYPHENS)

        Returns:
            Python attribute name (snake_case)

        Examples:
            SHORT-NAME → short_name
            SW-DATA-DEF-PROPS → sw_data_def_props
        """
        return tag.lower().replace('-', '_')
```

**Step 4: Run test to verify it passes**

```bash
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/unit/serialization/test_name_converter.py -v
```
Expected: PASS (4 tests)

**Step 5: Commit**

```bash
git add tests/unit/serialization/test_name_converter.py src/armodel/serialization/name_converter.py
git commit -m "feat: Add NameConverter utility for Python ↔ XML name conversion

- Convert snake_case ↔ UPPER-CASE-WITH-HYPHENS
- Handle private attributes (strip leading underscore)
- Add comprehensive unit tests

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

## Task 2: Create Serialization Decorators

**Files:**
- Create: `src/armodel/serialization/decorators.py`
- Test: `tests/unit/serialization/test_decorators.py`

**Step 1: Write the failing test**

```python
# tests/unit/serialization/test_decorators.py
from armodel.serialization.decorators import xml_attribute, xml_tag

def test_xml_attribute_decorator():
    @xml_attribute
    def category():
        return "STANDARD"

    assert hasattr(category, '_is_xml_attribute')
    assert category._is_xml_attribute == True

def test_xml_tag_decorator():
    @xml_tag("CUSTOM-TAG")
    class MyElement:
        pass

    assert hasattr(MyElement, '_xml_tag')
    assert MyElement._xml_tag == "CUSTOM-TAG"

def test_decorator_chain():
    @xml_attribute
    @property
    def schema_version(self):
        return self._schema_version

    assert hasattr(schema_version.fget, '_is_xml_attribute')
    assert schema_version.fget._is_xml_attribute == True
```

**Step 2: Run test to verify it fails**

```bash
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/unit/serialization/test_decorators.py -v
```
Expected: FAIL with "module 'armodel.serialization.decorators' not found"

**Step 3: Write minimal implementation**

```python
# src/armodel/serialization/decorators.py
"""Decorators for XML serialization edge cases."""


def xml_attribute(func):
    """Mark a property/attribute to be serialized as XML attribute instead of element.

    Usage:
        class AUTOSAR(ARObject):
            @xml_attribute
            @property
            def schema_version(self) -> str:
                return self._schema_version
    """
    func._is_xml_attribute = True
    return func


def xml_tag(tag_name: str):
    """Decorator to specify custom XML tag name for a class or attribute.

    Usage:
        @xml_tag("AUTOSAR")
        class AUTOSAR(ARObject):
            pass
    """
    def decorator(cls_or_func):
        cls_or_func._xml_tag = tag_name
        return cls_or_func
    return decorator
```

**Step 4: Run test to verify it passes**

```bash
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/unit/serialization/test_decorators.py -v
```
Expected: PASS (3 tests)

**Step 5: Commit**

```bash
git add tests/unit/serialization/test_decorators.py src/armodel/serialization/decorators.py
git commit -m "feat: Add serialization decorators for edge cases

- Add @xml_attribute decorator for XML attributes
- Add @xml_tag() decorator for custom tag names
- Support decorator chaining with @property
- Add unit tests

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

## Task 3: Implement ARObject.serialize() Method

**Files:**
- Modify: `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ArObject/ar_object.py`

**Step 1: Write the failing test**

```python
# tests/unit/models/test_ar_object_serialize.py
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String

class TestARObject(ARObject):
    def __init__(self):
        super().__init__()
        self.short_name: String = "test_name"
        self.category: str = "STANDARD"

def test_serialize_creates_element():
    obj = TestARObject()
    elem = obj.serialize("")

    assert elem.tag == "TESTAROBJECT"
    assert elem.find("SHORT-NAME") is not None
    assert elem.find("SHORT-NAME").text == "test_name"

def test_serialize_converts_names():
    obj = TestARObject()
    elem = obj.serialize("")

    # Verify snake_case → UPPER-CASE conversion
    assert elem.find("SHORT-NAME") is not None
    assert elem.find("CATEGORY") is not None
```

**Step 2: Run test to verify it fails**

```bash
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/unit/models/test_ar_object_serialize.py -v
```
Expected: FAIL with "TestARObject has no attribute 'serialize'"

**Step 3: Write minimal implementation**

Add to `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ArObject/ar_object.py`:

```python
# Add imports at top
from typing import Self, get_type_hints
from armodel.serialization.name_converter import NameConverter

# Add to ARObject class
def serialize(self, namespace: str = "") -> ET.Element:
    """Serialize object to XML element using reflection.

    Automatically discovers all non-private attributes via vars(self),
    converts names to XML tags, and serializes them as child elements.

    Args:
        namespace: XML namespace URI (optional)

    Returns:
        xml.etree.ElementTree.Element representing this object
    """
    # Get XML tag name for this class
    tag = self._get_xml_tag()
    elem = ET.Element(tag)

    # Add namespace if provided
    if namespace:
        elem.set("xmlns", namespace)

    # Get all instance attributes
    for name, value in vars(self).items():
        # Skip private attributes
        if name.startswith('_'):
            continue

        # Convert Python name to XML tag
        xml_tag = NameConverter.to_xml_tag(name)

        # Skip None values
        if value is None:
            continue

        # Check if this should be an XML attribute (via decorator)
        if self._is_xml_attribute(name):
            elem.set(xml_tag, str(value))
        elif hasattr(value, 'serialize'):
            # Recursively serialize child objects
            child = value.serialize(namespace)
            elem.append(child)
        elif isinstance(value, list):
            # Serialize list items
            for item in value:
                if hasattr(item, 'serialize'):
                    elem.append(item.serialize(namespace))
                else:
                    child = ET.Element(xml_tag)
                    child.text = str(item)
                    elem.append(child)
        else:
            # Primitive value - create element with text content
            child = ET.Element(xml_tag)
            child.text = str(value)
            elem.append(child)

    return elem

def _get_xml_tag(self) -> str:
    """Get XML tag name for this class.

    Checks for @xml_tag decorator override, otherwise auto-generates from class name.

    Returns:
        XML tag name
    """
    # Check for decorator override
    if hasattr(self.__class__, '_xml_tag'):
        return self.__class__._xml_tag

    # Auto-generate from class name
    return NameConverter.to_xml_tag(self.__class__.__name__)

def _is_xml_attribute(self, attr_name: str) -> bool:
    """Check if an attribute should be serialized as XML attribute.

    Checks for @xml_attribute decorator on the property.

    Args:
        attr_name: Name of the attribute to check

    Returns:
        True if should be XML attribute, False if element
    """
    # Get the property if it exists
    prop = getattr(self.__class__, attr_name, None)
    if prop and hasattr(prop, 'fget'):
        # Check if the property getter has the decorator marker
        return hasattr(prop.fget, '_is_xml_attribute') and prop.fget._is_xml_attribute

    # Check if the attribute itself has the marker
    attr = getattr(self.__class__, attr_name, None)
    if attr and hasattr(attr, '_is_xml_attribute'):
        return attr._is_xml_attribute

    return False
```

**Step 4: Run test to verify it passes**

```bash
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/unit/models/test_ar_object_serialize.py -v
```
Expected: PASS (2 tests)

**Step 5: Commit**

```bash
git add tests/unit/models/test_ar_object_serialize.py src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ArObject/ar_object.py
git commit -m "feat: Add ARObject.serialize() using reflection

- Use vars() to discover all attributes automatically
- Convert snake_case → UPPER-CASE-WITH-HYPHENS via NameConverter
- Support @xml_attribute decorator for XML attributes
- Support @xml_tag decorator for custom tag names
- Handle nested objects, lists, and primitives
- Add unit tests

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

## Task 4: Implement ARObject.deserialize() Method

**Files:**
- Modify: `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ArObject/ar_object.py`
- Test: `tests/unit/models/test_ar_object_deserialize.py`

**Step 1: Write the failing test**

```python
# tests/unit/models/test_ar_object_deserialize.py
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject

class TestARObject(ARObject):
    def __init__(self):
        super().__init__()
        self.short_name: str = None
        self.category: str = None

def test_deserialize_from_xml():
    xml = '''<TESTAROBJECT>
        <SHORT-NAME>test_name</SHORT-NAME>
        <CATEGORY>STANDARD</CATEGORY>
    </TESTAROBJECT>'''

    elem = ET.fromstring(xml)
    obj = TestARObject.deserialize(elem)

    assert obj.short_name == "test_name"
    assert obj.category == "STANDARD"

def test_deserialize_converts_names():
    xml = '''<TESTAROBJECT>
        <SW-DATA-DEF-PROPS>value</SW-DATA-DEF-PROPS>
    </TESTAROBJECT>'''

    elem = ET.fromstring(xml)
    obj = TestARObject.deserialize(elem)

    assert hasattr(obj, 'sw_data_def_props')
    assert obj.sw_data_def_props == "value"
```

**Step 2: Run test to verify it fails**

```bash
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/unit/models/test_ar_object_deserialize.py -v
```
Expected: FAIL with "TestARObject has no attribute 'deserialize'"

**Step 3: Write minimal implementation**

Add to `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ArObject/ar_object.py`:

```python
@classmethod
def deserialize(cls, element: ET.Element) -> Self:
    """Deserialize XML element to Python object.

    Creates a new instance and populates attributes by matching
    XML tags to Python attribute names.

    Args:
        element: XML element to deserialize from

    Returns:
        Deserialized Python object
    """
    # Create instance without calling __init__
    obj = cls.__new__(cls)

    # Call __init__ to set default values
    obj.__init__()

    # Get type hints to know what attributes to expect
    try:
        type_hints = get_type_hints(cls)
    except Exception:
        type_hints = {}

    # Process each attribute from type hints
    for attr_name, attr_type in type_hints.items():
        # Convert Python name to XML tag
        xml_tag = NameConverter.to_xml_tag(attr_name)

        # Check if this should be an XML attribute
        if cls._is_xml_attribute_static(attr_name):
            value = element.get(xml_tag)
        else:
            # Find child element
            child = element.find(xml_tag)
            if child is not None:
                # Get value based on type
                value = cls._extract_value(child, attr_type)
            else:
                value = None

        # Set attribute
        setattr(obj, attr_name, value)

    return obj

@staticmethod
def _is_xml_attribute_static(cls, attr_name: str) -> bool:
    """Static version to check if attribute should be XML attribute.

    Args:
        cls: The class to check
        attr_name: Name of the attribute

    Returns:
        True if should be XML attribute
    """
    prop = getattr(cls, attr_name, None)
    if prop and hasattr(prop, 'fget'):
        return hasattr(prop.fget, '_is_xml_attribute') and prop.fget._is_xml_attribute

    attr = getattr(cls, attr_name, None)
    if attr and hasattr(attr, '_is_xml_attribute'):
        return attr._is_xml_attribute

    return False

@staticmethod
def _extract_value(element: ET.Element, attr_type):
    """Extract value from XML element based on type.

    Args:
        element: XML element
        attr_type: Expected type (from type hints)

    Returns:
        Extracted value
    """
    if element is None:
        return None

    # Get text content
    text = element.text

    # Handle None
    if text is None:
        return None

    # For now, return as string
    # Type conversion will be added later
    return text
```

**Step 4: Run test to verify it passes**

```bash
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/unit/models/test_ar_object_deserialize.py -v
```
Expected: PASS (2 tests)

**Step 5: Commit**

```bash
git add tests/unit/models/test_ar_object_deserialize.py src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ArObject/ar_object.py
git commit -m "feat: Add ARObject.deserialize() using reflection

- Use get_type_hints() to discover expected attributes
- Convert XML tags → snake_case via NameConverter
- Extract values from XML elements and attributes
- Support @xml_attribute decorator detection
- Add unit tests

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

## Task 5: Update Code Generator to Remove XMLMember

**Files:**
- Modify: `tools/generate_models.py`

**Step 1: Remove _xml_members generation**

Delete lines 529-601 from `tools/generate_models.py` (the entire `_xml_members` dict generation section).

**Step 2: Remove XMLMember imports**

Find and remove these imports:
- Line 311: `from armodel.serialization.metadata import XMLMember`
- Line 346: `from armodel.serialization import XMLMember`

**Step 3: Test with small generation**

```bash
# Run generator to verify it works
python tools/generate_models.py docs/json/mapping.json docs/json/hierarchy.json /tmp/test_output --members --classes --no-enums --no-primitives
```
Expected: Generated classes have no `_xml_members` dict

**Step 4: Inspect generated class**

```bash
# Check a generated class
head -30 /tmp/test_output/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ArObject/ar_object.py
```
Expected: No `_xml_members: dict[str, XMLMember]` in the output

**Step 5: Commit**

```bash
git add tools/generate_models.py
git commit -m "refactor: Remove XMLMember generation from code generator

- Remove _xml_members dict generation (lines 529-601)
- Remove XMLMember imports
- Generated classes now rely on type hints only
- Prepare for reflection-based serialization

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

## Task 6: Integration Test - Read AUTOSAR_Datatypes.arxml

**Files:**
- Create: `tests/integration/test_read_datatypes.py`

**Step 1: Write the test**

```python
# tests/integration/test_read_datatypes.py
from armodel.reader import ARXMLReader

def test_read_autosar_datatypes():
    """Test reading AUTOSAR_Datatypes.arxml file."""
    reader = ARXMLReader()
    autosar = reader.load_arxml('demos/arxml/AUTOSAR_Datatypes.arxml')

    # Verify root element
    assert autosar is not None
    assert hasattr(autosar, 'ar_packages')

    # Verify structure
    assert len(autosar.ar_packages) > 0

    # Find AUTOSAR_Platform package
    platform_pkg = None
    for pkg in autosar.ar_packages:
        if pkg.short_name == 'AUTOSAR_Platform':
            platform_pkg = pkg
            break

    assert platform_pkg is not None, "AUTOSAR_Platform package not found"

    # Verify BaseTypes subpackage
    base_types = None
    for pkg in platform_pkg.ar_packages:
        if pkg.short_name == 'BaseTypes':
            base_types = pkg
            break

    assert base_types is not None, "BaseTypes package not found"

    # Verify we have SwBaseType elements
    assert hasattr(base_types, 'elements')
    assert len(base_types.elements) > 0

    # Verify first SwBaseType
    first_type = base_types.elements[0]
    assert first_type.short_name == 'float32'
```

**Step 2: Run test to verify it fails**

```bash
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/integration/test_read_datatypes.py -v
```
Expected: May fail if reader not updated yet

**Step 3: Update ARXMLReader if needed**

If test fails, update `src/armodel/reader/__init__.py` to use new deserialize:

```python
def load_arxml(self, file_path: str, validate: bool = False) -> AUTOSAR:
    """Load ARXML file and deserialize to AUTOSAR object."""
    # Parse with lxml
    tree = self._lxml_parser.parse(file_path)
    root_lxml = tree.getroot()

    # Convert to ElementTree
    root_et = self._lxml_to_elementtree(root_lxml)

    # Deserialize using ARObject.deserialize()
    from armodel.models.M2.AUTOSARTemplates.AutosarTopStructure.autosar import AUTOSAR
    return AUTOSAR.deserialize(root_et)
```

**Step 4: Run test to verify it passes**

```bash
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/integration/test_read_datatypes.py -v
```
Expected: PASS

**Step 5: Commit**

```bash
git add tests/integration/test_read_datatypes.py src/armodel/reader/__init__.py
git commit -m "feat: Add integration test for reading AUTOSAR_Datatypes.arxml

- Test reading complete ARXML file with new reflection-based deserialization
- Verify AUTOSAR_Platform, BaseTypes, and SwBaseType elements
- Update ARXMLReader to use ARObject.deserialize()

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

## Task 7: Integration Test - Round-Trip Serialization

**Files:**
- Create: `tests/integration/test_roundtrip.py`

**Step 1: Write the test**

```python
# tests/integration/test_roundtrip.py
import tempfile
from pathlib import Path
from armodel.reader import ARXMLReader
from armodel.writer import ARXMLWriter

def test_roundtrip_serialization():
    """Test read → serialize → write produces valid XML."""
    # Read original file
    reader = ARXMLReader()
    autosar = reader.load_arxml('demos/arxml/AUTOSAR_Datatypes.arxml')

    # Write to temp file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.arxml', delete=False) as f:
        temp_path = f.name

    try:
        writer = ARXMLWriter(pretty_print=True)
        writer.save_arxml(autosar, temp_path)

        # Read back
        autosar2 = reader.load_arxml(temp_path)

        # Basic verification
        assert autosar2 is not None
        assert len(autosar2.ar_packages) == len(autosar.ar_packages)

        # Verify structure is preserved
        for pkg1, pkg2 in zip(autosar.ar_packages, autosar2.ar_packages):
            assert pkg1.short_name == pkg2.short_name

    finally:
        # Cleanup
        Path(temp_path).unlink()
```

**Step 2: Run test to verify it fails**

```bash
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/integration/test_roundtrip.py -v
```
Expected: May fail if writer not updated yet

**Step 3: Update ARXMLWriter if needed**

If test fails, update `src/armodel/writer/__init__.py` to use new serialize:

```python
def save_arxml(self, autosar: AUTOSAR, file_path: str):
    """Serialize AUTOSAR object and write to ARXML file."""
    # Serialize using ARObject.serialize()
    namespace = autosar.schema_version if hasattr(autosar, 'schema_version') else ""
    root = autosar.serialize(namespace)

    # Write to file
    tree = ET.ElementTree(root)
    tree.write(file_path, encoding=self.encoding, xml_declaration=True)
```

**Step 4: Run test to verify it passes**

```bash
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/integration/test_roundtrip.py -v
```
Expected: PASS

**Step 5: Commit**

```bash
git add tests/integration/test_roundtrip.py src/armodel/writer/__init__.py
git commit -m "feat: Add round-trip serialization test

- Test reading and writing AUTOSAR_Datatypes.arxml
- Verify structure preservation through round-trip
- Update ARXMLWriter to use ARObject.serialize()

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

## Task 8: Verify with Existing Test Suite

**Files:**
- No new files
- Test: Run full test suite

**Step 1: Run all tests**

```bash
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest -v
```
Expected: May have some failures in unimplemented features

**Step 2: Check test results**

Review failures. Expected:
- New tests: PASS
- Old tests: May fail if they depended on old serialization
- Unimplemented feature tests: SKIP (as before)

**Step 3: Fix critical failures**

If any critical tests fail:
1. Identify the issue
2. Fix the implementation
3. Re-run tests

**Step 4: Commit**

```bash
git add -A
git commit -m "test: Fix test failures from reflection-based serialization migration

- Address any test failures from old serialization system
- Ensure all existing tests pass or are properly skipped

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

## Task 9: Update Documentation

**Files:**
- Modify: `CLAUDE.md`
- Modify: `docs/designs/design_rules.md`

**Step 1: Update CLAUDE.md**

Update the serialization section in `CLAUDE.md`:

```markdown
### Serialization Framework (Reflection-Based)

The project uses a reflection-based serialization framework that eliminates boilerplate:

**Key Components:**
- `ARObject.serialize()` - Base method that uses reflection to serialize
- `ARObject.deserialize()` - Class method that deserializes from XML
- `NameConverter` - Utility for snake_case ↔ UPPER-CASE conversion
- `@xml_attribute`, `@xml_tag()` - Decorators for edge cases

**Each class defines:**
- Type hints on `__init__` attributes (drive deserialization)
- Optional decorators for edge cases (XML attributes, custom tags)
- No `_xml_members` dict needed!

**The base class handles the rest:**
- Uses `vars()` to discover all attributes
- Uses `get_type_hints()` for type information
- Converts names automatically via NameConverter
```

**Step 2: Update DESIGN_RULES**

Add new rule about reflection-based serialization in `docs/designs/design_rules.md`:

```markdown
### 13. Reflection-Based Serialization
- **DESIGN_RULE_043**: Use reflection-based serialization instead of metadata dicts
- **DESIGN_RULE_044**: All attributes must have type hints for deserialization
- **DESIGN_RULE_045**: Use @xml_attribute decorator for XML attributes
- **DESIGN_RULE_046**: Use @xml_tag() decorator for non-standard tag names
```

**Step 3: Commit**

```bash
git add CLAUDE.md docs/designs/design_rules.md
git commit -m "docs: Update documentation for reflection-based serialization

- Update CLAUDE.md with new architecture
- Add design rules for reflection-based serialization
- Document decorator usage

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

## Task 10: Cleanup Deprecated Code

**Files:**
- Remove: `src/armodel/serialization/registry.py`
- Remove: `src/armodel/serialization/strategies/reflection_serializer.py`
- Remove: `src/armodel/serialization/strategies/custom_autosar.py`
- Remove: `src/armodel/serialization/metadata.py`
- Remove: `tests/unit/serialization/test_registry.py` (if exists)

**Step 1: Verify no imports of deprecated code**

```bash
grep -r "SerializationRegistry" src/armodel/ --include="*.py"
grep -r "XMLMember" src/armodel/ --include="*.py"
grep -r "from armodel.serialization.strategies" src/armodel/ --include="*.py"
```
Expected: Only imports should be in old generated code (will be regenerated)

**Step 2: Remove deprecated files**

```bash
git rm src/armodel/serialization/registry.py
git rm src/armodel/serialization/strategies/reflection_serializer.py
git rm src/armodel/serialization/strategies/custom_autosar.py
git rm src/armodel/serialization/metadata.py
```

**Step 3: Regenerate all model classes**

```bash
python tools/generate_models.py docs/json/mapping.json docs/json/hierarchy.json src/armodel/models/M2 --members --classes --enums --primitives
```

**Step 4: Run tests to verify**

```bash
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest -v
```
Expected: All tests pass

**Step 5: Commit**

```bash
git add -A
git commit -m "refactor: Remove deprecated serialization code

- Remove SerializationRegistry (100 lines)
- Remove ReflectionSerializer (395 lines)
- Remove CustomAutosar strategy
- Remove XMLMember descriptor (235 lines)
- Regenerate all model classes without _xml_members
- Total reduction: ~800 lines of code

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

## Summary

This implementation plan:
1. ✅ Builds core utilities (NameConverter, decorators)
2. ✅ Implements ARObject.serialize() and deserialize() using reflection
3. ✅ Updates code generator to remove XMLMember
4. ✅ Tests with real AUTOSAR_Datatypes.arxml file
5. ✅ Verifies round-trip serialization
6. ✅ Cleans up ~800 lines of deprecated code

**Total tasks:** 10
**Estimated time:** 2-3 hours
**Testing approach:** TDD with frequent commits
