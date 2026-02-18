"""IEEE1722TpConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 636)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols_IEEE1722Tp.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_config import (
    TpConfig,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.ieee1722_tp_connection import (
    IEEE1722TpConnection,
)


class IEEE1722TpConfig(TpConfig):
    """AUTOSAR IEEE1722TpConfig."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    tp_connections: list[IEEE1722TpConnection]
    def __init__(self) -> None:
        """Initialize IEEE1722TpConfig."""
        super().__init__()
        self.tp_connections: list[IEEE1722TpConnection] = []


class IEEE1722TpConfigBuilder:
    """Builder for IEEE1722TpConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IEEE1722TpConfig = IEEE1722TpConfig()

    def build(self) -> IEEE1722TpConfig:
        """Build and return IEEE1722TpConfig object.

        Returns:
            IEEE1722TpConfig instance
        """
        # TODO: Add validation
        return self._obj
