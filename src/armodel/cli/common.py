"""Common utilities for CLI commands."""

import os
from pathlib import Path


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

    if not os.access(filepath, os.R_OK):
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
