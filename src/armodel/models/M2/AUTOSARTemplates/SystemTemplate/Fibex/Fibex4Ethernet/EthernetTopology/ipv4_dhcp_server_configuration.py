"""Ipv4DhcpServerConfiguration AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 131)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.describable import (
    Describable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Ip4AddressString,
    TimeValue,
)


class Ipv4DhcpServerConfiguration(Describable):
    """AUTOSAR Ipv4DhcpServerConfiguration."""

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
        """Initialize Ipv4DhcpServerConfiguration."""
        super().__init__()
        self.address_range: Optional[Ip4AddressString] = None
        self.default_gateway: Optional[Ip4AddressString] = None
        self.default_lease: Optional[TimeValue] = None
        self.dns_servers: list[Ip4AddressString] = []
        self.network_mask: Optional[Ip4AddressString] = None


class Ipv4DhcpServerConfigurationBuilder:
    """Builder for Ipv4DhcpServerConfiguration."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Ipv4DhcpServerConfiguration = Ipv4DhcpServerConfiguration()

    def build(self) -> Ipv4DhcpServerConfiguration:
        """Build and return Ipv4DhcpServerConfiguration object.

        Returns:
            Ipv4DhcpServerConfiguration instance
        """
        # TODO: Add validation
        return self._obj
