"""TcpIpIcmpv4Props AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 156)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)


class TcpIpIcmpv4Props(ARObject):
    """AUTOSAR TcpIpIcmpv4Props."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    tcp_ip_icmp: Optional[Boolean]
    tcp_ip_icmp_v4_ttl: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize TcpIpIcmpv4Props."""
        super().__init__()
        self.tcp_ip_icmp: Optional[Boolean] = None
        self.tcp_ip_icmp_v4_ttl: Optional[PositiveInteger] = None


class TcpIpIcmpv4PropsBuilder:
    """Builder for TcpIpIcmpv4Props."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TcpIpIcmpv4Props = TcpIpIcmpv4Props()

    def build(self) -> TcpIpIcmpv4Props:
        """Build and return TcpIpIcmpv4Props object.

        Returns:
            TcpIpIcmpv4Props instance
        """
        # TODO: Add validation
        return self._obj
