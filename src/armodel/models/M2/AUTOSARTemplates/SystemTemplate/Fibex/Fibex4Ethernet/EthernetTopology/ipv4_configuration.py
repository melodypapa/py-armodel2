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
