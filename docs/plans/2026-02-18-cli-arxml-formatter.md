# CLI ARXML Formatter Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build a multi-command CLI interface for py-armodel2 starting with the `armodel format` command that reads unformatted ARXML files and produces formatted output.

**Architecture:** Multi-command CLI structure using argparse for command routing. The `format` command wraps existing ARXMLReader/ARXMLWriter infrastructure with configurable error handling via GlobalSettingsManager. Each command is a separate module for future extensibility.

**Tech Stack:** argparse (stdlib), existing ARXMLReader/ARXMLWriter classes, GlobalSettingsManager singleton, pytest for testing

---

## Task 1: Create CLI common utilities module

**Files:**
- Create: `src/armodel/cli/common.py`

**Context:** Shared utilities for CLI commands including exit code constants and file I/O helpers. This follows the DRY principle by centralizing common functionality.

**Step 1: Create common.py with exit codes and file helpers**

```python
"""Common utilities for CLI commands."""

from pathlib import Path
from typing import Optional


# Exit code constants
EXIT_SUCCESS = 0
EXIT_FILE_NOT_FOUND = 1
EXIT_PARSE_ERROR = 2
EXIT_WRITE_ERROR = 3
EXIT_UNHANDLED_ERROR = 4


def validate_input_file(filepath: str) -> Path:
    """Validate input file exists and is readable.

    Args:
        filepath: Input file path

    Returns:
        Path object for validated file

    Raises:
        FileNotFoundError: If file doesn't exist
        PermissionError: If file isn't readable
    """
    path = Path(filepath)

    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {filepath}")

    if not path.is_file():
        raise ValueError(f"Input path is not a file: {filepath}")

    if not path.is_file() or not path.readable():
        raise PermissionError(f"Cannot read input file: {filepath}")

    return path


def prepare_output_file(filepath: str) -> Path:
    """Prepare output file path (create parent directories if needed).

    Args:
        filepath: Output file path

    Returns:
        Path object for output file

    Raises:
        ValueError: If output path is a directory
    """
    path = Path(filepath)

    if path.exists() and path.is_dir():
        raise ValueError(f"Output path is a directory: {filepath}")

    # Create parent directories if they don't exist
    path.parent.mkdir(parents=True, exist_ok=True)

    return path
```

**Step 2: Run linter to verify code quality**

Run: `ruff check src/armodel/cli/common.py`
Expected: No errors

**Step 3: Run type checker**

Run: `mypy src/armodel/cli/common.py`
Expected: No errors

**Step 4: Commit**

```bash
git add src/armodel/cli/common.py
git commit -m "feat: add CLI common utilities with exit codes and file helpers

Add shared utilities for CLI commands including exit code constants
and file validation helpers. This provides a foundation for CLI commands.

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

## Task 2: Create CLI main entry point

**Files:**
- Create: `src/armodel/cli/main.py`
- Modify: `src/armodel/cli/__init__.py`

**Context:** The main entry point that routes CLI commands. Uses argparse for multi-command structure. Already configured in pyproject.toml:39 as entry point.

**Step 1: Write the failing test for main.py structure**

Create: `tests/unit/cli/test_main.py`

```python
"""Tests for CLI main entry point."""

from unittest.mock import patch
import pytest


def test_main_help_displays():
    """Test that main help message displays correctly."""
    with patch('sys.argv', ['armodel', '--help']):
        # Should show help and exit
        with pytest.raises(SystemExit) as exc_info:
            from armodel.cli.main import main
            main()
        # Help exits with code 0
        assert exc_info.value.code == 0


def test_main_version_displays():
    """Test that version information displays."""
    with patch('sys.argv', ['armodel', '--version']):
        # Should show version and exit
        with pytest.raises(SystemExit) as exc_info:
            from armodel.cli.main import main
            main()
        # Version exits with code 0
        assert exc_info.value.code == 0
```

**Step 2: Run test to verify it fails**

Run: `PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/unit/cli/test_main.py -v`
Expected: FAIL with "No module named 'armodel.cli.main'"

**Step 3: Create main.py with basic CLI structure**

```python
"""CLI main entry point for py-armodel2."""

import argparse
import sys


def get_version() -> str:
    """Get package version."""
    try:
        from importlib.metadata import version
        return version("armodel2")
    except Exception:
        return "0.1.0"


