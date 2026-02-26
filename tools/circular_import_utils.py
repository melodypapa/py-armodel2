"""
Utility functions for circular import detection.

This module provides standalone functions for analyzing AUTOSAR model code
to detect circular import dependencies without executing any Python imports.
"""

import json
import re
from pathlib import Path
from typing import Any, Dict, List, Set


def to_snake_case(name: str) -> str:
    """Convert PascalCase to snake_case.

    Args:
        name: PascalCase string

    Returns:
        snake_case string
    """
    # Handle acronyms and edge cases
    name = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1_\2', name)
    name = re.sub(r'([a-z\d])([A-Z])', r'\1_\2', name)
    name = name.replace('-', '_')
    return name.lower()


def load_package_data(json_dir: Path) -> Dict[str, Dict[str, Any]]:
    """Load all package JSON files.

    Args:
        json_dir: Path to directory containing *.classes.json files

    Returns:
        Dictionary mapping package names to their data
    """
    package_data: Dict[str, Dict[str, Any]] = {}

    if not json_dir.exists():
        raise FileNotFoundError(f"JSON directory not found: {json_dir}")

    for json_file in sorted(json_dir.glob("*.classes.json")):
        try:
            data = json.loads(json_file.read_text())
            package_data[json_file.stem] = data
        except json.JSONDecodeError as e:
            import sys
            print(f"Warning: Failed to parse {json_file}: {e}", file=sys.stderr)

    return package_data


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
                if prim.get("name") == type_name:
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
        if "enums" in data:
            for enum in data["enums"]:
                if enum.get("name") == type_name:
                    return True
    return False


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


def get_class_location(class_name: str, package_data: Dict[str, Dict[str, Any]]) -> tuple[str, int]:
    """Get file path and import line number for a class.

    Args:
        class_name: Name of the class to locate
        package_data: Package data dictionary

    Returns:
        Tuple of (file_path, import_line_number)
    """
    # Search for the class in all packages
    for package_path, data in package_data.items():
        if "classes" in data:
            for cls in data["classes"]:
                if cls["name"] == class_name:
                    class_package_path = cls.get("package", package_path)

                    # Convert package path to file path
                    # Package path format: M2::AUTOSARTemplates::...
                    # File path format: src/armodel/models/M2/AUTOSARTemplates/...
                    python_path = class_package_path.replace("::", "/")

                    # Convert class name to snake_case for filename
                    class_filename = to_snake_case(class_name)

                    file_path = f"src/armodel2/models/{python_path}/{class_filename}.py"

                    # Find the import line number
                    # We need to find where this class imports other classes
                    # For now, return line 1 as a placeholder
                    # In a more advanced version, we could parse the actual Python file
                    return (file_path, 1)

    # Class not found
    return (f"Unknown location for {class_name}", 0)