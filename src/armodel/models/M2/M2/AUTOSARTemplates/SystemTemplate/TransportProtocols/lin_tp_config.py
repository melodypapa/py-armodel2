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

    def __init__(self) -> None:
        """Initialize LinTpConfig."""
        super().__init__()
        self.tp_addresses: list[TpAddress] = []
        self.tp_connections: list[LinTpConnection] = []
        self.tp_nodes: list[LinTpNode] = []


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
