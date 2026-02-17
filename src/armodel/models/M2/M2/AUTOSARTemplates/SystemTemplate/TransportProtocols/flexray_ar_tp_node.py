"""FlexrayArTpNode AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 602)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_address import (
    TpAddress,
)


class FlexrayArTpNode(Identifiable):
    """AUTOSAR FlexrayArTpNode."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "connectors": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=Any,
        ),  # connectors
        "tp_address": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=TpAddress,
        ),  # tpAddress
    }

    def __init__(self) -> None:
        """Initialize FlexrayArTpNode."""
        super().__init__()
        self.connectors: list[Any] = []
        self.tp_address: Optional[TpAddress] = None


class FlexrayArTpNodeBuilder:
    """Builder for FlexrayArTpNode."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlexrayArTpNode = FlexrayArTpNode()

    def build(self) -> FlexrayArTpNode:
        """Build and return FlexrayArTpNode object.

        Returns:
            FlexrayArTpNode instance
        """
        # TODO: Add validation
        return self._obj
