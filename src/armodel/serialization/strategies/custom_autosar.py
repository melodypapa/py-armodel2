"""
Custom serializer for AUTOSAR root element.

This module implements special handling for the AUTOSAR root element,
including namespace management and schema location attributes.
"""

from __future__ import annotations

import xml.etree.ElementTree as ET
from typing import TYPE_CHECKING

from armodel.serialization.base import (
    DeserializationContext,
    SerializationContext,
    SerializationStrategy,
)

if TYPE_CHECKING:
    from armodel.core.version import SchemaVersionManager


class AUTOSARSerializer(SerializationStrategy):
    """
    Custom serializer for the AUTOSAR root element.

    Handles special requirements:
    - Schema namespace declarations
    - Schema location attributes (xsi:schemaLocation)
    - Multiple namespace support
    - Version-specific serialization
    """

    AUTOSAR_CLASS_NAME = "AUTOSAR"
    AUTOSAR_XML_TAG = "AUTOSAR"

    # Common AUTOSAR namespaces
    SCHEMA_INSTANCE_NS = "http://www.w3.org/2001/XMLSchema-instance"

    def can_handle(self, obj: type | object) -> bool:
        """
        Check if this strategy can handle the given object.

        Args:
            obj: The object or class to check

        Returns:
            True if the object is the AUTOSAR class
        """
        cls = obj if isinstance(obj, type) else type(obj)
        return cls.__name__ == self.AUTOSAR_CLASS_NAME

    def serialize(
        self,
        obj: object,
        context: SerializationContext,
        element: ET.Element | None = None,
    ) -> ET.Element:
        """
        Serialize AUTOSAR root element to XML.

        Args:
            obj: The AUTOSAR object to serialize
            context: Serialization context
            element: Optional existing element (typically None for root)

        Returns:
            The XML element representing the AUTOSAR root
        """
        # Import ReflectionSerializer for delegation

        # Create root element
        if element is None:
            element = ET.Element(self.AUTOSAR_XML_TAG)

        # Set namespace
        namespace = context.namespace
        if namespace:
            # Register namespace
            ET.register_namespace("", namespace)
            ET.register_namespace("xsi", self.SCHEMA_INSTANCE_NS)

            # Add namespace to element tag
            element.tag = f"{{{namespace}}}{self.AUTOSAR_XML_TAG}"

            # Add schema location if version manager is available
            if context.version_manager:
                schema_location = self._get_schema_location(context.version_manager)
                if schema_location:
                    element.set(f"{{{self.SCHEMA_INSTANCE_NS}}}schemaLocation", schema_location)

        # Serialize all child elements (ar_packages)
        if hasattr(obj, "ar_packages"):
            for pkg in obj.ar_packages:
                if hasattr(pkg, "serialize"):
                    child = pkg.serialize(namespace)
                    element.append(child)

        return element

    def _get_schema_location(self, version_manager: SchemaVersionManager) -> str | None:
        """
        Get the schema location for the current version.

        Args:
            version_manager: The schema version manager

        Returns:
            Schema location string or None
        """
        # Get default version
        version = version_manager.get_default_version()
        if not version:
            return None

        namespace = version_manager.get_namespace(version)
        xsd_path = version_manager.get_xsd_path(version)

        if namespace and xsd_path:
            return f"{namespace} {xsd_path}"

        return None

    def deserialize(
        self,
        cls: type,
        element: ET.Element,
        context: DeserializationContext,
    ) -> object:
        """
        Deserialize AUTOSAR root element from XML.

        Args:
            cls: The AUTOSAR class
            element: The XML element to deserialize from
            context: Deserialization context

        Returns:
            The deserialized AUTOSAR object
        """
        # Import ReflectionSerializer for delegation

        # Create instance
        instance = cls.__new__(cls)  # type: ignore[call-overload]

        # Initialize ar_packages list
        if hasattr(instance, "ar_packages"):
            instance.ar_packages = []

        # Deserialize child elements (ar_packages)
        for child in element:
            child_tag = child.tag
            if "{" in child_tag:
                child_tag = child_tag.split("}", 1)[1]

            # Look for AR-PACKAGES elements
            if child_tag in ("AR-PACKAGES", "AR_PACKAGES"):
                # Find AR-PACKAGE children
                for pkg_child in child:
                    pkg_tag = pkg_child.tag
                    if "{" in pkg_tag:
                        pkg_tag = pkg_tag.split("}", 1)[1]

                    if pkg_tag in ("AR-PACKAGE", "AR_PACKAGE"):
                        # Import here to avoid circular dependency
                        # type: ignore[attr-defined] - ARPackage is not explicitly exported but is defined in the module
                        # fmt: off
                        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (  # type: ignore[attr-defined]  # noqa: F401
                            ARPackage,
                        )
                        # fmt: on

                        pkg = ARPackage.deserialize(pkg_child)
                        instance.ar_packages.append(pkg)

        # Call __init__ if it exists
        if hasattr(instance, "__init__"):
            try:
                instance.__init__()
            except Exception:
                pass

        return instance
