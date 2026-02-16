"""TcpIpIcmpv6Props AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class TcpIpIcmpv6Props(ARObject):
    """AUTOSAR TcpIpIcmpv6Props."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("tcp_ip_icmp", None, True, False, None),  # tcpIpIcmp
    ]

    def __init__(self) -> None:
        """Initialize TcpIpIcmpv6Props."""
        super().__init__()
        self.tcp_ip_icmp: Optional[Boolean] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TcpIpIcmpv6Props to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TcpIpIcmpv6Props":
        """Create TcpIpIcmpv6Props from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TcpIpIcmpv6Props instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TcpIpIcmpv6Props since parent returns ARObject
        return cast("TcpIpIcmpv6Props", obj)


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
