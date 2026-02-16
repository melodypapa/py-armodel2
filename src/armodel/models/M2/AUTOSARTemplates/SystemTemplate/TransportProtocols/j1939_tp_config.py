"""J1939TpConfig AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_config import (
    TpConfig,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.j1939_tp_connection import (
    J1939TpConnection,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.j1939_tp_node import (
    J1939TpNode,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_address import (
    TpAddress,
)


class J1939TpConfig(TpConfig):
    """AUTOSAR J1939TpConfig."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("tp_addresses", None, False, True, TpAddress),  # tpAddresses
        ("tp_connections", None, False, True, J1939TpConnection),  # tpConnections
        ("tp_nodes", None, False, True, J1939TpNode),  # tpNodes
    ]

    def __init__(self) -> None:
        """Initialize J1939TpConfig."""
        super().__init__()
        self.tp_addresses: list[TpAddress] = []
        self.tp_connections: list[J1939TpConnection] = []
        self.tp_nodes: list[J1939TpNode] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert J1939TpConfig to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "J1939TpConfig":
        """Create J1939TpConfig from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            J1939TpConfig instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to J1939TpConfig since parent returns ARObject
        return cast("J1939TpConfig", obj)


class J1939TpConfigBuilder:
    """Builder for J1939TpConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: J1939TpConfig = J1939TpConfig()

    def build(self) -> J1939TpConfig:
        """Build and return J1939TpConfig object.

        Returns:
            J1939TpConfig instance
        """
        # TODO: Add validation
        return self._obj
