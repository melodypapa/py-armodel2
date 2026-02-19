"""FlexrayTpConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 592)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_config import (
    TpConfig,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    pdu_pools: list[FlexrayTpPduPool]
    tp_addresses: list[TpAddress]
    tp_connections: list[FlexrayTpConnection]
    tp_ecus: list[FlexrayTpEcu]
    tp_nodes: list[FlexrayTpNode]
    def __init__(self) -> None:
        """Initialize FlexrayTpConfig."""
        super().__init__()
        self.pdu_pools: list[FlexrayTpPduPool] = []
        self.tp_addresses: list[TpAddress] = []
        self.tp_connections: list[FlexrayTpConnection] = []
        self.tp_ecus: list[FlexrayTpEcu] = []
        self.tp_nodes: list[FlexrayTpNode] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlexrayTpConfig":
        """Deserialize XML element to FlexrayTpConfig object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FlexrayTpConfig object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse pdu_pools (list)
        obj.pdu_pools = []
        for child in ARObject._find_all_child_elements(element, "PDU-POOLS"):
            pdu_pools_value = ARObject._deserialize_by_tag(child, "FlexrayTpPduPool")
            obj.pdu_pools.append(pdu_pools_value)

        # Parse tp_addresses (list)
        obj.tp_addresses = []
        for child in ARObject._find_all_child_elements(element, "TP-ADDRESSES"):
            tp_addresses_value = ARObject._deserialize_by_tag(child, "TpAddress")
            obj.tp_addresses.append(tp_addresses_value)

        # Parse tp_connections (list)
        obj.tp_connections = []
        for child in ARObject._find_all_child_elements(element, "TP-CONNECTIONS"):
            tp_connections_value = ARObject._deserialize_by_tag(child, "FlexrayTpConnection")
            obj.tp_connections.append(tp_connections_value)

        # Parse tp_ecus (list)
        obj.tp_ecus = []
        for child in ARObject._find_all_child_elements(element, "TP-ECUS"):
            tp_ecus_value = ARObject._deserialize_by_tag(child, "FlexrayTpEcu")
            obj.tp_ecus.append(tp_ecus_value)

        # Parse tp_nodes (list)
        obj.tp_nodes = []
        for child in ARObject._find_all_child_elements(element, "TP-NODES"):
            tp_nodes_value = ARObject._deserialize_by_tag(child, "FlexrayTpNode")
            obj.tp_nodes.append(tp_nodes_value)

        return obj



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
