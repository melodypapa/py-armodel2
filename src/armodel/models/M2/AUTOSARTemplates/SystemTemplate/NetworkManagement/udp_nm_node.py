"""UdpNmNode AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 688)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_NetworkManagement.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_node import (
    NmNode,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    TimeValue,
)


class UdpNmNode(NmNode):
    """AUTOSAR UdpNmNode."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    all_nm_messages: Optional[Boolean]
    nm_msg_cycle: Optional[TimeValue]
    def __init__(self) -> None:
        """Initialize UdpNmNode."""
        super().__init__()
        self.all_nm_messages: Optional[Boolean] = None
        self.nm_msg_cycle: Optional[TimeValue] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "UdpNmNode":
        """Deserialize XML element to UdpNmNode object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized UdpNmNode object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(UdpNmNode, cls).deserialize(element)

        # Parse all_nm_messages
        child = ARObject._find_child_element(element, "ALL-NM-MESSAGES")
        if child is not None:
            all_nm_messages_value = child.text
            obj.all_nm_messages = all_nm_messages_value

        # Parse nm_msg_cycle
        child = ARObject._find_child_element(element, "NM-MSG-CYCLE")
        if child is not None:
            nm_msg_cycle_value = child.text
            obj.nm_msg_cycle = nm_msg_cycle_value

        return obj



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
