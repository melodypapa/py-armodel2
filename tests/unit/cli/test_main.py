"""Tests for CLI main entry point."""

from unittest.mock import patch
import pytest


class TestCLIMain:
    """Unit tests for CLI main entry point."""

    def test_main_help_displays(self):
        """Test that main help message displays correctly."""
        with patch("sys.argv", ["armodel", "--help"]):
            # Should show help and exit
            with pytest.raises(SystemExit) as exc_info:
                from armodel.cli.main import main

                main()
            # Help exits with code 0
            assert exc_info.value.code == 0

    def test_main_version_displays(self):
        """Test that version information displays."""
        with patch("sys.argv", ["armodel", "--version"]):
            # Should show version and exit
            with pytest.raises(SystemExit) as exc_info:
                from armodel.cli.main import main

                main()
            # Version exits with code 0
            assert exc_info.value.code == 0
