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
        # First, call parent's deserialize to handle inherited attributes
        obj = super(LinTpConfig, cls).deserialize(element)

        # Parse tp_addresses (list from container "TP-ADDRESSES")
        obj.tp_addresses = []
        container = ARObject._find_child_element(element, "TP-ADDRESSES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.tp_addresses.append(child_value)

        # Parse tp_connections (list from container "TP-CONNECTIONS")
        obj.tp_connections = []
        container = ARObject._find_child_element(element, "TP-CONNECTIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.tp_connections.append(child_value)

        # Parse tp_nodes (list from container "TP-NODES")
        obj.tp_nodes = []
        container = ARObject._find_child_element(element, "TP-NODES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.tp_nodes.append(child_value)

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
