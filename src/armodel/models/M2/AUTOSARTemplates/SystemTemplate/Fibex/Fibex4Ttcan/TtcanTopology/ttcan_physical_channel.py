"""TtcanPhysicalChannel AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology.abstract_can_physical_channel import (
    AbstractCanPhysicalChannel,
)


class TtcanPhysicalChannel(AbstractCanPhysicalChannel):
    """AUTOSAR TtcanPhysicalChannel."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize TtcanPhysicalChannel."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TtcanPhysicalChannel to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TtcanPhysicalChannel":
        """Create TtcanPhysicalChannel from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TtcanPhysicalChannel instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TtcanPhysicalChannel since parent returns ARObject
        return cast("TtcanPhysicalChannel", obj)


class TtcanPhysicalChannelBuilder:
    """Builder for TtcanPhysicalChannel."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TtcanPhysicalChannel = TtcanPhysicalChannel()

    def build(self) -> TtcanPhysicalChannel:
        """Build and return TtcanPhysicalChannel object.

        Returns:
            TtcanPhysicalChannel instance
        """
        # TODO: Add validation
        return self._obj
