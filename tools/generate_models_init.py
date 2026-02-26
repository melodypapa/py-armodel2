#!/usr/bin/env python3
"""Generate armodel/models/__init__.py with all model class exports.

This tool scans the models directory and generates a comprehensive __init__.py
that exports all model classes for convenient import from armodel2.models.
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Tuple

# Project root
PROJECT_ROOT = Path(__file__).parent.parent
MODELS_DIR = PROJECT_ROOT / "src" / "armodel2" / "models"
TARGET_FILE = MODELS_DIR / "__init__.py"


def find_python_files(models_dir: Path) -> List[Path]:
    """Find all Python files in the models directory."""
    python_files = []
    for root, dirs, files in os.walk(models_dir):
        # Skip __pycache__ and __init__.py files
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for file in files:
            if file.endswith(".py") and file != "__init__.py":
                python_files.append(Path(root) / file)
    return sorted(python_files)


def extract_classes_from_file(file_path: Path) -> List[Tuple[str, str]]:
    """Extract class definitions and their Builder classes from a Python file.

    Returns:
        List of tuples: (class_name, builder_name) where builder_name can be None
    """
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    class_names = []
    builder_names = set()

    # Find all class definitions (with or without parent classes)
    class_pattern = r"^class\s+(\w+)(?:\([^)]*\))?:"
    for match in re.finditer(class_pattern, content, re.MULTILINE):
        class_name = match.group(1)
        # Skip abstract classes and interfaces
        if class_name.startswith("_"):
            continue

        # Check if this is a Builder class
        if class_name.endswith("Builder"):
            builder_names.add(class_name)
        else:
            class_names.append(class_name)

    # Match builders with their classes
    result = []
    for class_name in sorted(class_names):
        builder_name = f"{class_name}Builder"
        if builder_name in builder_names:
            result.append((class_name, builder_name))
        else:
            result.append((class_name, None))

    return result


def get_import_path(file_path: Path, models_dir: Path) -> str:
    """Get the import path for a file relative to armodel2.models."""
    relative_path = file_path.relative_to(models_dir)
    # Convert path to module path (e.g., M2/Package/file.py -> M2.Package.file)
    module_path = str(relative_path.with_suffix("")).replace(os.sep, ".")
    return f"armodel2.models.{module_path}"


def generate_init_file(classes: Dict[str, str], builders: Dict[str, str]) -> str:
    """Generate the __init__.py file content."""
    lines = [
        '"""py-armodel2 models package.',
        '',
        'This package exports all AUTOSAR model classes for convenient import.',
        'All model classes can be imported directly from armodel2.models.',
        '',
        'Example:',
        '    from armodel.models import AUTOSAR, ARPackage, SwBaseType',
        '"""',
        '',
    ]

    # Special handling for manually maintained classes
    manual_classes = {
        "AUTOSAR": ("armodel2.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.autosar", True),
        "ARObject": ("armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object", True),
        "ARRef": ("armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref", False),
    }

    # Add manual classes first
    lines.append("# Manually Maintained Classes")
    for class_name, (import_path, has_builder) in sorted(manual_classes.items()):
        if has_builder:
            lines.append(f"from {import_path} import ({class_name}, {class_name}Builder)")
        else:
            lines.append(f"from {import_path} import {class_name}")
    lines.append("")

    # Group remaining classes by category
    categories = {
        "AUTOSAR Core": [],
        "AUTOSAR Templates": [],
        "MSR": [],
        "Documentation": [],
        "Other": [],
    }

    for class_name, import_path in sorted(classes.items()):
        # Skip manually maintained classes
        if class_name in manual_classes:
            continue

        if class_name in ["ARPackage", "ARElement", "PackageableElement", "ReferenceBase"]:
            categories["AUTOSAR Core"].append((class_name, import_path))
        elif class_name.startswith("Sw") or class_name in ["CompuMethod", "Compu"]:
            categories["MSR"].append((class_name, import_path))
        elif class_name.startswith("L") or class_name in ["DataConstr", "Limit", "IntervalTypeEnum"]:
            categories["AUTOSAR Templates"].append((class_name, import_path))
        elif "Paragraph" in class_name or "Chapter" in class_name or class_name in ["Annotation", "Documentation"]:
            categories["Documentation"].append((class_name, import_path))
        else:
            categories["Other"].append((class_name, import_path))

    # Generate imports for each category
    for category, items in categories.items():
        if not items:
            continue

        lines.append(f"# {category}")
        for class_name, import_path in items:
            builder_name = f"{class_name}Builder"
            if builder_name in builders:
                lines.append(f"from {import_path} import ({class_name}, {builder_name})")
            else:
                lines.append(f"from {import_path} import {class_name}")
        lines.append("")

    # Generate __all__
    lines.append("__all__ = [")
    all_items = []
    # Add manual classes
    for class_name, (_, has_builder) in sorted(manual_classes.items()):
        all_items.append(f'    "{class_name}"')
        if has_builder:
            all_items.append(f'    "{class_name}Builder"')
    # Add other classes
    for class_name, _ in sorted(classes.items()):
        if class_name in manual_classes:
            continue
        all_items.append(f'    "{class_name}"')
        builder_name = f"{class_name}Builder"
        if builder_name in builders:
            all_items.append(f'    "{builder_name}"')
    lines.extend(all_items)
    lines.append("]")

    return "\n".join(lines)


def main():
    """Main function to generate the __init__.py file."""
    print("Generating armodel/models/__init__.py...")

    # Find all Python files
    python_files = find_python_files(MODELS_DIR)
    print(f"Found {len(python_files)} Python files")

    # Extract classes from each file
    all_classes: Dict[str, str] = {}
    builders: Dict[str, str] = {}

    for file_path in python_files:
        classes = extract_classes_from_file(file_path)
        import_path = get_import_path(file_path, MODELS_DIR)

        for class_name, builder_name in classes:
            if class_name not in all_classes:
                all_classes[class_name] = import_path
            if builder_name and builder_name not in builders:
                builders[builder_name] = import_path

    print(f"Found {len(all_classes)} classes and {len(builders)} builders")

    # Remove manually maintained classes that are added separately
    skip_classes = {
        "ARObject",  # Base class
    }

    for class_name in list(all_classes.keys()):
        if class_name in skip_classes:
            del all_classes[class_name]

    # Generate the file content
    content = generate_init_file(all_classes, builders)

    # Write the file
    with open(TARGET_FILE, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Generated {TARGET_FILE}")
    print(f"Total exports: {len(all_classes) + len(builders)} items")


if __name__ == "__main__":
    main()