"""Ipv4ArpProps AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    TimeValue,
)


class Ipv4ArpProps(ARObject):
    """AUTOSAR Ipv4ArpProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("tcp_ip_arp_num", None, True, False, None),  # tcpIpArpNum
        ("tcp_ip_arp_packet", None, True, False, None),  # tcpIpArpPacket
        ("tcp_ip_arp", None, True, False, None),  # tcpIpArp
        ("tcp_ip_arp_table", None, True, False, None),  # tcpIpArpTable
    ]

    def __init__(self) -> None:
        """Initialize Ipv4ArpProps."""
        super().__init__()
        self.tcp_ip_arp_num: Optional[PositiveInteger] = None
        self.tcp_ip_arp_packet: Optional[Boolean] = None
        self.tcp_ip_arp: Optional[TimeValue] = None
        self.tcp_ip_arp_table: Optional[TimeValue] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert Ipv4ArpProps to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Ipv4ArpProps":
        """Create Ipv4ArpProps from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            Ipv4ArpProps instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to Ipv4ArpProps since parent returns ARObject
        return cast("Ipv4ArpProps", obj)


class Ipv4ArpPropsBuilder:
    """Builder for Ipv4ArpProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Ipv4ArpProps = Ipv4ArpProps()

    def build(self) -> Ipv4ArpProps:
        """Build and return Ipv4ArpProps object.

        Returns:
            Ipv4ArpProps instance
        """
        # TODO: Add validation
        return self._obj
