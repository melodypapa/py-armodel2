"""Utility functions for code generation."""

from pathlib import Path
from typing import Any, Dict

from ._common import to_snake_case


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
        init_content = f'"""{package_name} module."""\n\nfrom __future__ import annotations\nfrom typing import TYPE_CHECKING\n\n'

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
