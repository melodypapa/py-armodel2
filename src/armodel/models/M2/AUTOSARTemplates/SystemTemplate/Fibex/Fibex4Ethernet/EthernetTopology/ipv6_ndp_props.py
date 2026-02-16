"""Ipv6NdpProps AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    TimeValue,
)


class Ipv6NdpProps(ARObject):
    """AUTOSAR Ipv6NdpProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("tcp_ip_ndp_default", None, True, False, None),  # tcpIpNdpDefault
        ("tcp_ip_ndp_default_router_list_size", None, True, False, None),  # tcpIpNdpDefaultRouterListSize
        ("tcp_ip_ndp", None, True, False, None),  # tcpIpNdp
        ("tcp_ip_ndp_delay_first_probe_time_value", None, True, False, None),  # tcpIpNdpDelayFirstProbeTimeValue
        ("tcp_ip_ndp_max_random_factor", None, True, False, None),  # tcpIpNdpMaxRandomFactor
        ("tcp_ip_ndp_max_rtr", None, True, False, None),  # tcpIpNdpMaxRtr
        ("tcp_ip_ndp_min_random_factor", None, True, False, None),  # tcpIpNdpMinRandomFactor
        ("tcp_ip_ndp_num", None, True, False, None),  # tcpIpNdpNum
        ("tcp_ip_ndp_packet", None, True, False, None),  # tcpIpNdpPacket
        ("tcp_ip_ndp_prefix", None, True, False, None),  # tcpIpNdpPrefix
        ("tcp_ip_ndp_rnd_rtr", None, True, False, None),  # tcpIpNdpRndRtr
        ("tcp_ip_ndp_rtr", None, True, False, None),  # tcpIpNdpRtr
        ("tcp_ip_ndp_slaac", None, True, False, None),  # tcpIpNdpSlaac
    ]

    def __init__(self) -> None:
        """Initialize Ipv6NdpProps."""
        super().__init__()
        self.tcp_ip_ndp_default: Optional[TimeValue] = None
        self.tcp_ip_ndp_default_router_list_size: Optional[PositiveInteger] = None
        self.tcp_ip_ndp: Optional[Boolean] = None
        self.tcp_ip_ndp_delay_first_probe_time_value: Optional[TimeValue] = None
        self.tcp_ip_ndp_max_random_factor: Optional[PositiveInteger] = None
        self.tcp_ip_ndp_max_rtr: Optional[PositiveInteger] = None
        self.tcp_ip_ndp_min_random_factor: Optional[PositiveInteger] = None
        self.tcp_ip_ndp_num: Optional[PositiveInteger] = None
        self.tcp_ip_ndp_packet: Optional[Boolean] = None
        self.tcp_ip_ndp_prefix: Optional[PositiveInteger] = None
        self.tcp_ip_ndp_rnd_rtr: Optional[Boolean] = None
        self.tcp_ip_ndp_rtr: Optional[TimeValue] = None
        self.tcp_ip_ndp_slaac: Optional[Boolean] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert Ipv6NdpProps to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Ipv6NdpProps":
        """Create Ipv6NdpProps from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            Ipv6NdpProps instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to Ipv6NdpProps since parent returns ARObject
        return cast("Ipv6NdpProps", obj)


class Ipv6NdpPropsBuilder:
    """Builder for Ipv6NdpProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Ipv6NdpProps = Ipv6NdpProps()

    def build(self) -> Ipv6NdpProps:
        """Build and return Ipv6NdpProps object.

        Returns:
            Ipv6NdpProps instance
        """
        # TODO: Add validation
        return self._obj
