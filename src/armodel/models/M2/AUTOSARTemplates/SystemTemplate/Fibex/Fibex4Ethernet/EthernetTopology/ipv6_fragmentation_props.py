"""Ipv6FragmentationProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 148)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)


class Ipv6FragmentationProps(ARObject):
    """AUTOSAR Ipv6FragmentationProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    tcp_ip_ip: Optional[TimeValue]
    tcp_ip_ip_reassembly_buffer_size: Optional[PositiveInteger]
    tcp_ip_ip_tx: Optional[PositiveInteger]
    tcp_ip_ip_tx_fragment_buffer_size: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize Ipv6FragmentationProps."""
        super().__init__()
        self.tcp_ip_ip: Optional[TimeValue] = None
        self.tcp_ip_ip_reassembly_buffer_size: Optional[PositiveInteger] = None
        self.tcp_ip_ip_tx: Optional[PositiveInteger] = None
        self.tcp_ip_ip_tx_fragment_buffer_size: Optional[PositiveInteger] = None


class Ipv6FragmentationPropsBuilder:
    """Builder for Ipv6FragmentationProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Ipv6FragmentationProps = Ipv6FragmentationProps()

    def build(self) -> Ipv6FragmentationProps:
        """Build and return Ipv6FragmentationProps object.

        Returns:
            Ipv6FragmentationProps instance
        """
        # TODO: Add validation
        return self._obj
