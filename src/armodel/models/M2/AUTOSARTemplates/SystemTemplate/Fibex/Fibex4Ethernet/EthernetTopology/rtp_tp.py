"""RtpTp AUTOSAR element."""

from typing import Optional, cast
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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("ssrc", None, True, False, None),  # ssrc
        ("tcp_udp_config", None, False, False, TcpUdpConfig),  # tcpUdpConfig
    ]

    def __init__(self) -> None:
        """Initialize RtpTp."""
        super().__init__()
        self.ssrc: Optional[PositiveInteger] = None
        self.tcp_udp_config: Optional[TcpUdpConfig] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert RtpTp to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RtpTp":
        """Create RtpTp from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            RtpTp instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to RtpTp since parent returns ARObject
        return cast("RtpTp", obj)


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
