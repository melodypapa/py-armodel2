"""UdpTp AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.tcp_udp_config import (
    TcpUdpConfig,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.tp_port import (
    TpPort,
)


class UdpTp(TcpUdpConfig):
    """AUTOSAR UdpTp."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("udp_tp_port", None, False, False, TpPort),  # udpTpPort
    ]

    def __init__(self) -> None:
        """Initialize UdpTp."""
        super().__init__()
        self.udp_tp_port: Optional[TpPort] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert UdpTp to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "UdpTp":
        """Create UdpTp from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            UdpTp instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to UdpTp since parent returns ARObject
        return cast("UdpTp", obj)


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
