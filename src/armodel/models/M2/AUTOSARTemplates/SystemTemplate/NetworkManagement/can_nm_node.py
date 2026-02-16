"""CanNmNode AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_node import (
    NmNode,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    TimeValue,
)


class CanNmNode(NmNode):
    """AUTOSAR CanNmNode."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("all_nm_messages", None, True, False, None),  # allNmMessages
        ("nm_car_wake_up", None, True, False, None),  # nmCarWakeUp
        ("nm_msg_cycle", None, True, False, None),  # nmMsgCycle
        ("nm_msg", None, True, False, None),  # nmMsg
    ]

    def __init__(self) -> None:
        """Initialize CanNmNode."""
        super().__init__()
        self.all_nm_messages: Optional[Boolean] = None
        self.nm_car_wake_up: Optional[Boolean] = None
        self.nm_msg_cycle: Optional[TimeValue] = None
        self.nm_msg: Optional[TimeValue] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CanNmNode to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CanNmNode":
        """Create CanNmNode from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CanNmNode instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CanNmNode since parent returns ARObject
        return cast("CanNmNode", obj)


class CanNmNodeBuilder:
    """Builder for CanNmNode."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanNmNode = CanNmNode()

    def build(self) -> CanNmNode:
        """Build and return CanNmNode object.

        Returns:
            CanNmNode instance
        """
        # TODO: Add validation
        return self._obj
