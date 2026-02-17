"""RtpTp AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 460)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.transport_protocol_configuration import (
    TransportProtocolConfiguration,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.tcp_udp_config import (
    TcpUdpConfig,
)


class RtpTp(TransportProtocolConfiguration):
    """AUTOSAR RtpTp."""

    ssrc: Optional[PositiveInteger]
    tcp_udp_config: Optional[TcpUdpConfig]
    def __init__(self) -> None:
        """Initialize RtpTp."""
        super().__init__()
        self.ssrc: Optional[PositiveInteger] = None
        self.tcp_udp_config: Optional[TcpUdpConfig] = None


class RtpTpBuilder:
    """Builder for RtpTp."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RtpTp = RtpTp()

    def build(self) -> RtpTp:
        """Build and return RtpTp object.

        Returns:
            RtpTp instance
        """
        # TODO: Add validation
        return self._obj
