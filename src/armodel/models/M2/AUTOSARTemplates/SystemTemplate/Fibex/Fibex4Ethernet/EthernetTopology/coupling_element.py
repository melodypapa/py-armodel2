"""CouplingElement AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 107)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    CouplingElementEnum,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port import (
    CouplingPort,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.ecu_instance import (
    EcuInstance,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ethernet_cluster import (
    EthernetCluster,
)
from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall.state_dependent_firewall import (
    StateDependentFirewall,
)


class CouplingElement(FibexElement):
    """AUTOSAR CouplingElement."""

    def __init__(self) -> None:
        """Initialize CouplingElement."""
        super().__init__()
        self.communication: Optional[EthernetCluster] = None
        self.coupling: Optional[CouplingElement] = None
        self.coupling_ports: list[CouplingPort] = []
        self.coupling_type: Optional[CouplingElementEnum] = None
        self.ecu_instance: Optional[EcuInstance] = None
        self.firewall_rules: list[StateDependentFirewall] = []


class CouplingElementBuilder:
    """Builder for CouplingElement."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CouplingElement = CouplingElement()

    def build(self) -> CouplingElement:
        """Build and return CouplingElement object.

        Returns:
            CouplingElement instance
        """
        # TODO: Add validation
        return self._obj
