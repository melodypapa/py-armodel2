"""Code generation functions for AUTOSAR models."""

from typing import Any, Dict, List

from ._common import get_python_identifier, to_snake_case
from .type_utils import (
    detect_circular_import,
    get_python_type,
    get_type_import_path,
    get_type_package_path,
    is_primitive_type,
    is_enum_type,
)


# Base class names for AUTOSAR primitives and enums
PRIMITIVE_BASE_CLASS = "ARPrimitive"
ENUM_BASE_CLASS = "AREnum"


def generate_class_code(
    type_def: dict,
    hierarchy_info: Dict[str, Dict[str, Any]],
    package_data: Dict[str, Dict[str, Any]],
    include_members: bool = False,
    json_file_path: str = "",
    dependency_graph: Dict[str, set] = None,
    force_type_checking_imports: Dict[str, List[str]] = None,
) -> str:
    """Generate Python class code from type definition.

    Args:
        type_def: Type definition from mapping.json
        hierarchy_info: Dictionary with parent and abstract information from hierarchy.json
        package_data: Dictionary with package data including class attributes
        include_members: Whether to include member lists from package definitions
        json_file_path: Path to the JSON file containing the class definition
        dependency_graph: Complete dependency graph for circular import detection
        force_type_checking_imports: Dict mapping class names to types that should use TYPE_CHECKING

    Returns:
        Generated Python code as string
    """
    if dependency_graph is None:
        dependency_graph = {}
    if force_type_checking_imports is None:
        force_type_checking_imports = {}
    class_name = type_def["name"]
    is_splitable = type_def.get("splitable", False)
    split_file_name = type_def.get("split_file_name", "")
    package_path = type_def.get("package_path", "")

    # Get parent and abstract status from hierarchy
    parent_class = None
    is_abstract = False

    # First check hierarchy_info for parent and abstract status
    if class_name in hierarchy_info:
        parent_class = hierarchy_info[class_name]["parent"]
        is_abstract = hierarchy_info[class_name]["is_abstract"]

    # Also check package_data for abstract status (takes precedence if available)
    if include_members and package_path in package_data:
        for cls in package_data[package_path].get("classes", []):
            if cls["name"] == class_name:
                # Use is_abstract from JSON if available
                if "is_abstract" in cls:
                    is_abstract = cls["is_abstract"]
                # Use parent from JSON if available
                if "parent" in cls and cls["parent"]:
                    parent_class = cls["parent"]
                break

    # Ensure ARObject is not the parent of itself
    # Default to ARObject only if class_name is not "ARObject" and no parent found
    if not parent_class and class_name != "ARObject":
        parent_class = "ARObject"
    elif parent_class == "ARObject" and class_name == "ARObject":
        # Prevent ARObject from being its own parent
        parent_class = None

    # Get class information from package_data (includes sources with PDF references)
    sources = []
    if include_members and package_path in package_data:
        for cls in package_data[package_path].get("classes", []):
            if cls["name"] == class_name:
                sources = cls.get("sources", [])
                break

    # Build docstring with PDF references and JSON file path
    docstring_lines = [f"{class_name} AUTOSAR element."]

    # Add PDF file references if available
    if sources:
        docstring_lines.append("")
        docstring_lines.append("References:")
        for source in sources:
            pdf_file = source.get("pdf_file", "N/A")
            page_number = source.get("page_number", "N/A")
            docstring_lines.append(f"  - {pdf_file} (page {page_number})")

    # Add JSON file path if available
    if json_file_path:
        docstring_lines.append("")
        docstring_lines.append(f"JSON Source: {json_file_path}")

    docstring = "\n".join(docstring_lines)

    # Generate class code
    if class_name == "ARObject":
        future_import = "from __future__ import annotations\n"
        type_checking_import = "from typing import TYPE_CHECKING, Optional, Union, get_type_hints, get_args, get_origin\n"
        base_import = "import xml.etree.ElementTree as ET\n"
        # Import NameConverter for reflection-based serialization
        name_converter_import = "from armodel.serialization.name_converter import NameConverter\n"
        code = f'''"""{docstring}"""

{future_import}{type_checking_import}{base_import}{name_converter_import}
'''
    else:
        # For other classes, we need to check attribute types first to determine imports
        # Collect attribute types for imports
        attribute_types = {}
        if include_members and package_path in package_data:
            class_info = package_data[package_path].get("classes", [])
            for cls in class_info:
                if cls["name"] == class_name and "attributes" in cls:
                    for attr_name, attr_info in cls["attributes"].items():
                        attr_type = attr_info["type"]
                        multiplicity = attr_info["multiplicity"]
                        attribute_types[attr_name] = {"type": attr_type, "multiplicity": multiplicity}
                    break

        # Check if we need Any type
        uses_any_type = False
        if attribute_types:
            for attr_name, attr_info in attribute_types.items():
                attr_type = attr_info["type"]
                if attr_type.startswith("any ("):
                    uses_any_type = True
                    break

        # Build imports based on what we need
        future_import = "from __future__ import annotations\n"
        if uses_any_type:
            basic_import = "from typing import TYPE_CHECKING, Optional, Any\n"
        else:
            basic_import = "from typing import TYPE_CHECKING, Optional\n"
        base_import = "import xml.etree.ElementTree as ET\n"
        code = f'''"""{docstring}"""

{future_import}{basic_import}{base_import}
'''

    # Add parent class import
    if parent_class and parent_class != "ARObject":
        # Find parent class path from hierarchy or mapping
        parent_import = get_type_import_path(parent_class, package_data)
        if parent_import:
            code += f"{parent_import}\n"
        else:
            # Fallback to ARObject import
            code += "from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject\n"
    elif class_name != "ARObject":
        # Add ARObject import for classes that inherit from ARObject
        code += "from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject\n"

    # Collect attribute types for imports (if not already collected for non-ARObject classes)
    if class_name == "ARObject":
        attribute_types = {}
        if include_members and package_path in package_data:
            class_info = package_data[package_path].get("classes", [])
            for cls in class_info:
                if cls["name"] == class_name and "attributes" in cls:
                    for attr_name, attr_info in cls["attributes"].items():
                        attr_type = attr_info["type"]
                        multiplicity = attr_info["multiplicity"]
                        attribute_types[attr_name] = {"type": attr_type, "multiplicity": multiplicity}
                    break

    # Add type imports if needed
    if attribute_types:
        type_imports = set()
        primitive_imports = {}  # Changed from set to dict to track package path
        enum_imports = set()

        for attr_name, attr_info in attribute_types.items():
            attr_type = attr_info["type"]
            # Import class types and primitive types
            if is_primitive_type(attr_type, package_data):
                # Find the package path for this primitive
                for package_path, data in package_data.items():
                    if "primitives" in data:
                        for prim in data["primitives"]:
                            if prim["name"] == attr_type:
                                primitive_imports[attr_type] = package_path
                                break
                    if attr_type in primitive_imports:
                        break
            elif is_enum_type(attr_type, package_data):
                enum_imports.add(attr_type)
            elif not attr_type.startswith("any ("):
                # Import class types (skip polymorphic "any (xxx)" types)
                type_imports.add(attr_type)

        # Add import statements for enum types
        if enum_imports:
            # Find package path for each enum
            enums_by_package = {}
            for enum_name in enum_imports:
                for package_path, data in package_data.items():
                    if "enumerations" in data:
                        for enum in data["enumerations"]:
                            if enum["name"] == enum_name:
                                enums_by_package[package_path] = enums_by_package.get(package_path, [])
                                enums_by_package[package_path].append(enum_name)
                                break
                    if enum_name in [e for pkg in enums_by_package.values() for e in pkg]:
                        break

            for pkg_path, enum_names in sorted(enums_by_package.items()):
                python_path = pkg_path.replace("::", ".")
                code += f"from armodel.models.{python_path} import (\n"
                for i, enum in enumerate(sorted(enum_names)):
                    if i == len(enum_names) - 1:
                        code += f"    {enum},\n"
                    else:
                        code += f"    {enum},\n"
                code += ")\n"

        # Add import statements for primitive types
        # Group primitives by package path
        primitives_by_package = {}
        for prim_name, pkg_path in primitive_imports.items():
            if pkg_path not in primitives_by_package:
                primitives_by_package[pkg_path] = []
            primitives_by_package[pkg_path].append(prim_name)

        for pkg_path, prim_names in sorted(primitives_by_package.items()):
            python_path = pkg_path.replace("::", ".")
            code += f"from armodel.models.{python_path} import (\n"
            for i, prim in enumerate(sorted(prim_names)):
                if i == len(prim_names) - 1:
                    code += f"    {prim},\n"
                else:
                    code += f"    {prim},\n"
            code += ")\n"

        # Add import statements for class types
        # Track already-added imports to prevent duplicates
        # Get parent class import path to avoid importing it again as an attribute type
        added_imports = set()
        if parent_class and parent_class != "ARObject":
            parent_import_path = get_type_import_path(parent_class, package_data)
            if parent_import_path:
                added_imports.add(parent_import_path)

        # Add class_name to prevent self-import (class importing itself)
        # This prevents ARObject from importing itself
        class_import_path = get_type_import_path(class_name, package_data)
        if class_import_path:
            added_imports.add(class_import_path)

        # Get forced TYPE_CHECKING imports for this class
        forced_type_checking_for_class = force_type_checking_imports.get(class_name, [])

        # Separate circular and non-circular imports
        circular_imports = set()
        non_circular_imports = set()

        if type_imports:
            for import_type in sorted(type_imports):
                # Skip self-import (class importing itself)
                if import_type == class_name:
                    continue
                import_path = get_type_import_path(import_type, package_data)
                if import_path and import_path not in added_imports:
                    # Check if this import should be forced into TYPE_CHECKING
                    # 1. Check if the import_type is globally forced ("*")
                    forced_globally = force_type_checking_imports.get(import_type) == "*"
                    # 2. Check if this class has specific types forced
                    forced_for_this_class = import_type in forced_type_checking_for_class
                    # 3. Check for circular import via dependency graph
                    is_circular = detect_circular_import(class_name, import_type, package_data, dependency_graph)

                    if forced_globally or forced_for_this_class or is_circular:
                        circular_imports.add((import_type, import_path))
                    else:
                        non_circular_imports.add((import_type, import_path))
                    added_imports.add(import_path)

        # Add non-circular imports directly
        for import_type, import_path in sorted(non_circular_imports):
            code += f"{import_path}\n"

        # Add circular imports in TYPE_CHECKING block
        if circular_imports:
            code += "\nif TYPE_CHECKING:\n"
            for import_type, import_path in sorted(circular_imports):
                # Reconstruct just the type name for TYPE_CHECKING import
                # Remove the "from ... import (\n    TYPE,\n)" wrapper
                # and use a simpler TYPE_CHECKING format
                type_package = get_type_package_path(import_type, package_data)
                if type_package:
                    python_path = type_package.replace("::", ".")
                    module_path = f"armodel.models.{python_path}.{to_snake_case(import_type)}"
                    code += f"    from {module_path} import (\n        {import_type},\n    )\n"
            code += "\n"

    # Generate class definition with ABC for abstract classes
    if is_abstract:
        # Abstract classes inherit from ABC
        # Add abc import for abstract classes
        code += "from abc import ABC, abstractmethod\n"
        if parent_class:
            code += f'''\n
class {class_name}({parent_class}, ABC):
    """AUTOSAR {class_name}."""\n'''
        else:
            code += f'''\n
class {class_name}(ABC):
    """AUTOSAR {class_name}."""\n'''
        # Add is_abstract property for abstract classes
        code += '''
    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

'''
    else:
        # Non-abstract classes
        if parent_class:
            code += f'''\n
class {class_name}({parent_class}):
    """AUTOSAR {class_name}."""\n'''
        else:
            code += f'''\n
class {class_name}:
    """AUTOSAR {class_name}."""\n'''
        # Add is_abstract property for non-abstract classes
        code += '''
    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

'''

    if is_splitable:
        code += f'''    is_splitable = True
    split_file_name = "{split_file_name}"

'''

    # Add class-level type annotations for get_type_hints() to work
    if attribute_types:
        for attr_name, attr_info in attribute_types.items():
            attr_type = attr_info["type"]
            multiplicity = attr_info["multiplicity"]

            # Determine Python type
            python_type = get_python_type(attr_type, multiplicity, package_data)

            # Get Python identifier
            python_name, _ = get_python_identifier(attr_name)

            # Add class-level annotation
            code += f"    {python_name}: {python_type}\n"

    code += f'''    def __init__(self) -> None:
        """Initialize {class_name}."""\n'''

    # Add super().__init__() call for all classes except ARObject
    if class_name != "ARObject":
        code += """        super().__init__()
"""

    # Add member attributes if requested
    if attribute_types:
        for attr_name, attr_info in attribute_types.items():
            attr_type = attr_info["type"]
            multiplicity = attr_info["multiplicity"]

            # Determine Python type
            python_type = get_python_type(attr_type, multiplicity, package_data)

            # Determine initial value based on type
            # Optional types initialize with None
            # list types initialize with []
            # Non-optional types initialize with None
            if python_type.startswith("Optional["):
                initial_value = "None"
            elif python_type.startswith("list["):
                initial_value = "[]"
            else:
                initial_value = "None"

            # Get Python identifier (handles Python keywords)
            python_name, _ = get_python_identifier(attr_name)
            attr_code = f"        self.{python_name}: {python_type} = {initial_value}\n"
            code += attr_code

    # Add serialize/deserialize methods
    # Special handling for ARObject which implements the reflection-based pattern
    # All other classes inherit serialize/deserialize from ARObject
    if class_name == "ARObject":
        # ARObject uses reflection-based serialization framework
        # Add serialize(), deserialize(), and helper methods
        code += _generate_ar_object_methods()

    return code


