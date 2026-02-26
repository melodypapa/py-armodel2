"""Main entry point for AUTOSAR model generation."""

import argparse
from pathlib import Path
from typing import Optional

from .parsers import (
    load_all_package_data,
    load_skip_list,
    parse_enum_json,
    parse_hierarchy_json,
    parse_mapping_json,
    parse_primitive_json,
)
from .generators import (
    generate_builder_code,
    generate_class_code,
    generate_enum_code,
    generate_primitive_code,
)
from .utils import create_directory_structure, to_snake_case
from .type_utils import build_complete_dependency_graph


def generate_all_models(
    mapping_file: Path,
    hierarchy_file: Path,
    output_dir: Path,
    generate_classes: bool = True,
    generate_enums: bool = True,
    generate_primitives: bool = True,
    include_members: bool = False,
    skip_list_file: Optional[Path] = None,
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
        skip_list_file: Path to skip_classes.yaml (optional, defaults to tools/skip_classes.yaml)
    """
    total_generated = 0

    # Load skip list and force_type_checking_imports from YAML configuration
    if skip_list_file is None:
        # Default to the skip_classes.yaml in the tools directory
        skip_list_file = Path(__file__).parent.parent / "skip_classes.yaml"
    skip_list, force_type_checking_imports = load_skip_list(skip_list_file)

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
        # Create a mapping of class names to their class details (including atp_type)
        class_details_map = {}
        for package_path, package_info in package_data.items():
            if "classes" in package_info:
                json_file_path = (
                    packages_dir / f"{package_path.replace('::', '_')}.classes.json"
                ).as_posix()
                for cls in package_info["classes"]:
                    class_json_file_map[cls["name"]] = json_file_path
                    # Store the full class details (including atp_type)
                    class_details_map[cls["name"]] = cls

        # Generate each class
        for type_def in types:
            if type_def.get("type") != "Class":
                continue

            class_name = type_def["name"]
            package_path = type_def.get("package_path", "")

            # Skip classes that are in the skip list (manually maintained)
            if class_name in skip_list:
                print(f"Skipping {class_name} - manually maintained special class")
                continue

            # Get the JSON file path for this class
            json_file_path = class_json_file_map.get(class_name, "")

            # Merge class details from package_data into type_def
            # This includes fields like atp_type, parent, bases, etc.
            if class_name in class_details_map:
                for key, value in class_details_map[class_name].items():
                    if key not in type_def:  # Don't override existing fields
                        type_def[key] = value

            # Convert package path to file path
            dir_path = output_dir / package_path.replace("::", "/")
            filename = dir_path / f"{to_snake_case(class_name)}.py"

            # Generate class code
            # Get builder imports first (to add at top of file)
            builder_imports, builder_class_code = generate_builder_code(
                type_def,
                hierarchy_info,
                package_data,
                include_members,
            )

            class_code = generate_class_code(
                type_def,
                hierarchy_info,
                package_data,
                include_members,
                json_file_path,
                dependency_graph,
                force_type_checking_imports,
                builder_imports,  # Pass builder imports to be added at top
            )

            # Write to file (class code already includes builder imports at top)
            full_code = class_code + "\n\n" + builder_class_code
            filename.write_text(full_code, encoding="utf-8")
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
                json_file_path = enum_file.relative_to(packages_dir.parent).as_posix()
                enum_code = generate_enum_code(enum_def, json_file_path)

                # Write to file
                filename.write_text(enum_code, encoding="utf-8")
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

                # Generate primitive code with JSON file path and package data
                json_file_path = primitive_file.relative_to(packages_dir.parent).as_posix()
                primitive_code = generate_primitive_code(
                    primitive_def, package_data, json_file_path
                )

                # Write to file
                filename.write_text(primitive_code, encoding="utf-8")
                total_generated += 1
                total_primitives += 1

        print(
            f"Generated {len(primitive_files)} primitive files with {total_primitives} primitives"
        )

    print(f"Total generated files: {total_generated} in {output_dir}")


def main() -> None:
    """CLI entry point for model generation."""
    parser = argparse.ArgumentParser(
        description="Generate AUTOSAR model classes, enums, and primitives from JSON definitions"
    )

    # Optional arguments with defaults based on project structure
    parser.add_argument(
        "--mapping-file",
        type=Path,
        default=Path("docs/json/mapping.json"),
        help="Path to mapping.json file (default: docs/json/mapping.json)",
    )
    parser.add_argument(
        "--hierarchy-file",
        type=Path,
        default=Path("docs/json/hierarchy.json"),
        help="Path to hierarchy.json file (default: docs/json/hierarchy.json)",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("src/armodel2/models"),
        help="Output directory for generated files (default: src/armodel2/models/M2)",
    )

    # Generation options
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
        default=True,
        help="Include member lists from package definitions (default: True)",
    )
    parser.add_argument(
        "--no-members", action="store_false", dest="members", help="Skip member list generation"
    )
    parser.add_argument(
        "--skip-list",
        type=Path,
        default=None,
        help="Path to skip_classes.yaml file (default: tools/skip_classes.yaml)",
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
        skip_list_file=args.skip_list,
    )


if __name__ == "__main__":
    main()
