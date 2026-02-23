"""JSON parsing functions for AUTOSAR schema files."""

import json
from pathlib import Path
from typing import Any, Dict, List, Union, Optional, cast

try:
    import yaml

    _yaml: Optional[Any] = yaml
except ImportError:
    _yaml = None


def parse_mapping_json(mapping_file: Path) -> Dict[str, Any]:
    """Parse mapping.json file.

    Args:
        mapping_file: Path to mapping.json file

    Returns:
        Parsed JSON data as dictionary
    """
    with open(mapping_file, "r", encoding="utf-8") as f:
        data = json.load(f)
        return cast(Dict[str, Any], data)


def parse_enum_json(enum_file: Path) -> Dict[str, Any]:
    """Parse enum JSON file.

    Args:
        enum_file: Path to enum JSON file

    Returns:
        Parsed JSON data as dictionary
    """
    with open(enum_file, "r", encoding="utf-8") as f:
        data = json.load(f)
        return cast(Dict[str, Any], data)


def parse_primitive_json(primitive_file: Path) -> Dict[str, Any]:
    """Parse primitive JSON file.

    Args:
        primitive_file: Path to primitive JSON file

    Returns:
        Parsed JSON data as dictionary
    """
    with open(primitive_file, "r", encoding="utf-8") as f:
        data = json.load(f)
        return cast(Dict[str, Any], data)


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
    indent_stack: List[tuple[int, str]] = []

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


def load_skip_list(
    skip_list_file: Path,
) -> tuple[List[str], Dict[str, Union[List[str], str]]]:
    """Parse skip_classes.yaml file to get list of classes to skip during generation.

    Args:
        skip_list_file: Path to skip_classes.yaml file

    Returns:
        Tuple of (skip_classes_list, force_type_checking_imports)
        - skip_classes_list: List of class names to skip
        - force_type_checking_imports: Dict mapping class names to list of types or "*" to force into TYPE_CHECKING
          (empty dicts if file doesn't exist or yaml not available)
    """
    empty_result: tuple[List[str], Dict[str, Union[List[str], str]]] = ([], {})

    if _yaml is None:
        # YAML module not available, return empty result
        return empty_result

    if not skip_list_file.exists():
        # File doesn't exist, return empty result
        return empty_result

    try:
        with open(skip_list_file, "r", encoding="utf-8") as f:
            data = _yaml.safe_load(f) if _yaml else {}
            skip_classes = data.get("skip_classes", [])
            force_type_checking = data.get("force_type_checking_imports", {})
            return skip_classes, force_type_checking
    except Exception:
        # If there's any error loading the file, return empty result
        return empty_result


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
