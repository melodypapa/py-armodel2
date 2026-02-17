"""ARXML writing functionality."""

from pathlib import Path
from typing import Union, Optional
import xml.etree.ElementTree as ET

from armodel.core import SchemaVersionManager
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.autosar import AUTOSAR


class ARXMLWriter:
    """Handles serializing AUTOSAR objects and saving to ARXML files.

    This class provides a high-level API for writing AUTOSAR objects
    to ARXML files with configurable formatting options.
    """

    def __init__(
        self,
        pretty_print: bool = True,
        encoding: str = "UTF-8",
        version_manager: Optional[SchemaVersionManager] = None,
    ):
        """Initialize ARXMLWriter.

        Args:
            pretty_print: Whether to format XML with indentation
            encoding: File encoding
            version_manager: SchemaVersionManager for namespace handling.
                           If None, uses the singleton instance.
        """
        self._pretty_print = pretty_print
        self._encoding = encoding
        self._version_manager = version_manager or SchemaVersionManager()

    def save_arxml(self, autosar: AUTOSAR, filepath: Union[str, Path]) -> None:
        """Save AUTOSAR object to ARXML file.

        Args:
            autosar: AUTOSAR object to save
            filepath: Output file path
        """
        root = self._serialize_to_xml(autosar)
        self._save_to_file(root, filepath)

    def _serialize_to_xml(self, autosar: AUTOSAR) -> ET.Element:
        """Serialize AUTOSAR object to XML element.

        Args:
            autosar: AUTOSAR object to serialize

        Returns:
            Root XML element
        """
        # Get default namespace for version-aware XML output
        version = self._version_manager.get_default_version()
        namespace = self._version_manager.get_namespace(version)

        if namespace:
            # Register default namespace (empty prefix)
            ET.register_namespace("", namespace)
        # Register xsi namespace
        ET.register_namespace("xsi", "http://www.w3.org/2001/XMLSchema-instance")

        # Use reflection-based serialize method
        root = autosar.serialize(namespace=namespace or "")
        return root

    def _save_to_file(self, root: ET.Element, filepath: Union[str, Path]) -> None:
        """Save XML element to ARXML file.

        Args:
            root: Root XML element
            filepath: Output file path
        """
        filepath = Path(filepath)

        # Ensure parent directory exists
        filepath.parent.mkdir(parents=True, exist_ok=True)

        # Create tree and write
        tree = ET.ElementTree(root)

        # Configure pretty printing
        if self._pretty_print:
            tree_root = tree.getroot()
            if tree_root is not None:
                self._indent(tree_root)

        tree.write(str(filepath), encoding=self._encoding, xml_declaration=True)

    def _indent(self, elem: ET.Element, level: int = 0) -> None:
        """Add indentation to XML element for pretty printing.

        Args:
            elem: XML element to indent
            level: Current indentation level
        """
        indent_str = "\n" + "  " * level
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = indent_str + "  "
            if not elem.tail or not elem.tail.strip():
                elem.tail = indent_str
            child = None
            for child in elem:
                self._indent(child, level + 1)
            if child is not None and (not child.tail or not child.tail.strip()):
                child.tail = indent_str
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = indent_str

    def configure(
        self, pretty_print: Optional[bool] = None, encoding: Optional[str] = None
    ) -> None:
        """Update writer configuration.

        Args:
            pretty_print: Whether to format XML with indentation
            encoding: File encoding
        """
        if pretty_print is not None:
            self._pretty_print = pretty_print
        if encoding is not None:
            self._encoding = encoding

    def to_string(self, autosar: AUTOSAR) -> str:
        """Convert AUTOSAR object to XML string.

        Args:
            autosar: AUTOSAR object to convert

        Returns:
            XML string representation
        """
        root = self._serialize_to_xml(autosar)

        if self._pretty_print:
            self._indent(root)

        xml_bytes = ET.tostring(root, encoding=self._encoding, xml_declaration=True)
        return xml_bytes.decode(self._encoding) if xml_bytes else ""


__all__ = [
    "ARXMLWriter",
]
