"""RtpTp AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "ssrc": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # ssrc
        "tcp_udp_config": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=TcpUdpConfig,
        ),  # tcpUdpConfig
    }

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
