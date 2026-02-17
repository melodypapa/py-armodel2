"""Integration tests for CLI format command."""

import os
import subprocess
import sys
import tempfile
from pathlib import Path
import pytest


# Get the src directory dynamically - works in all environments
# From tests/integration/cli/test_format_command.py -> go to repo root -> src
_SRC_DIR = Path(__file__).parent.parent.parent.parent / "src"


def test_format_command_integration():
    """Test format command with real ARXML file."""
    # Use existing test fixture
    fixture_path = Path("tests/fixtures/arxml/AUTOSAR_Datatypes.arxml")

    if not fixture_path.exists():
        pytest.skip("Test fixture not available")

    with tempfile.NamedTemporaryFile(suffix=".arxml", delete=False) as tmp:
        output_path = tmp.name

    try:
        # Prepare environment with PYTHONPATH
        env = os.environ.copy()
        env["PYTHONPATH"] = str(_SRC_DIR)

        # Run CLI command
        result = subprocess.run(
            [sys.executable, "-m", "armodel.cli.main", "format", str(fixture_path), "-o", output_path],
            capture_output=True,
            text=True,
            env=env,
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
    # Prepare environment with PYTHONPATH
    env = os.environ.copy()
    env["PYTHONPATH"] = str(_SRC_DIR)

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "armodel.cli.main",
            "format",
            "/nonexistent/file.arxml",
            "-o",
            "/tmp/output.arxml",
        ],
        capture_output=True,
        text=True,
        env=env,
    )

    assert result.returncode == 1  # EXIT_FILE_NOT_FOUND
    assert "not found" in result.stderr.lower()
