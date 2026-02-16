"""CanTpConfig AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_config import (
    TpConfig,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.can_tp_address import (
    CanTpAddress,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.can_tp_channel import (
    CanTpChannel,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.can_tp_connection import (
    CanTpConnection,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.can_tp_ecu import (
    CanTpEcu,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.can_tp_node import (
    CanTpNode,
)


class CanTpConfig(TpConfig):
    """AUTOSAR CanTpConfig."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("tp_addresses", None, False, True, CanTpAddress),  # tpAddresses
        ("tp_channels", None, False, True, CanTpChannel),  # tpChannels
        ("tp_connections", None, False, True, CanTpConnection),  # tpConnections
        ("tp_ecus", None, False, True, CanTpEcu),  # tpEcus
        ("tp_nodes", None, False, True, CanTpNode),  # tpNodes
    ]

    def __init__(self) -> None:
        """Initialize CanTpConfig."""
        super().__init__()
        self.tp_addresses: list[CanTpAddress] = []
        self.tp_channels: list[CanTpChannel] = []
        self.tp_connections: list[CanTpConnection] = []
        self.tp_ecus: list[CanTpEcu] = []
        self.tp_nodes: list[CanTpNode] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CanTpConfig to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CanTpConfig":
        """Create CanTpConfig from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CanTpConfig instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CanTpConfig since parent returns ARObject
        return cast("CanTpConfig", obj)


class CanTpConfigBuilder:
    """Builder for CanTpConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanTpConfig = CanTpConfig()

    def build(self) -> CanTpConfig:
        """Build and return CanTpConfig object.

        Returns:
            CanTpConfig instance
        """
        # TODO: Add validation
        return self._obj
