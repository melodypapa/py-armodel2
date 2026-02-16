"""DhcpServerConfiguration AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ipv4_dhcp_server_configuration import (
    Ipv4DhcpServerConfiguration,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ipv6_dhcp_server_configuration import (
    Ipv6DhcpServerConfiguration,
)


class DhcpServerConfiguration(ARObject):
    """AUTOSAR DhcpServerConfiguration."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("ipv4_dhcp_server", None, False, False, Ipv4DhcpServerConfiguration),  # ipv4DhcpServer
        ("ipv6_dhcp_server", None, False, False, Ipv6DhcpServerConfiguration),  # ipv6DhcpServer
    ]

    def __init__(self) -> None:
        """Initialize DhcpServerConfiguration."""
        super().__init__()
        self.ipv4_dhcp_server: Optional[Ipv4DhcpServerConfiguration] = None
        self.ipv6_dhcp_server: Optional[Ipv6DhcpServerConfiguration] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DhcpServerConfiguration to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DhcpServerConfiguration":
        """Create DhcpServerConfiguration from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DhcpServerConfiguration instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DhcpServerConfiguration since parent returns ARObject
        return cast("DhcpServerConfiguration", obj)


class DhcpServerConfigurationBuilder:
    """Builder for DhcpServerConfiguration."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DhcpServerConfiguration = DhcpServerConfiguration()

    def build(self) -> DhcpServerConfiguration:
        """Build and return DhcpServerConfiguration object.

        Returns:
            DhcpServerConfiguration instance
        """
        # TODO: Add validation
        return self._obj
