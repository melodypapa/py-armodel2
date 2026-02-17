"""EthTcpIpIcmpProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 156)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.tcp_ip_icmpv4_props import (
    TcpIpIcmpv4Props,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.tcp_ip_icmpv6_props import (
    TcpIpIcmpv6Props,
)


class EthTcpIpIcmpProps(ARElement):
    """AUTOSAR EthTcpIpIcmpProps."""

    icmp_v4_props: Optional[TcpIpIcmpv4Props]
    icmp_v6_props: Optional[TcpIpIcmpv6Props]
    def __init__(self) -> None:
        """Initialize EthTcpIpIcmpProps."""
        super().__init__()
        self.icmp_v4_props: Optional[TcpIpIcmpv4Props] = None
        self.icmp_v6_props: Optional[TcpIpIcmpv6Props] = None


class EthTcpIpIcmpPropsBuilder:
    """Builder for EthTcpIpIcmpProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EthTcpIpIcmpProps = EthTcpIpIcmpProps()

    def build(self) -> EthTcpIpIcmpProps:
        """Build and return EthTcpIpIcmpProps object.

        Returns:
            EthTcpIpIcmpProps instance
        """
        # TODO: Add validation
        return self._obj
