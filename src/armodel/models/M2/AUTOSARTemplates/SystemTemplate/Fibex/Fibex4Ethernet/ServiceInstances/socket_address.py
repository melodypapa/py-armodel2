"""SocketAddress AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.application_endpoint import (
    ApplicationEndpoint,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.IPv6HeaderFilterList.i_pv6_ext_header_filter_list import (
    IPv6ExtHeaderFilterList,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.static_socket_connection import (
    StaticSocketConnection,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.TcpOptionFilterSet.tcp_option_filter_list import (
    TcpOptionFilterList,
)


class SocketAddress(Identifiable):
    """AUTOSAR SocketAddress."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("allowed_i_pv6_ext", None, False, False, IPv6ExtHeaderFilterList),  # allowedIPv6Ext
        ("allowed_tcp", None, False, False, TcpOptionFilterList),  # allowedTcp
        ("application_endpoint_endpoint", None, False, False, ApplicationEndpoint),  # applicationEndpointEndpoint
        ("connector", None, False, False, any (EthernetCommunication)),  # connector
        ("differentiated", None, True, False, None),  # differentiated
        ("flow_label", None, True, False, None),  # flowLabel
        ("multicasts", None, False, True, any (EthernetCommunication)),  # multicasts
        ("path_mtu", None, True, False, None),  # pathMtu
        ("pdu_collection", None, True, False, None),  # pduCollection
        ("static_sockets", None, False, True, StaticSocketConnection),  # staticSockets
        ("udp_checksum", None, False, False, UdpChecksumCalculationEnum),  # udpChecksum
    ]

    def __init__(self) -> None:
        """Initialize SocketAddress."""
        super().__init__()
        self.allowed_i_pv6_ext: Optional[IPv6ExtHeaderFilterList] = None
        self.allowed_tcp: Optional[TcpOptionFilterList] = None
        self.application_endpoint_endpoint: Optional[ApplicationEndpoint] = None
        self.connector: Optional[Any] = None
        self.differentiated: Optional[PositiveInteger] = None
        self.flow_label: Optional[PositiveInteger] = None
        self.multicasts: list[Any] = []
        self.path_mtu: Optional[Boolean] = None
        self.pdu_collection: Optional[TimeValue] = None
        self.static_sockets: list[StaticSocketConnection] = []
        self.udp_checksum: Optional[UdpChecksumCalculationEnum] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SocketAddress to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SocketAddress":
        """Create SocketAddress from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SocketAddress instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SocketAddress since parent returns ARObject
        return cast("SocketAddress", obj)


class SocketAddressBuilder:
    """Builder for SocketAddress."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SocketAddress = SocketAddress()

    def build(self) -> SocketAddress:
        """Build and return SocketAddress object.

        Returns:
            SocketAddress instance
        """
        # TODO: Add validation
        return self._obj
