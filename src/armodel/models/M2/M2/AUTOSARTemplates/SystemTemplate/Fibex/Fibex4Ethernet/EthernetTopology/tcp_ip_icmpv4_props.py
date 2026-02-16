"""TcpIpIcmpv4Props AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)


class TcpIpIcmpv4Props(ARObject):
    """AUTOSAR TcpIpIcmpv4Props."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "tcp_ip_icmp": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # tcpIpIcmp
        "tcp_ip_icmp_v4_ttl": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # tcpIpIcmpV4Ttl
    }

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
