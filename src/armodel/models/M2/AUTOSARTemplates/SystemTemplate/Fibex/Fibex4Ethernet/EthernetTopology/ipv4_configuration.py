"""Ipv4Configuration AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.network_endpoint_address import (
    NetworkEndpointAddress,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Ip4AddressString,
    PositiveInteger,
)


class Ipv4Configuration(NetworkEndpointAddress):
    """AUTOSAR Ipv4Configuration."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("assignment", None, True, False, None),  # assignment
        ("default_gateway", None, True, False, None),  # defaultGateway
        ("dns_servers", None, False, True, None),  # dnsServers
        ("ip_address_keep_enum", None, False, False, IpAddressKeepEnum),  # ipAddressKeepEnum
        ("ipv4_address", None, True, False, None),  # ipv4Address
        ("ipv4_address_source", None, False, False, Ipv4AddressSourceEnum),  # ipv4AddressSource
        ("network_mask", None, True, False, None),  # networkMask
        ("ttl", None, True, False, None),  # ttl
    ]

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

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert Ipv4Configuration to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Ipv4Configuration":
        """Create Ipv4Configuration from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            Ipv4Configuration instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to Ipv4Configuration since parent returns ARObject
        return cast("Ipv4Configuration", obj)


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
