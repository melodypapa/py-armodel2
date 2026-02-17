"""CouplingPortShaper AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 123)

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
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port_fifo import (
    CouplingPortFifo,
)


class CouplingPortShaper(CouplingPortStructuralElement):
    """AUTOSAR CouplingPortShaper."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "idle_slope": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # idleSlope
        "predecessor_fifo": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=CouplingPortFifo,
        ),  # predecessorFifo
    }

    def __init__(self) -> None:
        """Initialize CouplingPortShaper."""
        super().__init__()
        self.idle_slope: Optional[PositiveInteger] = None
        self.predecessor_fifo: CouplingPortFifo = None


class CouplingPortShaperBuilder:
    """Builder for CouplingPortShaper."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CouplingPortShaper = CouplingPortShaper()

    def build(self) -> CouplingPortShaper:
        """Build and return CouplingPortShaper object.

        Returns:
            CouplingPortShaper instance
        """
        # TODO: Add validation
        return self._obj
