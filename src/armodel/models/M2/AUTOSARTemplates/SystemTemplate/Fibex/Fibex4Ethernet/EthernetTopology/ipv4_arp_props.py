"""Ipv4ArpProps AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    TimeValue,
)


class Ipv4ArpProps(ARObject):
    """AUTOSAR Ipv4ArpProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "tcp_ip_arp_num": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # tcpIpArpNum
        "tcp_ip_arp_packet": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # tcpIpArpPacket
        "tcp_ip_arp": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # tcpIpArp
        "tcp_ip_arp_table": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # tcpIpArpTable
    }

    def __init__(self) -> None:
        """Initialize Ipv4ArpProps."""
        super().__init__()
        self.tcp_ip_arp_num: Optional[PositiveInteger] = None
        self.tcp_ip_arp_packet: Optional[Boolean] = None
        self.tcp_ip_arp: Optional[TimeValue] = None
        self.tcp_ip_arp_table: Optional[TimeValue] = None


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
