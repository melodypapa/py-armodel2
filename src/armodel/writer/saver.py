"""ARXML file saving."""

from pathlib import Path
from typing import Union
from lxml import etree


def save_arxml_file(
    root: etree.Element,
    filepath: Union[str, Path],
    pretty_print: bool = True,
    encoding: str = "UTF-8"
):
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
    tree = etree.ElementTree(root)
    tree.write(
        str(filepath),
        pretty_print=pretty_print,
        xml_declaration=True,
        encoding=encoding
    )
