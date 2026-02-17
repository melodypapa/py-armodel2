"""UdpTp AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 459)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.tcp_udp_config import (
    TcpUdpConfig,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.tp_port import (
    TpPort,
)


class UdpTp(TcpUdpConfig):
    """AUTOSAR UdpTp."""

    udp_tp_port: Optional[TpPort]
    def __init__(self) -> None:
        """Initialize UdpTp."""
        super().__init__()
        self.udp_tp_port: Optional[TpPort] = None


class UdpTpBuilder:
    """Builder for UdpTp."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: UdpTp = UdpTp()

    def build(self) -> UdpTp:
        """Build and return UdpTp object.

        Returns:
            UdpTp instance
        """
        # TODO: Add validation
        return self._obj
