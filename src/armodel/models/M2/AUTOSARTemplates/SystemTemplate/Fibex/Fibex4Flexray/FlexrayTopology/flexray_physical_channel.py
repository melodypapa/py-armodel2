"""FlexrayPhysicalChannel AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.physical_channel import (
    PhysicalChannel,
)


class FlexrayPhysicalChannel(PhysicalChannel):
    """AUTOSAR FlexrayPhysicalChannel."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("channel_name", None, False, False, FlexrayChannelName),  # channelName
    ]

    def __init__(self) -> None:
        """Initialize FlexrayPhysicalChannel."""
        super().__init__()
        self.channel_name: Optional[FlexrayChannelName] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert FlexrayPhysicalChannel to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlexrayPhysicalChannel":
        """Create FlexrayPhysicalChannel from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            FlexrayPhysicalChannel instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to FlexrayPhysicalChannel since parent returns ARObject
        return cast("FlexrayPhysicalChannel", obj)


class FlexrayPhysicalChannelBuilder:
    """Builder for FlexrayPhysicalChannel."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlexrayPhysicalChannel = FlexrayPhysicalChannel()

    def build(self) -> FlexrayPhysicalChannel:
        """Build and return FlexrayPhysicalChannel object.

        Returns:
            FlexrayPhysicalChannel instance
        """
        # TODO: Add validation
        return self._obj
