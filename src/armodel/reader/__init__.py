"""ARXML reading functionality."""

from pathlib import Path
from typing import Union, Optional, cast
import xml.etree.ElementTree as ET
from lxml import etree

from armodel.core import SchemaVersionManager
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.autosar import AUTOSAR


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

    def load_arxml(
        self,
        autosar: AUTOSAR,
        filepath: Union[str, Path],
        validate: bool = False
    ) -> AUTOSAR:
        """Load ARXML file into existing AUTOSAR object.

        This method reads an ARXML file and populates the provided AUTOSAR
        object with the file's contents. The same AUTOSAR instance can be
        reused for multiple load operations.

        Args:
            autosar: AUTOSAR object to populate with file contents
            filepath: Path to ARXML file
            validate: Whether to validate against XSD schema

        Returns:
            The populated AUTOSAR object (same instance as passed in)

        Raises:
            FileNotFoundError: If file doesn't exist
            etree.XMLSyntaxError: If XML is malformed
            Exception: If validation fails

        Example:
            >>> autosar = AUTOSAR()
            >>> reader = ARXMLReader()
            >>> reader.load_arxml(autosar, "file1.arxml")
            >>> reader.load_arxml(autosar, "file2.arxml")  # Appends to same object
        """
        root = self._load_file(filepath)
        self._populate_autosar(autosar, root)

        if validate:
            self._validate_against_schema(root, autosar)

        return autosar

    def _load_file(self, filepath: Union[str, Path]) -> etree._Element:
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

    def _populate_autosar(self, autosar: AUTOSAR, root: etree._Element) -> AUTOSAR:
        """Populate AUTOSAR object from XML element.

        This method deserializes the XML element and merges its contents
        into the existing AUTOSAR object.

        Args:
            autosar: AUTOSAR object to populate
            root: Root XML element

        Returns:
            The populated AUTOSAR object
        """
        # Convert lxml Element to ElementTree Element
        xml_str = etree.tostring(root, encoding='unicode')
        et_root = ET.fromstring(xml_str)

        # Deserialize to get a new AUTOSAR object
        loaded_autosar = cast(AUTOSAR, AUTOSAR.deserialize(et_root))

        # Merge the loaded data into the provided autosar object
        # Copy all attributes from loaded_autosar to autosar
        if hasattr(loaded_autosar, 'ar_packages') and loaded_autosar.ar_packages:
            if not hasattr(autosar, 'ar_packages'):
                autosar.ar_packages = []
            # Append all packages from loaded file
            autosar.ar_packages.extend(loaded_autosar.ar_packages)

        return autosar

    def _validate_against_schema(self, root: etree._Element, autosar: AUTOSAR) -> None:
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