def _generate_ar_object_methods() -> str:
    """Generate the serialize/deserialize methods for ARObject.

    Returns:
        Generated code for ARObject methods
    """
    return '''
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
                # Serialize list items - create wrapper element
                wrapper = ET.Element(xml_tag)
                for item in value:
                    if hasattr(item, 'serialize'):
                        wrapper.append(item.serialize(namespace))
                    else:
                        child = ET.Element(xml_tag)
                        child.text = str(item)
                        wrapper.append(child)
                elem.append(wrapper)
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

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ARObject":
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
            # Fallback: Use __annotations__ directly if get_type_hints fails
            # This can happen due to circular imports or missing types
            # Note: Annotations will be strings due to 'from __future__ import annotations'
            type_hints = {}
            # Collect annotations from entire MRO
            for base_cls in cls.__mro__:
                if hasattr(base_cls, '__annotations__'):
                    for attr_name, attr_type_str in base_cls.__annotations__.items():
                        if attr_name not in type_hints:
                            # Keep as string - _extract_value will handle it
                            type_hints[attr_name] = attr_type_str

        # Helper function to strip namespace from tag
        def strip_namespace(tag: str) -> str:
            """Strip namespace from XML tag.

            Args:
                tag: XML tag with optional namespace

            Returns:
                Tag without namespace
            """
            if '}' in tag:
                return tag.split('}')[1]
            return tag

        # Strip namespace from element tag for matching
        element_tag_stripped = strip_namespace(element.tag)

        # Process each attribute from type hints
        for attr_name, attr_type in type_hints.items():
            # Convert Python name to XML tag
            xml_tag = NameConverter.to_xml_tag(attr_name)

            # Check if this should be an XML attribute
            if ARObject._is_xml_attribute_static(cls, attr_name):
                value = element.get(xml_tag)
            else:
                # Find child element - try both with and without namespace
                child = element.find(xml_tag)
                if child is None:
                    # Try to find by matching stripped tag names
                    for elem in element:
                        if strip_namespace(elem.tag) == xml_tag:
                            child = elem
                            break

                if child is not None:
                    # Get value based on type
                    value = ARObject._extract_value(child, attr_type)
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
    def _import_class_by_name(class_name: str):
        """Import a class by name from armodel.models.M2.

        Args:
            class_name: Name of the class to import (e.g., "ARPackage")

        Returns:
            The imported class, or None if not found
        """
        import sys
        import importlib

        # Check if already in sys.modules
        for module_name, module in sys.modules.items():
            if module_name.startswith('armodel.models.M2'):
                if hasattr(module, class_name):
                    cls = getattr(module, class_name)
                    if isinstance(cls, type):
                        return cls

        # Try to import from known locations
        # Convert class name to snake_case for filename
        class_filename = class_name.replace('<', '_').replace('>', '_')

        # Common package paths to search
        search_paths = [
            f'armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.{class_name}.{class_filename}',
            f'armodel.models.M2.AUTOSARTemplates.{class_name}.{class_filename}',
            f'armodel.models.M2.MSR.{class_name}.{class_filename}',
        ]

        for module_path in search_paths:
            try:
                module = importlib.import_module(module_path)
                if hasattr(module, class_name):
                    return getattr(module, class_name)
            except (ImportError, ModuleNotFoundError):
                continue

        # Fallback: try searching through all M2 modules
        try:
            from armodel.models.M2 import AUTOSARTemplates, MSR

            # Search in AUTOSARTemplates
            if hasattr(AUTOSARTemplates, '__path__'):
                from pkgutil import walk_packages
                for importer, modname, ispkg in walk_packages(AUTOSARTemplates.__path__, AUTOSARTemplates.__name__ + '.'):
                    try:
                        module = importlib.import_module(modname)
                        if hasattr(module, class_name):
                            cls = getattr(module, class_name)
                            if isinstance(cls, type):
                                return cls
                    except (ImportError, ModuleNotFoundError):
                        continue
        except Exception:
            pass

        return None

    @staticmethod
    def _extract_value(element: ET.Element, attr_type):
        """Extract value from XML element based on type.

        Args:
            element: XML element
            attr_type: Expected type (from type hints) - can be type object or string

        Returns:
            Extracted value
        """
        if element is None:
            return None

        # Handle string type annotations (from __annotations__ with future import)
        if isinstance(attr_type, str):
            # Parse string type annotations like "list[ARPackage]" or "Optional[SomeType]"
            import re

            # Extract list type
            list_match = re.match(r'list\[(.+?)\]', attr_type)
            if list_match:
                inner_type_str = list_match.group(1)
                # Find all direct child elements
                children = list(element)

                # Try to import the class and deserialize
                result = []
                for child in children:
                    # Try to deserialize using the class
                    item_class = ARObject._import_class_by_name(inner_type_str)
                    if item_class and hasattr(item_class, 'deserialize'):
                        item = item_class.deserialize(child)
                        result.append(item)
                    else:
                        # Fallback to text content
                        result.append(child.text if child.text else None)

                return result

            # Handle optional types
            optional_match = re.match(r'Optional\[(.+?)\]', attr_type)
            if optional_match:
                inner_type_str = optional_match.group(1)
                # Try to import and deserialize
                item_class = ARObject._import_class_by_name(inner_type_str)
                if item_class and hasattr(item_class, 'deserialize'):
                    return item_class.deserialize(element)

                # Fallback to text content
                return element.text if element.text else None

            # For simple class names, try to import and deserialize
            item_class = ARObject._import_class_by_name(attr_type)
            if item_class and hasattr(item_class, 'deserialize'):
                return item_class.deserialize(element)

            # For simple string types, just return text
            return element.text if element.text else None

        # Check if it's a list type
        if get_origin(attr_type) is list:
            # Get the element type
            type_args = get_args(attr_type)
            if type_args:
                item_type = type_args[0]

                # Find all direct child elements (not grandchildren)
                children = list(element)

                # Deserialize each child element
                result = []
                for child in children:
                    # For object types, deserialize recursively
                    if hasattr(item_type, 'deserialize'):
                        item = item_type.deserialize(child)
                        result.append(item)
                    else:
                        # For primitives, get text content
                        result.append(child.text if child.text else None)

                return result

        # Check if it's an Optional type
        if get_origin(attr_type) is Union:
            type_args = get_args(attr_type)
            # Get the first non-None type
            for arg in type_args:
                if arg is not type(None):
                    attr_type = arg
                    break

        # For object types with deserialize method, recursively deserialize
        # Check if attr_type is a class (not a primitive type like str, int, etc.)
        if isinstance(attr_type, type) and hasattr(attr_type, 'deserialize'):
            return attr_type.deserialize(element)

        # For primitive types, return text content
        text = element.text
        if text is None:
            return None

        # Simple type conversions for primitives
        if attr_type == str:
            return text
        elif attr_type == int:
            try:
                return int(text)
            except ValueError:
                return text
        elif attr_type == float:
            try:
                return float(text)
            except ValueError:
                return text
        elif attr_type == bool:
            return text.lower() in ('true', '1', 'yes')
        else:
            # Default to string
            return text
'''


