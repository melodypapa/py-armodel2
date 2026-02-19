"""DhcpServerConfiguration AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 131)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ipv4_dhcp_server_configuration import (
    Ipv4DhcpServerConfiguration,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ipv6_dhcp_server_configuration import (
    Ipv6DhcpServerConfiguration,
)


class DhcpServerConfiguration(ARObject):
    """AUTOSAR DhcpServerConfiguration."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ipv4_dhcp_server: Optional[Ipv4DhcpServerConfiguration]
    ipv6_dhcp_server: Optional[Ipv6DhcpServerConfiguration]
    def __init__(self) -> None:
        """Initialize DhcpServerConfiguration."""
        super().__init__()
        self.ipv4_dhcp_server: Optional[Ipv4DhcpServerConfiguration] = None
        self.ipv6_dhcp_server: Optional[Ipv6DhcpServerConfiguration] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DhcpServerConfiguration":
        """Deserialize XML element to DhcpServerConfiguration object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DhcpServerConfiguration object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse ipv4_dhcp_server
        child = ARObject._find_child_element(element, "IPV4-DHCP-SERVER")
        if child is not None:
            ipv4_dhcp_server_value = ARObject._deserialize_by_tag(child, "Ipv4DhcpServerConfiguration")
            obj.ipv4_dhcp_server = ipv4_dhcp_server_value

        # Parse ipv6_dhcp_server
        child = ARObject._find_child_element(element, "IPV6-DHCP-SERVER")
        if child is not None:
            ipv6_dhcp_server_value = ARObject._deserialize_by_tag(child, "Ipv6DhcpServerConfiguration")
            obj.ipv6_dhcp_server = ipv6_dhcp_server_value

        return obj



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
