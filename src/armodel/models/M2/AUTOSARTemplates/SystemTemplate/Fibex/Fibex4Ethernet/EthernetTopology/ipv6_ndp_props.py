"""Ipv6NdpProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 150)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    TimeValue,
)


class Ipv6NdpProps(ARObject):
    """AUTOSAR Ipv6NdpProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "tcp_ip_ndp_default": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # tcpIpNdpDefault
        "tcp_ip_ndp_default_router_list_size": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # tcpIpNdpDefaultRouterListSize
        "tcp_ip_ndp": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # tcpIpNdp
        "tcp_ip_ndp_delay_first_probe_time_value": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # tcpIpNdpDelayFirstProbeTimeValue
        "tcp_ip_ndp_max_random_factor": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # tcpIpNdpMaxRandomFactor
        "tcp_ip_ndp_max_rtr": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # tcpIpNdpMaxRtr
        "tcp_ip_ndp_min_random_factor": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # tcpIpNdpMinRandomFactor
        "tcp_ip_ndp_num": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # tcpIpNdpNum
        "tcp_ip_ndp_packet": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # tcpIpNdpPacket
        "tcp_ip_ndp_prefix": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # tcpIpNdpPrefix
        "tcp_ip_ndp_rnd_rtr": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # tcpIpNdpRndRtr
        "tcp_ip_ndp_rtr": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # tcpIpNdpRtr
        "tcp_ip_ndp_slaac": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # tcpIpNdpSlaac
    }

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
