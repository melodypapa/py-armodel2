"""TcpProps AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    TimeValue,
)


class TcpProps(ARObject):
    """AUTOSAR TcpProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("tcp_congestion", None, True, False, None),  # tcpCongestion
        ("tcp_delayed_ack", None, True, False, None),  # tcpDelayedAck
        ("tcp_fast_recovery", None, False, False, any (BooleanRecovery)),  # tcpFastRecovery
        ("tcp_fast", None, True, False, None),  # tcpFast
        ("tcp_fin", None, True, False, None),  # tcpFin
        ("tcp_keep_alive", None, True, False, None),  # tcpKeepAlive
        ("tcp_max_rtx", None, True, False, None),  # tcpMaxRtx
        ("tcp_msl", None, True, False, None),  # tcpMsl
        ("tcp_nagle", None, True, False, None),  # tcpNagle
        ("tcp_receive_window_max", None, True, False, None),  # tcpReceiveWindowMax
        ("tcp", None, True, False, None),  # tcp
        ("tcp_slow_start", None, True, False, None),  # tcpSlowStart
        ("tcp_syn_max_rtx", None, True, False, None),  # tcpSynMaxRtx
        ("tcp_syn_received", None, True, False, None),  # tcpSynReceived
        ("tcp_ttl", None, True, False, None),  # tcpTtl
    ]

    def __init__(self) -> None:
        """Initialize TcpProps."""
        super().__init__()
        self.tcp_congestion: Optional[Boolean] = None
        self.tcp_delayed_ack: Optional[TimeValue] = None
        self.tcp_fast_recovery: Optional[Any] = None
        self.tcp_fast: Optional[Boolean] = None
        self.tcp_fin: Optional[TimeValue] = None
        self.tcp_keep_alive: Optional[TimeValue] = None
        self.tcp_max_rtx: Optional[PositiveInteger] = None
        self.tcp_msl: Optional[TimeValue] = None
        self.tcp_nagle: Optional[Boolean] = None
        self.tcp_receive_window_max: Optional[PositiveInteger] = None
        self.tcp: Optional[TimeValue] = None
        self.tcp_slow_start: Optional[Boolean] = None
        self.tcp_syn_max_rtx: Optional[PositiveInteger] = None
        self.tcp_syn_received: Optional[TimeValue] = None
        self.tcp_ttl: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TcpProps to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TcpProps":
        """Create TcpProps from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TcpProps instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TcpProps since parent returns ARObject
        return cast("TcpProps", obj)


class TcpPropsBuilder:
    """Builder for TcpProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TcpProps = TcpProps()

    def build(self) -> TcpProps:
        """Build and return TcpProps object.

        Returns:
            TcpProps instance
        """
        # TODO: Add validation
        return self._obj
