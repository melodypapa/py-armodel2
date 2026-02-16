"""Dhcpv6Props AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class Dhcpv6Props(ARObject):
    """AUTOSAR Dhcpv6Props."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("tcp_ip_dhcp", None, True, False, None),  # tcpIpDhcp
        ("tcp_ip_dhcp_v6_inf", None, True, False, None),  # tcpIpDhcpV6Inf
        ("tcp_ip_dhcp_v6_sol", None, True, False, None),  # tcpIpDhcpV6Sol
    ]

    def __init__(self) -> None:
        """Initialize Dhcpv6Props."""
        super().__init__()
        self.tcp_ip_dhcp: Optional[TimeValue] = None
        self.tcp_ip_dhcp_v6_inf: Optional[TimeValue] = None
        self.tcp_ip_dhcp_v6_sol: Optional[TimeValue] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert Dhcpv6Props to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Dhcpv6Props":
        """Create Dhcpv6Props from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            Dhcpv6Props instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to Dhcpv6Props since parent returns ARObject
        return cast("Dhcpv6Props", obj)


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