def create_parser() -> argparse.ArgumentParser:
    """Create the main argument parser.

    Returns:
        Configured ArgumentParser
    """
    parser = argparse.ArgumentParser(
        prog="armodel",
        description="Command-line interface for AUTOSAR ARXML model processing",
    )

    parser.add_argument(
        "--version",
        action="store_true",
        help="Show version information and exit",
    )

    # Subcommands
    subparsers = parser.add_subparsers(
        dest="command",
        help="Available commands",
        metavar="COMMAND",
    )

    # Format subcommand (placeholder for now)
    format_parser = subparsers.add_parser(
        "format",
        help="Format ARXML files",
        description="Format ARXML files with pretty-printing",
    )
    format_parser.add_argument(
        "input",
        help="Input ARXML file to format",
    )
    format_parser.add_argument(
        "-o", "--output",
        required=True,
        help="Output ARXML file path",
    )
    format_parser.add_argument(
        "--strict",
        action="store_true",
        help="Enable strict validation (fail on errors)",
    )
    format_parser.add_argument(
        "--permissive",
        action="store_true",
        help="Enable permissive mode (continue on warnings)",
    )
    format_parser.add_argument(
        "--encoding",
        default="UTF-8",
        help="Output encoding (default: UTF-8)",
    )
    format_parser.add_argument(
        "--no-pretty-print",
        action="store_true",
        help="Disable pretty-printing",
    )
    format_parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Show detailed error messages",
    )
    format_parser.add_argument(
        "-q", "--quiet",
        action="store_true",
        help="Suppress output messages",
    )

    return parser


def main() -> int:
    """Main CLI entry point.

    Returns:
        Exit code
    """
    parser = create_parser()
    args = parser.parse_args()

    # Handle --version flag
    if args.version:
        print(f"armodel {get_version()}")
        return 0

    # If no command specified, show help
    if args.command is None:
        parser.print_help()
        return 0

    # Route to command handler
    if args.command == "format":
        from armodel.cli.commands.format import format_command
        return format_command(args)

    parser.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

**Step 4: Update cli/__init__.py**

```python
"""CLI module for py-armodel2."""

from armodel.cli.main import main

__all__ = ["main"]
```

**Step 5: Run test to verify it passes**

Run: `PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/unit/cli/test_main.py::test_main_help_displays -v`
Expected: PASS (may need to adjust for argparse behavior)

**Step 6: Run linter**

Run: `ruff check src/armodel/cli/`
Expected: No errors

**Step 7: Run type checker**

Run: `mypy src/armodel/cli/`
Expected: No errors

**Step 8: Commit**

```bash
git add src/armodel/cli/main.py src/armodel/cli/__init__.py tests/unit/cli/test_main.py
git commit -m "feat: add CLI main entry point with multi-command structure

Add main.py with argparse-based CLI router supporting --version and
placeholder for format command. Structure enables future commands.

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

## Task 3: Create commands package structure

**Files:**
- Create: `src/armodel/cli/commands/__init__.py`

**Context:** Package for CLI command implementations. Each command will be a separate module.

**Step 1: Create commands/__init__.py**

```python
"""CLI command implementations.

This package contains individual command modules for the CLI.
Each command is implemented as a separate function that receives
parsed arguments and returns an exit code.
"""

# Command registry for future extensibility
COMMANDS = {
    "format": "armodel.cli.commands.format",
}

__all__ = ["COMMANDS"]
```

**Step 2: Run linter**

Run: `ruff check src/armodel/cli/commands/__init__.py`
Expected: No errors

**Step 3: Commit**

```bash
git add src/armodel/cli/commands/__init__.py
git commit -m "feat: add CLI commands package structure

Create package for CLI command implementations with command
registry for extensibility.

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

## Task 4: Implement format command

**Files:**
- Create: `src/armodel/cli/commands/format.py`

**Context:** The core format command implementation. Uses ARXMLReader to load, ARXMLWriter to save, and integrates with GlobalSettingsManager for error handling configuration.

**Step 1: Write the failing test for format command**

Create: `tests/unit/cli/commands/test_format.py`

