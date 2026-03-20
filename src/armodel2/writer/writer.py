"""ARXML writing functionality."""

import re
from pathlib import Path
from typing import Union, Optional
import xml.etree.ElementTree as ET

from armodel2.core import SchemaVersionManager
from armodel2.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.autosar import AUTOSAR

# Pre-compiled regex patterns for performance
_XML_DECL_PATTERN = re.compile(r"<\?xml version='1\.0' encoding='([^']+)'\?\>")
_SELF_CLOSING_TAG_PATTERN = re.compile(r'<([A-Z][A-Z0-9-]*)([^>]*)/>')
_TEXT_CONTENT_PATTERN = re.compile(r'>([^<]*?)<', flags=re.DOTALL)


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

    def save_arxml(
        self,
        filepath: Union[str, Path],
        autosar: Optional[AUTOSAR] = None
    ) -> None:
        """Save AUTOSAR object to ARXML file.

        If no AUTOSAR object is provided, saves the AUTOSAR singleton.

        Args:
            filepath: Output file path
            autosar: AUTOSAR object to save. If None, uses AUTOSAR singleton.

        Example:
            >>> writer = ARXMLWriter()
            >>> 
            >>> # Save singleton (convenient)
            >>> writer.save_arxml("output.arxml")
            >>> 
            >>> # Save custom instance
            >>> autosar = AUTOSAR()
            >>> reader.load_arxml("input.arxml", autosar)
            >>> writer.save_arxml("output.arxml", autosar)
        """
        # Use singleton if no AUTOSAR instance provided
        if autosar is None:
            autosar = AUTOSAR()

        root = self._serialize_to_xml(autosar)
        self._save_to_file(root, filepath, autosar)

    def _serialize_to_xml(self, autosar: AUTOSAR) -> ET.Element:
        """Serialize AUTOSAR object to XML element.

        The AUTOSAR root element handles namespace attributes internally.
        No namespace parameter is needed as it's managed by AUTOSAR class.

        Args:
            autosar: AUTOSAR object to serialize

        Returns:
            Root XML element
        """
        # Register xsi namespace for proper XML serialization
        ET.register_namespace("xsi", "http://www.w3.org/2001/XMLSchema-instance")

        # Use reflection-based serialize method
        # AUTOSAR class handles namespace attributes internally
        root = autosar.serialize()
        return root

    def _save_to_file(self, root: ET.Element, filepath: Union[str, Path], autosar: Optional[AUTOSAR] = None) -> None:
        """Save XML element to ARXML file.

        Args:
            root: Root XML element
            filepath: Output file path
            autosar: AUTOSAR object to get encoding from (optional)
        """
        filepath = Path(filepath)

        # Ensure parent directory exists
        filepath.parent.mkdir(parents=True, exist_ok=True)

        # Use encoding from AUTOSAR object if available, otherwise use configured encoding
        encoding = self._encoding
        if autosar is not None and autosar.encoding is not None:
            encoding = autosar.encoding

        # Create tree and apply pretty printing
        tree = ET.ElementTree(root)
        if self._pretty_print:
            tree_root = tree.getroot()
            if tree_root is not None:
                self._indent(tree_root)

        # Serialize to bytes with all post-processing applied in memory
        xml_bytes = self._serialize_with_post_processing(root, encoding)

        # Write final result to file (single write operation)
        with open(filepath, 'wb') as f:
            f.write(xml_bytes)

    def _serialize_with_post_processing(self, root: ET.Element, encoding: str) -> bytes:
        """Serialize XML element to bytes with all post-processing applied in memory.

        This method combines:
        1. XML serialization with declaration
        2. Fix XML declaration quotes
        3. Convert self-closing tags to empty tags
        4. Preserve HTML entity encoding

        All operations are done in memory to avoid multiple file reads/writes.

        Args:
            root: Root XML element
            encoding: File encoding to use

        Returns:
            Processed XML content as bytes
        """
        # Serialize to bytes
        xml_bytes = ET.tostring(root, encoding=encoding, xml_declaration=True)

        # Convert to string for processing (regex works better with strings)
        xml_str = xml_bytes.decode(encoding)

        # 1. Fix XML declaration quotes: ' -> "
        # Pattern: <?xml version='1.0' encoding='ANY_VALUE'?>
        # Replace with: <?xml version="1.0" encoding="ANY_VALUE"?>
        replacement = f'<?xml version="1.0" encoding="{encoding}"?>'
        xml_str = _XML_DECL_PATTERN.sub(replacement, xml_str)

        # 2. Convert self-closing empty elements to separate opening and closing tags
        # Pattern: <TAG />, <TAG attr="value" />, etc.
        xml_str = _SELF_CLOSING_TAG_PATTERN.sub(
            lambda m: f'<{m.group(1)}{m.group(2).rstrip()}></{m.group(1)}>',
            xml_str
        )

        # 3. Preserve HTML entity encoding in text content
        xml_str = self._preserve_html_entities_str(xml_str)

        return xml_str.encode(encoding)

    def _preserve_html_entities_str(self, xml_str: str) -> str:
        """Preserve HTML entity encoding in XML string.

        Escapes special characters in text content to match AUTOSAR format:
        - " -> &quot; (quotes in text content)
        Note: Does NOT escape <, >, & in tag names or attribute values.
        Note: Does NOT escape apostrophes as AUTOSAR files use literal '.

        Args:
            xml_str: XML string to process

        Returns:
            XML string with preserved HTML entity encoding
        """
        def escape_quotes_in_text(match: re.Match[str]) -> str:
            """Escape quotes in text content between tags."""
            text = match.group(1)
            if text:
                # Escape quotes in text content
                text = text.replace('"', '&quot;')
            return f'>{text}<'

        # Replace text content between tags
        # Use re.DOTALL flag to match across newlines
        # This regex matches >...< where ... is any text (including newlines)
        # but not another tag (which starts with <)
        return _TEXT_CONTENT_PATTERN.sub(escape_quotes_in_text, xml_str)

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
            for child in elem:
                self._indent(child, level + 1)
            if not child.tail or not child.tail.strip():
                child.tail = indent_str
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = indent_str

    def to_string(self, autosar: Optional[AUTOSAR] = None) -> str:
        """Serialize AUTOSAR object to XML string.

        If no AUTOSAR object is provided, serializes the AUTOSAR singleton.

        Args:
            autosar: AUTOSAR object to serialize. If None, uses AUTOSAR singleton.

        Returns:
            XML string representation
        """
        # Use singleton if no AUTOSAR instance provided
        if autosar is None:
            autosar = AUTOSAR()

        root = self._serialize_to_xml(autosar)

        # Get encoding from AUTOSAR object if available
        encoding = self._encoding
        if autosar.encoding is not None:
            encoding = autosar.encoding

        # Apply pretty printing if needed
        if self._pretty_print:
            self._indent(root)

        # Serialize with all post-processing in memory
        xml_bytes = self._serialize_with_post_processing(root, encoding)
        return xml_bytes.decode(encoding)