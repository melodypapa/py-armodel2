"""Ipv6Configuration AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.network_endpoint_address import (
    NetworkEndpointAddress,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Ip6AddressString,
    PositiveInteger,
)


class Ipv6Configuration(NetworkEndpointAddress):
    """AUTOSAR Ipv6Configuration."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("assignment", None, True, False, None),  # assignment
        ("default_router", None, True, False, None),  # defaultRouter
        ("dns_servers", None, False, True, None),  # dnsServers
        ("enable_anycast", None, True, False, None),  # enableAnycast
        ("hop_count", None, True, False, None),  # hopCount
        ("ip_address_keep_enum", None, False, False, IpAddressKeepEnum),  # ipAddressKeepEnum
        ("ip_address_prefix", None, True, False, None),  # ipAddressPrefix
        ("ipv6_address", None, True, False, None),  # ipv6Address
        ("ipv6_address_source", None, False, False, Ipv6AddressSourceEnum),  # ipv6AddressSource
    ]

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

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert Ipv6Configuration to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Ipv6Configuration":
        """Create Ipv6Configuration from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            Ipv6Configuration instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to Ipv6Configuration since parent returns ARObject
        return cast("Ipv6Configuration", obj)


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
