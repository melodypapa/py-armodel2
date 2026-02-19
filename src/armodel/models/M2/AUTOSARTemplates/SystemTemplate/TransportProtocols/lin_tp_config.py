"""LinTpConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 614)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_config import (
    TpConfig,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    tp_addresses: list[TpAddress]
    tp_connections: list[LinTpConnection]
    tp_nodes: list[LinTpNode]
    def __init__(self) -> None:
        """Initialize LinTpConfig."""
        super().__init__()
        self.tp_addresses: list[TpAddress] = []
        self.tp_connections: list[LinTpConnection] = []
        self.tp_nodes: list[LinTpNode] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "LinTpConfig":
        """Deserialize XML element to LinTpConfig object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LinTpConfig object
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
            tp_connections_value = ARObject._deserialize_by_tag(child, "LinTpConnection")
            obj.tp_connections.append(tp_connections_value)

        # Parse tp_nodes (list)
        obj.tp_nodes = []
        for child in ARObject._find_all_child_elements(element, "TP-NODES"):
            tp_nodes_value = ARObject._deserialize_by_tag(child, "LinTpNode")
            obj.tp_nodes.append(tp_nodes_value)

        return obj



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
