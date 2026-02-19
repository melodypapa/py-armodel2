#!/usr/bin/env python3
"""
XSD Metadata Generator Tool

Converts AUTOSAR XSD schemas to YAML format for fast parsing.

Usage:
    python tools/generate_xsd_metadata.py [OPTIONS]

Examples:
    # Generate metadata for default schema (00046)
    python tools/generate_xsd_metadata.py

    # Generate for specific version
    python tools/generate_xsd_metadata.py --version 00048

    # Generate for all supported versions
    python tools/generate_xsd_metadata.py --all

    # Validate existing YAML against XSD
    python tools/generate_xsd_metadata.py --version 00046 --validate

    # Verbose output
    python tools/generate_xsd_metadata.py --version 00046 --verbose
"""

import argparse
import sys
from pathlib import Path
import yaml

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from armodel.cfg.xsd_parser import XSDParser


class XSDMetadataGenerator:
    """Generates YAML metadata from XSD schemas."""

    # Supported schema versions
    SUPPORTED_VERSIONS = [
        "00042",
        "00043",
        "00044",
        "00045",
        "00046",
        "00047",
        "00048",
        "00049",
        "00050",
        "00051",
        "00052",
        "00053",
        "00054",
        "3_2_3",
    ]

    def __init__(self, verbose: bool = False):
        """
        Initialize generator.

        Args:
            verbose: Enable verbose output
        """
        self.verbose = verbose
        self.xsd_base_path = Path(__file__).parent.parent / "demos" / "xsd"
        self.output_base_path = (
            Path(__file__).parent.parent / "src" / "armodel" / "cfg" / "xsd_metadata"
        )

    def generate(self, version: str) -> bool:
        """
        Generate YAML metadata for a specific schema version.

        Args:
            version: Schema version (e.g., "00046")

        Returns:
            True if successful, False otherwise
        """
        if version not in self.SUPPORTED_VERSIONS:
            print(f"Error: Unsupported version '{version}'")
            print(f"Supported versions: {', '.join(self.SUPPORTED_VERSIONS)}")
            return False

        # Construct paths
        xsd_file = self.xsd_base_path / f"AUTOSAR_{version}" / f"AUTOSAR_{version}.xsd"
        output_file = self.output_base_path / f"schema_{version}.yaml"

        if self.verbose:
            print(f"Generating metadata for version {version}")
            print(f"  XSD file: {xsd_file}")
            print(f"  Output file: {output_file}")

        # Check XSD exists
        if not xsd_file.exists():
            # Try COMPACT version for older schemas
            compact_file = (
                self.xsd_base_path / f"AUTOSAR_{version}" / f"AUTOSAR_{version}_COMPACT.xsd"
            )
            if compact_file.exists():
                xsd_file = compact_file
                if self.verbose:
                    print(f"  Using COMPACT version: {xsd_file}")
            else:
                print(f"Error: XSD file not found: {xsd_file}")
                return False

        try:
            # Parse XSD
            if self.verbose:
                print("  Parsing XSD...")

            parser = XSDParser(xsd_file)
            parser.parse()

            # Convert to dictionary
            if self.verbose:
                print("  Converting to dictionary...")

            metadata = parser.to_dict()

            # Add indexes for fast lookups
            if self.verbose:
                print("  Building indexes...")

            metadata["indexes"] = self._build_indexes(parser)

            # Create output directory if needed
            output_file.parent.mkdir(parents=True, exist_ok=True)

            # Write YAML
            if self.verbose:
                print("  Writing YAML...")

            with open(output_file, "w") as f:
                yaml.dump(metadata, f, default_flow_style=False, sort_keys=False)

            # Summary
            if self.verbose:
                print("\nGeneration complete!")
                print(f"  Complex types: {len(parser.complex_types)}")
                print(f"  Simple types: {len(parser.simple_types)}")
                print(f"  Inheritance mappings: {len(parser.inheritance_map)}")

            return True

        except Exception as e:
            print(f"Error: Failed to generate metadata: {e}")
            if self.verbose:
                import traceback

                traceback.print_exc()
            return False

    def generate_all(self) -> bool:
        """
        Generate metadata for all supported schema versions.

        Returns:
            True if all successful, False otherwise
        """
        print(f"Generating metadata for {len(self.SUPPORTED_VERSIONS)} versions...")

        success_count = 0
        failed_versions = []

        for version in self.SUPPORTED_VERSIONS:
            print(f"\n--- Processing version {version} ---")
            if self.generate(version):
                success_count += 1
            else:
                failed_versions.append(version)

        # Summary
        print(f"\n{'=' * 60}")
        print("Generation complete!")
        print(f"  Successful: {success_count}/{len(self.SUPPORTED_VERSIONS)}")

        if failed_versions:
            print(f"  Failed: {', '.join(failed_versions)}")
            return False

        return True

    def validate(self, version: str) -> bool:
        """
        Validate existing YAML metadata against XSD.

        Args:
            version: Schema version to validate

        Returns:
            True if valid, False otherwise
        """
        yaml_file = self.output_base_path / f"schema_{version}.yaml"

        if not yaml_file.exists():
            print(f"Error: YAML file not found: {yaml_file}")
            return False

        # Load YAML
        with open(yaml_file, "r") as f:
            yaml_metadata = yaml.safe_load(f)

        # Regenerate from XSD
        xsd_file = self.xsd_base_path / f"AUTOSAR_{version}" / f"AUTOSAR_{version}.xsd"
        if not xsd_file.exists():
            compact_file = (
                self.xsd_base_path / f"AUTOSAR_{version}" / f"AUTOSAR_{version}_COMPACT.xsd"
            )
            if compact_file.exists():
                xsd_file = compact_file
            else:
                print(f"Error: XSD file not found: {xsd_file}")
                return False

        parser = XSDParser(xsd_file)
        parser.parse()
        xsd_metadata = parser.to_dict()
        xsd_metadata["indexes"] = self._build_indexes(parser)

        # Compare
        yaml_version = yaml_metadata.get("version")
        xsd_version = xsd_metadata.get("version")

        if yaml_version != xsd_version:
            print(f"Version mismatch: YAML={yaml_version}, XSD={xsd_version}")
            return False

        # Compare complex types count
        yaml_complex_count = len(yaml_metadata.get("complex_types", {}))
        xsd_complex_count = len(xsd_metadata.get("complex_types", {}))

        if yaml_complex_count != xsd_complex_count:
            print(
                f"Complex types count mismatch: YAML={yaml_complex_count}, XSD={xsd_complex_count}"
            )
            return False

        # Compare simple types count
        yaml_simple_count = len(yaml_metadata.get("simple_types", {}))
        xsd_simple_count = len(xsd_metadata.get("simple_types", {}))

        if yaml_simple_count != xsd_simple_count:
            print(f"Simple types count mismatch: YAML={yaml_simple_count}, XSD={xsd_simple_count}")
            return False

        print(f"Validation successful for version {version}")
        print(f"  Complex types: {yaml_complex_count}")
        print(f"  Simple types: {yaml_simple_count}")

        return True

    def _build_indexes(self, parser: XSDParser) -> dict:
        """
        Build fast lookup indexes.

        Args:
            parser: Parsed XSD data

        Returns:
            Dictionary of indexes
        """
        element_to_types = {}
        type_to_elements = {}

        # Build element -> types mapping
        for type_name, type_info in parser.complex_types.items():
            for elem in type_info.elements:
                elem_name = elem.name
                if elem_name not in element_to_types:
                    element_to_types[elem_name] = []
                element_to_types[elem_name].append(type_name)

        # Build type -> elements mapping (including inherited)
        for type_name, type_info in parser.complex_types.items():
            all_elements = parser.get_all_elements_for_type(type_name)
            type_to_elements[type_name] = [
                {
                    "name": elem.name,
                    "type": elem.type,
                    "min_occurs": elem.min_occurs,
                    "max_occurs": elem.max_occurs,
                    "required": elem.required,
                }
                for elem in all_elements
            ]

        return {"element_to_types": element_to_types, "type_to_elements": type_to_elements}


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Generate XSD metadata YAML files from AUTOSAR schemas",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                           # Generate for default version (00046)
  %(prog)s --version 00048           # Generate for specific version
  %(prog)s --all                     # Generate for all versions
  %(prog)s --version 00046 --validate  # Validate existing YAML
  %(prog)s --version 00046 --verbose    # Verbose output
        """,
    )

    parser.add_argument(
        "--version",
        choices=XSDMetadataGenerator.SUPPORTED_VERSIONS,
        help="Schema version to generate (default: 00046)",
    )

    parser.add_argument(
        "--all", action="store_true", help="Generate metadata for all supported versions"
    )

    parser.add_argument(
        "--validate",
        action="store_true",
        help="Validate existing YAML against XSD (does not regenerate)",
    )

    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")

    args = parser.parse_args()

    generator = XSDMetadataGenerator(verbose=args.verbose)

    # Execute requested action
    if args.all:
        success = generator.generate_all()
        sys.exit(0 if success else 1)

    # Determine version
    version = args.version or "00046"

    if args.validate:
        success = generator.validate(version)
        sys.exit(0 if success else 1)

    success = generator.generate(version)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
