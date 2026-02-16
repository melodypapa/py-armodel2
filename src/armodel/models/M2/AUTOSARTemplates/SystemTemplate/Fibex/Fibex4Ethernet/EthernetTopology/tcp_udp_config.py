"""TcpUdpConfig AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.transport_protocol_configuration import (
    TransportProtocolConfiguration,
)


class TcpUdpConfig(TransportProtocolConfiguration):
    """AUTOSAR TcpUdpConfig."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize TcpUdpConfig."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TcpUdpConfig to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TcpUdpConfig":
        """Create TcpUdpConfig from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TcpUdpConfig instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TcpUdpConfig since parent returns ARObject
        return cast("TcpUdpConfig", obj)


class TcpUdpConfigBuilder:
    """Builder for TcpUdpConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TcpUdpConfig = TcpUdpConfig()

    def build(self) -> TcpUdpConfig:
        """Build and return TcpUdpConfig object.

        Returns:
            TcpUdpConfig instance
        """
        # TODO: Add validation
        return self._obj
