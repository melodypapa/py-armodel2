#!/usr/bin/env python3
"""
Format ARXML files using xmllint.

Usage:
    python scripts/format_arxml_xmllint.py                    # Format all files from demos/arxml
    python scripts/format_arxml_xmllint.py <file1> <file2>    # Format specific files
    python scripts/format_arxml_xmllint.py --verbose          # Show detailed output
    python scripts/format_arxml_xmllint.py --dry-run          # List files without formatting
    python scripts/format_arxml_xmllint.py --test             # Format from demos/test
    python scripts/format_arxml_xmllint.py --keep-empty-elements  # Keep empty elements

This script uses xmllint for fast, reliable XML formatting.
Features:
    - XML comments are removed during formatting
    - Original file encoding is always preserved (auto-detected)
    - Empty elements are removed by default (use --keep-empty-elements to preserve)
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Optional

try:
    import chardet
except ImportError:
    chardet = None


def check_xmllint() -> bool:
    """Check if xmllint is available on the system."""
    return shutil.which("xmllint") is not None


def detect_file_encoding(file_path: Path) -> str:
    """
    Detect the encoding of an XML file.

    First checks the XML declaration for encoding attribute.
    If not found or chardet is available, uses chardet for detection.
    Defaults to UTF-8 if unable to detect.

    Args:
        file_path: Path to the file

    Returns:
        Detected encoding string (e.g., 'UTF-8', 'ISO-8859-1', 'UTF-16')
    """
    # First, try to read XML declaration
    try:
        with open(file_path, 'rb') as f:
            # Read first line to check for XML declaration
            first_line = f.readline()
            first_line_str = first_line.decode('utf-8', errors='ignore')

            # Check for encoding attribute in XML declaration
            encoding_match = re.search(r'encoding=["\']([^"\']+)["\']', first_line_str)
            if encoding_match:
                return encoding_match.group(1)
    except Exception:
        pass

    # If no encoding in XML declaration and chardet is available, use it
    if chardet is not None:
        try:
            with open(file_path, 'rb') as f:
                raw_data = f.read()
                result = chardet.detect(raw_data)
                if result and result.get('encoding'):
                    return result['encoding']
        except Exception:
            pass

    # Default to UTF-8
    return 'UTF-8'


def remove_xml_comments(content: str) -> str:
    """
    Remove XML comments from content.

    Args:
        content: XML content as string

    Returns:
        XML content with comments removed
    """
    # Remove XML comments <!-- ... -->
    # This pattern handles multi-line comments and nested comment-like structures
    content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)

    # Remove empty lines (lines with only whitespace)
    # This cleans up the blank lines left behind after removing comments
    lines = content.split('\n')
    non_empty_lines = [line for line in lines if line.strip()]

    # Join with newlines and ensure trailing newline at the end
    result = '\n'.join(non_empty_lines)
    if result:  # Only add trailing newline if content is not empty
        result += '\n'

    return result


def fix_empty_element_indentation(content: str) -> str:
    """
    Fix indentation of empty XML elements.

    xmllint sometimes creates inconsistent indentation for empty elements where
    the closing tag has 2 fewer spaces than the opening tag. This function
    aligns them properly.

    Args:
        content: XML content as string

    Returns:
        XML content with fixed empty element indentation
    """
    lines = content.split('\n')
    result = []

    i = 0
    while i < len(lines):
        current_line = lines[i]

        # Check if current line contains only an opening tag (no closing tag)
        if re.match(r'^(\s*)<(\w+(?:-\w+)*)>\s*$', current_line):
            indent_match = re.match(r'^(\s*)<(\w+(?:-\w+)*)>\s*$', current_line)
            opening_indent = indent_match.group(1)
            tag_name = indent_match.group(2)

            # Check if the next line is the matching closing tag with different indentation
            if i + 1 < len(lines):
                next_line = lines[i + 1]
                closing_pattern = rf'^(\s*)</{tag_name}>\s*$'
                closing_match = re.match(closing_pattern, next_line)

                if closing_match:
                    closing_indent = closing_match.group(1)
                    # If closing indent is less than opening indent (xmllint quirk)
                    if len(closing_indent) < len(opening_indent):
                        # Fix the closing tag indentation to match opening
                        fixed_closing = opening_indent + f'</{tag_name}>'
                        result.append(current_line)
                        result.append(fixed_closing)
                        i += 2
                        continue

        result.append(current_line)
        i += 1

    return '\n'.join(result)


def remove_empty_elements(content: str) -> str:
    """
    Remove empty XML elements from content.

    An empty element is defined as an opening tag followed only by whitespace
    and then a closing tag on the next line, with no content between them.

    Args:
        content: XML content as string

    Returns:
        XML content with empty elements removed
    """
    lines = content.split('\n')
    result = []
    i = 0

    while i < len(lines):
        current_line = lines[i]

        # Check if current line contains only an opening tag (no closing tag, no content)
        if re.match(r'^(\s*)<(\w+(?:-\w+)*)>\s*$', current_line):
            indent_match = re.match(r'^(\s*)<(\w+(?:-\w+)*)>\s*$', current_line)
            tag_name = indent_match.group(2)

            # Check if the next line is the matching closing tag
            if i + 1 < len(lines):
                next_line = lines[i + 1]
                closing_pattern = rf'^\s*</{tag_name}>\s*$'

                if re.match(closing_pattern, next_line):
                    # Skip both lines (remove the empty element)
                    i += 2
                    continue

        result.append(current_line)
        i += 1

    return '\n'.join(result)


def format_arxml(
    input_file: Path,
    output_file: Path,
    indent: int = 2,
    keep_empty_elements: bool = False,
    verbose: bool = False,
) -> tuple[bool, Optional[str]]:
    """
    Format a single ARXML file using xmllint.

    Note: XML comments are removed during formatting.
    Original file encoding is always preserved.

    Args:
        input_file: Path to input ARXML file
        output_file: Path to output formatted file
        indent: Number of spaces for indentation (default: 2)
        keep_empty_elements: If False, remove empty elements (default: False)
        verbose: Show detailed output

    Returns:
        Tuple of (success, error_message)
    """
    if not input_file.exists():
        return False, f"Input file not found: {input_file}"

    # Detect encoding from input file (always preserve original encoding)
    encoding = detect_file_encoding(input_file)
    if verbose:
        print(f"      Detected encoding: {encoding}")

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

        # Remove XML comments from formatted output
        content = remove_xml_comments(result.stdout)

        # Fix empty element indentation if keeping empty elements
        if keep_empty_elements:
            content = fix_empty_element_indentation(content)
        else:
            # Remove empty elements entirely
            content = remove_empty_elements(content)

        # Write the formatted content to output file
        output_file.write_text(content, encoding=encoding)

        return True, None

    except Exception as e:
        return False, str(e)


def format_arxml_to_stdout(
    input_file: Path,
    indent: int = 2,
    keep_empty_elements: bool = False,
) -> tuple[bool, Optional[str]]:
    """
    Format ARXML file and output to stdout.

    Note: XML comments are removed during formatting.
    Original file encoding is preserved.

    Args:
        input_file: Path to input ARXML file
        indent: Number of spaces for indentation (default: 2)
        keep_empty_elements: If False, remove empty elements (default: False)

    Returns:
        Tuple of (success, error_message)
    """
    if not input_file.exists():
        return False, f"Input file not found: {input_file}"

    # Detect encoding from input file
    encoding = detect_file_encoding(input_file)

    try:
        cmd = [
            "xmllint",
            "--format",
            "--encode", encoding,
            str(input_file),
        ]

        # Set indent via environment variable
        env = {"XMLLINT_INDENT": " " * indent}

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            env={**os.environ, **env},
        )

        if result.returncode != 0:
            return False, "xmllint failed"

        # Remove XML comments
        content = remove_xml_comments(result.stdout)

        # Fix empty element indentation if keeping empty elements
        if keep_empty_elements:
            content = fix_empty_element_indentation(content)
        else:
            # Remove empty elements entirely
            content = remove_empty_elements(content)

        print(content, end='')

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
        "--keep-empty-elements",
        action="store_true",
        help="Keep empty XML elements (default: remove them)",
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
        success, error = format_arxml_to_stdout(
            files_to_format[0],
            indent=args.indent,
            keep_empty_elements=args.keep_empty_elements,
        )
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
    empty_elements_action = "Keep" if args.keep_empty_elements else "Remove"
    print(f"Empty elements: {empty_elements_action}")
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
            keep_empty_elements=args.keep_empty_elements,
            verbose=args.verbose,
        )

        if success:
            print("      [OK] Success")
            success_count += 1
        else:
            print("      [FAIL] Failed")
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
            print(f"  [FAIL] {file.name}")
            if args.verbose:
                print(f"    Error: {error}")

    print()
    print(f"Output directory: {args.output}")

    return 1 if failed_count > 0 else 0


if __name__ == "__main__":
    sys.exit(main())