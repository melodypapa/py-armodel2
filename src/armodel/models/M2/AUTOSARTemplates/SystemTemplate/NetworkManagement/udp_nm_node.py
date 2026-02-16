"""UdpNmNode AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_node import (
    NmNode,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    TimeValue,
)


class UdpNmNode(NmNode):
    """AUTOSAR UdpNmNode."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("all_nm_messages", None, True, False, None),  # allNmMessages
        ("nm_msg_cycle", None, True, False, None),  # nmMsgCycle
    ]

    def __init__(self) -> None:
        """Initialize UdpNmNode."""
        super().__init__()
        self.all_nm_messages: Optional[Boolean] = None
        self.nm_msg_cycle: Optional[TimeValue] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert UdpNmNode to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "UdpNmNode":
        """Create UdpNmNode from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            UdpNmNode instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to UdpNmNode since parent returns ARObject
        return cast("UdpNmNode", obj)


class UdpNmNodeBuilder:
    """Builder for UdpNmNode."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: UdpNmNode = UdpNmNode()

    def build(self) -> UdpNmNode:
        """Build and return UdpNmNode object.

        Returns:
            UdpNmNode instance
        """
        # TODO: Add validation
        return self._obj
