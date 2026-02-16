"""CanNmNode AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "all_nm_messages": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # allNmMessages
        "nm_car_wake_up": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # nmCarWakeUp
        "nm_msg_cycle": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # nmMsgCycle
        "nm_msg": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # nmMsg
    }

    def __init__(self) -> None:
        """Initialize CanNmNode."""
        super().__init__()
        self.all_nm_messages: Optional[Boolean] = None
        self.nm_car_wake_up: Optional[Boolean] = None
        self.nm_msg_cycle: Optional[TimeValue] = None
        self.nm_msg: Optional[TimeValue] = None


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
