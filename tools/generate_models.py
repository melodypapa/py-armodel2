#!/usr/bin/env python3
"""Code generator for AUTOSAR model classes, enums, and primitives."""

import argparse
import json
import re
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


def parse_enum_json(enum_file: Path) -> Dict[str, Any]:
    """Parse enum JSON file.

    Args:
        enum_file: Path to enum JSON file

    Returns:
        Parsed JSON data as dictionary
    """
    with open(enum_file, "r", encoding="utf-8") as f:
        return json.load(f)


def parse_primitive_json(primitive_file: Path) -> Dict[str, Any]:
    """Parse primitive JSON file.

    Args:
        primitive_file: Path to primitive JSON file

    Returns:
        Parsed JSON data as dictionary
    """
    with open(primitive_file, "r", encoding="utf-8") as f:
        return json.load(f)


def parse_hierarchy_json(hierarchy_file: Path) -> Dict[str, Dict[str, Any]]:
    """Parse hierarchy.json file to extract class parent and abstract information.

    Args:
        hierarchy_file: Path to hierarchy.json file

    Returns:
        Dictionary mapping class names to their parent and abstract status
    """
    with open(hierarchy_file, "r", encoding="utf-8") as f:
        hierarchy_content = f.read()

    # Extract the hierarchy structure
    lines = hierarchy_content.split("\n")

    # Find classes and their parent/abstract status
    class_info: Dict[str, Dict[str, Any]] = {}
    indent_stack = []

    for line in lines:
        if line.startswith("## Class Hierarchy"):
            continue
        if not line.strip():
            continue

        # Count indentation
        indent = len(line) - len(line.lstrip())
        line = line.strip()

        # Check for abstract marker
        is_abstract = "(abstract)" in line

        # Extract class name
        class_name = line.replace("(abstract)", "").replace("*", "").strip()

        # Determine parent based on indentation
        while indent_stack and indent_stack[-1][0] >= indent:
            indent_stack.pop()

        if indent_stack:
            parent = indent_stack[-1][1]
        else:
            parent = None

        # Store class info
        if class_name:
            class_info[class_name] = {"parent": parent, "is_abstract": is_abstract}
            indent_stack.append((indent, class_name))

    return class_info


