# Class Generator for AUTOSAR Models

Generate Python classes from AUTOSAR ARXML files based on M2 model definitions with proper type handling, inheritance, and namespace support.

## When to Use

- Analyze new AUTOSAR ARXML files for class structures
- Generate new classes with correct AUTOSAR inheritance
- Update existing classes to match M2 model specifications
- Fix class attributes with proper type annotations
- Implement serialize/deserialize with namespace support

## Actions

### Step 1: Analyze ARXML File

Parse the ARXML file to identify all element types (e.g., `SW-BASE-TYPE`, `COMPU-METHOD`, `DATA-CONSTR`).

### Step 2: Query JSON Metadata

For each class found in the ARXML:
1. Look up the class in `docs/json/hierarchy.json` to find its parent class
2. Find the class definition in the appropriate `docs/json/packages/*.classes.json` file
3. Extract all attributes with their types and multiplicities

### Step 3: Generate or Update Class

For each class:

**3.1. Set Parent Class:**
```python
from armodel.models.M2.<parent_package_path> import <ParentClass>

class MyClass(ParentClass):
    """AUTOSAR MyClass."""
```

**3.2. Import Required Types:**
- Import parent class
- Import all attribute types from their packages (including AUTOSAR primitive types from PrimitiveTypes)

**3.3. Add Attributes to `__init__`:**
```python
def __init__(self) -> None:
    """Initialize MyClass."""
    super().__init__()
    self.attribute_name: Optional[str] = None  # For multiplicity 0..1 or 1
    self.list_attribute: list[ItemType] = []  # For multiplicity * or 0..*
```

**3.4. Define `_xml_members` for This Class Only:**
```python
# XML member definitions for this class only (not inherited from parent classes)
# Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
_xml_members = [
    ("attribute_name", None, True, False, None),  # XML attribute
    ("child_element", None, False, False, None),  # Child element (primitive)
    ("list_element", None, False, True, ItemType),  # List of child elements
]
```

**3.5. Implement `serialize()` with Namespace:**
```python
def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
    """Convert MyClass to XML element.

    Args:
        namespace: XML namespace for the element
        element: Optional existing element to add members to (for subclass chaining)

    Returns:
        XML element representing this object
    """
    # Let parent class handle its members first
    element = super().serialize(namespace, element)
    # This class's members are already handled by parent's serialize via _xml_members
    return element
```

**3.6. Implement `deserialize()` with Namespace Handling:**
```python
@classmethod
def deserialize(cls, element: ET.Element) -> "MyClass":
    """Create MyClass from XML element.

    Args:
        element: XML element to deserialize from

    Returns:
        MyClass instance
    """
    # Let parent class handle its members first
    obj = super().deserialize(element)
    # This class's members are already handled by parent's deserialize via _xml_members
    return obj
```

## Critical Rules

### 1. Type Mapping

**Use AUTOSAR primitive types**

**For class types**, import from their package paths (found in `docs/json/mapping.json`).

### 2. Multiplicity to Python Type

| Multiplicity | Python Type      | Initial Value                       |
| ------------ | ---------------- | ----------------------------------- |
| `0..1`       | `Optional[Type]` | `None`                              |
| `1`          | `Type`           | `None` (set during deserialization) |
| `*`          | `list[Type]`     | `[]`                                |
| `0..*`       | `list[Type]`     | `[]`                                |

### 3. Namespace Handling

**All serialize() methods MUST accept namespace parameter:**
```python
def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
```

**All deserialize() methods MUST strip namespace from tags (handled by ARObject base class):**
```python
tag = child.tag.split('}')[1] if '}' in child.tag else child.tag
```

### 4. Initialization Rules

✅ **CORRECT:**
```python
self.short_name: Optional[str] = None
self.items: list[ItemType] = []
```

❌ **WRONG:**
```python
self.short_name: str = ""  # Don't use default values
self.items: Optional[list[ItemType]] = None  # Don't use Optional for lists
```

**Key principles:**
- All single objects: Initialize to `None` (except required primitives)
- All lists: Initialize to `[]` (never `None`)
- Required primitives (multiplicity 1): Can initialize to `0`, `""`, `False` or use `None`
- Never use Optional for lists

### 5. Member-to-XML Pattern (_xml_members)

**CRITICAL: Each class only defines _xml_members for its own attributes, not inherited ones.**

The `_xml_members` class attribute defines how to map Python attributes to XML:

```python
# Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
_xml_members = [
    ("short_name", None, False, False, None),           # Primitive child element
    ("category", "CATEGORY", True, False, None),        # XML attribute with custom tag
    ("items", None, False, True, ItemClass),            # List of child objects
    ("data", None, False, False, None),                 # Primitive child element
]
```

**Parameters:**
- `member_name`: Python attribute name (snake_case)
- `xml_tag_name`: XML tag/attribute name (or `None` to auto-convert from member_name)
- `is_attribute`: `True` = XML attribute, `False` = child element
- `is_list`: `True` = member is a list, `False` = single value
- `element_class`: For child elements, the class to deserialize (or `None` for primitives)