def generate_builder_code(type_def: dict) -> str:
    """Generate builder class code from type definition.

    Args:
        type_def: Type definition from mapping.json

    Returns:
        Generated builder code as string
    """
    class_name = type_def["name"]
    builder_name = f"{class_name}Builder"

    # ARObject is instantiated without parentheses
    if class_name == "ARObject":
        obj_init = f"{class_name}"
    else:
        obj_init = f"{class_name}()"

    code = f'''class {builder_name}:
    """Builder for {class_name}."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: {class_name} = {obj_init}

    def build(self) -> {class_name}:
        """Build and return {class_name} object.

        Returns:
            {class_name} instance
        """
        # TODO: Add validation
        return self._obj
'''

    return code


def generate_enum_code(enum_def: dict, json_file_path: str = "") -> str:
    """Generate Python Enum code from enum definition.

    Args:
        enum_def: Enum definition from enum JSON file
        json_file_path: Path to the JSON file containing the enum definition

    Returns:
        Generated Python Enum code as string
    """
    enum_name = enum_def["name"]
    literals = enum_def.get("literals", [])
    sources = enum_def.get("sources", [])

    # Build docstring with PDF references and JSON file path
    docstring_lines = [f"AUTOSAR {enum_name} enumeration."]

    # Add PDF file references if available
    if sources:
        docstring_lines.append("")
        docstring_lines.append("References:")
        for source in sources:
            pdf_file = source.get("pdf_file", "N/A")
            page_number = source.get("page_number", "N/A")
            docstring_lines.append(f"  - {pdf_file} (page {page_number})")

    # Add JSON file path if available
    if json_file_path:
        docstring_lines.append("")
        docstring_lines.append(f"JSON Source: {json_file_path}")

    docstring = "\n".join(docstring_lines)

    # Generate enum code as a class inheriting from AREnum only
    # The serialize() and deserialize() methods are inherited from AREnum
    code = f'''"""{docstring}"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class {enum_name}(AREnum):
    """AUTOSAR {enum_name} enumeration.

    This enum inherits from AREnum, which provides:
    - serialize(): XML serialization
    - deserialize(): XML deserialization with automatic member matching
    - Transparent equality comparison with string values
    """

    def __init__(self, value: str) -> None:
        """Initialize enum member.

        Args:
            value: The enum value as a string
        """
        self._value_ = value

'''

    # Deduplicate literals by name (keep first occurrence)
    seen_names = set()
    duplicates = []
    unique_literals = []

    for literal in literals:
        literal_name = literal["name"]
        if literal_name in seen_names:
            duplicates.append(literal_name)
        else:
            seen_names.add(literal_name)
            unique_literals.append(literal)

    # Warn about duplicates
    if duplicates:
        duplicate_set = set(duplicates)
        code += f'    # Note: {len(duplicate_set)} duplicate literal(s) found and removed: {", ".join(sorted(duplicate_set))}\n'

    # Generate enum members from unique literals
    for literal in unique_literals:
        literal_value = literal["name"]
        # Convert enum member name to UPPER_SNAKE_CASE with underscores between words
        literal_name = to_snake_case(literal_value).upper()
        code += f'    {literal_name} = "{literal_value}"\n'

    return code


