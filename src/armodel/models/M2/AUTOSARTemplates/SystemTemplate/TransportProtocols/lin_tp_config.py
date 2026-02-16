"""LinTpConfig AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_config import (
    TpConfig,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.lin_tp_connection import (
    LinTpConnection,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.lin_tp_node import (
    LinTpNode,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_address import (
    TpAddress,
)


class LinTpConfig(TpConfig):
    """AUTOSAR LinTpConfig."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("tp_addresses", None, False, True, TpAddress),  # tpAddresses
        ("tp_connections", None, False, True, LinTpConnection),  # tpConnections
        ("tp_nodes", None, False, True, LinTpNode),  # tpNodes
    ]

    def __init__(self) -> None:
        """Initialize LinTpConfig."""
        super().__init__()
        self.tp_addresses: list[TpAddress] = []
        self.tp_connections: list[LinTpConnection] = []
        self.tp_nodes: list[LinTpNode] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert LinTpConfig to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LinTpConfig":
        """Create LinTpConfig from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            LinTpConfig instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to LinTpConfig since parent returns ARObject
        return cast("LinTpConfig", obj)


class LinTpConfigBuilder:
    """Builder for LinTpConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LinTpConfig = LinTpConfig()

    def build(self) -> LinTpConfig:
        """Build and return LinTpConfig object.

        Returns:
            LinTpConfig instance
        """
        # TODO: Add validation
        return self._obj
