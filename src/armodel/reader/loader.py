"""ARXML file loading."""

from pathlib import Path
from lxml import etree
from typing import Union


def load_arxml_file(filepath: Union[str, Path]) -> etree.Element:
    """Load ARXML file and return root element.

    Args:
        filepath: Path to ARXML file

    Returns:
        Root XML element

    Raises:
        FileNotFoundError: If file doesn't exist
        etree.XMLSyntaxError: If XML is malformed
    """
    filepath = Path(filepath)

    if not filepath.exists():
        raise FileNotFoundError(f"ARXML file not found: {filepath}")

    # Parse XML file
    tree = etree.parse(str(filepath))
    return tree.getroot()