```python
"""Tests for format command."""

import tempfile
from pathlib import Path
from unittest.mock import Mock, patch
import pytest

from armodel.cli.common import EXIT_SUCCESS, EXIT_FILE_NOT_FOUND, EXIT_PARSE_ERROR


def test_format_command_missing_input_file():
    """Test format command with missing input file."""
    from argparse import Namespace

    args = Namespace(
        input="/nonexistent/file.arxml",
        output="/tmp/output.arxml",
        strict=False,
        permissive=False,
        encoding="UTF-8",
        no_pretty_print=False,
        verbose=False,
        quiet=False,
    )

    from armodel.cli.commands.format import format_command
    result = format_command(args)

    assert result == EXIT_FILE_NOT_FOUND


@patch('armodel.cli.commands.format.ARXMLReader')
@patch('armodel.cli.commands.format.ARXMLWriter')
def test_format_command_success(mock_writer_class, mock_reader_class):
    """Test format command with valid file."""
    from argparse import Namespace

    # Mock ARXMLReader
    mock_reader = Mock()
    mock_autosar = Mock()
    mock_reader.load_arxml.return_value = mock_autosar
    mock_reader_class.return_value = mock_reader

    # Mock ARXMLWriter
    mock_writer = Mock()
    mock_writer_class.return_value = mock_writer

    with tempfile.NamedTemporaryFile(suffix=".arxml", delete=False) as tmp:
        tmp.write(b"<AUTOSAR/>")
        tmp_path = tmp.name

    try:
        with tempfile.NamedTemporaryFile(suffix=".arxml", delete=False) as out_tmp:
            output_path = out_tmp.name

        args = Namespace(
            input=tmp_path,
            output=output_path,
            strict=False,
            permissive=False,
            encoding="UTF-8",
            no_pretty_print=False,
            verbose=False,
            quiet=False,
        )

        from armodel.cli.commands.format import format_command
        result = format_command(args)

        assert result == EXIT_SUCCESS
        mock_reader.load_arxml.assert_called_once()
        mock_writer.save_arxml.assert_called_once_with(mock_autosar, Path(output_path))
    finally:
        Path(tmp_path).unlink(missing_ok=True)
        Path(output_path).unlink(missing_ok=True)
```

**Step 2: Run test to verify it fails**

Run: `PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/unit/cli/commands/test_format.py -v`
Expected: FAIL with "No module named 'armodel.cli.commands.format'"

**Step 3: Implement format command**

```python
"""Format command implementation."""

import sys
from pathlib import Path
from typing import Union

from armodel.cli.common import (
    EXIT_SUCCESS,
    EXIT_FILE_NOT_FOUND,
    EXIT_PARSE_ERROR,
    EXIT_WRITE_ERROR,
    EXIT_UNHANDLED_ERROR,
    validate_input_file,
    prepare_output_file,
)
from armodel.core import GlobalSettingsManager
from armodel.reader import ARXMLReader
from armodel.writer import ARXMLWriter


def format_command(args) -> int:
    """Execute format command.

    Args:
        args: Parsed command-line arguments

    Returns:
        Exit code
    """
    try:
        # Validate input file
        input_path = validate_input_file(args.input)

        # Prepare output file
        output_path = prepare_output_file(args.output)

        # Configure global settings based on CLI arguments
        settings = GlobalSettingsManager()

        if args.strict:
            settings.strict_validation = True
        elif args.permissive:
            settings.strict_validation = False

        # Load ARXML file
        reader = ARXMLReader()

        if not args.quiet:
            print(f"Loading ARXML file: {input_path}")

        try:
            autosar = reader.load_arxml(str(input_path))
        except Exception as e:
            if args.verbose:
                print(f"Error parsing ARXML: {e}", file=sys.stderr)
            else:
                print(f"Error parsing ARXML file: {e}", file=sys.stderr)
            return EXIT_PARSE_ERROR

        # Write formatted ARXML
        writer = ARXMLWriter(
            pretty_print=not args.no_pretty_print,
            encoding=args.encoding,
        )

        if not args.quiet:
            print(f"Writing formatted ARXML to: {output_path}")

        try:
            writer.save_arxml(autosar, str(output_path))
        except Exception as e:
            if args.verbose:
                print(f"Error writing file: {e}", file=sys.stderr)
            else:
                print(f"Error writing output file: {e}", file=sys.stderr)
            return EXIT_WRITE_ERROR

        if not args.quiet:
            print("Formatting complete.")

        return EXIT_SUCCESS

    except FileNotFoundError as e:
        print(str(e), file=sys.stderr)
        return EXIT_FILE_NOT_FOUND
    except Exception as e:
        if args.verbose:
            import traceback
            traceback.print_exc()
        else:
            print(f"Unexpected error: {e}", file=sys.stderr)
        return EXIT_UNHANDLED_ERROR
```

**Step 4: Run tests to verify they pass**

Run: `PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/unit/cli/commands/test_format.py -v`
Expected: PASS

**Step 5: Run linter**

Run: `ruff check src/armodel/cli/commands/format.py`
Expected: No errors

**Step 6: Run type checker**

Run: `mypy src/armodel/cli/commands/format.py`
Expected: No errors

**Step 7: Commit**

