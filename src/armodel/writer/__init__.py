"""ARXML writing functionality."""

from pathlib import Path
from typing import Union

from armodel.writer.serializer import serialize_autosar_to_xml
from armodel.writer.saver import save_arxml_file


def save_arxml(
    autosar,
    filepath: Union[str, Path],
    pretty_print: bool = True
):
    """Save AUTOSAR object to ARXML file.

    Args:
        autosar: AUTOSAR object to save
        filepath: Output file path
        pretty_print: Whether to format XML with indentation
    """
    # Serialize to XML
    root = serialize_autosar_to_xml(autosar)

    # Save to file
    save_arxml_file(root, filepath, pretty_print=pretty_print)


__all__ = ["save_arxml", "serialize_autosar_to_xml", "save_arxml_file"]
