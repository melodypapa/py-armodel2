"""CouplingPortFifo AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 124)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port_structural_element import (
    CouplingPortStructuralElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class CouplingPortFifo(CouplingPortStructuralElement):
    """AUTOSAR CouplingPortFifo."""

    assigned_traffic: PositiveInteger
    minimum_fifo: Optional[PositiveInteger]
    shaper: Optional[Any]
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
