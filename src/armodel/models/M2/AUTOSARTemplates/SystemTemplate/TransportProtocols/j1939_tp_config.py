"""J1939TpConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 623)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_config import (
    TpConfig,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    tp_addresses: list[TpAddress]
    tp_connections: list[J1939TpConnection]
    tp_nodes: list[J1939TpNode]
    def __init__(self) -> None:
        """Initialize J1939TpConfig."""
        super().__init__()
        self.tp_addresses: list[TpAddress] = []
        self.tp_connections: list[J1939TpConnection] = []
        self.tp_nodes: list[J1939TpNode] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "J1939TpConfig":
        """Deserialize XML element to J1939TpConfig object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized J1939TpConfig object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse tp_addresses (list)
        obj.tp_addresses = []
        for child in ARObject._find_all_child_elements(element, "TP-ADDRESSES"):
            tp_addresses_value = ARObject._deserialize_by_tag(child, "TpAddress")
            obj.tp_addresses.append(tp_addresses_value)

        # Parse tp_connections (list)
        obj.tp_connections = []
        for child in ARObject._find_all_child_elements(element, "TP-CONNECTIONS"):
            tp_connections_value = ARObject._deserialize_by_tag(child, "J1939TpConnection")
            obj.tp_connections.append(tp_connections_value)

        # Parse tp_nodes (list)
        obj.tp_nodes = []
        for child in ARObject._find_all_child_elements(element, "TP-NODES"):
            tp_nodes_value = ARObject._deserialize_by_tag(child, "J1939TpNode")
            obj.tp_nodes.append(tp_nodes_value)

        return obj



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
