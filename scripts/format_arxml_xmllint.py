#!/usr/bin/env python3
"""
Format ARXML files using xmllint.

Usage:
    python scripts/format_arxml_xmllint.py                    # Format all files from demos/arxml
    python scripts/format_arxml_xmllint.py <file1> <file2>    # Format specific files
    python scripts/format_arxml_xmllint.py --verbose          # Show detailed output
    python scripts/format_arxml_xmllint.py --dry-run          # List files without formatting
    python scripts/format_arxml_xmllint.py --test             # Format from demos/test

This script uses xmllint for fast, reliable XML formatting.
"""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Optional


def check_xmllint() -> bool:
    """Check if xmllint is available on the system."""
    return shutil.which("xmllint") is not None


def format_arxml(
    input_file: Path,
    output_file: Path,
    indent: int = 2,
    encoding: str = "UTF-8",
    verbose: bool = False,
) -> tuple[bool, Optional[str]]:
    """
    Format a single ARXML file using xmllint.

    Args:
        input_file: Path to input ARXML file
        output_file: Path to output formatted file
        indent: Number of spaces for indentation (default: 2)
        encoding: Output encoding (default: UTF-8)
        verbose: Show detailed output

    Returns:
        Tuple of (success, error_message)
    """
    if not input_file.exists():
        return False, f"Input file not found: {input_file}"

    # Ensure output directory exists
    output_file.parent.mkdir(parents=True, exist_ok=True)

    try:
        # Build xmllint command
        # Note: macOS xmllint doesn't support --indent N, use XMLLINT_INDENT env var
        cmd = [
            "xmllint",
            "--format",
            "--encode", encoding,
            str(input_file),
            "--output", str(output_file),
        ]

        # Set indent via environment variable
        env = {"XMLLINT_INDENT": " " * indent}

        if verbose:
            print(f"      Running: {' '.join(cmd)}")
            print(f"      XMLLINT_INDENT: '{' ' * indent}'")

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            env={**os.environ, **env},
        )

        if result.returncode != 0:
            error_msg = result.stderr.strip() if result.stderr else "Unknown error"
            return False, error_msg

        return True, None

    except Exception as e:
        return False, str(e)


def format_arxml_to_stdout(
    input_file: Path,
    indent: int = 2,
) -> tuple[bool, Optional[str]]:
    """
    Format ARXML file and output to stdout.

    Args:
        input_file: Path to input ARXML file
        indent: Number of spaces for indentation (default: 2)

    Returns:
        Tuple of (success, error_message)
    """
    if not input_file.exists():
        return False, f"Input file not found: {input_file}"

    try:
        cmd = [
            "xmllint",
            "--format",
            str(input_file),
        ]

        # Set indent via environment variable
        env = {"XMLLINT_INDENT": " " * indent}

        result = subprocess.run(
            cmd,
            capture_output=False,
            text=True,
            env={**os.environ, **env},
        )

        if result.returncode != 0:
            return False, "xmllint failed"

        return True, None

    except Exception as e:
        return False, str(e)


def main() -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Format ARXML files using xmllint",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    %(prog)s                              # Format all files from demos/arxml
    %(prog)s BswM.arxml Can.arxml         # Format specific files
    %(prog)s --verbose                    # Format with detailed output
    %(prog)s --dry-run                    # List files without formatting
    %(prog)s --test                       # Format from demos/test
    %(prog)s --stdout file.arxml          # Output to stdout
    %(prog)s -i input.arxml -o output.arxml  # Single file with paths