**XML Tag Inference:**
When `xml_tag_name` is `None`, the tag is automatically inferred from `member_name`:
- `short_name` → `SHORT-NAME`
- `category` → `CATEGORY`
- `data_type` → `DATA-TYPE`

**Automatic Hierarchy Handling:**
The `ARObject` base class automatically collects `_xml_members` from the entire class hierarchy (parent to child order). You only need to define `_xml_members` for each class's own attributes - the base class handles the rest.

### 6. Serialize/Deserialize Pattern

**Each class ONLY defines _xml_members for its own attributes. The ARObject base class automatically handles the entire hierarchy.**

**Serialization pattern:**
```python
def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
    """Convert MyClass to XML element.

    Args:
        namespace: XML namespace for the element
        element: Optional existing element to add members to (for subclass chaining)

    Returns:
        XML element representing this object
    """
    # ARObject.serialize() handles entire class hierarchy automatically
    return super().serialize(namespace, element)
```

**Deserialization pattern:**
```python
@classmethod
def deserialize(cls, element: ET.Element) -> "MyClass":
    """Create MyClass from XML element.

    Args:
        element: XML element to deserialize from

    Returns:
        MyClass instance
    """
    from typing import cast
    # ARObject.deserialize() handles entire class hierarchy automatically
    obj = super().deserialize(element)
    # Cast to MyClass since parent returns ARObject
    return cast("MyClass", obj)
```

**DO NOT manually implement serialization/deserialization logic.** The base `ARObject` class handles everything via the `_xml_members` pattern, including collecting members from the entire class hierarchy.

### 7. Namespace Configuration

**Namespaces are defined in `src/armodel/cfg/schemas/config.yaml`:**

| Version | Namespace URL                    | Schema File       | Features                                          |
| ------- | -------------------------------- | ----------------- | ------------------------------------------------- |
| 00044   | `http://autosar.org/3.0.4`       | AUTOSAR_00044.xsd | strict validation                                 |
| 00046   | `http://autosar.org/schema/r4.0` | AUTOSAR_00046.xsd | compact_schema, standard validation               |
| 00052   | `http://autosar.org/schema/r5.0` | AUTOSAR_00052.xsd | compact_schema, strict_compact, strict validation |

**Default version:** 00046

**Using namespaces in serialization:**
```python
from armodel.core import SchemaVersionManager

# Get the version manager singleton
version_mgr = SchemaVersionManager()

# Get namespace for a specific version
namespace = version_mgr.get_namespace("00046")  # Returns: "http://autosar.org/schema/r4.0"

# Or get namespace for current default version
namespace = version_mgr.get_namespace()  # Returns default version namespace

# Use in serialization
element = my_class.serialize(namespace)
```

## Complete Example

```python
from typing import Optional
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import Referrable
from armodel.models.M2.AUTOSARTemplates.SomePackage.SomeClass import SomeClass
from armodel.core import SchemaVersionManager

class SwBaseType(Referrable):
    """AUTOSAR SwBaseType."""

    # XML member definitions for this class only (not inherited from Referrable)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("category", None, True, False, None),  # XML attribute
        ("sub_elements", None, False, True, SomeClass),  # List of child elements
    ]

    def __init__(self) -> None:
        """Initialize SwBaseType."""
        super().__init__()  # Initializes parent's members (short_name, etc.)
        self.category: Optional[str] = None
        self.sub_elements: list[SomeClass] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SwBaseType to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # Parent class handles its members (short_name, etc.) via _xml_members
        element = super().serialize(namespace, element)
        # This class's members (category, sub_elements) handled automatically
        return element

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwBaseType":
        """Create SwBaseType from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SwBaseType instance
        """
        # Parent class handles its members (short_name, etc.) via _xml_members
        obj = super().deserialize(element)
        # This class's members (category, sub_elements) handled automatically
        return obj

# Usage example with proper namespace:
version_mgr = SchemaVersionManager()
namespace = version_mgr.get_namespace()  # Gets default version namespace

# Serialize with namespace
sw_base_type = SwBaseTypeBuilder().with_short_name("MyType").with_category("FIXED").build()
xml_element = sw_base_type.serialize(namespace)

# Or specify version explicitly
namespace = version_mgr.get_namespace("00046")  # "http://autosar.org/schema/r4.0"
xml_element = sw_base_type.serialize(namespace)
```

## Arguments

- `--arxml-file <path>`: Specify ARXML file to analyze (default: `demos/arxml/AUTOSAR_Datatypes.arxml`)
- `--dry-run`: Analyze and report without making changes

## Validation

After generating classes, verify:

1. **Import Validation**: All imports resolve correctly
2. **Type Validation**: MyPy type checking passes
3. **Lint Validation**: Ruff linting passes
4. **Round-trip Test**: Load ARXML → serialize → deserialize → compare

```bash
ruff check src/
mypy src/
```

## References

- Hierarchy: `docs/json/hierarchy.json`
- Type mapping: `docs/json/mapping.json`
- Package definitions: `docs/json/packages/*.classes.json`
