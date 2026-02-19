"""CanNmNode AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 684)

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


class CanNmNode(NmNode):
    """AUTOSAR CanNmNode."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    all_nm_messages: Optional[Boolean]
    nm_car_wake_up: Optional[Boolean]
    nm_msg_cycle: Optional[TimeValue]
    nm_msg: Optional[TimeValue]
    def __init__(self) -> None:
        """Initialize CanNmNode."""
        super().__init__()
        self.all_nm_messages: Optional[Boolean] = None
        self.nm_car_wake_up: Optional[Boolean] = None
        self.nm_msg_cycle: Optional[TimeValue] = None
        self.nm_msg: Optional[TimeValue] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "CanNmNode":
        """Deserialize XML element to CanNmNode object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CanNmNode object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CanNmNode, cls).deserialize(element)

        # Parse all_nm_messages
        child = ARObject._find_child_element(element, "ALL-NM-MESSAGES")
        if child is not None:
            all_nm_messages_value = child.text
            obj.all_nm_messages = all_nm_messages_value

        # Parse nm_car_wake_up
        child = ARObject._find_child_element(element, "NM-CAR-WAKE-UP")
        if child is not None:
            nm_car_wake_up_value = child.text
            obj.nm_car_wake_up = nm_car_wake_up_value

        # Parse nm_msg_cycle
        child = ARObject._find_child_element(element, "NM-MSG-CYCLE")
        if child is not None:
            nm_msg_cycle_value = child.text
            obj.nm_msg_cycle = nm_msg_cycle_value

        # Parse nm_msg
        child = ARObject._find_child_element(element, "NM-MSG")
        if child is not None:
            nm_msg_value = child.text
            obj.nm_msg = nm_msg_value

        return obj



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
