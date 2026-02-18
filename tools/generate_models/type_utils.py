"""Type-related functions for code generation."""

from typing import Any, Dict

from ._common import to_snake_case


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
    type_name: str, multiplicity: str, package_data: Dict[str, Dict[str, Any]], is_ref: bool = False
) -> str:
    """Get Python type annotation for AUTOSAR type.

    Args:
        type_name: AUTOSAR type name
        multiplicity: Multiplicity (e.g., "0..1", "*", "1")
        package_data: Package data dictionary
        is_ref: Whether this is a reference type (wraps in ARRef)

    Returns:
        Python type annotation string
    """
    # Check if type_name matches "any (xxx)" pattern and convert to Any
    if type_name.startswith("any ("):
        # This is a polymorphic type that can be any type implementing the interface
        # Convert to Any in Python
        type_name = "Any"

    # Determine the base type before multiplicity
    base_type: str

    # Check if it's a primitive type
    if is_primitive_type(type_name, package_data):
        # Use AUTOSAR primitive type names directly instead of Python types
        # The primitive types are imported from PrimitiveTypes module
        base_type = type_name
    elif type_name == "Any":
        # Handle the Any type specifically
        base_type = "Any"
    else:
        # It's a class type
        base_type = type_name

    # Handle reference types - wrap in ARRef
    if is_ref:
        base_type = "ARRef"

    # Apply multiplicity
    # For all types:
    # - multiplicity 0..1: Use Optional[Type] and initialize with None
    # - multiplicity *: Use list[Type] and initialize with []
    # - multiplicity 1: Use Type and initialize with None
    if multiplicity == "0..1":
        return f"Optional[{base_type}]"
    elif multiplicity == "*":
        return f"list[{base_type}]"
    elif multiplicity == "1":
        return base_type
    else:
        return f"Optional[{base_type}]"


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

                    # Return import path in block import format as required by DESIGN_RULE_041
                    # Format: from armodel.models.M2.MSR.AsamHdo.AdminData.admin_data import (AdminData,)
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