```bash
git add src/armodel/cli/commands/format.py tests/unit/cli/commands/test_format.py
git commit -m "feat: implement format command for ARXML formatting

Add format command that reads unformatted ARXML files and produces
formatted output using ARXMLReader and ARXMLWriter. Supports
--strict/--permissive modes via GlobalSettingsManager integration.

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

## Task 5: Integration test with real ARXML file

**Files:**
- Create: `tests/integration/cli/test_format_command.py`

**Context:** End-to-end test with real ARXML files to ensure the format command works correctly with actual data.

**Step 1: Write integration test**

```python
"""Integration tests for CLI format command."""

import subprocess
import tempfile
from pathlib import Path
import pytest


def test_format_command_integration():
    """Test format command with real ARXML file."""
    # Use existing test fixture
    fixture_path = Path("tests/fixtures/arxml/AUTOSAR_Datatypes.arxml")

    if not fixture_path.exists():
        pytest.skip("Test fixture not available")

    with tempfile.NamedTemporaryFile(suffix=".arxml", delete=False) as tmp:
        output_path = tmp.name

    try:
        # Run CLI command
        result = subprocess.run(
            ["python", "-m", "armodel.cli.main", "format",
             str(fixture_path), "-o", output_path],
            capture_output=True,
            text=True,
            env={"PYTHONPATH": "/Users/ray/Workspace/py-armodel2/src"},
        )

        assert result.returncode == 0, f"CLI failed: {result.stderr}"

        # Verify output file was created
        output = Path(output_path)
        assert output.exists()

        # Verify output is valid XML
        content = output.read_text()
        assert "<?xml" in content
        assert "<AUTOSAR" in content

    finally:
        Path(output_path).unlink(missing_ok=True)


def test_format_command_nonexistent_file():
    """Test format command with nonexistent input file."""
    result = subprocess.run(
        ["python", "-m", "armodel.cli.main", "format",
         "/nonexistent/file.arxml", "-o", "/tmp/output.arxml"],
        capture_output=True,
        text=True,
        env={"PYTHONPATH": "/Users/ray/Workspace/py-armodel2/src"},
    )

    assert result.returncode == 1  # EXIT_FILE_NOT_FOUND
    assert "not found" in result.stderr.lower()
```

**Step 2: Run integration test**

Run: `PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/integration/cli/test_format_command.py -v`
Expected: PASS (may skip if fixture not available)

**Step 3: Commit**

```bash
git add tests/integration/cli/test_format_command.py
git commit -m "test: add integration tests for format command

Add end-to-end tests using real ARXML files to verify format
command works correctly with actual AUTOSAR data.

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

## Task 6: Verify CLI as installed package

**Context:** Ensure the CLI entry point configured in pyproject.toml works correctly when the package is installed.

**Step 1: Install package in development mode**

Run: `pip install -e .`
Expected: Successfully installs armodel2 with CLI entry point

**Step 2: Test CLI entry point**

Run: `armodel --version`
Expected: Displays version information

Run: `armodel --help`
Expected: Displays help message

**Step 3: Test format command**

Run: `armodel format tests/fixtures/arxml/AUTOSAR_Datatypes.arxml -o /tmp/test_output.arxml`
Expected: Successfully formats file (may skip if fixture not available)

**Step 4: Clean up test output**

Run: `rm /tmp/test_output.arxml`
Expected: File removed

**Step 5: Update documentation**

Add CLI usage to README.md or create separate CLI documentation.

**Step 6: Commit documentation updates**

```bash
git add README.md docs/  # As applicable
git commit -m "docs: add CLI usage documentation

Document the new armodel CLI with format command usage examples.

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

## Task 7: Final verification and cleanup

**Context:** Run full test suite, lint, and type check to ensure everything works together.

**Step 1: Run full test suite**

Run: `PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest`
Expected: All tests pass

**Step 2: Run linter on entire codebase**

Run: `ruff check src/ tests/`
Expected: No errors

**Step 3: Run type checker**

Run: `mypy src/`
Expected: No new errors (existing model errors are exempt)

**Step 4: Final commit**

```bash
git add .
git commit -m "feat: complete CLI formatter implementation

Complete implementation of multi-command CLI interface with format
command. All tests passing, lint and type check clean.

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

## References

- Design document: `docs/plans/2026-02-18-cli-arxml-formatter-design.md`
- ARXMLReader: `src/armodel/reader/__init__.py`
- ARXMLWriter: `src/armodel/writer/__init__.py`
- GlobalSettingsManager: `src/armodel/core/global_settings.py`
- Test fixtures: `tests/fixtures/arxml/`, `demos/arxml/`
- Development commands: Run tests with `PYTHONPATH` set, use ruff/mypy for quality checks
