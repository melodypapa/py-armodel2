"""EthernetPhysicalChannel AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 314)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 105)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.physical_channel import (
    PhysicalChannel,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.network_endpoint import (
    NetworkEndpoint,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.so_ad_config import (
    SoAdConfig,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.vlan_config import (
    VlanConfig,
)


class EthernetPhysicalChannel(PhysicalChannel):
    """AUTOSAR EthernetPhysicalChannel."""

    def __init__(self) -> None:
        """Initialize EthernetPhysicalChannel."""
        super().__init__()
        self.network_endpoints: list[NetworkEndpoint] = []
        self.so_ad_config: Optional[SoAdConfig] = None
        self.vlan: Optional[VlanConfig] = None


class EthernetPhysicalChannelBuilder:
    """Builder for EthernetPhysicalChannel."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EthernetPhysicalChannel = EthernetPhysicalChannel()

    def build(self) -> EthernetPhysicalChannel:
        """Build and return EthernetPhysicalChannel object.

        Returns:
            EthernetPhysicalChannel instance
        """
        # TODO: Add validation
        return self._obj
