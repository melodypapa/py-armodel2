"""Ipv6DhcpServerConfiguration AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.describable import (
    Describable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Ip6AddressString,
    TimeValue,
)


class Ipv6DhcpServerConfiguration(Describable):
    """AUTOSAR Ipv6DhcpServerConfiguration."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "address_range": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # addressRange
        "default_gateway": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # defaultGateway
        "default_lease": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # defaultLease
        "dns_servers": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
        ),  # dnsServers
        "network_mask": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # networkMask
    }

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
