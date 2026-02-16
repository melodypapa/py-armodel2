#!/usr/bin/env python3
"""Code generator for AUTOSAR model classes, enums, and primitives."""

import argparse
import json
import re
from pathlib import Path
from typing import Dict, Any


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
    lines = hierarchy_content.split('\n')

    # Find classes and their parent/abstract status
    class_info: Dict[str, Dict[str, Any]] = {}
    indent_stack = []

    for line in lines:
        if line.startswith('## Class Hierarchy'):
            continue
        if not line.strip():
            continue

        # Count indentation
        indent = len(line) - len(line.lstrip())
        line = line.strip()

        # Check for abstract marker
        is_abstract = '(abstract)' in line

        # Extract class name
        class_name = line.replace('(abstract)', '').replace('*', '').strip()

        # Determine parent based on indentation
        while indent_stack and indent_stack[-1][0] >= indent:
            indent_stack.pop()

        if indent_stack:
            parent = indent_stack[-1][1]
        else:
            parent = None

        # Store class info
        if class_name:
            class_info[class_name] = {
                'parent': parent,
                'is_abstract': is_abstract
            }
            indent_stack.append((indent, class_name))

    return class_info


def create_directory_structure(types: list, output_dir: Path, package_data: Dict[str, Dict[str, Any]]) -> None:
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
        init_content = f'"""{package_name} module."""\n'

        # Check if this package has primitive types and export them
        if package_path in package_data and 'primitives' in package_data[package_path]:
            primitives = package_data[package_path]['primitives']
            if primitives:
                # Generate imports for individual primitive types
                for prim in primitives:
                    prim_name = prim['name']
                    init_content += f'from .{to_snake_case(prim_name)} import {prim_name}\n'
                init_content += '\n'

        # Check if this package has classes and export them
        if package_path in package_data and 'classes' in package_data[package_path]:
            classes = package_data[package_path]['classes']
            if classes:
                # Generate imports for individual classes
                for cls in classes:
                    class_name = cls['name']
                    init_content += f'from .{to_snake_case(class_name)} import {class_name}\n'
                init_content += '\n'

        # Check if this package has enums and export them
        if package_path in package_data and 'enumerations' in package_data[package_path]:
            enums = package_data[package_path]['enumerations']
            if enums:
                # Generate imports for individual enums
                for enum in enums:
                    enum_name = enum['name']
                    init_content += f'from .{to_snake_case(enum_name)} import {enum_name}\n'
                init_content += '\n'

        # Write __init__.py
        init_file = dir_path / "__init__.py"
        with open(init_file, "w", encoding="utf-8") as f:
            f.write(init_content)

    # Create __init__.py for each level to ensure proper package structure
    for init_path in sorted(output_dir.rglob("__init__.py"), reverse=True):
        if init_path.parent != output_dir:
            # Ensure parent packages have __init__.py
            parent_init = init_path.parent.parent / "__init__.py"
            if not parent_init.exists():
                parent_path_parts = init_path.parent.relative_to(output_dir).parts
                parent_name = parent_path_parts[-2] if len(parent_path_parts) >= 2 else "armodel"
                parent_init.write_text(f'"""{parent_name} module."""\n')


