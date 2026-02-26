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
