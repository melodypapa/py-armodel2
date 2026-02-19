"""Ipv6Configuration AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 466)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.network_endpoint_address import (
    NetworkEndpointAddress,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    IpAddressKeepEnum,
    Ipv6AddressSourceEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Ip6AddressString,
    PositiveInteger,
)


class Ipv6Configuration(NetworkEndpointAddress):
    """AUTOSAR Ipv6Configuration."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    assignment: Optional[PositiveInteger]
    default_router: Optional[Ip6AddressString]
    dns_servers: list[Ip6AddressString]
    enable_anycast: Optional[Boolean]
    hop_count: Optional[PositiveInteger]
    ip_address_keep_enum: Optional[IpAddressKeepEnum]
    ip_address_prefix: Optional[PositiveInteger]
    ipv6_address: Optional[Ip6AddressString]
    ipv6_address_source: Optional[Ipv6AddressSourceEnum]
    def __init__(self) -> None:
        """Initialize Ipv6Configuration."""
        super().__init__()
        self.assignment: Optional[PositiveInteger] = None
        self.default_router: Optional[Ip6AddressString] = None
        self.dns_servers: list[Ip6AddressString] = []
        self.enable_anycast: Optional[Boolean] = None
        self.hop_count: Optional[PositiveInteger] = None
        self.ip_address_keep_enum: Optional[IpAddressKeepEnum] = None
        self.ip_address_prefix: Optional[PositiveInteger] = None
        self.ipv6_address: Optional[Ip6AddressString] = None
        self.ipv6_address_source: Optional[Ipv6AddressSourceEnum] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "Ipv6Configuration":
        """Deserialize XML element to Ipv6Configuration object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Ipv6Configuration object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Ipv6Configuration, cls).deserialize(element)

        # Parse assignment
        child = ARObject._find_child_element(element, "ASSIGNMENT")
        if child is not None:
            assignment_value = child.text
            obj.assignment = assignment_value

        # Parse default_router
        child = ARObject._find_child_element(element, "DEFAULT-ROUTER")
        if child is not None:
            default_router_value = child.text
            obj.default_router = default_router_value

        # Parse dns_servers (list from container "DNS-SERVERS")
        obj.dns_servers = []
        container = ARObject._find_child_element(element, "DNS-SERVERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.dns_servers.append(child_value)

        # Parse enable_anycast
        child = ARObject._find_child_element(element, "ENABLE-ANYCAST")
        if child is not None:
            enable_anycast_value = child.text
            obj.enable_anycast = enable_anycast_value

        # Parse hop_count
        child = ARObject._find_child_element(element, "HOP-COUNT")
        if child is not None:
            hop_count_value = child.text
            obj.hop_count = hop_count_value

        # Parse ip_address_keep_enum
        child = ARObject._find_child_element(element, "IP-ADDRESS-KEEP-ENUM")
        if child is not None:
            ip_address_keep_enum_value = IpAddressKeepEnum.deserialize(child)
            obj.ip_address_keep_enum = ip_address_keep_enum_value

        # Parse ip_address_prefix
        child = ARObject._find_child_element(element, "IP-ADDRESS-PREFIX")
        if child is not None:
            ip_address_prefix_value = child.text
            obj.ip_address_prefix = ip_address_prefix_value

        # Parse ipv6_address
        child = ARObject._find_child_element(element, "IPV6-ADDRESS")
        if child is not None:
            ipv6_address_value = child.text
            obj.ipv6_address = ipv6_address_value

        # Parse ipv6_address_source
        child = ARObject._find_child_element(element, "IPV6-ADDRESS-SOURCE")
        if child is not None:
            ipv6_address_source_value = Ipv6AddressSourceEnum.deserialize(child)
            obj.ipv6_address_source = ipv6_address_source_value

        return obj



class Ipv6ConfigurationBuilder:
    """Builder for Ipv6Configuration."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Ipv6Configuration = Ipv6Configuration()

    def build(self) -> Ipv6Configuration:
        """Build and return Ipv6Configuration object.

        Returns:
            Ipv6Configuration instance
        """
        # TODO: Add validation
        return self._obj
