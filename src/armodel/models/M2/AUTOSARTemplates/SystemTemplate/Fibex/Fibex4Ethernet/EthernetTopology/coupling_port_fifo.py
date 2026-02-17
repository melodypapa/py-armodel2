"""CouplingPortFifo AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 124)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port_structural_element import (
    CouplingPortStructuralElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class CouplingPortFifo(CouplingPortStructuralElement):
    """AUTOSAR CouplingPortFifo."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "assigned_traffic": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="1",
        ),  # assignedTraffic
        "minimum_fifo": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # minimumFifo
        "shaper": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (CouplingPortAbstract),
        ),  # shaper
    }

    def __init__(self) -> None:
        """Initialize CouplingPortFifo."""
        super().__init__()
        self.assigned_traffic: PositiveInteger = None
        self.minimum_fifo: Optional[PositiveInteger] = None
        self.shaper: Optional[Any] = None


class CouplingPortFifoBuilder:
    """Builder for CouplingPortFifo."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CouplingPortFifo = CouplingPortFifo()

    def build(self) -> CouplingPortFifo:
        """Build and return CouplingPortFifo object.

        Returns:
            CouplingPortFifo instance
        """
        # TODO: Add validation
        return self._obj
