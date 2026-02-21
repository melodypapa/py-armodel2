"""Format command implementation."""

import sys
from argparse import Namespace

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


def format_command(args: Namespace) -> int:
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

        # Load ARXML file using singleton
        reader = ARXMLReader()

        if not args.quiet:
            print(f"Loading ARXML file: {input_path}")

        try:
            # Use load_arxml_with_clear for fresh state (CLI should not accumulate state)
            reader.load_arxml_with_clear(str(input_path))
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
            # Save using singleton (no need to pass autosar)
            writer.save_arxml(str(output_path))
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