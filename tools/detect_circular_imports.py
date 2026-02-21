#!/usr/bin/env python3
"""
Offline circular import detector for AUTOSAR model code.

Analyzes generated code to detect circular import dependencies without
executing any Python imports. Uses JSON-based dependency analysis.

Usage:
    python tools/detect_circular_imports.py
    python tools/detect_circular_imports.py --format json --output report.json
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, List

try:
    import yaml
    _yaml: Any = yaml
except ImportError:
    _yaml = None

# Import from standalone circular import utilities
from circular_import_utils import (
    build_complete_dependency_graph,
    find_all_cycles_in_graph,
    get_class_location,
    load_package_data,
)


def generate_text_report(
    cycles: List[List[str]],
    package_data: Dict[str, Dict[str, Any]]
) -> str:
    """Generate plain text report with detailed information.

    Args:
        cycles: List of circular import cycles
        package_data: Package data dictionary

    Returns:
        Formatted text report string
    """
    lines = [
        "=" * 70,
        "Circular Import Detection Report",
        "=" * 70,
        f"Total cycles found: {len(cycles)}",
        ""
    ]

    if not cycles:
        lines.append("✓ No circular imports detected!")
        lines.append("")
        return "\n".join(lines)

    for i, cycle in enumerate(cycles, 1):
        lines.append(f"Cycle #{i}:")
        lines.append("-" * 70)

        for j, class_name in enumerate(cycle):
            file_path, line_num = get_class_location(class_name, package_data)
            next_class = cycle[(j + 1) % len(cycle)]

            lines.append(f"  {j+1}. {class_name}")
            lines.append(f"     File: {file_path}")
            if line_num > 0:
                lines.append(f"     Line: {line_num}")
            lines.append(f"     Imports: {next_class}")
            lines.append("")

        lines.append("Suggested fix:")
        lines.append(f"  Move import of '{cycle[1]}' to TYPE_CHECKING in '{cycle[0]}'")
        lines.append("  Add to tools/skip_classes.yaml:")
        for class_in_cycle in cycle:
            lines.append(f'    "{class_in_cycle}": "*"')
        lines.append("")

    return "\n".join(lines)


def generate_json_report(
    cycles: List[List[str]],
    package_data: Dict[str, Dict[str, Any]]
) -> str:
    """Generate JSON report for programmatic consumption.

    Args:
        cycles: List of circular import cycles
        package_data: Package data dictionary

    Returns:
        JSON formatted report string
    """
    report = {
        "total_cycles": len(cycles),
        "cycles": []
    }

    for cycle in cycles:
        cycle_info = {
            "classes": [],
            "suggested_fix": {
                "class_to_fix": cycle[0],
                "import_to_move": cycle[1],
                "skip_classes_entries": cycle
            }
        }

        for class_name in cycle:
            file_path, line_num = get_class_location(class_name, package_data)
            cycle_info["classes"].append({
                "name": class_name,
                "file": file_path,
                "line": line_num
            })

        report["cycles"].append(cycle_info)

    return json.dumps(report, indent=2)


def generate_markdown_report(
    cycles: List[List[str]],
    package_data: Dict[str, Dict[str, Any]]
) -> str:
    """Generate Markdown report for documentation.

    Args:
        cycles: List of circular import cycles
        package_data: Package data dictionary

    Returns:
        Markdown formatted report string
    """
    lines = [
        "# Circular Import Detection Report",
        "",
        f"**Total cycles found:** {len(cycles)}",
        ""
    ]

    if not cycles:
        lines.append("✅ **No circular imports detected!**")
        lines.append("")
        return "\n".join(lines)

    for i, cycle in enumerate(cycles, 1):
        lines.append(f"## Cycle #{i}")
        lines.append("")

        for j, class_name in enumerate(cycle):
            file_path, line_num = get_class_location(class_name, package_data)
            next_class = cycle[(j + 1) % len(cycle)]

            lines.append(f"{j+1}. **{class_name}**")
            lines.append(f"   - File: `{file_path}`")
            if line_num > 0:
                lines.append(f"   - Line: {line_num}")
            lines.append(f"   - Imports: `{next_class}`")
            lines.append("")

        lines.append("### Suggested Fix")
        lines.append("")
        lines.append(f"Move import of `{cycle[1]}` to `TYPE_CHECKING` in `{cycle[0]}`:")
        lines.append("")
        lines.append("```yaml")
        lines.append("# Add to tools/skip_classes.yaml")
        lines.append("force_type_checking_imports:")
        for class_in_cycle in cycle:
            lines.append(f'  "{class_in_cycle}": "*"')
        lines.append("```")
        lines.append("")

    return "\n".join(lines)


def main() -> int:
    """Main entry point for the CLI tool."""
    parser = argparse.ArgumentParser(
        description="Detect circular imports in AUTOSAR model code",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic usage - detect all circular imports
  python tools/detect_circular_imports.py

  # Save report to file
  python tools/detect_circular_imports.py --output report.txt

  # JSON output for CI/CD integration
  python tools/detect_circular_imports.py --format json --output report.json

  # Markdown output for documentation
  python tools/detect_circular_imports.py --format markdown --output report.md
        """
    )

    parser.add_argument(
        "--json-dir",
        type=Path,
        default=Path("docs/json/packages"),
        help="Path to JSON package data directory (default: docs/json/packages)"
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("docs/reports/circular_imports.txt"),
        help="Output file for report (default: docs/reports/circular_imports.txt)"
    )
    parser.add_argument(
        "--format",
        choices=["text", "json", "markdown"],
        default="text",
        help="Output format (default: text, inferred from output file extension if specified)"
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Suppress output except for errors"
    )

    args = parser.parse_args()

    # Infer format from output file extension if not explicitly specified
    if args.output and args.format == "text":
        ext = args.output.suffix.lower()
        if ext == ".json":
            args.format = "json"
        elif ext == ".md":
            args.format = "markdown"

    try:
        # Ensure docs/reports directory exists
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)

        # Load package data
        if not args.quiet:
            print(f"Loading package data from: {args.json_dir}", file=sys.stderr)

        package_data = load_package_data(args.json_dir)

        if not args.quiet:
            print(f"Loaded {len(package_data)} packages", file=sys.stderr)

        # Build dependency graph
        if not args.quiet:
            print("Building dependency graph...", file=sys.stderr)

        graph = build_complete_dependency_graph(package_data)

        if not args.quiet:
            print(f"Dependency graph has {len(graph)} classes", file=sys.stderr)

        # Find all cycles
        if not args.quiet:
            print("Detecting circular imports...", file=sys.stderr)

        cycles = find_all_cycles_in_graph(graph)

        # Generate report
        if args.format == "text":
            report = generate_text_report(cycles, package_data)
        elif args.format == "json":
            report = generate_json_report(cycles, package_data)
        elif args.format == "markdown":
            report = generate_markdown_report(cycles, package_data)
        else:
            report = generate_text_report(cycles, package_data)

        # Output
        if args.output:
            args.output.write_text(report)
            if not args.quiet:
                print(f"Report saved to: {args.output}", file=sys.stderr)
        else:
            print(report)

        # Exit with error if cycles found
        if cycles:
            if not args.quiet:
                print(f"\n⚠️  Found {len(cycles)} circular import cycle(s)!", file=sys.stderr)
            return 1
        else:
            if not args.quiet:
                print("\n✅ No circular imports found!", file=sys.stderr)
            return 0

    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 2
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return 3


if __name__ == "__main__":
    sys.exit(main())