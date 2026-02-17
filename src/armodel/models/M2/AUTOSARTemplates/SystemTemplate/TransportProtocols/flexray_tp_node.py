"""FlexrayTpNode AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 596)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_address import (
    TpAddress,
)


class FlexrayTpNode(Identifiable):
    """AUTOSAR FlexrayTpNode."""

    connectors: list[Any]
    tp_address: Optional[TpAddress]
    def __init__(self) -> None:
        """Initialize FlexrayTpNode."""
        super().__init__()
        self.connectors: list[Any] = []
        self.tp_address: Optional[TpAddress] = None


class FlexrayTpNodeBuilder:
    """Builder for FlexrayTpNode."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlexrayTpNode = FlexrayTpNode()

    def build(self) -> FlexrayTpNode:
        """Build and return FlexrayTpNode object.

        Returns:
            FlexrayTpNode instance
        """
        # TODO: Add validation
        return self._obj
