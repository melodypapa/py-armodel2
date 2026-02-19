"""Dhcpv6Props AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 149)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class Dhcpv6Props(ARObject):
    """AUTOSAR Dhcpv6Props."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    tcp_ip_dhcp: Optional[TimeValue]
    tcp_ip_dhcp_v6_inf: Optional[TimeValue]
    tcp_ip_dhcp_v6_sol: Optional[TimeValue]
    def __init__(self) -> None:
        """Initialize Dhcpv6Props."""
        super().__init__()
        self.tcp_ip_dhcp: Optional[TimeValue] = None
        self.tcp_ip_dhcp_v6_inf: Optional[TimeValue] = None
        self.tcp_ip_dhcp_v6_sol: Optional[TimeValue] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "Dhcpv6Props":
        """Deserialize XML element to Dhcpv6Props object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Dhcpv6Props object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse tcp_ip_dhcp
        child = ARObject._find_child_element(element, "TCP-IP-DHCP")
        if child is not None:
            tcp_ip_dhcp_value = child.text
            obj.tcp_ip_dhcp = tcp_ip_dhcp_value

        # Parse tcp_ip_dhcp_v6_inf
        child = ARObject._find_child_element(element, "TCP-IP-DHCP-V6-INF")
        if child is not None:
            tcp_ip_dhcp_v6_inf_value = child.text
            obj.tcp_ip_dhcp_v6_inf = tcp_ip_dhcp_v6_inf_value

        # Parse tcp_ip_dhcp_v6_sol
        child = ARObject._find_child_element(element, "TCP-IP-DHCP-V6-SOL")
        if child is not None:
            tcp_ip_dhcp_v6_sol_value = child.text
            obj.tcp_ip_dhcp_v6_sol = tcp_ip_dhcp_v6_sol_value

        return obj



class Dhcpv6PropsBuilder:
    """Builder for Dhcpv6Props."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Dhcpv6Props = Dhcpv6Props()

    def build(self) -> Dhcpv6Props:
        """Build and return Dhcpv6Props object.

        Returns:
            Dhcpv6Props instance
        """
        # TODO: Add validation
        return self._obj
