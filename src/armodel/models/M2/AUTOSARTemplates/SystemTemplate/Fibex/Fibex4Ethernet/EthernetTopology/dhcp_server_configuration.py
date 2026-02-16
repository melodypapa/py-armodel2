"""DhcpServerConfiguration AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "ipv4_dhcp_server": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Ipv4DhcpServerConfiguration,
        ),  # ipv4DhcpServer
        "ipv6_dhcp_server": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Ipv6DhcpServerConfiguration,
        ),  # ipv6DhcpServer
    }

    def __init__(self) -> None:
        """Initialize DhcpServerConfiguration."""
        super().__init__()
        self.ipv4_dhcp_server: Optional[Ipv4DhcpServerConfiguration] = None
        self.ipv6_dhcp_server: Optional[Ipv6DhcpServerConfiguration] = None


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