def generate_class_code(
    type_def: dict,
    hierarchy_info: Dict[str, Dict[str, Any]],
    package_data: Dict[str, Dict[str, Any]],
    include_members: bool = False,
) -> str:
    """Generate Python class code from type definition.

    Args:
        type_def: Type definition from mapping.json
        hierarchy_info: Dictionary with parent and abstract information from hierarchy.json
        package_data: Dictionary with package data including class attributes
        include_members: Whether to include member lists from package definitions

    Returns:
        Generated Python code as string
    """
    class_name = type_def["name"]
    is_splitable = type_def.get("splitable", False)
    split_file_name = type_def.get("split_file_name", "")
    package_path = type_def.get("package_path", "")

    # Get parent and abstract status from hierarchy
    parent_class = None
    is_abstract = False

    if class_name in hierarchy_info:
        parent_class = hierarchy_info[class_name]['parent']
        is_abstract = hierarchy_info[class_name]['is_abstract']

    # Ensure ARObject is not the parent of itself
    # Default to ARObject only if class_name is not "ARObject" and no parent found
    if not parent_class and class_name != "ARObject":
        parent_class = "ARObject"
    elif parent_class == "ARObject" and class_name == "ARObject":
        # Prevent ARObject from being its own parent
        parent_class = None

    # Generate class code
    # For ARObject, we need TYPE_CHECKING import for XMLMember type hint
    if class_name == "ARObject":
        type_checking_import = "from typing import TYPE_CHECKING, Optional, Union\n"
        base_import = "import xml.etree.ElementTree as ET\n"
        code = f'''"""{class_name} AUTOSAR element."""

{type_checking_import}{base_import}

if TYPE_CHECKING:
    from armodel.serialization.metadata import XMLMember
'''
    else:
        # For other classes, add Optional import and XMLMember
        basic_import = "from typing import Optional\n"
        base_import = "import xml.etree.ElementTree as ET\n"
        xmlmember_import = "from armodel.serialization import XMLMember\n"
        code = f'''"""{class_name} AUTOSAR element."""

{basic_import}{base_import}{xmlmember_import}
'''

    # Add parent class import
    if parent_class and parent_class != "ARObject":
        # Find parent class path from hierarchy or mapping
        parent_import = get_type_import_path(parent_class, package_data)
        if parent_import:
            code += f'{parent_import}\n'
        else:
            # Fallback to ARObject import
            code += 'from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject\n'
    else:
        code += 'from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject\n'

    # Collect attribute types for imports
    attribute_types = {}
    if include_members and package_path in package_data:
        class_info = package_data[package_path].get('classes', [])
        for cls in class_info:
            if cls['name'] == class_name and 'attributes' in cls:
                for attr_name, attr_info in cls['attributes'].items():
                    attr_type = attr_info['type']
                    multiplicity = attr_info['multiplicity']
                    attribute_types[attr_name] = {
                        'type': attr_type,
                        'multiplicity': multiplicity
                    }
                break

    # Add type imports if needed
    if attribute_types:
        type_imports = set()
        primitive_imports = set()

        for attr_name, attr_info in attribute_types.items():
            attr_type = attr_info['type']
            # Import class types and primitive types
            if is_primitive_type(attr_type, package_data):
                primitive_imports.add(attr_type)
            elif not attr_type.startswith("any ("):
                # Import class types (skip polymorphic "any (xxx)" types)
                type_imports.add(attr_type)

        # Add import statements for primitive types
        if primitive_imports:
            code += 'from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (\n'
            for i, prim in enumerate(sorted(primitive_imports)):
                if i == len(primitive_imports) - 1:
                    code += f'    {prim},\n'
                else:
                    code += f'    {prim},\n'
            code += ')\n'

        # Add import statements for class types
        # Track already-added imports to prevent duplicates
        added_imports = set()
        if type_imports:
            for import_type in sorted(type_imports):
                import_path = get_type_import_path(import_type, package_data)
                if import_path and import_path not in added_imports:
                    code += f'{import_path}\n'
                    added_imports.add(import_path)

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
        code += '''
'''

    if is_splitable:
        code += f'''    is_splitable = True
    split_file_name = "{split_file_name}"

'''

    # Add _xml_members class attribute BEFORE __init__
    # This defines the member-to-XML mapping for this class only (not inherited)
    # Using new XMLMember dict format for declarative metadata
    code += '''    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
'''
    if attribute_types:
        for attr_name, attr_info in attribute_types.items():
            attr_type = attr_info['type']
            multiplicity = attr_info['multiplicity']

            # Determine if it's a list
            is_list = multiplicity in ('*', '0..*', '1..*')

            # Determine multiplicity string
            if multiplicity in ('*', '0..*'):
                multiplicity_str = "*"
            elif multiplicity == '1..*':
                multiplicity_str = "1..*"
            elif multiplicity in ('0..1', '1'):
                multiplicity_str = multiplicity
            else:
                multiplicity_str = "*" if is_list else "0..1"

            # Determine if it should be an attribute (simple types can be attributes)
            # For now, we'll assume single primitives can be attributes, lists are elements
            is_attribute = not is_list and is_primitive_type(attr_type, package_data)

            # Get element class for child elements (non-primitives)
            element_class = attr_type if not is_primitive_type(attr_type, package_data) else None

            # Get Python identifier and XML tag (handles Python keywords)
            python_name, xml_tag_override = get_python_identifier(attr_name)

            # Generate the XMLMember entry
            code += f'        "{python_name}": XMLMember(\n'
            code += f'            xml_tag={repr(xml_tag_override)},\n'
            code += f'            is_attribute={str(is_attribute)},\n'
            code += f'            multiplicity="{multiplicity_str}",\n'

            if element_class:
                code += f'            element_class={element_class},\n'

            # Add xml_name_override if tag was modified for Python keyword
            if xml_tag_override and xml_tag_override != python_name.replace('_', '-').upper():
                # The original tag name was preserved, it's a Python keyword escape
                # We need to pass the original XML tag
                code += f'            xml_name_override={repr(xml_tag_override)},\n'

            code += f'        ),  # {attr_name}\n'

    code += '''    }

'''

    code += f'''    def __init__(self) -> None:
        """Initialize {class_name}."""
'''

    # Add super().__init__() call for all classes except ARObject
    if class_name != "ARObject":
        code += '''        super().__init__()
'''

    # Add member attributes if requested
    if attribute_types:
        for attr_name, attr_info in attribute_types.items():
            attr_type = attr_info['type']
            multiplicity = attr_info['multiplicity']

            # Determine Python type
            python_type = get_python_type(attr_type, multiplicity, package_data)

            # Determine initial value based on type
            # Optional types initialize with None
            # list types initialize with []
            # Non-optional types initialize with None
            if python_type.startswith('Optional['):
                initial_value = 'None'
            elif python_type.startswith('list['):
                initial_value = '[]'
            else:
                initial_value = 'None'

            # Get Python identifier (handles Python keywords)
            python_name, _ = get_python_identifier(attr_name)
            attr_code = f'        self.{python_name}: {python_type} = {initial_value}\n'
            code += attr_code

    # Add serialize/deserialize methods
    # Special handling for ARObject which implements the base pattern
    # All other classes inherit serialize/deserialize from ARObject
    if class_name == "ARObject":
        # ARObject uses the new registry-based serialization framework
        # It already has serialize/deserialize methods that delegate to the registry
        # Just add a helper method for backward compatibility
        code += '''
    @staticmethod
    def _member_to_xml_tag(member_name: str) -> str:
        """Convert Python member name to XML tag name.

        Args:
            member_name: Python attribute name (snake_case)

        Returns:
            XML tag name (UPPER-CASE with hyphens)

        Examples:
            short_name -> SHORT-NAME
            category -> CATEGORY
        """
        return member_name.replace('_', '-').upper()
'''
    else:
        # Other classes inherit serialize/deserialize from ARObject
        # No need to generate these methods anymore - they're handled by the framework!
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


