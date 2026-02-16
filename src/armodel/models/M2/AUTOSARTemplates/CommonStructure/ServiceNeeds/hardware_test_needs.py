"""HardwareTestNeeds AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_needs import (
    ServiceNeeds,
)


class HardwareTestNeeds(ServiceNeeds):
    """AUTOSAR HardwareTestNeeds."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize HardwareTestNeeds."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert HardwareTestNeeds to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "HardwareTestNeeds":
        """Create HardwareTestNeeds from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            HardwareTestNeeds instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to HardwareTestNeeds since parent returns ARObject
        return cast("HardwareTestNeeds", obj)


class HardwareTestNeedsBuilder:
    """Builder for HardwareTestNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: HardwareTestNeeds = HardwareTestNeeds()

    def build(self) -> HardwareTestNeeds:
        """Build and return HardwareTestNeeds object.

        Returns:
            HardwareTestNeeds instance
        """
        # TODO: Add validation
        return self._obj
