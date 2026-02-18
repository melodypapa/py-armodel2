"""EthTpConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 617)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_config import (
    TpConfig,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.eth_tp_connection import (
    EthTpConnection,
)


class EthTpConfig(TpConfig):
    """AUTOSAR EthTpConfig."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    tp_connections: list[EthTpConnection]
    def __init__(self) -> None:
        """Initialize EthTpConfig."""
        super().__init__()
        self.tp_connections: list[EthTpConnection] = []


class EthTpConfigBuilder:
    """Builder for EthTpConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EthTpConfig = EthTpConfig()

    def build(self) -> EthTpConfig:
        """Build and return EthTpConfig object.

        Returns:
            EthTpConfig instance
        """
        # TODO: Add validation
        return self._obj
