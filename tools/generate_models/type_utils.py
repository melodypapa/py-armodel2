"""Type-related functions for code generation."""

from typing import Any, Dict, Set, List, Optional, cast

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
    type_name: str, multiplicity: str, package_data: Dict[str, Dict[str, Any]], is_ref: bool = False, kind: str = "attribute"
) -> str:
    """Get Python type annotation for AUTOSAR type.

    Args:
        type_name: AUTOSAR type name
        multiplicity: Multiplicity (e.g., "0..1", "*", "1")
        package_data: Package data dictionary
        is_ref: Whether this is a reference type (wraps in ARRef)
        kind: Kind of attribute (e.g., "attribute", "ref", "tref", "iref")

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
    elif is_enum_type(type_name, package_data):
        # Enum types are used directly, not wrapped in ARRef
        base_type = type_name
    elif type_name == "Any":
        # Handle the Any type specifically
        base_type = "Any"
    else:
        # It's a class type
        base_type = type_name

    # Handle reference types - wrap in ARRef only for class types
    # Primitive types and enum types are referenced by their string values, not by ARRef
    # Note: iref kind represents instance references which are complex objects, not simple references
    # For iref kind, use the actual class type directly, not wrapped in ARRef
    if is_ref and kind != "iref" and not is_primitive_type(type_name, package_data) and not is_enum_type(type_name, package_data) and type_name != "Any":
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
                    class_package_path = cast(str, cls.get("package", package_path))
                    return class_package_path
    return ""


def build_complete_dependency_graph(package_data: Dict[str, Dict[str, Any]]) -> Dict[str, Set[str]]:
    """Build a complete dependency graph for all classes.

    Includes both attribute-based dependencies and inheritance-based dependencies.

    Args:
        package_data: Package data dictionary

    Returns:
        Dictionary mapping class names to their dependencies
    """
    dependency_graph: Dict[str, Set[str]] = {}

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
                        if (
                            is_primitive_type(attr_type, package_data)
                            or is_enum_type(attr_type, package_data)
                            or attr_type.startswith("any (")
                            or attr_type == class_name
                        ):
                            continue

                        # Add to dependencies
                        dependency_graph[class_name].add(attr_type)

                # Collect inheritance-based dependencies (parent class)
                if "parent" in cls and cls["parent"]:
                    parent_type = cls["parent"]

                    # Skip if parent is a primitive or enum
                    if (
                        not is_primitive_type(parent_type, package_data)
                        and not is_enum_type(parent_type, package_data)
                        and parent_type != class_name
                    ):
                        # Add parent as a dependency
                        # This ensures that if a class imports its child's type,
                        # we can detect the circular import through the inheritance chain
                        dependency_graph[class_name].add(parent_type)

    return dependency_graph


def detect_circular_import(
    current_class: str,
    attribute_type: str,
    package_data: Dict[str, Dict[str, Any]],
    dependency_graph: Dict[str, Set[str]],
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
    visited: Set[str] = set()
    to_visit: List[str] = [attribute_type]

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


def find_all_cycles_in_graph(
    dependency_graph: Dict[str, Set[str]]
) -> List[List[str]]:
    """Find all cycles in the dependency graph using Tarjan's strongly connected components algorithm.

    Args:
        dependency_graph: Graph of class dependencies (complete graph)

    Returns:
        List of cycles, where each cycle is a list of class names forming a strongly connected component
        Cycles are sorted deterministically by the first class name in each cycle
    """
    cycles: List[List[str]] = []

    # Tarjan's strongly connected components algorithm
    # Each SCC with more than 1 node represents a cycle
    indices: Dict[str, int] = {}
    lowlinks: Dict[str, int] = {}
    stack: List[str] = []
    onstack: Set[str] = set()
    index = 0

    def strongconnect(v: str) -> None:
        nonlocal index
        indices[v] = index
        lowlinks[v] = index
        index += 1
        stack.append(v)
        onstack.add(v)

        # Consider successors of v
        for w in dependency_graph.get(v, []):
            if w not in indices:
                # Successor w has not yet been visited; recurse on it
                strongconnect(w)
                lowlinks[v] = min(lowlinks[v], lowlinks[w])
            elif w in onstack:
                # Successor w is in stack and hence in the current SCC
                lowlinks[v] = min(lowlinks[v], indices[w])

        # If v is a root node, pop the stack and generate an SCC
        if lowlinks[v] == indices[v]:
            scc: List[str] = []
            while True:
                w = stack.pop()
                onstack.remove(w)
                scc.append(w)
                if w == v:
                    break
            # SCC with more than 1 node indicates a cycle
            if len(scc) > 1:
                cycles.append(scc)

    # Call strongconnect for all nodes in the graph in a deterministic order
    for v in sorted(dependency_graph.keys()):
        if v not in indices:
            strongconnect(v)

    # Sort cycles deterministically by the first class name in each cycle
    # Then sort the classes within each cycle to ensure consistent ordering
    for cycle in cycles:
        # Find the "starting point" of the cycle (lexicographically smallest class)
        # and rotate the cycle so it starts there
        if cycle:
            min_idx = cycle.index(min(cycle))
            # Rotate the cycle to start from the smallest class name
            cycle[:] = cycle[min_idx:] + cycle[:min_idx]
    
    # Sort cycles by their first class name
    cycles.sort(key=lambda c: c[0] if c else "")

    return cycles


def get_type_coercion_function(target_type: str) -> Optional[str]:
    """Get the type coercion function name for a target type.

    Args:
        target_type: Target type name (e.g., "int", "float", "bool", "str")

    Returns:
        Function name or None if no coercion is available.
    """
    coercion_map = {
        "int": "_coerce_to_int",
        "float": "_coerce_to_float",
        "bool": "_coerce_to_bool",
        "str": "_coerce_to_str",
    }
    return coercion_map.get(target_type)


def generate_type_coercion_helper() -> str:
    """Generate type coercion helper methods for Builder class.

    Returns:
        String containing static methods for type coercion.
    """
    return '''
    @staticmethod
    def _coerce_to_int(value: Any) -> int:
        """Coerce value to int.

        Args:
            value: Value to coerce

        Returns:
            Integer value

        Raises:
            ValueError: If value cannot be coerced to int
        """
        if isinstance(value, int):
            return value
        if isinstance(value, str) and value.isdigit():
            return int(value)
        if isinstance(value, float):
            return int(value)
        if isinstance(value, bool):
            return int(value)
        raise ValueError(f"Cannot coerce {type(value).__name__} to int: {value}")

    @staticmethod
    def _coerce_to_float(value: Any) -> float:
        """Coerce value to float.

        Args:
            value: Value to coerce

        Returns:
            Float value

        Raises:
            ValueError: If value cannot be coerced to float
        """
        if isinstance(value, float):
            return value
        if isinstance(value, int):
            return float(value)
        if isinstance(value, str):
            try:
                return float(value)
            except ValueError:
                pass
        raise ValueError(f"Cannot coerce {type(value).__name__} to float: {value}")

    @staticmethod
    def _coerce_to_bool(value: Any) -> bool:
        """Coerce value to bool.

        Args:
            value: Value to coerce

        Returns:
            Boolean value

        Raises:
            ValueError: If value cannot be coerced to bool
        """
        if isinstance(value, bool):
            return value
        if isinstance(value, int):
            return bool(value)
        if isinstance(value, str):
            if value.lower() in ("true", "1", "yes"):
                return True
            if value.lower() in ("false", "0", "no"):
                return False
        raise ValueError(f"Cannot coerce {type(value).__name__} to bool: {value}")

    @staticmethod
    def _coerce_to_str(value: Any) -> str:
        """Coerce value to str.

        Args:
            value: Value to coerce

        Returns:
            String value
        """
        return str(value)


    @staticmethod
    def _coerce_to_list(value: Any, item_type: str) -> list:
        """Coerce value to list.

        Args:
            value: Value to coerce
            item_type: Expected item type (for error messages)

        Returns:
            List value

        Raises:
            ValueError: If value cannot be coerced to list
        """
        if isinstance(value, list):
            return value
        if isinstance(value, tuple):
            return list(value)
        raise ValueError(f"Cannot coerce {type(value).__name__} to list[{item_type}]: {value}")
'''


def should_apply_type_coercion(target_type: str) -> bool:
    """Check if type coercion should be applied for a target type.

    Args:
        target_type: Target type name

    Returns:
        True if coercion should be applied, False otherwise
    """
    coercible_types = {"int", "float", "bool", "str", "list"}
    return target_type in coercible_types


def extract_base_type(type_str: str) -> str:
    """Extract base type from complex type hints.

    Examples:
        "Optional[str]" -> "str"
        "list[int]" -> "int"
        "List[SomeClass]" -> "SomeClass"
        "str" -> "str"

    Args:
        type_str: Type hint string

    Returns:
        Base type string
    """
    # Remove outer wrapper
    if type_str.startswith("Optional[") or type_str.startswith("List[") or type_str.startswith("list["):
        inner = type_str[type_str.index("[") + 1 : type_str.rindex("]")]
        return extract_base_type(inner)

    # Handle Union types
    if type_str.startswith("Union["):
        # Return first non-None type
        types = type_str[type_str.index("[") + 1 : type_str.rindex("]")].split(",")
        for t in types:
            t = t.strip()
            if t != "None":
                return extract_base_type(t)
        return "Any"

    return type_str.strip()


def extract_attribute_metadata(
    class_name: str,
    attributes: Dict[str, Dict[str, Any]],
) -> List[Dict[str, Any]]:
    """Extract enhanced metadata for builder generation.

    Args:
        class_name: Name of the model class
        attributes: Raw attribute dict from mapping

    Returns:
        Enhanced attribute metadata with is_list, is_optional flags
    """
    enhanced_attrs = []

    for attr_name, attr_info in attributes.items():
        attr_type = attr_info["type"]
        multiplicity = attr_info.get("multiplicity", "1")

        # Determine if attribute is a list
        is_list = multiplicity in ("*", "0..*") or attr_type.startswith("list[") or attr_type.startswith("List[")

        # Determine if attribute is optional
        is_optional = multiplicity == "0..1" or attr_type.startswith("Optional[") or attr_type.startswith("Union[")

        # Extract base type for lists and optional types
        base_type = extract_base_type(attr_type)

        enhanced_attrs.append({
            "name": attr_name,
            "type": attr_type,
            "base_type": base_type,
            "is_list": is_list,
            "is_optional": is_optional,
            "multiplicity": multiplicity,
        })

    return enhanced_attrs
