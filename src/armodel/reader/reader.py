"""ARXML reading functionality."""

from pathlib import Path
from typing import Union, Optional
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
        filepath: Union[str, Path],
        autosar: Optional[AUTOSAR] = None,
        validate: bool = False
    ) -> AUTOSAR:
        """Load ARXML file into AUTOSAR object.

        This method reads an ARXML file and populates the provided AUTOSAR
        object with the file's contents. If no AUTOSAR object is provided,
        it uses the AUTOSAR singleton instance.

        The same AUTOSAR instance can be reused for multiple load operations.
        Content from multiple files is merged into the same instance.

        Args:
            filepath: Path to ARXML file
            autosar: AUTOSAR object to populate. If None, uses AUTOSAR singleton.
            validate: Whether to validate against XSD schema

        Returns:
            The populated AUTOSAR object

        Raises:
            FileNotFoundError: If file doesn't exist
            ET.ParseError: If XML is malformed
            Exception: If validation fails

        Example:
            >>> reader = ARXMLReader()
            >>> 
            >>> # Use singleton (convenient)
            >>> reader.load_arxml("file1.arxml")
            >>> reader.load_arxml("file2.arxml")  # Appends to same singleton
            >>> 
            >>> # Use fresh state (clears singleton first)
            >>> AUTOSAR().clear()
            >>> reader.load_arxml("file3.arxml")
            >>> 
            >>> # Use custom instance (for isolation)
            >>> autosar = AUTOSAR()
            >>> reader.load_arxml("file1.arxml", autosar)
        """
        # Use singleton if no AUTOSAR instance provided
        if autosar is None:
            autosar = AUTOSAR()

        root = self._load_file(filepath)
        self._populate_autosar(autosar, root)

        if validate:
            self._validate_against_schema(root, autosar)

        return autosar

    def load_arxml_with_clear(
        self,
        filepath: Union[str, Path],
        validate: bool = False
    ) -> AUTOSAR:
        """Load ARXML file into a cleared AUTOSAR singleton.

        This is a convenience method that clears the AUTOSAR singleton
        before loading, ensuring a fresh state for the new file.

        Args:
            filepath: Path to ARXML file
            validate: Whether to validate against XSD schema

        Returns:
            The populated AUTOSAR singleton

        Raises:
            FileNotFoundError: If file doesn't exist
            ET.ParseError: If XML is malformed
            Exception: If validation fails

        Example:
            >>> reader = ARXMLReader()
            >>> reader.load_arxml_with_clear("file1.arxml")  # Fresh state
            >>> reader.load_arxml_with_clear("file2.arxml")  # Fresh state again
        """
        AUTOSAR().clear()
        return self.load_arxml(filepath, validate=validate)

    def _load_file(self, filepath: Union[str, Path]) -> ET.Element:
        """Load ARXML file and return root element.

        Args:
            filepath: Path to ARXML file

        Returns:
            Root XML element

        Raises:
            FileNotFoundError: If file doesn't exist
            ET.ParseError: If XML is malformed
            UnicodeDecodeError: If file is not valid UTF-8
        """
        filepath = Path(filepath)

        if not filepath.exists():
            raise FileNotFoundError(f"ARXML file not found: {filepath}")

        # Explicitly open with UTF-8 encoding to avoid system default encoding issues
        # On Windows with non-UTF-8 locales (e.g., Chinese GBK), ET.parse(filepath)
        # would use system default encoding instead of the XML declaration's encoding
        with open(filepath, 'r', encoding='utf-8') as f:
            tree = ET.parse(f)

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
        loaded_autosar = AUTOSAR.deserialize(root)

        # Copy all attributes from loaded_autosar to autosar
        for attr_name in vars(loaded_autosar).keys():
            # Skip private attributes
            if attr_name.startswith('_'):
                continue

            value = getattr(loaded_autosar, attr_name)
            if value is None:
                continue

            if attr_name == 'ar_packages':
                # Special handling for ar_packages (extend, not replace)
                if not hasattr(autosar, 'ar_packages'):
                    autosar.ar_packages = []
                # For singleton AUTOSAR, loaded_autosar and autosar are the same object
                # We need to avoid extending a list with itself
                if loaded_autosar is autosar:
                    # Already populated by deserialize(), no need to extend
                    pass
                else:
                    autosar.ar_packages.extend(value)
            elif isinstance(value, list):
                # For list attributes, extend if exists, otherwise set
                if not hasattr(autosar, attr_name):
                    setattr(autosar, attr_name, [])
                getattr(autosar, attr_name).extend(value)
            else:
                # For non-list attributes, replace if not None
                if value is not None:
                    setattr(autosar, attr_name, value)

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