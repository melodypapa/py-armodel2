#!/usr/bin/env python3
"""Code generator for AUTOSAR model classes."""

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


def create_directory_structure(types: list, output_dir: Path) -> None:
    """Create directory structure from package paths.

    Args:
        types: List of type definitions from mapping.json
        output_dir: Base directory for generated files

    Returns:
        None
    """
    # Extract all unique package paths
    package_paths = set()
    for type_def in types:
        package_path = type_def.get("package_path", "")
        if package_path:
            package_paths.add(package_path)

    # Create directories for each unique package path
    for package_path in package_paths:
        # Convert package path to directory path
        dir_path = output_dir / package_path.replace("::", "/")

        # Create directory
        dir_path.mkdir(parents=True, exist_ok=True)

        # Create __init__.py
        init_file = dir_path / "__init__.py"
        with open(init_file, "w", encoding="utf-8") as f:
            f.write(f'"""{package_path}"""\n')

    # Create __init__.py for each level
    for init_path in output_dir.rglob("__init__.py"):
        if init_path.parent != output_dir:
            # Ensure parent packages have __init__.py
            parent_init = init_path.parent.parent / "__init__.py"
            if not parent_init.exists():
                parent_init.write_text('"""AUTOSAR model package."""\n')


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

    # Generate class code - removed unused Optional import
    code = f'''"""{class_name} AUTOSAR element."""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
import xml.etree.ElementTree as ET


class {class_name}(ARObject):
    """AUTOSAR {class_name}."""

'''

    if is_splitable:
        code += f'''    is_splitable = True
    split_file_name = "{split_file_name}"

'''

    code += f'''    def __init__(self) -> None:
        """Initialize {class_name}."""
        super().__init__()
'''

    # Add serialize method with proper return type
    code += f'''
    def serialize(self) -> ET.Element:
        """Convert {class_name} to XML element.

        Returns:
            XML element representing this object
        """
        element = ET.Element("{class_name.upper()}")
        # TODO: Add serialization logic
        return element

    @classmethod
    def deserialize(cls, element: ET.Element) -> "{class_name}":
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

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj = {class_name}()

    def build(self) -> {class_name}:
        """Build and return {class_name} object.

        Returns:
            {class_name} instance
        """
        # TODO: Add validation
        return self._obj
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


def generate_all_models(mapping_file: Path, output_dir: Path) -> None:
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


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("Usage: generate_models.py <mapping.json> <output_dir>")
        sys.exit(1)

    mapping_file = Path(sys.argv[1])
    output_dir = Path(sys.argv[2])

    # Generate all models
    generate_all_models(mapping_file, output_dir)
