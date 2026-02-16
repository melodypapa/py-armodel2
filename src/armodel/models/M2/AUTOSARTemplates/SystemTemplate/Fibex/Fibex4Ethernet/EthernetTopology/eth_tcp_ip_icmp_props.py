"""EthTcpIpIcmpProps AUTOSAR element."""

from typing import Optional, cast
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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("icmp_v4_props", None, False, False, TcpIpIcmpv4Props),  # icmpV4Props
        ("icmp_v6_props", None, False, False, TcpIpIcmpv6Props),  # icmpV6Props
    ]

    def __init__(self) -> None:
        """Initialize EthTcpIpIcmpProps."""
        super().__init__()
        self.icmp_v4_props: Optional[TcpIpIcmpv4Props] = None
        self.icmp_v6_props: Optional[TcpIpIcmpv6Props] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EthTcpIpIcmpProps to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EthTcpIpIcmpProps":
        """Create EthTcpIpIcmpProps from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EthTcpIpIcmpProps instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EthTcpIpIcmpProps since parent returns ARObject
        return cast("EthTcpIpIcmpProps", obj)


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
