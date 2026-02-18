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
