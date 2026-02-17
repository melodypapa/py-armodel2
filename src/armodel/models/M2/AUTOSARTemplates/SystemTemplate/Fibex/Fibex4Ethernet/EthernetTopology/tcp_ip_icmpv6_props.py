"""TcpIpIcmpv6Props AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 156)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class TcpIpIcmpv6Props(ARObject):
    """AUTOSAR TcpIpIcmpv6Props."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "tcp_ip_icmp": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # tcpIpIcmp
    }

    def __init__(self) -> None:
        """Initialize TcpIpIcmpv6Props."""
        super().__init__()
        self.tcp_ip_icmp: Optional[Boolean] = None


class TcpIpIcmpv6PropsBuilder:
    """Builder for TcpIpIcmpv6Props."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TcpIpIcmpv6Props = TcpIpIcmpv6Props()

    def build(self) -> TcpIpIcmpv6Props:
        """Build and return TcpIpIcmpv6Props object.

        Returns:
            TcpIpIcmpv6Props instance
        """
        # TODO: Add validation
        return self._obj
