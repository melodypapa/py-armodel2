"""ARXML reading functionality."""

from pathlib import Path
from typing import Union

from armodel.reader.loader import load_arxml_file
from armodel.reader.mapper import map_xml_to_autosar


def load_arxml(filepath: Union[str, Path], validate: bool = False):
    """Load ARXML file and return AUTOSAR object.

    Args:
        filepath: Path to ARXML file
        validate: Whether to validate against XSD schema (not yet implemented)

    Returns:
        AUTOSAR object representing document

    Raises:
        FileNotFoundError: If file doesn't exist
        Exception: If XML is malformed
    """
    # Load XML
    root = load_arxml_file(filepath)

    # Map to Python object
    autosar = map_xml_to_autosar(root)

    # TODO: Add validation if requested

    return autosar


__all__ = ["load_arxml", "load_arxml_file", "map_xml_to_autosar"]

