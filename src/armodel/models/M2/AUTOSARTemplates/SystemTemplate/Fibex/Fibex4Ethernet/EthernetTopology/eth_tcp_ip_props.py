"""EthTcpIpProps AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
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
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("tcp_props", None, False, False, TcpProps),  # tcpProps
        ("udp_props", None, False, False, UdpProps),  # udpProps
    ]

    def __init__(self) -> None:
        """Initialize EthTcpIpProps."""
        super().__init__()
        self.tcp_props: Optional[TcpProps] = None
        self.udp_props: Optional[UdpProps] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EthTcpIpProps to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EthTcpIpProps":
        """Create EthTcpIpProps from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EthTcpIpProps instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EthTcpIpProps since parent returns ARObject
        return cast("EthTcpIpProps", obj)


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