def create_directory_structure(
    types: list, output_dir: Path, package_data: Dict[str, Dict[str, Any]]
) -> None:
    """Create directory structure from package paths.

    Args:
        types: List of type definitions from mapping.json
        output_dir: Base directory for generated files
        package_data: Dictionary with package data including primitive types

    Returns:
        None
    """
    # Extract all unique package paths
    package_paths = set()
    for type_def in types:
        package_path = type_def.get("package_path", "")
        if package_path:
            package_paths.add(package_path)

    # Also add package paths from package_data (for primitives and enums)
    for package_path in package_data.keys():
        if package_path:
            package_paths.add(package_path)

    # Create directories for each unique package path
    for package_path in sorted(package_paths):
        # Convert package path to directory path
        dir_path = output_dir / package_path.replace("::", "/")

        # Create directory
        dir_path.mkdir(parents=True, exist_ok=True)

        # Generate __init__.py content with proper docstring
        package_name = package_path.split("::")[-1] if "::" in package_path else package_path
        init_content = f'''"""{package_name} module."""

from __future__ import annotations
from typing import TYPE_CHECKING

'''

        # Collect all exports for __all__
        exports = []

        # Check if this package has primitive types and export them
        if package_path in package_data and "primitives" in package_data[package_path]:
            primitives = package_data[package_path]["primitives"]
            if primitives:
                # Generate imports for individual primitive types using absolute paths
                # Use block import format as required by DESIGN_RULE_041
                for prim in primitives:
                    prim_name = prim["name"]
                    # Convert package path to absolute import path
                    python_path = package_path.replace("::", ".")
                    module_path = f"armodel.models.{python_path}.{to_snake_case(prim_name)}"
                    init_content += f"from {module_path} import (\n    {prim_name},\n)\n"
                    exports.append(prim_name)
                init_content += "\n"

        # Check if this package has classes and export them
        # Use TYPE_CHECKING to avoid circular imports
        if package_path in package_data and "classes" in package_data[package_path]:
            classes = package_data[package_path]["classes"]
            if classes:
                init_content += "if TYPE_CHECKING:\n"
                # Generate imports for individual classes using absolute paths
                # Use block import format as required by DESIGN_RULE_041
                for cls in classes:
                    class_name = cls["name"]
                    # Convert package path to absolute import path
                    python_path = package_path.replace("::", ".")
                    module_path = f"armodel.models.{python_path}.{to_snake_case(class_name)}"
                    init_content += f"    from {module_path} import (\n        {class_name},\n    )\n"
                    exports.append(class_name)
                init_content += "\n"

        # Check if this package has enums and export them
        if package_path in package_data and "enumerations" in package_data[package_path]:
            enums = package_data[package_path]["enumerations"]
            if enums:
                # Generate imports for individual enums using absolute paths
                # Use block import format as required by DESIGN_RULE_041
                for enum in enums:
                    enum_name = enum["name"]
                    # Convert package path to absolute import path
                    python_path = package_path.replace("::", ".")
                    module_path = f"armodel.models.{python_path}.{to_snake_case(enum_name)}"
                    init_content += f"from {module_path} import (\n    {enum_name},\n)\n"
                    exports.append(enum_name)
                init_content += "\n"

        # Add __all__ definition with alphabetically sorted exports
        if exports:
            init_content += "__all__ = [\n"
            for export in sorted(exports):
                init_content += f'    "{export}",\n'
            init_content += "]\n"

        # Write __init__.py
        init_file = dir_path / "__init__.py"
        with open(init_file, "w", encoding="utf-8") as f:
            f.write(init_content)

    # Create __init__.py for each level to ensure proper package structure
    # Every __init__.py must define __all__ as required by DESIGN_RULE_041
    for init_path in sorted(output_dir.rglob("__init__.py"), reverse=True):
        if init_path.parent != output_dir:
            # Ensure parent packages have __init__.py with __all__ definition
            parent_init = init_path.parent.parent / "__init__.py"
            if not parent_init.exists():
                parent_path_parts = init_path.parent.relative_to(output_dir).parts
                parent_name = parent_path_parts[-2] if len(parent_path_parts) >= 2 else "armodel"
                # Collect subpackages to export
                subpackages = []
                for item in init_path.parent.iterdir():
                    if item.is_dir() and (item / "__init__.py").exists():
                        subpackages.append(item.name)
                # Generate __init__.py with __all__ definition
                # Note: Parent packages just define __all__ without wildcard imports
                # as required by DESIGN_RULE_041 (avoid wildcard imports)
                init_content = f'"""{parent_name} module."""\n'
                if subpackages:
                    init_content += "\n"
                    init_content += "__all__ = [\n"
                    for subpkg in sorted(subpackages):
                        init_content += f'    "{subpkg}",\n'
                    init_content += "]\n"
                parent_init.write_text(init_content)


def generate_class_code(
    type_def: dict,
    hierarchy_info: Dict[str, Dict[str, Any]],
    package_data: Dict[str, Dict[str, Any]],
    include_members: bool = False,
    json_file_path: str = "",
    dependency_graph: Dict[str, set] = None,
) -> str:
    """Generate Python class code from type definition.

    Args:
        type_def: Type definition from mapping.json
        hierarchy_info: Dictionary with parent and abstract information from hierarchy.json
        package_data: Dictionary with package data including class attributes
        include_members: Whether to include member lists from package definitions
        json_file_path: Path to the JSON file containing the class definition
        dependency_graph: Complete dependency graph for circular import detection

    Returns:
        Generated Python code as string
    """
    if dependency_graph is None:
        dependency_graph = {}
    class_name = type_def["name"]
    is_splitable = type_def.get("splitable", False)
    split_file_name = type_def.get("split_file_name", "")
    package_path = type_def.get("package_path", "")

    # Get parent and abstract status from hierarchy
    parent_class = None
    is_abstract = False

    if class_name in hierarchy_info:
        parent_class = hierarchy_info[class_name]["parent"]
        is_abstract = hierarchy_info[class_name]["is_abstract"]

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
                    # Check for circular import
                    if detect_circular_import(class_name, import_type, package_data, dependency_graph):
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

    # Generate class definition with parent or empty parentheses for ARObject
    if parent_class:
        code += f'''

class {class_name}({parent_class}):
    """AUTOSAR {class_name}."""
'''
    else:
        code += f'''

class {class_name}:
    """AUTOSAR {class_name}."""
'''

    # Add abstract marker if needed
    if is_abstract:
        code += '''    """Abstract base class - do not instantiate directly."""

'''
    else:
        code += """
"""

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
        """Initialize {class_name}."""