def generate_primitive_type_base() -> str:
    """Generate the ARPrimitive base class code.

    Returns:
        Generated Python code as string
    """
    code = '''"""ARPrimitive base class for all AUTOSAR primitive types."""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject

class ARPrimitive(ARObject):
    """Base class for all AUTOSAR primitive types.

    All primitive types (String, Integer, Float, etc.) inherit from this class.
    Provides common functionality for value wrapping and serialization.
    """

    python_type: type = str
    """The underlying Python type for this primitive."""

    def __init__(self) -> None:
        """Initialize ARPrimitive."""
        super().__init__()
        self.value: Optional[Any] = None

    def serialize(self, namespace: str = "") -> ET.Element:
        """Serialize the primitive to an XML element.

        Args:
            namespace: XML namespace URI (optional)

        Returns:
            xml.etree.ElementTree.Element representing this primitive
        """
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        if namespace:
            elem.set("xmlns", namespace)

        if self.value is not None:
            elem.text = str(self.value)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ARPrimitive":
        """Deserialize an XML element to an ARPrimitive instance.

        Automatically converts the text content to the appropriate Python type
        based on the python_type class attribute.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ARPrimitive instance
        """
        obj = cls()
        if element.text:
            # Convert to the appropriate Python type based on python_type
            if cls.python_type is str:
                obj.value = element.text
            elif cls.python_type is int:
                try:
                    obj.value = int(element.text)
                except ValueError:
                    obj.value = element.text  # Keep as string if conversion fails
            elif cls.python_type is float:
                try:
                    obj.value = float(element.text)
                except ValueError:
                    obj.value = element.text
            elif cls.python_type is bool:
                obj.value = element.text.lower() in ('true', '1', 'yes')
            else:
                obj.value = element.text
        return obj

    def __str__(self) -> str:
        """Return string representation of the primitive value."""
        return str(self.value) if self.value is not None else ""

    def __repr__(self) -> str:
        """Return detailed string representation."""
        return f"{self.__class__.__name__}({self.value!r})"
'''
    return code


