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
        prog="armodel2",
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
        "-o",
        "--output",
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
        "-v",
        "--verbose",
        action="store_true",
        help="Show detailed error messages",
    )
    format_parser.add_argument(
        "-q",
        "--quiet",
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
        print(f"armodel2 {get_version()}")
        sys.exit(0)

    # If no command specified, show help
    if args.command is None:
        parser.print_help()
        return 0

    # Route to command handler
    if args.command == "format":
        from armodel2.cli.commands.format import format_command

        return format_command(args)

    parser.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
