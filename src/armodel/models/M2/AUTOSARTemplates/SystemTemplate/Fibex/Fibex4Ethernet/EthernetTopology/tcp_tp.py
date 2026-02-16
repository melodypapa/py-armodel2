"""TcpTp AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.tcp_udp_config import (
    TcpUdpConfig,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.tp_port import (
    TpPort,
)


class TcpTp(TcpUdpConfig):
    """AUTOSAR TcpTp."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("keep_alive", None, True, False, None),  # keepAlive
        ("keep_alives", None, True, False, None),  # keepAlives
        ("keep_alive_time", None, True, False, None),  # keepAliveTime
        ("nagles_algorithm", None, True, False, None),  # naglesAlgorithm
        ("receive_window_min", None, True, False, None),  # receiveWindowMin
        ("tcp", None, True, False, None),  # tcp
        ("tcp_tp_port", None, False, False, TpPort),  # tcpTpPort
    ]

    def __init__(self) -> None:
        """Initialize TcpTp."""
        super().__init__()
        self.keep_alive: Optional[PositiveInteger] = None
        self.keep_alives: Optional[Boolean] = None
        self.keep_alive_time: Optional[TimeValue] = None
        self.nagles_algorithm: Optional[Boolean] = None
        self.receive_window_min: Optional[PositiveInteger] = None
        self.tcp: Optional[TimeValue] = None
        self.tcp_tp_port: Optional[TpPort] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TcpTp to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TcpTp":
        """Create TcpTp from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TcpTp instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TcpTp since parent returns ARObject
        return cast("TcpTp", obj)


class TcpTpBuilder:
    """Builder for TcpTp."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TcpTp = TcpTp()

    def build(self) -> TcpTp:
        """Build and return TcpTp object.

        Returns:
            TcpTp instance
        """
        # TODO: Add validation
        return self._obj
