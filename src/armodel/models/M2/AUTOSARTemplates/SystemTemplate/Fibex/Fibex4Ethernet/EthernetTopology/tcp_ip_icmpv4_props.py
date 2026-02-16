"""TcpIpIcmpv4Props AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)


class TcpIpIcmpv4Props(ARObject):
    """AUTOSAR TcpIpIcmpv4Props."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("tcp_ip_icmp", None, True, False, None),  # tcpIpIcmp
        ("tcp_ip_icmp_v4_ttl", None, True, False, None),  # tcpIpIcmpV4Ttl
    ]

    def __init__(self) -> None:
        """Initialize TcpIpIcmpv4Props."""
        super().__init__()
        self.tcp_ip_icmp: Optional[Boolean] = None
        self.tcp_ip_icmp_v4_ttl: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TcpIpIcmpv4Props to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TcpIpIcmpv4Props":
        """Create TcpIpIcmpv4Props from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TcpIpIcmpv4Props instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TcpIpIcmpv4Props since parent returns ARObject
        return cast("TcpIpIcmpv4Props", obj)


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
