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
        
        # Fix XML declaration quotes
        self._fix_xml_declaration_quotes_file(filepath)
        
        # Preserve HTML entity encoding in text content
        self._preserve_html_entities_file(filepath)

    def _fix_xml_declaration_quotes_file(self, filepath: Path) -> None:
        """Replace single quotes with double quotes in XML declaration.

        Post-processes the file to convert:
        <?xml version='1.0' encoding='UTF-8'?>
        to:
        <?xml version="1.0" encoding="UTF-8"?>

        Args:
            filepath: Path to the ARXML file to fix
        """
        with open(filepath, 'rb') as f:
            content = f.read()
        
        content = content.replace(b"<?xml version='1.0'", b'<?xml version="1.0"')
        content = content.replace(b"encoding='UTF-8'?>", b'encoding="UTF-8"?>')
        
        with open(filepath, 'wb') as f:
            f.write(content)

    def _fix_xml_declaration_quotes_str(self, xml_str: str) -> str:
        """Replace single quotes with double quotes in XML declaration string.

        Args:
            xml_str: XML string to fix

        Returns:
            XML string with corrected quotes
        """
        xml_str = xml_str.replace("<?xml version='1.0'", '<?xml version="1.0"')
        xml_str = xml_str.replace("encoding='UTF-8'?>", 'encoding="UTF-8"?>')
        return xml_str

    def _preserve_html_entities_file(self, filepath: Path) -> None:
        """Preserve HTML entity encoding in text content.

        Post-processes the file to escape special characters in text content
        to match AUTOSAR format (e.g., &quot; instead of " in text nodes).

        Args:
            filepath: Path to the ARXML file to process
        """
        with open(filepath, 'rb') as f:
            content = f.read()
        
        # Decode to string for processing
        xml_str = content.decode(self._encoding)
        
        # Apply HTML entity preservation
        xml_str = self._preserve_html_entities_str(xml_str)
        
        # Write back
        with open(filepath, 'wb') as f:
            f.write(xml_str.encode(self._encoding))

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
        import re
        
        # Process the XML string line by line
        # We need to escape quotes only in text content (between > and <)
        # and NOT in attribute values or tag names
        
        lines = xml_str.split('\n')
        processed_lines = []
        
        for line in lines:
            # Skip lines that are purely tags (no text content)
            if not line.strip():
                processed_lines.append(line)
                continue
            
            # For each line, identify text content and escape quotes
            # Text content appears after > and before <
            # We need to be careful not to escape quotes in attributes
            
            # Escape quotes in text content only
            # Look for patterns like ">text<" where text contains quotes
            # Use regex to find text between tags and escape quotes
            
            def escape_quotes_in_text(match: re.Match[str]) -> str:
                """Escape quotes in text content between tags."""
                text = match.group(1)
                if text:
                    # Escape quotes in text content
                    text = text.replace('"', '&quot;')
                return f'>{text}<'
            
            # Replace text content between tags
            # This regex matches >...< where ... is not a tag
            processed_line = re.sub(r'>([^<]*?)<', escape_quotes_in_text, line)
            processed_lines.append(processed_line)
        
        return '\n'.join(processed_lines)

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

    def to_string(self, autosar: AUTOSAR) -> str:
        """Serialize AUTOSAR object to XML string.

        Args:
            autosar: AUTOSAR object to serialize

        Returns:
            XML string representation
        """
        root = self._serialize_to_xml(autosar)
        tree = ET.ElementTree(root)

        if self._pretty_print:
            tree_root = tree.getroot()
            if tree_root is not None:
                self._indent(tree_root)

        # Convert to string (ET.tostring returns bytes, need to decode)
        xml_bytes = ET.tostring(root, encoding=self._encoding, xml_declaration=True)
        xml_str = xml_bytes.decode(self._encoding)
        
        # Fix XML declaration quotes
        xml_str = self._fix_xml_declaration_quotes_str(xml_str)
        
        return xml_str
