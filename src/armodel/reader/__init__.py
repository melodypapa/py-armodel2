"""ARXML reading functionality."""

from pathlib import Path
from typing import Union, Optional
import xml.etree.ElementTree as ET
from lxml import etree

from armodel.core import SchemaVersionManager
from armodel.models.M2.AUTOSARTemplates.autosar import AUTOSAR


class ARXMLReader:
    """Handles loading ARXML files and mapping to Python objects.

    This class provides a high-level API for reading ARXML files,
    detecting schema versions, and mapping XML to AUTOSAR objects.
    """

    def __init__(self, version_manager: Optional[SchemaVersionManager] = None):
        """Initialize ARXMLReader.

        Args:
            version_manager: SchemaVersionManager instance for version detection.
                           If None, uses the singleton instance.
        """
        self._version_manager = version_manager or SchemaVersionManager()

    def load_arxml(self, filepath: Union[str, Path], validate: bool = False) -> AUTOSAR:
        """Load ARXML file and return AUTOSAR object.

        Args:
            filepath: Path to ARXML file
            validate: Whether to validate against XSD schema

        Returns:
            AUTOSAR object representing document

        Raises:
            FileNotFoundError: If file doesn't exist
            etree.XMLSyntaxError: If XML is malformed
            Exception: If validation fails
        """
        root = self._load_file(filepath)
        autosar = self._map_to_autosar(root)

        if validate:
            self._validate_against_schema(root, autosar)

        return autosar

    def _load_file(self, filepath: Union[str, Path]) -> etree.Element:
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

        tree = etree.parse(str(filepath))
        return tree.getroot()

    def _map_to_autosar(self, root: etree.Element) -> AUTOSAR:
        """Map XML element to AUTOSAR object.

        Args:
            root: Root XML element

        Returns:
            AUTOSAR object instance
        """
        # Convert lxml Element to ElementTree Element
        xml_str = etree.tostring(root, encoding='unicode')
        et_root = ET.fromstring(xml_str)

        # Use deserialize method to create AUTOSAR object
        autosar = AUTOSAR.deserialize(et_root)

        return autosar

    def _validate_against_schema(self, root: etree.Element, autosar: AUTOSAR) -> None:
        """Validate ARXML against XSD schema.

        Args:
            root: Root XML element
            autosar: AUTOSAR object

        Raises:
            Exception: If validation fails
        """
        # Convert lxml Element to ET.Element for version detection
        xml_str = etree.tostring(root, encoding='unicode')
        et_root = ET.fromstring(xml_str)

        version = self._version_manager.detect_schema_version(et_root)
        if not version:
            raise ValueError("Cannot validate: unknown schema version")

        config = self._version_manager.get_config(version)
        xsd_file = config.get("xsd_file") if config else None

        if not xsd_file:
            raise ValueError(f"Cannot validate: no XSD file for version {version}")

        # Construct XSD file path
        from pathlib import Path

        xsd_path = Path("demos/xsd/AUTOSAR_") / version / xsd_file

        # Load XSD schema
        try:
            xsd_doc = etree.parse(str(xsd_path))
            xsd_schema = etree.XMLSchema(xsd_doc)

            # Validate
            if not xsd_schema.validate(root):
                raise ValueError(f"Validation failed: {xsd_schema.error_log}")
        except Exception as e:
            raise ValueError(f"Schema validation error: {e}")

    def get_schema_version(self, filepath: Union[str, Path]) -> Optional[str]:
        """Get schema version of ARXML file without loading entire file.

        Args:
            filepath: Path to ARXML file

        Returns:
            Schema version string or None if unknown
        """
        root = self._load_file(filepath)
        # Convert lxml Element to ET.Element for version detection
        xml_str = etree.tostring(root, encoding='unicode')
        et_root = ET.fromstring(xml_str)
        return self._version_manager.detect_schema_version(et_root)


__all__ = [
    "ARXMLReader",
]
