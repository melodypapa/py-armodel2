"""Ipv6NdpProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 150)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    TimeValue,
)


class Ipv6NdpProps(ARObject):
    """AUTOSAR Ipv6NdpProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    tcp_ip_ndp_default: Optional[TimeValue]
    tcp_ip_ndp_default_router_list_size: Optional[PositiveInteger]
    tcp_ip_ndp: Optional[Boolean]
    tcp_ip_ndp_delay_first_probe_time_value: Optional[TimeValue]
    tcp_ip_ndp_max_random_factor: Optional[PositiveInteger]
    tcp_ip_ndp_max_rtr: Optional[PositiveInteger]
    tcp_ip_ndp_min_random_factor: Optional[PositiveInteger]
    tcp_ip_ndp_num: Optional[PositiveInteger]
    tcp_ip_ndp_packet: Optional[Boolean]
    tcp_ip_ndp_prefix: Optional[PositiveInteger]
    tcp_ip_ndp_rnd_rtr: Optional[Boolean]
    tcp_ip_ndp_rtr: Optional[TimeValue]
    tcp_ip_ndp_slaac: Optional[Boolean]
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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "Ipv6NdpProps":
        """Deserialize XML element to Ipv6NdpProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Ipv6NdpProps object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse tcp_ip_ndp_default
        child = ARObject._find_child_element(element, "TCP-IP-NDP-DEFAULT")
        if child is not None:
            tcp_ip_ndp_default_value = child.text
            obj.tcp_ip_ndp_default = tcp_ip_ndp_default_value

        # Parse tcp_ip_ndp_default_router_list_size
        child = ARObject._find_child_element(element, "TCP-IP-NDP-DEFAULT-ROUTER-LIST-SIZE")
        if child is not None:
            tcp_ip_ndp_default_router_list_size_value = child.text
            obj.tcp_ip_ndp_default_router_list_size = tcp_ip_ndp_default_router_list_size_value

        # Parse tcp_ip_ndp
        child = ARObject._find_child_element(element, "TCP-IP-NDP")
        if child is not None:
            tcp_ip_ndp_value = child.text
            obj.tcp_ip_ndp = tcp_ip_ndp_value

        # Parse tcp_ip_ndp_delay_first_probe_time_value
        child = ARObject._find_child_element(element, "TCP-IP-NDP-DELAY-FIRST-PROBE-TIME-VALUE")
        if child is not None:
            tcp_ip_ndp_delay_first_probe_time_value_value = child.text
            obj.tcp_ip_ndp_delay_first_probe_time_value = tcp_ip_ndp_delay_first_probe_time_value_value

        # Parse tcp_ip_ndp_max_random_factor
        child = ARObject._find_child_element(element, "TCP-IP-NDP-MAX-RANDOM-FACTOR")
        if child is not None:
            tcp_ip_ndp_max_random_factor_value = child.text
            obj.tcp_ip_ndp_max_random_factor = tcp_ip_ndp_max_random_factor_value

        # Parse tcp_ip_ndp_max_rtr
        child = ARObject._find_child_element(element, "TCP-IP-NDP-MAX-RTR")
        if child is not None:
            tcp_ip_ndp_max_rtr_value = child.text
            obj.tcp_ip_ndp_max_rtr = tcp_ip_ndp_max_rtr_value

        # Parse tcp_ip_ndp_min_random_factor
        child = ARObject._find_child_element(element, "TCP-IP-NDP-MIN-RANDOM-FACTOR")
        if child is not None:
            tcp_ip_ndp_min_random_factor_value = child.text
            obj.tcp_ip_ndp_min_random_factor = tcp_ip_ndp_min_random_factor_value

        # Parse tcp_ip_ndp_num
        child = ARObject._find_child_element(element, "TCP-IP-NDP-NUM")
        if child is not None:
            tcp_ip_ndp_num_value = child.text
            obj.tcp_ip_ndp_num = tcp_ip_ndp_num_value

        # Parse tcp_ip_ndp_packet
        child = ARObject._find_child_element(element, "TCP-IP-NDP-PACKET")
        if child is not None:
            tcp_ip_ndp_packet_value = child.text
            obj.tcp_ip_ndp_packet = tcp_ip_ndp_packet_value

        # Parse tcp_ip_ndp_prefix
        child = ARObject._find_child_element(element, "TCP-IP-NDP-PREFIX")
        if child is not None:
            tcp_ip_ndp_prefix_value = child.text
            obj.tcp_ip_ndp_prefix = tcp_ip_ndp_prefix_value

        # Parse tcp_ip_ndp_rnd_rtr
        child = ARObject._find_child_element(element, "TCP-IP-NDP-RND-RTR")
        if child is not None:
            tcp_ip_ndp_rnd_rtr_value = child.text
            obj.tcp_ip_ndp_rnd_rtr = tcp_ip_ndp_rnd_rtr_value

        # Parse tcp_ip_ndp_rtr
        child = ARObject._find_child_element(element, "TCP-IP-NDP-RTR")
        if child is not None:
            tcp_ip_ndp_rtr_value = child.text
            obj.tcp_ip_ndp_rtr = tcp_ip_ndp_rtr_value

        # Parse tcp_ip_ndp_slaac
        child = ARObject._find_child_element(element, "TCP-IP-NDP-SLAAC")
        if child is not None:
            tcp_ip_ndp_slaac_value = child.text
            obj.tcp_ip_ndp_slaac = tcp_ip_ndp_slaac_value

        return obj



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
