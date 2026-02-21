"""CLI tool for validating JSON class definitions against AUTOSAR XSD schema."""

import argparse
import sys
from pathlib import Path

from tools.validation.comparator import SchemaComparator
from tools.validation.json_loader import JSONClassLoader
from tools.validation.models import DiscrepancySeverity
from tools.validation.reporter import DiscrepancyReporter
from tools.validation.xsd_parser import XSDParser


def create_parser() -> argparse.ArgumentParser:
    """Create CLI argument parser.

    Returns:
        Configured ArgumentParser
    """
    parser = argparse.ArgumentParser(
        prog="validate_json_against_xsd",
        description="Validate JSON class definitions against AUTOSAR XSD schema",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Validate all classes against AUTOSAR 00052
  python -m tools.validation

  # Validate specific class
  python -m tools.validation --class Collection

  # Save Markdown report
  python -m tools.validation --output validation_report.md

  # Only show errors and warnings
  python -m tools.validation --severity WARNING

  # Use different XSD version
  python -m tools.validation --xsd-version 00051
        """,
    )

    parser.add_argument(
        "--xsd-version",
        default="00052",
        help="AUTOSAR XSD schema version (default: 00052)",
    )

    parser.add_argument(
        "--class",
        dest="class_name",
        help="Validate only specific class (e.g., Collection)",
    )

    parser.add_argument(
        "-o",
        "--output",
        help="Output Markdown report file path",
    )

    parser.add_argument(
        "--severity",
        choices=["ERROR", "WARNING", "INFO"],
        default="INFO",
        help="Minimum severity level to include (default: INFO)",
    )

    parser.add_argument(
        "--no-color",
        action="store_true",
        help="Disable colored console output",
    )

    parser.add_argument(
        "--json-dir",
        default="docs/json/packages",
        help="Directory containing JSON package files (default: docs/json/packages)",
    )

    parser.add_argument(
        "--xsd-dir",
        default="demos/xsd",
        help="Directory containing XSD schema files (default: demos/xsd)",
    )

    parser.add_argument(
        "--skip-list",
        default="tools/skip_classes.yaml",
        help="Path to skip_classes.yaml file (default: tools/skip_classes.yaml)",
    )

    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Show verbose output",
    )

    return parser


def main() -> int:
    """Main CLI entry point.

    Returns:
        Exit code (0 on success, 1 on validation failures)
    """
    parser = create_parser()
    args = parser.parse_args()

    try:
        # Construct XSD file path
        xsd_dir = Path(args.xsd_dir)
        xsd_version = args.xsd_version
        xsd_file = xsd_dir / f"AUTOSAR_{xsd_version}" / f"AUTOSAR_{xsd_version}.xsd"

        if not xsd_file.exists():
            print(f"Error: XSD file not found: {xsd_file}", file=sys.stderr)
            return 1

        if args.verbose:
            print(f"Loading XSD schema: {xsd_file}")

        # Parse XSD
        xsd_parser = XSDParser(str(xsd_file))
        xsd_types = xsd_parser.parse()

        if args.verbose:
            print(f"Loaded {len(xsd_types)} complex types from XSD")

        # Load JSON classes
        json_dir = Path(args.json_dir)
        json_loader = JSONClassLoader(str(json_dir))
        json_classes = json_loader.load_all()

        # Load skip list
        skip_classes = json_loader.load_skip_list(args.skip_list)

        if args.verbose:
            print(f"Loaded {len(json_classes)} classes from JSON")
            print(f"Skip list contains {len(skip_classes)} classes")

        # Filter to specific class if requested
        if args.class_name:
            if args.class_name not in json_classes:
                print(f"Error: Class '{args.class_name}' not found in JSON definitions", file=sys.stderr)
                return 1

            json_classes = {args.class_name: json_classes[args.class_name]}

            if args.verbose:
                print(f"Validating single class: {args.class_name}")

        # Compare schemas
        comparator = SchemaComparator(skip_classes=skip_classes)
        discrepancies = comparator.compare_all(json_classes, xsd_types)

        # Generate report
        severity = DiscrepancySeverity[args.severity]
        reporter = DiscrepancyReporter(discrepancies, use_colors=not args.no_color)

        # Print console report
        exit_code = reporter.print_console_report(severity)

        # Generate Markdown report if requested
        if args.output:
            reporter.generate_markdown_report(args.output, severity)

        return exit_code

    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        if args.verbose:
            import traceback

            traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())