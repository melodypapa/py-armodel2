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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    allowed_i_pv6_ext_ref: Optional[ARRef]
    allowed_tcp_ref: Optional[ARRef]
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
        self.allowed_i_pv6_ext_ref: Optional[ARRef] = None
        self.allowed_tcp_ref: Optional[ARRef] = None
        self.application_endpoint_endpoint: Optional[ApplicationEndpoint] = None
        self.connector: Optional[Any] = None
        self.differentiated: Optional[PositiveInteger] = None
        self.flow_label: Optional[PositiveInteger] = None
        self.multicasts: list[Any] = []
        self.path_mtu: Optional[Boolean] = None
        self.pdu_collection: Optional[TimeValue] = None
        self.static_sockets: list[StaticSocketConnection] = []
        self.udp_checksum: Optional[UdpChecksumCalculationEnum] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SocketAddress":
        """Deserialize XML element to SocketAddress object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SocketAddress object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse allowed_i_pv6_ext_ref
        child = ARObject._find_child_element(element, "ALLOWED-I-PV6-EXT")
        if child is not None:
            allowed_i_pv6_ext_ref_value = ARObject._deserialize_by_tag(child, "IPv6ExtHeaderFilterList")
            obj.allowed_i_pv6_ext_ref = allowed_i_pv6_ext_ref_value

        # Parse allowed_tcp_ref
        child = ARObject._find_child_element(element, "ALLOWED-TCP")
        if child is not None:
            allowed_tcp_ref_value = ARObject._deserialize_by_tag(child, "TcpOptionFilterList")
            obj.allowed_tcp_ref = allowed_tcp_ref_value

        # Parse application_endpoint_endpoint
        child = ARObject._find_child_element(element, "APPLICATION-ENDPOINT-ENDPOINT")
        if child is not None:
            application_endpoint_endpoint_value = ARObject._deserialize_by_tag(child, "ApplicationEndpoint")
            obj.application_endpoint_endpoint = application_endpoint_endpoint_value

        # Parse connector
        child = ARObject._find_child_element(element, "CONNECTOR")
        if child is not None:
            connector_value = child.text
            obj.connector = connector_value

        # Parse differentiated
        child = ARObject._find_child_element(element, "DIFFERENTIATED")
        if child is not None:
            differentiated_value = child.text
            obj.differentiated = differentiated_value

        # Parse flow_label
        child = ARObject._find_child_element(element, "FLOW-LABEL")
        if child is not None:
            flow_label_value = child.text
            obj.flow_label = flow_label_value

        # Parse multicasts (list)
        obj.multicasts = []
        for child in ARObject._find_all_child_elements(element, "MULTICASTS"):
            multicasts_value = child.text
            obj.multicasts.append(multicasts_value)

        # Parse path_mtu
        child = ARObject._find_child_element(element, "PATH-MTU")
        if child is not None:
            path_mtu_value = child.text
            obj.path_mtu = path_mtu_value

        # Parse pdu_collection
        child = ARObject._find_child_element(element, "PDU-COLLECTION")
        if child is not None:
            pdu_collection_value = child.text
            obj.pdu_collection = pdu_collection_value

        # Parse static_sockets (list)
        obj.static_sockets = []
        for child in ARObject._find_all_child_elements(element, "STATIC-SOCKETS"):
            static_sockets_value = ARObject._deserialize_by_tag(child, "StaticSocketConnection")
            obj.static_sockets.append(static_sockets_value)

        # Parse udp_checksum
        child = ARObject._find_child_element(element, "UDP-CHECKSUM")
        if child is not None:
            udp_checksum_value = child.text
            obj.udp_checksum = udp_checksum_value

        return obj



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
