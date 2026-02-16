"""FramePort AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.comm_connector_port import (
    CommConnectorPort,
)


class FramePort(CommConnectorPort):
    """AUTOSAR FramePort."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize FramePort."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert FramePort to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FramePort":
        """Create FramePort from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            FramePort instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to FramePort since parent returns ARObject
        return cast("FramePort", obj)


class FramePortBuilder:
    """Builder for FramePort."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FramePort = FramePort()

    def build(self) -> FramePort:
        """Build and return FramePort object.

        Returns:
            FramePort instance
        """
        # TODO: Add validation
        return self._obj
