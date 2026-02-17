"""EthTcpIpProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 153)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.tcp_props import (
    TcpProps,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.udp_props import (
    UdpProps,
)


class EthTcpIpProps(ARElement):
    """AUTOSAR EthTcpIpProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "tcp_props": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=TcpProps,
        ),  # tcpProps
        "udp_props": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=UdpProps,
        ),  # udpProps
    }

    def __init__(self) -> None:
        """Initialize EthTcpIpProps."""
        super().__init__()
        self.tcp_props: Optional[TcpProps] = None
        self.udp_props: Optional[UdpProps] = None


class EthTcpIpPropsBuilder:
    """Builder for EthTcpIpProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EthTcpIpProps = EthTcpIpProps()

    def build(self) -> EthTcpIpProps:
        """Build and return EthTcpIpProps object.

        Returns:
            EthTcpIpProps instance
        """
        # TODO: Add validation
        return self._obj
