"""Ipv4DhcpServerConfiguration AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
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
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("address_range", None, True, False, None),  # addressRange
        ("default_gateway", None, True, False, None),  # defaultGateway
        ("default_lease", None, True, False, None),  # defaultLease
        ("dns_servers", None, False, True, None),  # dnsServers
        ("network_mask", None, True, False, None),  # networkMask
    ]

    def __init__(self) -> None:
        """Initialize Ipv4DhcpServerConfiguration."""
        super().__init__()
        self.address_range: Optional[Ip4AddressString] = None
        self.default_gateway: Optional[Ip4AddressString] = None
        self.default_lease: Optional[TimeValue] = None
        self.dns_servers: list[Ip4AddressString] = []
        self.network_mask: Optional[Ip4AddressString] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert Ipv4DhcpServerConfiguration to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Ipv4DhcpServerConfiguration":
        """Create Ipv4DhcpServerConfiguration from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            Ipv4DhcpServerConfiguration instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to Ipv4DhcpServerConfiguration since parent returns ARObject
        return cast("Ipv4DhcpServerConfiguration", obj)


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
