"""Tests for format command."""

import tempfile
from pathlib import Path
from unittest.mock import Mock, patch

from armodel.cli.common import EXIT_SUCCESS, EXIT_FILE_NOT_FOUND


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


@patch("armodel.cli.commands.format.ARXMLReader")
@patch("armodel.cli.commands.format.ARXMLWriter")
def test_format_command_success(mock_writer_class, mock_reader_class):
    """Test format command with valid file."""
    from argparse import Namespace

    # Mock ARXMLReader
    mock_reader = Mock()
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
        # Verify load_arxml was called with an AUTOSAR instance and the input path
        mock_reader.load_arxml.assert_called_once()
        load_arxml_call_args = mock_reader.load_arxml.call_args
        assert str(load_arxml_call_args[0][1]) == tmp_path
        # Verify save_arxml was called
        mock_writer.save_arxml.assert_called_once()
        call_args = mock_writer.save_arxml.call_args
        # Check that the first arg is an AUTOSAR instance
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.autosar import AUTOSAR

        assert isinstance(call_args[0][0], AUTOSAR)
        assert str(call_args[0][1]) == output_path
    finally:
        Path(tmp_path).unlink(missing_ok=True)
        Path(output_path).unlink(missing_ok=True)
