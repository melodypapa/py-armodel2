"""EthTpConfig AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_config import (
    TpConfig,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.eth_tp_connection import (
    EthTpConnection,
)


class EthTpConfig(TpConfig):
    """AUTOSAR EthTpConfig."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("tp_connections", None, False, True, EthTpConnection),  # tpConnections
    ]

    def __init__(self) -> None:
        """Initialize EthTpConfig."""
        super().__init__()
        self.tp_connections: list[EthTpConnection] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EthTpConfig to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EthTpConfig":
        """Create EthTpConfig from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EthTpConfig instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EthTpConfig since parent returns ARObject
        return cast("EthTpConfig", obj)


class EthTpConfigBuilder:
    """Builder for EthTpConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EthTpConfig = EthTpConfig()

    def build(self) -> EthTpConfig:
        """Build and return EthTpConfig object.

        Returns:
            EthTpConfig instance
        """
        # TODO: Add validation
        return self._obj
