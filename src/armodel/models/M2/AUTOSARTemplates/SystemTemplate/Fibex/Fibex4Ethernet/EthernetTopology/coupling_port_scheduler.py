"""CouplingPortScheduler AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 123)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port_structural_element import (
    CouplingPortStructuralElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    EthernetCouplingPortSchedulerEnum,
)


class CouplingPortScheduler(CouplingPortStructuralElement):
    """AUTOSAR CouplingPortScheduler."""

    def __init__(self) -> None:
        """Initialize CouplingPortScheduler."""
        super().__init__()
        self.port_scheduler_scheduler_enum: Optional[EthernetCouplingPortSchedulerEnum] = None
        self.predecessors: list[CouplingPortStructuralElement] = []


class CouplingPortSchedulerBuilder:
    """Builder for CouplingPortScheduler."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CouplingPortScheduler = CouplingPortScheduler()

    def build(self) -> CouplingPortScheduler:
        """Build and return CouplingPortScheduler object.

        Returns:
            CouplingPortScheduler instance
        """
        # TODO: Add validation
        return self._obj