def generate_enum_code(enum_def: dict) -> str:
    """Generate Python Enum code from enum definition.

    Args:
        enum_def: Enum definition from enum JSON file

    Returns:
        Generated Python Enum code as string
    """
    enum_name = enum_def["name"]
    literals = enum_def.get("literals", [])

    # Generate enum code
    code = f'''"""{enum_name} enumeration."""

from enum import Enum


class {enum_name}(Enum):
    """AUTOSAR {enum_name} enumeration."""

'''

    for literal in literals:
        literal_name = literal["name"].upper()
        literal_value = literal["name"]
        code += f'    {literal_name} = "{literal_value}"\n'

    return code


def generate_primitive_code(primitive_def: dict) -> str:
    """Generate Python primitive type definition from primitive definition.

    Args:
        primitive_def: Primitive definition from primitive JSON file

    Returns:
        Generated Python code as string
    """
    primitive_name = primitive_def["name"]
    note = primitive_def.get("note", "")

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
    code = f'''"""{primitive_name} primitive type."""

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
        'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
        'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
        'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
        'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while',
        'with', 'yield'
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
        if 'primitives' in data:
            for prim in data['primitives']:
                if prim['name'] == type_name:
                    return True
    return False


def get_python_type(type_name: str, multiplicity: str, package_data: Dict[str, Dict[str, Any]]) -> str:
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
        if multiplicity == '0..1':
            return f'Optional[{type_name}]'
        elif multiplicity == '*':
            return f'list[{type_name}]'
        elif multiplicity == '1':
            return type_name
        else:
            return type_name
    elif type_name == "Any":
        # Handle the Any type specifically
        if multiplicity == '0..1':
            return 'Optional[Any]'
        elif multiplicity == '*':
            return 'list[Any]'
        elif multiplicity == '1':
            return 'Any'
        else:
            return 'Any'
    else:
        # It's a class type
        # Apply multiplicity
        # For class types:
        # - multiplicity 0..1: Use Optional[type_name] and initialize with None
        # - multiplicity *: Use list[type_name] and initialize with []
        # - multiplicity 1: Use type_name and initialize with None (class types can be nullable)
        if multiplicity == '0..1':
            return f'Optional[{type_name}]'
        elif multiplicity == '*':
            return f'list[{type_name}]'
        elif multiplicity == '1':
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
        if 'classes' in data:
            for cls in data['classes']:
                if cls['name'] == type_name:
                    # Convert package path to Python import path
                    # Package path format: M2::AUTOSARTemplates::...
                    # Python import path: armodel.models.M2.AUTOSARTemplates...
                    # Import from the specific class file, not module
                    python_path = package_path.replace('::', '.')
                    
                    # Return import path in format: from armodel.models.M2.MSR.AsamHdo.AdminData.admin_data import AdminData
                    class_filename = to_snake_case(type_name)
                    module_path = f'armodel.models.{python_path}.{class_filename}'
                    
                    # Format import with proper line breaks if type name is long
                    return f'from {module_path} import (\n    {type_name},\n)'
    return ''


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
                        package_data[package_path]['primitives'] = data.get('primitives', [])
                    else:
                        package_data[package_path] = {'primitives': data.get('primitives', [])}
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
            class_code = generate_class_code(type_def, hierarchy_info, package_data, include_members)
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

                # Generate enum code
                enum_code = generate_enum_code(enum_def)

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

                # Generate primitive code
                primitive_code = generate_primitive_code(primitive_def)

                # Write to file
                filename.write_text(primitive_code)
                total_generated += 1
                total_primitives += 1

        print(f"Generated {len(primitive_files)} primitive files with {total_primitives} primitives")

    print(f"Total generated files: {total_generated} in {output_dir}")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Generate AUTOSAR model classes, enums, and primitives from JSON definitions"
    )
    parser.add_argument(
        "mapping_file",
        type=Path,
        help="Path to mapping.json file"
    )
    parser.add_argument(
        "hierarchy_file",
        type=Path,
        help="Path to hierarchy.json file"
    )
    parser.add_argument(
        "output_dir",
        type=Path,
        help="Output directory for generated files"
    )
    parser.add_argument(
        "--classes",
        action="store_true",
        default=True,
        help="Generate class files (default: True)"
    )
    parser.add_argument(
        "--no-classes",
        action="store_false",
        dest="classes",
        help="Skip class file generation"
    )
    parser.add_argument(
        "--enums",
        action="store_true",
        default=True,
        help="Generate enum files (default: True)"
    )
    parser.add_argument(
        "--no-enums",
        action="store_false",
        dest="enums",
        help="Skip enum file generation"
    )
    parser.add_argument(
        "--primitives",
        action="store_true",
        default=True,
        help="Generate primitive files (default: True)"
    )
    parser.add_argument(
        "--no-primitives",
        action="store_false",
        dest="primitives",
        help="Skip primitive file generation"
    )
    parser.add_argument(
        "--members",
        action="store_true",
        default=False,
        help="Include member lists from package definitions"
    )
    parser.add_argument(
        "--no-members",
        action="store_false",
        dest="members",
        help="Skip member list generation"
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
