"""DoIpGidNeeds AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.do_ip_service_needs import (
    DoIpServiceNeeds,
)


class DoIpGidNeeds(DoIpServiceNeeds):
    """AUTOSAR DoIpGidNeeds."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize DoIpGidNeeds."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DoIpGidNeeds to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DoIpGidNeeds":
        """Create DoIpGidNeeds from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DoIpGidNeeds instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DoIpGidNeeds since parent returns ARObject
        return cast("DoIpGidNeeds", obj)


class DoIpGidNeedsBuilder:
    """Builder for DoIpGidNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DoIpGidNeeds = DoIpGidNeeds()

    def build(self) -> DoIpGidNeeds:
        """Build and return DoIpGidNeeds object.

        Returns:
            DoIpGidNeeds instance
        """
        # TODO: Add validation
        return self._obj