def generate_enumeration_type_base() -> str:
    """Generate the AREnum base class code.

    Returns:
        Generated Python code as string
    """
    code = '''"""AREnum base class for all AUTOSAR enumeration types."""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject

class AREnum(ARObject):
    """Base class for all AUTOSAR enumeration types.

    All enumeration types inherit from this class.
    Provides common functionality for enum value serialization.
    """

    def __init__(self) -> None:
        """Initialize AREnum."""
        super().__init__()

    def serialize(self, namespace: str = "") -> ET.Element:
        """Serialize the enum to an XML element.

        Args:
            namespace: XML namespace URI (optional)

        Returns:
            xml.etree.ElementTree.Element representing this enum value
        """
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        if namespace:
            elem.set("xmlns", namespace)

        # Get the value from the enum
        if hasattr(self, 'value'):
            elem.text = str(self.value)
        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AREnum":
        """Deserialize an XML element to an AREnum instance.

        This base method should be overridden by concrete enum classes
        to handle matching against specific enum members.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AREnum instance

        Raises:
            ValueError: If element is empty
        """
        if element.text:
            # Fallback: create a custom instance
            # Subclasses should override this to match against their members
            text = element.text.strip()
            obj = cls.__new__(cls)
            object.__setattr__(obj, '_value_', text)
            # Initialize parent class (ARObject)
            super(cls, obj).__init__()
            return obj
        raise ValueError(f"Cannot deserialize {{cls.__name__}} from empty element")

    def __str__(self) -> str:
        """Return string representation of the enum value."""
        return str(self.value) if hasattr(self, 'value') else ""

    def __repr__(self) -> str:
        """Return detailed string representation."""
        return f"{self.__class__.__name__}.{self.name if hasattr(self, 'name') else self.value}"
'''
    return code


