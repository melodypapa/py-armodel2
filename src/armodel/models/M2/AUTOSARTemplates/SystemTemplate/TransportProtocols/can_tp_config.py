"""CanTpConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 606)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_config import (
    TpConfig,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    tp_addresses: list[CanTpAddress]
    tp_channels: list[CanTpChannel]
    tp_connections: list[CanTpConnection]
    tp_ecus: list[CanTpEcu]
    tp_nodes: list[CanTpNode]
    def __init__(self) -> None:
        """Initialize CanTpConfig."""
        super().__init__()
        self.tp_addresses: list[CanTpAddress] = []
        self.tp_channels: list[CanTpChannel] = []
        self.tp_connections: list[CanTpConnection] = []
        self.tp_ecus: list[CanTpEcu] = []
        self.tp_nodes: list[CanTpNode] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "CanTpConfig":
        """Deserialize XML element to CanTpConfig object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CanTpConfig object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse tp_addresses (list)
        obj.tp_addresses = []
        for child in ARObject._find_all_child_elements(element, "TP-ADDRESSES"):
            tp_addresses_value = ARObject._deserialize_by_tag(child, "CanTpAddress")
            obj.tp_addresses.append(tp_addresses_value)

        # Parse tp_channels (list)
        obj.tp_channels = []
        for child in ARObject._find_all_child_elements(element, "TP-CHANNELS"):
            tp_channels_value = ARObject._deserialize_by_tag(child, "CanTpChannel")
            obj.tp_channels.append(tp_channels_value)

        # Parse tp_connections (list)
        obj.tp_connections = []
        for child in ARObject._find_all_child_elements(element, "TP-CONNECTIONS"):
            tp_connections_value = ARObject._deserialize_by_tag(child, "CanTpConnection")
            obj.tp_connections.append(tp_connections_value)

        # Parse tp_ecus (list)
        obj.tp_ecus = []
        for child in ARObject._find_all_child_elements(element, "TP-ECUS"):
            tp_ecus_value = ARObject._deserialize_by_tag(child, "CanTpEcu")
            obj.tp_ecus.append(tp_ecus_value)

        # Parse tp_nodes (list)
        obj.tp_nodes = []
        for child in ARObject._find_all_child_elements(element, "TP-NODES"):
            tp_nodes_value = ARObject._deserialize_by_tag(child, "CanTpNode")
            obj.tp_nodes.append(tp_nodes_value)

        return obj



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
