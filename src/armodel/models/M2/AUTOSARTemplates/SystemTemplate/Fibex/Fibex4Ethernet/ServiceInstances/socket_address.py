"""SocketAddress AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 452)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ServiceInstances.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import (
    UdpChecksumCalculationEnum,
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
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.TcpOptionFilterSet.tcp_option_filter_list import (
    TcpOptionFilterList,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.static_socket_connection import (
        StaticSocketConnection,
    )



class SocketAddress(Identifiable):
    """AUTOSAR SocketAddress."""

    allowed_i_pv6_ext: Optional[IPv6ExtHeaderFilterList]
    allowed_tcp: Optional[TcpOptionFilterList]
    application_endpoint_endpoint: Optional[ApplicationEndpoint]
    connector: Optional[Any]
    differentiated: Optional[PositiveInteger]
    flow_label: Optional[PositiveInteger]
    multicasts: list[Any]
    path_mtu: Optional[Boolean]
    pdu_collection: Optional[TimeValue]
    static_sockets: list[StaticSocketConnection]
    udp_checksum: Optional[UdpChecksumCalculationEnum]
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
