"""AUTOSAR root element - singleton pattern."""

from typing import Any, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import (
    ARObject,
)
import xml.etree.ElementTree as ET


class AUTOSAR(ARObject):
    """AUTOSAR root element representing the entire ARXML document.

    This class implements the singleton pattern - there is only one
    AUTOSAR instance per document.
    """

    _instance = None

    def __new__(cls) -> "AUTOSAR":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        """Initialize AUTOSAR singleton."""
        if hasattr(self, "_initialized"):
            return
        super().__init__()
        self._initialized = True
        # Splitable elements (top-level children)
        self.ar_packages: list[Any] = []
        self.administrative_data: list[Any] = []
        # Schema version for serialization (e.g., "00046")
        self._schema_version: Optional[str] = None

    def get_splitable_elements(self) -> list[Any]:
        """Get all splitable child elements.

        Returns:
            List of splitable elements
        """
        splitable: list[Any] = []
        for elem in self.ar_packages:
            if getattr(elem, "is_splitable", False):
                splitable.append(elem)
        return splitable

    def set_schema_version(self, version: str) -> None:
        """Set the schema version for serialization.

        Args:
            version: Schema version string (e.g., "00046")
        """
        self._schema_version = version

    def get_schema_version(self) -> Optional[str]:
        """Get the current schema version.

        Returns:
            Schema version string or None if not set
        """
        return self._schema_version

    def serialize(self, schema_version: Optional[str] = None, xsd_file: Optional[str] = None) -> ET.Element:
        """Convert AUTOSAR to XML element with proper namespace handling.

        Args:
            schema_version: Schema version string (e.g., "00046"). If None, uses instance version.
            xsd_file: XSD filename for schemaLocation attribute. If None, uses config default.

        Returns:
            XML element representing this document
        """
        from armodel.core import SchemaVersionManager

        # Determine which version to use
        version = schema_version or self._schema_version
        if version is None:
            version_manager = SchemaVersionManager()
            version = version_manager.get_default_version()

        # Get namespace and XSD file from config
        version_manager = SchemaVersionManager()
        namespace = version_manager.get_namespace(version)
        if namespace is None:
            # Fallback to r4.0 namespace if config is missing
            namespace = "http://autosar.org/schema/r4.0"

        if xsd_file is None:
            config = version_manager.get_config(version)
            xsd_file = config.get("xsd_file") if config else None

        # Create element with namespace
        element = ET.Element(f"{{{namespace}}}AUTOSAR")

        # Add xsi:schemaLocation attribute
        if xsd_file:
            schema_location = f"{namespace} {xsd_file}"
            element.set("{http://www.w3.org/2001/XMLSchema-instance}schemaLocation",
                       schema_location)

        # Serialize child elements
        if self.ar_packages:
            ar_packages_elem = ET.SubElement(element, f"{{{namespace}}}AR-PACKAGES")
            for pkg in self.ar_packages:
                if hasattr(pkg, "serialize"):
                    pkg_elem = pkg.serialize(namespace)
                    ar_packages_elem.append(pkg_elem)

        return element

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AUTOSAR":
        """Create AUTOSAR object from XML element.

        Args:
            element: XML element to deserialize

        Returns:
            AUTOSAR object instance
        """
        # Import ARPackage here to avoid circular imports
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_package import (
            ARPackage,
        )
        from armodel.core import SchemaVersionManager

        # Return singleton instance
        autosar = cls()

        # Detect and store schema version
        version_manager = SchemaVersionManager()
        detected_version = version_manager.detect_schema_version(element)
        if detected_version:
            autosar._schema_version = detected_version

        # Parse AR-PACKAGES
        for child in element:
            if child.tag.endswith("AR-PACKAGES"):
                for pkg_elem in child:
                    if pkg_elem.tag.endswith("AR-PACKAGE"):
                        pkg = ARPackage.deserialize(pkg_elem)
                        autosar.ar_packages.append(pkg)
            elif child.tag.endswith("ADMIN-DATA"):
                # TODO: Parse administrative data if needed
                pass

        return autosar
