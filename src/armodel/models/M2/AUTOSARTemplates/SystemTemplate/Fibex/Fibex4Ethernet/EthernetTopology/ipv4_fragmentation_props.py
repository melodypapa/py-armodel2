"""Ipv4FragmentationProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 147)

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


class Ipv4FragmentationProps(ARObject):
    """AUTOSAR Ipv4FragmentationProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "tcp_ip_ip": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # tcpIpIp
        "tcp_ip_ip_num": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # tcpIpIpNum
        "tcp_ip_ip_reass": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # tcpIpIpReass
    }

    def __init__(self) -> None:
        """Initialize Ipv4FragmentationProps."""
        super().__init__()
        self.tcp_ip_ip: Optional[Boolean] = None
        self.tcp_ip_ip_num: Optional[PositiveInteger] = None
        self.tcp_ip_ip_reass: Optional[TimeValue] = None


class Ipv4FragmentationPropsBuilder:
    """Builder for Ipv4FragmentationProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Ipv4FragmentationProps = Ipv4FragmentationProps()

    def build(self) -> Ipv4FragmentationProps:
        """Build and return Ipv4FragmentationProps object.

        Returns:
            Ipv4FragmentationProps instance
        """
        # TODO: Add validation
        return self._obj
