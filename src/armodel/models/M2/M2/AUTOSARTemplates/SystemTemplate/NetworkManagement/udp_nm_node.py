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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    TimeValue,
)


class UdpNmNode(NmNode):
    """AUTOSAR UdpNmNode."""

    def __init__(self) -> None:
        """Initialize UdpNmNode."""
        super().__init__()
        self.all_nm_messages: Optional[Boolean] = None
        self.nm_msg_cycle: Optional[TimeValue] = None


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
