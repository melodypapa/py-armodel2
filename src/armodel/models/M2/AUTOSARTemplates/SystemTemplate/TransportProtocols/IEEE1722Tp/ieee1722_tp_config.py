"""IEEE1722TpConfig AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_config import (
    TpConfig,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.ieee1722_tp_connection import (
    IEEE1722TpConnection,
)


class IEEE1722TpConfig(TpConfig):
    """AUTOSAR IEEE1722TpConfig."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("tp_connections", None, False, True, IEEE1722TpConnection),  # tpConnections
    ]

    def __init__(self) -> None:
        """Initialize IEEE1722TpConfig."""
        super().__init__()
        self.tp_connections: list[IEEE1722TpConnection] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert IEEE1722TpConfig to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IEEE1722TpConfig":
        """Create IEEE1722TpConfig from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            IEEE1722TpConfig instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to IEEE1722TpConfig since parent returns ARObject
        return cast("IEEE1722TpConfig", obj)


class IEEE1722TpConfigBuilder:
    """Builder for IEEE1722TpConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IEEE1722TpConfig = IEEE1722TpConfig()

    def build(self) -> IEEE1722TpConfig:
        """Build and return IEEE1722TpConfig object.

        Returns:
            IEEE1722TpConfig instance
        """
        # TODO: Add validation
        return self._obj
