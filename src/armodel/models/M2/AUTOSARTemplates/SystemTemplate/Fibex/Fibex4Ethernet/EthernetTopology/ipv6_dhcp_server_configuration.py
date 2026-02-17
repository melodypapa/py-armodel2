"""Ipv6DhcpServerConfiguration AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 132)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.describable import (
    Describable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Ip6AddressString,
    TimeValue,
)


class Ipv6DhcpServerConfiguration(Describable):
    """AUTOSAR Ipv6DhcpServerConfiguration."""

    address_range: Optional[Ip6AddressString]
    default_gateway: Optional[Ip6AddressString]
    default_lease: Optional[TimeValue]
    dns_servers: list[Ip6AddressString]
    network_mask: Optional[Ip6AddressString]
    def __init__(self) -> None:
        """Initialize Ipv6DhcpServerConfiguration."""
        super().__init__()
        self.address_range: Optional[Ip6AddressString] = None
        self.default_gateway: Optional[Ip6AddressString] = None
        self.default_lease: Optional[TimeValue] = None
        self.dns_servers: list[Ip6AddressString] = []
        self.network_mask: Optional[Ip6AddressString] = None


class Ipv6DhcpServerConfigurationBuilder:
    """Builder for Ipv6DhcpServerConfiguration."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Ipv6DhcpServerConfiguration = Ipv6DhcpServerConfiguration()

    def build(self) -> Ipv6DhcpServerConfiguration:
        """Build and return Ipv6DhcpServerConfiguration object.

        Returns:
            Ipv6DhcpServerConfiguration instance
        """
        # TODO: Add validation
        return self._obj
