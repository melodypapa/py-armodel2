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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.tcp_udp_config import (
    TcpUdpConfig,
)


class RtpTp(TransportProtocolConfiguration):
    """AUTOSAR RtpTp."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ssrc: Optional[PositiveInteger]
    tcp_udp_config: Optional[TcpUdpConfig]
    def __init__(self) -> None:
        """Initialize RtpTp."""
        super().__init__()
        self.ssrc: Optional[PositiveInteger] = None
        self.tcp_udp_config: Optional[TcpUdpConfig] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "RtpTp":
        """Deserialize XML element to RtpTp object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RtpTp object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse ssrc
        child = ARObject._find_child_element(element, "SSRC")
        if child is not None:
            ssrc_value = child.text
            obj.ssrc = ssrc_value

        # Parse tcp_udp_config
        child = ARObject._find_child_element(element, "TCP-UDP-CONFIG")
        if child is not None:
            tcp_udp_config_value = ARObject._deserialize_by_tag(child, "TcpUdpConfig")
            obj.tcp_udp_config = tcp_udp_config_value

        return obj



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
