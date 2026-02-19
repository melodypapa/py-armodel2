"""Ipv4Configuration AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 465)

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
    Ipv4AddressSourceEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Ip4AddressString,
    PositiveInteger,
)


class Ipv4Configuration(NetworkEndpointAddress):
    """AUTOSAR Ipv4Configuration."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    assignment: Optional[PositiveInteger]
    default_gateway: Optional[Ip4AddressString]
    dns_servers: list[Ip4AddressString]
    ip_address_keep_enum: Optional[IpAddressKeepEnum]
    ipv4_address: Optional[Ip4AddressString]
    ipv4_address_source: Optional[Ipv4AddressSourceEnum]
    network_mask: Optional[Ip4AddressString]
    ttl: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize Ipv4Configuration."""
        super().__init__()
        self.assignment: Optional[PositiveInteger] = None
        self.default_gateway: Optional[Ip4AddressString] = None
        self.dns_servers: list[Ip4AddressString] = []
        self.ip_address_keep_enum: Optional[IpAddressKeepEnum] = None
        self.ipv4_address: Optional[Ip4AddressString] = None
        self.ipv4_address_source: Optional[Ipv4AddressSourceEnum] = None
        self.network_mask: Optional[Ip4AddressString] = None
        self.ttl: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "Ipv4Configuration":
        """Deserialize XML element to Ipv4Configuration object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Ipv4Configuration object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse assignment
        child = ARObject._find_child_element(element, "ASSIGNMENT")
        if child is not None:
            assignment_value = child.text
            obj.assignment = assignment_value

        # Parse default_gateway
        child = ARObject._find_child_element(element, "DEFAULT-GATEWAY")
        if child is not None:
            default_gateway_value = child.text
            obj.default_gateway = default_gateway_value

        # Parse dns_servers (list)
        obj.dns_servers = []
        for child in ARObject._find_all_child_elements(element, "DNS-SERVERS"):
            dns_servers_value = child.text
            obj.dns_servers.append(dns_servers_value)

        # Parse ip_address_keep_enum
        child = ARObject._find_child_element(element, "IP-ADDRESS-KEEP-ENUM")
        if child is not None:
            ip_address_keep_enum_value = child.text
            obj.ip_address_keep_enum = ip_address_keep_enum_value

        # Parse ipv4_address
        child = ARObject._find_child_element(element, "IPV4-ADDRESS")
        if child is not None:
            ipv4_address_value = child.text
            obj.ipv4_address = ipv4_address_value

        # Parse ipv4_address_source
        child = ARObject._find_child_element(element, "IPV4-ADDRESS-SOURCE")
        if child is not None:
            ipv4_address_source_value = child.text
            obj.ipv4_address_source = ipv4_address_source_value

        # Parse network_mask
        child = ARObject._find_child_element(element, "NETWORK-MASK")
        if child is not None:
            network_mask_value = child.text
            obj.network_mask = network_mask_value

        # Parse ttl
        child = ARObject._find_child_element(element, "TTL")
        if child is not None:
            ttl_value = child.text
            obj.ttl = ttl_value

        return obj



class Ipv4ConfigurationBuilder:
    """Builder for Ipv4Configuration."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Ipv4Configuration = Ipv4Configuration()

    def build(self) -> Ipv4Configuration:
        """Build and return Ipv4Configuration object.

        Returns:
            Ipv4Configuration instance
        """
        # TODO: Add validation
        return self._obj
