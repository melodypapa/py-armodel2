"""FlexrayNmNode AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 679)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_NetworkManagement.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_node import (
    NmNode,
)


class FlexrayNmNode(NmNode):
    """AUTOSAR FlexrayNmNode."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

    def __init__(self) -> None:
        """Initialize FlexrayNmNode."""
        super().__init__()


class FlexrayNmNodeBuilder:
    """Builder for FlexrayNmNode."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlexrayNmNode = FlexrayNmNode()

    def build(self) -> FlexrayNmNode:
        """Build and return FlexrayNmNode object.

        Returns:
            FlexrayNmNode instance
        """
        # TODO: Add validation
        return self._obj
