"""UdpTp AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.tcp_udp_config import (
    TcpUdpConfig,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.tp_port import (
    TpPort,
)


class UdpTp(TcpUdpConfig):
    """AUTOSAR UdpTp."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "udp_tp_port": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=TpPort,
        ),  # udpTpPort
    }

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
