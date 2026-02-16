"""DoIpPowerModeStatusNeeds AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.do_ip_service_needs import (
    DoIpServiceNeeds,
)


class DoIpPowerModeStatusNeeds(DoIpServiceNeeds):
    """AUTOSAR DoIpPowerModeStatusNeeds."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize DoIpPowerModeStatusNeeds."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DoIpPowerModeStatusNeeds to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DoIpPowerModeStatusNeeds":
        """Create DoIpPowerModeStatusNeeds from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DoIpPowerModeStatusNeeds instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DoIpPowerModeStatusNeeds since parent returns ARObject
        return cast("DoIpPowerModeStatusNeeds", obj)


class DoIpPowerModeStatusNeedsBuilder:
    """Builder for DoIpPowerModeStatusNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DoIpPowerModeStatusNeeds = DoIpPowerModeStatusNeeds()

    def build(self) -> DoIpPowerModeStatusNeeds:
        """Build and return DoIpPowerModeStatusNeeds object.

        Returns:
            DoIpPowerModeStatusNeeds instance
        """
        # TODO: Add validation
        return self._obj
