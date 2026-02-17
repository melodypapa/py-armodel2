"""Ipv6Configuration AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 466)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.network_endpoint_address import (
    NetworkEndpointAddress,
)
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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "assignment": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # assignment
        "default_router": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # defaultRouter
        "dns_servers": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
        ),  # dnsServers
        "enable_anycast": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # enableAnycast
        "hop_count": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # hopCount
        "ip_address_keep_enum": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=IpAddressKeepEnum,
        ),  # ipAddressKeepEnum
        "ip_address_prefix": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # ipAddressPrefix
        "ipv6_address": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # ipv6Address
        "ipv6_address_source": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Ipv6AddressSourceEnum,
        ),  # ipv6AddressSource
    }

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