'''

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
        code += '''
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
    def deserialize(cls, element: ET.Element) -> ARObject:
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
            except (ImportError, ModuleError):
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
                    except (ImportError, ModuleError):
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
    else:
        # Other classes inherit serialize/deserialize from ARObject
        # No need to generate these methods - they're inherited!
        pass

    return code


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

    # Generate enum code
    code = f'''"""{docstring}"""

from enum import Enum


class {enum_name}(Enum):
    """AUTOSAR {enum_name} enumeration."""

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
        literal_name = literal["name"].upper()
        literal_value = literal["name"]
        code += f'    {literal_name} = "{literal_value}"\n'

    return code


def generate_primitive_code(primitive_def: dict, json_file_path: str = "") -> str:
    """Generate Python primitive type definition from primitive definition.

    Args:
        primitive_def: Primitive definition from primitive JSON file
        json_file_path: Path to the JSON file containing the primitive definition

    Returns:
        Generated Python code as string
    """
    primitive_name = primitive_def["name"]
    note = primitive_def.get("note", "")
    sources = primitive_def.get("sources", [])

    # Build docstring with PDF references and JSON file path
    docstring_lines = [f"{primitive_name} primitive type."]

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

    # Generate primitive type code
    code = f'''"""{docstring}"""

# {note}
{primitive_name} = {python_type}
'''

    return code


def to_snake_case(name: str) -> str:
    """Convert CamelCase to snake_case.

    Args:
        name: CamelCase string

    Returns:
        snake_case string
    """
    s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower()


def get_python_identifier(name: str) -> tuple[str, str]:
    """Convert a name to a valid Python identifier, handling keywords.

    Args:
        name: Name to convert (e.g., AUTOSAR attribute name)

    Returns:
        Tuple of (python_identifier, xml_tag_name)
        - python_identifier: Valid Python identifier (with underscore appended if keyword)
        - xml_tag_name: XML tag name to use (None if same as identifier, otherwise uppercase form)

    Examples:
        "shortName" -> ("short_name", None)
        "class" -> ("class_", "CLASS")
        "from" -> ("from_", "FROM")
    """
    # Python keywords that cannot be used as attribute names
    python_keywords = {
        "False",
        "None",
        "True",
        "and",
        "as",
        "assert",
        "async",
        "await",
        "break",
        "class",
        "continue",
        "def",
        "del",
        "elif",
        "else",
        "except",
        "finally",
        "for",
        "from",
        "global",
        "if",
        "import",
        "in",
        "is",
        "lambda",
        "nonlocal",
        "not",
        "or",
        "pass",
        "raise",
        "return",
        "try",
        "while",
        "with",
        "yield",
    }

    snake_name = to_snake_case(name)

    # Check if the name is a Python keyword
    if snake_name in python_keywords:
        # Append underscore and use uppercase original as XML tag
        return f"{snake_name}_", name.upper()
    else:
        # Not a keyword, use as-is
        return snake_name, None


def is_primitive_type(type_name: str, package_data: Dict[str, Dict[str, Any]]) -> bool:
    """Check if a type is a primitive type.

    Args:
        type_name: Name of the type to check
        package_data: Package data dictionary

    Returns:
        True if the type is a primitive, False otherwise
    """
    # Check in all packages
    for package_path, data in package_data.items():
        if "primitives" in data:
            for prim in data["primitives"]:
                if prim["name"] == type_name:
                    return True
    return False


def is_enum_type(type_name: str, package_data: Dict[str, Dict[str, Any]]) -> bool:
    """Check if a type is an enum type.

    Args:
        type_name: Name of the type to check
        package_data: Package data dictionary

    Returns:
        True if the type is an enum, False otherwise
    """
    # Check in all packages
    for package_path, data in package_data.items():
        if "enumerations" in data:
            for enum in data["enumerations"]:
                if enum["name"] == type_name:
                    return True
    return False


def get_python_type(
    type_name: str, multiplicity: str, package_data: Dict[str, Dict[str, Any]]
) -> str:
    """Get Python type annotation for AUTOSAR type.

    Args:
        type_name: AUTOSAR type name
        multiplicity: Multiplicity (e.g., "0..1", "*", "1")
        package_data: Package data dictionary

    Returns:
        Python type annotation string
    """
    # Check if type_name matches "any (xxx)" pattern and convert to Any
    if type_name.startswith("any ("):
        # This is a polymorphic type that can be any type implementing the interface
        # Convert to Any in Python
        type_name = "Any"

    # Check if it's a primitive type
    if is_primitive_type(type_name, package_data):
        # Use AUTOSAR primitive type names directly instead of Python types
        # The primitive types are imported from PrimitiveTypes module

        # Apply multiplicity
        # For primitive types:
        # - multiplicity 0..1: Use Optional[PrimitiveType] and initialize with None
        # - multiplicity *: Use list[PrimitiveType] and initialize with []
        # - multiplicity 1: Use PrimitiveType and initialize with None (primitive types are nullable)
        if multiplicity == "0..1":
            return f"Optional[{type_name}]"
        elif multiplicity == "*":
            return f"list[{type_name}]"
        elif multiplicity == "1":
            return type_name
        else:
            return type_name
    elif type_name == "Any":
        # Handle the Any type specifically
        if multiplicity == "0..1":
            return "Optional[Any]"
        elif multiplicity == "*":
            return "list[Any]"
        elif multiplicity == "1":
            return "Any"
        else:
            return "Any"
    else:
        # It's a class type
        # Apply multiplicity
        # For class types:
        # - multiplicity 0..1: Use Optional[type_name] and initialize with None
        # - multiplicity *: Use list[type_name] and initialize with []
        # - multiplicity 1: Use type_name and initialize with None (class types can be nullable)
        if multiplicity == "0..1":
            return f"Optional[{type_name}]"
        elif multiplicity == "*":
            return f"list[{type_name}]"
        elif multiplicity == "1":
            return type_name
        else:
            return type_name


def get_type_import_path(type_name: str, package_data: Dict[str, Dict[str, Any]]) -> str:
    """Get Python import path for a class type.

    Args:
        type_name: Name of the class type
        package_data: Package data dictionary

    Returns:
        Python import statement or empty string if not found
    """
    # Search for the type in all packages
    for package_path, data in package_data.items():
        if "classes" in data:
            for cls in data["classes"]:
                if cls["name"] == type_name:
                    # Use the package field from the class itself to ensure correct directory structure
                    # This is important because some classes have different directory names than expected
                    # (e.g., ARObject is in ArObject directory, not ar_object)
                    class_package_path = cls.get("package", package_path)
                    
                    # Convert package path to Python import path
                    # Package path format: M2::AUTOSARTemplates::...
                    # Python import path: armodel.models.M2.AUTOSARTemplates...
                    # Import from the specific class file, not module
                    python_path = class_package_path.replace("::", ".")

                    # Return import path in format: from armodel.models.M2.MSR.AsamHdo.AdminData.admin_data import (\n    AdminData,\n)
                    # Use block import format as required by DESIGN_RULE_041
                    class_filename = to_snake_case(type_name)
                    module_path = f"armodel.models.{python_path}.{class_filename}"

                    return f"from {module_path} import (\n    {type_name},\n)"
    return ""


def get_type_package_path(type_name: str, package_data: Dict[str, Dict[str, Any]]) -> str:
    """Get the package path for a class type.

    Args:
        type_name: Name of the class type
        package_data: Package data dictionary

    Returns:
        Package path string or empty string if not found
    """
    for package_path, data in package_data.items():
        if "classes" in data:
            for cls in data["classes"]:
                if cls["name"] == type_name:
                    class_package_path = cls.get("package", package_path)
                    return class_package_path
    return ""


def build_complete_dependency_graph(package_data: Dict[str, Dict[str, Any]]) -> Dict[str, set]:
    """Build a complete dependency graph for all classes.

    Args:
        package_data: Package data dictionary

    Returns:
        Dictionary mapping class names to their dependencies
    """
    dependency_graph = {}
    
    # Initialize all classes with empty dependency sets
    for package_path, data in package_data.items():
        if "classes" in data:
            for cls in data["classes"]:
                class_name = cls["name"]
                dependency_graph[class_name] = set()
                
                # Collect class-type dependencies from attributes
                if "attributes" in cls:
                    for attr_name, attr_info in cls["attributes"].items():
                        attr_type = attr_info["type"]
                        
                        # Skip primitives, enums, "any" types, and self-references
                        if (is_primitive_type(attr_type, package_data) or 
                            is_enum_type(attr_type, package_data) or 
                            attr_type.startswith("any (") or
                            attr_type == class_name):
                            continue
                        
                        # Add to dependencies
                        dependency_graph[class_name].add(attr_type)
    
    return dependency_graph


def detect_circular_import(
    current_class: str,
    attribute_type: str,
    package_data: Dict[str, Dict[str, Any]],
    dependency_graph: Dict[str, set],
) -> bool:
    """Detect if importing attribute_type would cause a circular import.

    Args:
        current_class: Name of the current class being generated
        attribute_type: Name of the attribute type to import
        package_data: Package data dictionary
        dependency_graph: Graph of class dependencies (complete graph)

    Returns:
        True if circular import detected, False otherwise
    """
    # If current_class is attribute_type, it's a self-reference
    if current_class == attribute_type:
        return True
    
    # Check if attribute_type is in dependency graph
    if attribute_type not in dependency_graph:
        return False
    
    # Check if current_class is in the dependency chain of attribute_type
    # Use depth-first search to detect cycles
    visited = set()
    to_visit = [attribute_type]
    
    while to_visit:
        node = to_visit.pop()
        if node == current_class:
            return True
        if node in visited:
            continue
        visited.add(node)
        
        # Add dependencies of this node
        if node in dependency_graph:
            to_visit.extend(dependency_graph[node] - visited)
    
    return False


def load_all_package_data(packages_dir: Path) -> Dict[str, Dict[str, Any]]:
    """Load all package JSON files.

    Args:
        packages_dir: Directory containing package JSON files

    Returns:
        Dictionary mapping package paths to package data
    """
    package_data = {}

    # Load all .classes.json files
    for class_file in packages_dir.rglob("*.classes.json"):
        try:
            with open(class_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                package_path = data.get("package", "")
                if package_path:
                    package_data[package_path] = data
        except Exception:
            pass

    # Load all .primitives.json files
    for primitive_file in packages_dir.rglob("*.primitives.json"):
        try:
            with open(primitive_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                package_path = data.get("package", "")
                if package_path:
                    # Add primitives to existing package data or create new entry
                    if package_path in package_data:
                        package_data[package_path]["primitives"] = data.get("primitives", [])
                    else:
                        package_data[package_path] = {"primitives": data.get("primitives", [])}
        except Exception:
            pass

    # Load all .enums.json files
    for enum_file in packages_dir.rglob("*.enums.json"):
        try:
            with open(enum_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                package_path = data.get("package", "")
                if package_path:
                    # Add enumerations to existing package data or create new entry
                    if package_path in package_data:
                        package_data[package_path]["enumerations"] = data.get("enumerations", [])
                    else:
                        package_data[package_path] = {"enumerations": data.get("enumerations", [])}
        except Exception:
            pass

    return package_data


def generate_all_models(
    mapping_file: Path,
    hierarchy_file: Path,
    output_dir: Path,
    generate_classes: bool = True,
    generate_enums: bool = True,
    generate_primitives: bool = True,
    include_members: bool = False,
) -> None:
    """Generate all model classes, enums, and primitives from JSON definitions.

    Args:
        mapping_file: Path to mapping.json
        hierarchy_file: Path to hierarchy.json
        output_dir: Output directory for generated files
        generate_classes: Whether to generate class files
        generate_enums: Whether to generate enum files
        generate_primitives: Whether to generate primitive files
        include_members: Whether to include member lists from package definitions
    """
    total_generated = 0

    # Parse hierarchy.json for parent and abstract information
    hierarchy_info = parse_hierarchy_json(hierarchy_file)

    # Load all package data for member generation
    packages_dir = mapping_file.parent / "packages"
    package_data = load_all_package_data(packages_dir) if include_members else {}

    if generate_classes:
        # Generate classes from mapping.json
        data = parse_mapping_json(mapping_file)
        types = data.get("types", [])

        # Create directory structure
        create_directory_structure(types, output_dir, package_data)

        # Build complete dependency graph for circular import detection
        dependency_graph = build_complete_dependency_graph(package_data) if include_members else {}

        # Create a mapping of class names to their JSON file paths
        class_json_file_map = {}
        for package_path, package_info in package_data.items():
            if "classes" in package_info:
                json_file_path = str(packages_dir / f"{package_path.replace('::', '_')}.classes.json")
                for cls in package_info["classes"]:
                    class_json_file_map[cls["name"]] = json_file_path

        # Generate each class
        for type_def in types:
            if type_def.get("type") != "Class":
                continue

            class_name = type_def["name"]
            package_path = type_def.get("package_path", "")

            # Get the JSON file path for this class
            json_file_path = class_json_file_map.get(class_name, "")

            # Convert package path to file path
            dir_path = output_dir / package_path.replace("::", "/")
            filename = dir_path / f"{to_snake_case(class_name)}.py"

            # Generate class code
            class_code = generate_class_code(
                type_def, hierarchy_info, package_data, include_members, json_file_path, dependency_graph
            )
            builder_code = generate_builder_code(type_def)

            # Write to file
            full_code = class_code + "\n\n" + builder_code
            filename.write_text(full_code)
            total_generated += 1

        print(f"Generated {len([t for t in types if t.get('type') == 'Class'])} model classes")

    if generate_enums:
        # Generate enums from enum JSON files in packages directory
        enum_files = list(packages_dir.rglob("*.enums.json"))
        total_enums = 0
        for enum_file in enum_files:
            enum_data = parse_enum_json(enum_file)
            package_path = enum_data.get("package", "")

            # Convert package path to file path
            dir_path = output_dir / package_path.replace("::", "/")
            dir_path.mkdir(parents=True, exist_ok=True)

            # Generate each enum
            for enum_def in enum_data.get("enumerations", []):
                enum_name = enum_def["name"]
                filename = dir_path / f"{to_snake_case(enum_name)}.py"

                # Generate enum code with JSON file path
                json_file_path = f"packages/{enum_file.name}"
                enum_code = generate_enum_code(enum_def, json_file_path)

                # Write to file
                filename.write_text(enum_code)
                total_generated += 1
                total_enums += 1

        print(f"Generated {len(enum_files)} enum files with {total_enums} enums")

    if generate_primitives:
        # Generate primitives from primitive JSON files in packages directory
        primitive_files = list(packages_dir.rglob("*.primitives.json"))
        total_primitives = 0
        for primitive_file in primitive_files:
            primitive_data = parse_primitive_json(primitive_file)
            package_path = primitive_data.get("package", "")

            # Convert package path to file path
            dir_path = output_dir / package_path.replace("::", "/")
            dir_path.mkdir(parents=True, exist_ok=True)

            # Generate each primitive
            for primitive_def in primitive_data.get("primitives", []):
                primitive_name = primitive_def["name"]
                filename = dir_path / f"{to_snake_case(primitive_name)}.py"

                # Generate primitive code with JSON file path
                json_file_path = f"packages/{primitive_file.name}"
                primitive_code = generate_primitive_code(primitive_def, json_file_path)

                # Write to file
                filename.write_text(primitive_code)
                total_generated += 1
                total_primitives += 1

        print(
            f"Generated {len(primitive_files)} primitive files with {total_primitives} primitives"
        )

    print(f"Total generated files: {total_generated} in {output_dir}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate AUTOSAR model classes, enums, and primitives from JSON definitions"
    )
    parser.add_argument("mapping_file", type=Path, help="Path to mapping.json file")
    parser.add_argument("hierarchy_file", type=Path, help="Path to hierarchy.json file")
    parser.add_argument("output_dir", type=Path, help="Output directory for generated files")
    parser.add_argument(
        "--classes", action="store_true", default=True, help="Generate class files (default: True)"
    )
    parser.add_argument(
        "--no-classes", action="store_false", dest="classes", help="Skip class file generation"
    )
    parser.add_argument(
        "--enums", action="store_true", default=True, help="Generate enum files (default: True)"
    )
    parser.add_argument(
        "--no-enums", action="store_false", dest="enums", help="Skip enum file generation"
    )
    parser.add_argument(
        "--primitives",
        action="store_true",
        default=True,
        help="Generate primitive files (default: True)",
    )
    parser.add_argument(
        "--no-primitives",
        action="store_false",
        dest="primitives",
        help="Skip primitive file generation",
    )
    parser.add_argument(
        "--members",
        action="store_true",
        default=False,
        help="Include member lists from package definitions",
    )
    parser.add_argument(
        "--no-members", action="store_false", dest="members", help="Skip member list generation"
    )

    args = parser.parse_args()

    # Generate models
    generate_all_models(
        mapping_file=args.mapping_file,
        hierarchy_file=args.hierarchy_file,
        output_dir=args.output_dir,
        generate_classes=args.classes,
        generate_enums=args.enums,
        generate_primitives=args.primitives,
        include_members=args.members,
    )
