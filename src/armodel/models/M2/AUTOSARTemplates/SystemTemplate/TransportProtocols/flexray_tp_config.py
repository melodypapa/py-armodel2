"""FlexrayTpConfig AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_config import (
    TpConfig,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.flexray_tp_connection import (
    FlexrayTpConnection,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.flexray_tp_ecu import (
    FlexrayTpEcu,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.flexray_tp_node import (
    FlexrayTpNode,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.flexray_tp_pdu_pool import (
    FlexrayTpPduPool,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_address import (
    TpAddress,
)


class FlexrayTpConfig(TpConfig):
    """AUTOSAR FlexrayTpConfig."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("pdu_pools", None, False, True, FlexrayTpPduPool),  # pduPools
        ("tp_addresses", None, False, True, TpAddress),  # tpAddresses
        ("tp_connections", None, False, True, FlexrayTpConnection),  # tpConnections
        ("tp_ecus", None, False, True, FlexrayTpEcu),  # tpEcus
        ("tp_nodes", None, False, True, FlexrayTpNode),  # tpNodes
    ]

    def __init__(self) -> None:
        """Initialize FlexrayTpConfig."""
        super().__init__()
        self.pdu_pools: list[FlexrayTpPduPool] = []
        self.tp_addresses: list[TpAddress] = []
        self.tp_connections: list[FlexrayTpConnection] = []
        self.tp_ecus: list[FlexrayTpEcu] = []
        self.tp_nodes: list[FlexrayTpNode] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert FlexrayTpConfig to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlexrayTpConfig":
        """Create FlexrayTpConfig from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            FlexrayTpConfig instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to FlexrayTpConfig since parent returns ARObject
        return cast("FlexrayTpConfig", obj)


class FlexrayTpConfigBuilder:
    """Builder for FlexrayTpConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlexrayTpConfig = FlexrayTpConfig()

    def build(self) -> FlexrayTpConfig:
        """Build and return FlexrayTpConfig object.

        Returns:
            FlexrayTpConfig instance
        """
        # TODO: Add validation
        return self._obj
