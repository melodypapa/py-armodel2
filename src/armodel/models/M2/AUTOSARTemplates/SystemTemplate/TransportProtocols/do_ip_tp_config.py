"""DoIpTpConfig AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_config import (
    TpConfig,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.do_ip_logic_address import (
    DoIpLogicAddress,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection.do_ip_tp_connection import (
    DoIpTpConnection,
)


class DoIpTpConfig(TpConfig):
    """AUTOSAR DoIpTpConfig."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("do_ip_logic_address_addresses", None, False, True, DoIpLogicAddress),  # doIpLogicAddressAddresses
        ("tp_connections", None, False, True, DoIpTpConnection),  # tpConnections
    ]

    def __init__(self) -> None:
        """Initialize DoIpTpConfig."""
        super().__init__()
        self.do_ip_logic_address_addresses: list[DoIpLogicAddress] = []
        self.tp_connections: list[DoIpTpConnection] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DoIpTpConfig to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DoIpTpConfig":
        """Create DoIpTpConfig from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DoIpTpConfig instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DoIpTpConfig since parent returns ARObject
        return cast("DoIpTpConfig", obj)


class DoIpTpConfigBuilder:
    """Builder for DoIpTpConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DoIpTpConfig = DoIpTpConfig()

    def build(self) -> DoIpTpConfig:
        """Build and return DoIpTpConfig object.

        Returns:
            DoIpTpConfig instance
        """
        # TODO: Add validation
        return self._obj
