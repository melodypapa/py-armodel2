"""CouplingPortConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 112)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port import (
    CouplingPort,
)


class CouplingPortConnection(ARObject):
    """AUTOSAR CouplingPortConnection."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    first_port: Optional[CouplingPort]
    node_ports: list[CouplingPort]
    plca_local_node: Optional[PositiveInteger]
    plca_transmit: Optional[PositiveInteger]
    second_port: Optional[CouplingPort]
    def __init__(self) -> None:
        """Initialize CouplingPortConnection."""
        super().__init__()
        self.first_port: Optional[CouplingPort] = None
        self.node_ports: list[CouplingPort] = []
        self.plca_local_node: Optional[PositiveInteger] = None
        self.plca_transmit: Optional[PositiveInteger] = None
        self.second_port: Optional[CouplingPort] = None


class CouplingPortConnectionBuilder:
    """Builder for CouplingPortConnection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CouplingPortConnection = CouplingPortConnection()

    def build(self) -> CouplingPortConnection:
        """Build and return CouplingPortConnection object.

        Returns:
            CouplingPortConnection instance
        """
        # TODO: Add validation
        return self._obj