""",
    )

    # Positional arguments for specific files
    parser.add_argument(
        "files",
        nargs="*",
        help="Specific ARXML files to format (default: all in input directory)",
    )

    # Directory options
    parser.add_argument(
        "-i", "--input",
        type=Path,
        default=Path("demos/arxml"),
        help="Input directory (default: demos/arxml)",
    )
    parser.add_argument(
        "-o", "--output",
        type=Path,
        default=Path("formatted/arxml"),
        help="Output directory (default: formatted/arxml)",
    )

    # Preset directories
    parser.add_argument(
        "--test",
        action="store_true",
        help="Use demos/test -> formatted/test",
    )
    parser.add_argument(
        "--validated",
        action="store_true",
        help="Use demos/validated -> formatted/validated",
    )
    parser.add_argument(
        "--test-validated",
        action="store_true",
        help="Use demos/test_validated -> formatted/test_validated",
    )

    # Formatting options
    parser.add_argument(
        "--indent",
        type=int,
        default=2,
        help="Indentation spaces (default: 2)",
    )
    parser.add_argument(
        "--encoding",
        default="UTF-8",
        help="Output encoding (default: UTF-8)",
    )

    # Output options
    parser.add_argument(
        "--stdout",
        action="store_true",
        help="Output formatted XML to stdout instead of file",
    )

    # Flags
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Show detailed output",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="List files without formatting",
    )

    args = parser.parse_args()

    # Check xmllint availability
    if not check_xmllint():
        print("Error: xmllint not found. Please install libxml2.", file=sys.stderr)
        print("  macOS: brew install libxml2", file=sys.stderr)
        print("  Ubuntu: sudo apt-get install libxml2-utils", file=sys.stderr)
        return 1

    # Handle presets
    if args.test:
        args.input = Path("demos/test")
        args.output = Path("formatted/test")
    elif args.validated:
        args.input = Path("demos/validated")
        args.output = Path("formatted/validated")
    elif args.test_validated:
        args.input = Path("demos/test_validated")
        args.output = Path("formatted/test_validated")

    # Get files to format
    if args.files:
        files_to_format = [Path(f) if Path(f).is_absolute() else args.input / f for f in args.files]
    else:
        if not args.input.exists():
            print(f"Error: Input directory not found: {args.input}", file=sys.stderr)
            return 1
        files_to_format = sorted(args.input.glob("*.arxml"))

    if not files_to_format:
        print(f"No ARXML files found in {args.input}", file=sys.stderr)
        return 1

    # Handle stdout mode
    if args.stdout:
        if len(files_to_format) > 1:
            print("Error: --stdout can only be used with a single file", file=sys.stderr)
            return 1
        success, error = format_arxml_to_stdout(files_to_format[0], indent=args.indent)
        if not success:
            print(f"Error: {error}", file=sys.stderr)
            return 1
        return 0

    # Print header
    print("=" * 40)
    print("ARXML Format Script (xmllint)")
    print("=" * 40)
    print(f"Input:    {args.input}")
    print(f"Output:   {args.output}")
    print(f"Files:    {len(files_to_format)}")
    print(f"Indent:   {args.indent} spaces")
    print(f"Encoding: {args.encoding}")
    print()

    # Dry run: just list files
    if args.dry_run:
        print("Files to be formatted:")
        for i, file in enumerate(files_to_format, 1):
            print(f"  [{i}] {file.name}")
        print()
        print("Dry run complete. No files were modified.")
        return 0

    # Process files
    success_count = 0
    failed_count = 0
    failed_files: list[tuple[Path, str]] = []

    for i, input_file in enumerate(files_to_format, 1):
        output_file = args.output / input_file.name

        print(f"[{i}/{len(files_to_format)}] Formatting: {input_file.name}")

        success, error = format_arxml(
            input_file,
            output_file,
            indent=args.indent,
            encoding=args.encoding,
            verbose=args.verbose,
        )

        if success:
            print("      ✓ Success")
            success_count += 1
        else:
            print("      ✗ Failed")
            failed_count += 1
            if error:
                failed_files.append((input_file, error))

    # Print summary
    print()
    print("=" * 40)
    print("Formatting Summary:")
    print("=" * 40)
    print(f"Total files:     {len(files_to_format)}")
    print(f"Successful:      {success_count}")
    print(f"Failed:          {failed_count}")

    if failed_files:
        print()
        print("Failed files:")
        for file, error in failed_files:
            print(f"  ✗ {file.name}")
            if args.verbose:
                print(f"    Error: {error}")

    print()
    print(f"Output directory: {args.output}")

    return 1 if failed_count > 0 else 0


if __name__ == "__main__":
    sys.exit(main())