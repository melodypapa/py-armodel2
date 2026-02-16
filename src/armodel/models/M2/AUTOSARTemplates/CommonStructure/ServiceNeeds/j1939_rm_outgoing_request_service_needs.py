"""J1939RmOutgoingRequestServiceNeeds AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_needs import (
    ServiceNeeds,
)


class J1939RmOutgoingRequestServiceNeeds(ServiceNeeds):
    """AUTOSAR J1939RmOutgoingRequestServiceNeeds."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize J1939RmOutgoingRequestServiceNeeds."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert J1939RmOutgoingRequestServiceNeeds to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "J1939RmOutgoingRequestServiceNeeds":
        """Create J1939RmOutgoingRequestServiceNeeds from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            J1939RmOutgoingRequestServiceNeeds instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to J1939RmOutgoingRequestServiceNeeds since parent returns ARObject
        return cast("J1939RmOutgoingRequestServiceNeeds", obj)


class J1939RmOutgoingRequestServiceNeedsBuilder:
    """Builder for J1939RmOutgoingRequestServiceNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: J1939RmOutgoingRequestServiceNeeds = J1939RmOutgoingRequestServiceNeeds()

    def build(self) -> J1939RmOutgoingRequestServiceNeeds:
        """Build and return J1939RmOutgoingRequestServiceNeeds object.

        Returns:
            J1939RmOutgoingRequestServiceNeeds instance
        """
        # TODO: Add validation
        return self._obj
