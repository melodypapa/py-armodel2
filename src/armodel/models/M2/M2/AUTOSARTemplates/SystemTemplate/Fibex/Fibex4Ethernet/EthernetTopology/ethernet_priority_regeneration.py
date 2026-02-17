"""EthernetPriorityRegeneration AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 128)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class EthernetPriorityRegeneration(Referrable):
    """AUTOSAR EthernetPriorityRegeneration."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "ingress_priority": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # ingressPriority
        "regenerated": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # regenerated
    }

    def __init__(self) -> None:
        """Initialize EthernetPriorityRegeneration."""
        super().__init__()
        self.ingress_priority: Optional[PositiveInteger] = None
        self.regenerated: Optional[PositiveInteger] = None


class EthernetPriorityRegenerationBuilder:
    """Builder for EthernetPriorityRegeneration."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EthernetPriorityRegeneration = EthernetPriorityRegeneration()

    def build(self) -> EthernetPriorityRegeneration:
        """Build and return EthernetPriorityRegeneration object.

        Returns:
            EthernetPriorityRegeneration instance
        """
        # TODO: Add validation
        return self._obj
