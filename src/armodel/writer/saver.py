"""ARXML file saving."""

from pathlib import Path
from typing import Union
import xml.etree.ElementTree as ET


def save_arxml_file(
    root: ET.Element, filepath: Union[str, Path], pretty_print: bool = True, encoding: str = "UTF-8"
) -> None:
    """Save XML element to ARXML file.

    Args:
        root: Root XML element
        filepath: Output file path
        pretty_print: Whether to format XML with indentation
        encoding: File encoding
    """
    filepath = Path(filepath)

    # Ensure parent directory exists
    filepath.parent.mkdir(parents=True, exist_ok=True)

    # Create tree and write
    tree = ET.ElementTree(root)
    tree.write(str(filepath), encoding=encoding, xml_declaration=True)