def generate_primitive_code(primitive_def: dict, package_data: Dict[str, Dict[str, Any]] = None, json_file_path: str = "") -> str:
    """Generate Python primitive type definition from primitive definition.

    Args:
        primitive_def: Primitive definition from primitive JSON file
        package_data: Package data dictionary for type resolution
        json_file_path: Path to the JSON file containing the primitive definition

    Returns:
        Generated Python code as string
    """
    if package_data is None:
        package_data = {}

    primitive_name = primitive_def["name"]
    note = primitive_def.get("note", "")
    sources = primitive_def.get("sources", [])
    attributes = primitive_def.get("attributes", {})

    # Build docstring with PDF references and JSON file path
    docstring_lines = [f"{primitive_name} AUTOSAR primitive type."]

    # Add PDF file references if available
    if sources:
        docstring_lines.append("")
        docstring_lines.append("References:")
        for source in sources:
            pdf_file = source.get("pdf_file", "N/A")
            page_number = source.get("page_number", "N/A")
            docstring_lines.append(f"  - {pdf_file} (page {page_number})")

    # Add JSON file path if available
    if json_file_path:
        docstring_lines.append("")
        docstring_lines.append(f"JSON Source: {json_file_path}")

    docstring = "\n".join(docstring_lines)

    # Determine Python type mapping
    primitive_type_map = {
        "String": "str",
        "Integer": "int",
        "Float": "float",
        "Boolean": "bool",
        "Numerical": "str",  # Complex numerical representation
        "PositiveInteger": "str",  # Can be hex/octal/binary
        "Limit": "str",  # Special limit representation
        "Ref": "str",  # Reference string
        "CIdentifier": "str",
        "NameToken": "str",
        "Identifier": "str",
        "DateTime": "str",
        "TimeValue": "float",
        "AlignmentType": "str",
        # Add more mappings as needed
    }

    python_type = primitive_type_map.get(primitive_name, "str")

    # Collect imports needed for attributes
    enum_imports = set()
    primitive_imports = set()

    # Process attributes to determine types and imports
    attribute_types = {}
    for attr_name, attr_info in attributes.items():
        attr_type = attr_info["type"]
        multiplicity = attr_info["multiplicity"]

        # Determine Python type for the attribute
        if is_primitive_type(attr_type, package_data):
            attribute_type = get_python_type(attr_type, multiplicity, package_data)
            primitive_imports.add(attr_type)
        elif is_enum_type(attr_type, package_data):
            attribute_type = get_python_type(attr_type, multiplicity, package_data)
            enum_imports.add(attr_type)
        else:
            # Class type
            attribute_type = get_python_type(attr_type, multiplicity, package_data)

        attribute_types[attr_name] = {
            "type": attribute_type,
            "multiplicity": multiplicity,
            "original_type": attr_type,
            "kind": attr_info.get("kind", "attribute")
        }

    # Build imports section
    import_statements = []
    import_statements.append("from __future__ import annotations")
    import_statements.append("from typing import TYPE_CHECKING, Optional")
    import_statements.append("import xml.etree.ElementTree as ET")
    import_statements.append("")
    import_statements.append("from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_primitive import ARPrimitive")

    # Add enum imports
    if enum_imports:
        import_statements.append("")
        # Import each enum from its specific module file to avoid circular imports
        for enum_name in sorted(enum_imports):
            enum_snake_name = to_snake_case(enum_name)
            import_statements.append(f"from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.{enum_snake_name} import (")
            import_statements.append(f"    {enum_name},")
            import_statements.append(")")

    # Add primitive imports
    if primitive_imports:
        import_statements.append("")
        # Import each primitive from its specific module file to avoid circular imports
        for prim_name in sorted(primitive_imports):
            prim_snake_name = to_snake_case(prim_name)
            import_statements.append(f"from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.{prim_snake_name} import (")
            import_statements.append(f"    {prim_name},")
            import_statements.append(")")

    # Generate primitive type code as a class inheriting from ARPrimitive
    # Note: deserialize() is inherited from ARPrimitive base class
    code = f'''"""{docstring}"""

{chr(10).join(import_statements)}

# {note}
class {primitive_name}(ARPrimitive):
    """AUTOSAR {primitive_name} primitive type.

    Inherits deserialize() from ARPrimitive which automatically converts
    XML text content to the appropriate Python type based on python_type.
    """

    python_type: type = {python_type}
    """The underlying Python type for this primitive."""

'''

    # Add class-level type annotations for attributes
    if attribute_types:
        for attr_name, attr_info in attribute_types.items():
            python_name, _ = get_python_identifier(attr_name)
            code += f"    {python_name}: {attr_info['type']}\n"
        code += "\n"

    # Build __init__ signature
    init_params = [f"value: Optional[{python_type}] = None"]
    for attr_name, attr_info in attribute_types.items():
        python_name, _ = get_python_identifier(attr_name)
        init_params.append(f"{python_name}: {attr_info['type']} = None")

    code += f'''    def __init__(self, {', '.join(init_params)}) -> None:
        """Initialize {primitive_name}.

        Args:
            value: The primitive value
'''

    # Add docstring for attribute parameters
    for attr_name, attr_info in attribute_types.items():
        python_name, _ = get_python_identifier(attr_name)
        code += f"            {python_name}: {attr_name}\n"

    code += '''        """
        super().__init__()
        self.value: Optional[{}] = value
'''.format(python_type)

    # Initialize attributes
    if attribute_types:
        for attr_name, attr_info in attribute_types.items():
            python_name, _ = get_python_identifier(attr_name)
            code += f"        self.{python_name}: {attr_info['type']} = {python_name}\n"

    return code
