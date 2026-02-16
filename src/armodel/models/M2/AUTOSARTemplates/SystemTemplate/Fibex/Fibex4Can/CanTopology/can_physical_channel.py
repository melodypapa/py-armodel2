"""CanPhysicalChannel AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology.abstract_can_physical_channel import (
    AbstractCanPhysicalChannel,
)


class CanPhysicalChannel(AbstractCanPhysicalChannel):
    """AUTOSAR CanPhysicalChannel."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize CanPhysicalChannel."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CanPhysicalChannel to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CanPhysicalChannel":
        """Create CanPhysicalChannel from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CanPhysicalChannel instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CanPhysicalChannel since parent returns ARObject
        return cast("CanPhysicalChannel", obj)


class CanPhysicalChannelBuilder:
    """Builder for CanPhysicalChannel."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanPhysicalChannel = CanPhysicalChannel()

    def build(self) -> CanPhysicalChannel:
        """Build and return CanPhysicalChannel object.

        Returns:
            CanPhysicalChannel instance
        """
        # TODO: Add validation
        return self._obj
