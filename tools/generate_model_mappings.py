#!/usr/bin/env python3
"""Generate YAML model mappings from JSON mapping data.

This script reads the JSON mapping files from docs/json/ and generates
a YAML file with XML tag to class mappings, polymorphic type mappings,
and import path mappings for the ModelFactory.

Usage:
    python tools/generate_model_mappings.py
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List, Any
from datetime import datetime


def to_snake_case(name: str) -> str:
    """Convert PascalCase to snake_case.

    Args:
        name: PascalCase string

    Returns:
        snake_case string
    """
    result = []
    for i, c in enumerate(name):
        # Add underscore before uppercase letters that follow lowercase letters
        # or before uppercase letters that are followed by lowercase letters
        if i > 0 and c.isupper():
            prev_char = name[i-1]
            next_char = name[i+1] if i < len(name) - 1 else None

            # Add underscore if previous char is lowercase
            # or if next char is lowercase (acronym boundary)
            if prev_char.islower() or (next_char and next_char.islower()):
                result.append('_')

        result.append(c.lower())

    return ''.join(result)


def package_to_import_path(package_path: str, class_name: str) -> str:
    """Convert AUTOSAR package path to Python import path.
    
    Args:
        package_path: AUTOSAR package path (e.g., M2::AUTOSARTemplates::...)
        class_name: Name of the class
        
    Returns:
        Python import path string
    """
    # Convert package path to Python module path
    python_path = package_path.replace("::", ".")
    
    # Convert class name to snake_case for filename
    class_filename = to_snake_case(class_name)
    
    # Build full module path
    module_path = f"armodel.models.{python_path}.{class_filename}"
    
    return module_path


def generate_xml_tag_mappings(mapping_json: Dict[str, Any]) -> Dict[str, str]:
    """Generate XML tag to class name mappings.
    
    Args:
        mapping_json: Contents of mapping.json
        
    Returns:
        Dictionary mapping XML tags to class names
    """
    from armodel.serialization.name_converter import NameConverter
    
    mappings = {}
    
    for type_info in mapping_json.get("types", []):
        class_name = type_info.get("name")
        type_kind = type_info.get("type")
        
        if class_name and type_kind == "Class":
            xml_tag = NameConverter.to_xml_tag(class_name)
            mappings[xml_tag] = class_name
    
    return mappings


def generate_import_paths(mapping_json: Dict[str, Any]) -> Dict[str, str]:
    """Generate class name to import path mappings.
    
    Args:
        mapping_json: Contents of mapping.json
        
    Returns:
        Dictionary mapping class names to import paths
    """
    paths = {}
    
    for type_info in mapping_json.get("types", []):
        class_name = type_info.get("name")
        type_kind = type_info.get("type")
        package_path = type_info.get("package_path", "")
        
        if class_name and type_kind == "Class":
            import_path = package_to_import_path(package_path, class_name)
            paths[class_name] = import_path
    
    return paths


def generate_polymorphic_mappings(package_files: List[Path]) -> Dict[str, List[str]]:
    """Generate polymorphic type mappings from package JSON files.
    
    Args:
        package_files: List of package JSON file paths
        
    Returns:
        Dictionary mapping abstract base classes to their concrete implementations
    """
    
    polymorphic_types = {}
    
    for package_file in package_files:
        with open(package_file, "r") as f:
            data = json.load(f)
        
        for class_info in data.get("classes", []):
            # Check if this is an abstract base class
            if class_info.get("is_abstract", False):
                base_class = class_info["name"]
                
                # Get concrete implementations
                subclasses = class_info.get("subclasses", [])
                
                if subclasses:
                    polymorphic_types[base_class] = subclasses
    
    return polymorphic_types


def generate_yaml_mappings(
    mapping_json_path: Path,
    packages_dir: Path,
    output_yaml_path: Path,
) -> None:
    """Generate YAML mappings file from JSON data.
    
    Args:
        mapping_json_path: Path to mapping.json
        packages_dir: Path to packages directory
        output_yaml_path: Path to output YAML file
    """
    # Load mapping.json
    print(f"Loading {mapping_json_path}...")
    with open(mapping_json_path, "r") as f:
        mapping_json = json.load(f)
    
    # Load all package JSON files
    print(f"Loading package files from {packages_dir}...")
    package_files = list(packages_dir.glob("*.json"))
    print(f"Found {len(package_files)} package files")
    
    # Generate mappings
    print("Generating XML tag mappings...")
    generated_mappings = generate_xml_tag_mappings(mapping_json)
    print(f"  Analyzed {len(generated_mappings)} potential XML tag mappings")
    print("  Filtering to exceptional cases only...")
    
    print("Generating import path mappings...")
    import_paths = generate_import_paths(mapping_json)
    print(f"  Generated {len(import_paths)} import path mappings")
    
    print("Generating polymorphic type mappings...")
    polymorphic_types = generate_polymorphic_mappings(package_files)
    print(f"  Generated {len(polymorphic_types)} polymorphic type mappings")
    
    # Define exceptional cases that don't follow the normal pattern
    # Normal pattern: XML tag -> class name via NameConverter.tag_to_class_name()
    # These exceptional cases must be explicitly mapped in the YAML
    exceptional_xml_tag_mappings = {
        # AR prefix - keep uppercase (not converted to Ar)
        "AR-ELEMENT": "ARElement",
        "AR-PACKAGE": "ARPackage",
        "AR-OBJECT": "ARObject",
        "AR-LIST": "ARList",
        # AR-VARIABLE and AR-PARAMETER - keep AR uppercase
        "AR-VARIABLE-IN-IMPLEMENTATION-DATA-INSTANCE-REF": "ArVariableInImplementationDataInstanceRef",
        "AR-PARAMETER-IN-IMPLEMENTATION-DATA-INSTANCE-REF": "ArParameterInImplementationDataInstanceRef",
        # Words starting with "AR" but not the AR prefix - use lowercase "Ar"
        "ARGUMENT-DATA-PROTOTYPE": "ArgumentDataPrototype",
        "ARBITRARY-EVENT-TRIGGERING": "ArbitraryEventTriggering",
        "ARRAY-VALUE-SPECIFICATION": "ArrayValueSpecification",
        # AUTOSAR - keep fully uppercase
        "AUTOSAR": "AUTOSAR",
        # V2X prefix - special casing (V2x instead of V2X)
        "V2X-FAC-USER-NEEDS": "V2xFacUserNeeds",
        "V2X-M-USER-NEEDS": "V2xMUserNeeds",
        "V2X-DATA-MANAGER-NEEDS": "V2xDataManagerNeeds",
        # Special abbreviation
        "VT": "CompuConstTextContent",
        # Conditional variant
        "BSW-MODULE-ENTRY-REF-CONDITIONAL": "BswModuleClientServerEntry",
    }
    
    # Only keep exceptional cases in xml_tag_mappings
    # All other mappings will be handled by NameConverter.tag_to_class_name() fallback
    xml_tag_mappings = exceptional_xml_tag_mappings
    
    # Build YAML structure
    yaml_data = {
        "version": "1.0.0",
        "generated_from": str(mapping_json_path.relative_to(Path.cwd())),
        "generated_at": datetime.now().isoformat(),
        "metadata": {
            "total_classes": len(mapping_json.get("types", [])),
            "total_packages": len(package_files),
            "total_polymorphic_types": len(polymorphic_types),
        },
        "xml_tag_mappings": xml_tag_mappings,
        "class_import_paths": import_paths,
        "polymorphic_types": polymorphic_types,
    }
    
    # Write YAML file
    print(f"Writing {output_yaml_path}...")
    output_yaml_path.parent.mkdir(parents=True, exist_ok=True)
    
    import yaml
    with open(output_yaml_path, "w") as f:
        yaml.dump(yaml_data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
    
    print(f"Done! Generated YAML file with {len(xml_tag_mappings)} exceptional XML tag mappings")
    print(f"  Polymorphic types: {len(polymorphic_types)}")
    print(f"  Total classes: {len(import_paths)} (normal pattern handled by NameConverter)")


def main() -> None:
    """Main entry point."""
    # Get project root
    project_root = Path(__file__).parent.parent
    
    # Define paths
    mapping_json_path = project_root / "docs" / "json" / "mapping.json"
    packages_dir = project_root / "docs" / "json" / "packages"
    output_yaml_path = project_root / "src" / "armodel" / "cfg" / "model_mappings.yaml"
    
    # Validate paths
    if not mapping_json_path.exists():
        raise FileNotFoundError(f"mapping.json not found at {mapping_json_path}")
    
    if not packages_dir.exists():
        raise FileNotFoundError(f"packages directory not found at {packages_dir}")
    
    # Generate YAML mappings
    generate_yaml_mappings(
        mapping_json_path=mapping_json_path,
        packages_dir=packages_dir,
        output_yaml_path=output_yaml_path,
    )


if __name__ == "__main__":
    main()