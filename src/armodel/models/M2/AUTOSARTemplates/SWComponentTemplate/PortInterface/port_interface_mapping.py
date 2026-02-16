"""PortInterfaceMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)


class PortInterfaceMapping(Identifiable):
    """AUTOSAR PortInterfaceMapping."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize PortInterfaceMapping."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert PortInterfaceMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PortInterfaceMapping":
        """Create PortInterfaceMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            PortInterfaceMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to PortInterfaceMapping since parent returns ARObject
        return cast("PortInterfaceMapping", obj)


class PortInterfaceMappingBuilder:
    """Builder for PortInterfaceMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PortInterfaceMapping = PortInterfaceMapping()

    def build(self) -> PortInterfaceMapping:
        """Build and return PortInterfaceMapping object.

        Returns:
            PortInterfaceMapping instance
        """
        # TODO: Add validation
        return self._obj
