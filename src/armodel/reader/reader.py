"""ARXML reading functionality."""

from pathlib import Path
from typing import Union, Optional, cast
import xml.etree.cElementTree as ET

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
            ET.ParseError: If XML is malformed
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

    def _load_file(self, filepath: Union[str, Path]) -> ET.Element:
        """Load ARXML file and return root element.

        Args:
            filepath: Path to ARXML file

        Returns:
            Root XML element

        Raises:
            FileNotFoundError: If file doesn't exist
            ET.ParseError: If XML is malformed
        """
        filepath = Path(filepath)

        if not filepath.exists():
            raise FileNotFoundError(f"ARXML file not found: {filepath}")

        tree = ET.parse(str(filepath))
        return tree.getroot()

    def _populate_autosar(self, autosar: AUTOSAR, root: ET.Element) -> AUTOSAR:
        """Populate AUTOSAR object from XML element.

        This method deserializes the XML element and merges its contents
        into the existing AUTOSAR object.

        Args:
            autosar: AUTOSAR object to populate
            root: Root XML element

        Returns:
            The populated AUTOSAR object
        """
        # Deserialize to get a new AUTOSAR object
        loaded_autosar = cast(AUTOSAR, AUTOSAR.deserialize(root))

        # Merge the loaded data into the provided autosar object
        # Copy all attributes from loaded_autosar to autosar
        if hasattr(loaded_autosar, 'ar_packages') and loaded_autosar.ar_packages:
            if not hasattr(autosar, 'ar_packages'):
                autosar.ar_packages = []
            # Append all packages from loaded file
            autosar.ar_packages.extend(loaded_autosar.ar_packages)

        return autosar

    def _validate_against_schema(self, root: ET.Element, autosar: AUTOSAR) -> None:
        """Validate ARXML against XSD schema.

        Note: CElementTree does not support XSD validation natively.
        This method is kept for API compatibility but validation
        must be performed using external tools.

        Args:
            root: Root XML element
            autosar: AUTOSAR object

        Raises:
            NotImplementedError: XSD validation not supported with CElementTree
        """
        raise NotImplementedError(
            "XSD schema validation is not supported with CElementTree. "
            "Please use external XSD validation tools if validation is required."
        )

    def get_schema_version(self, filepath: Union[str, Path]) -> Optional[str]:
        """Get schema version of ARXML file without loading entire file.

        Args:
            filepath: Path to ARXML file

        Returns:
            Schema version string or None if unknown
        """
        root = self._load_file(filepath)
        return self._version_manager.detect_schema_version(root)