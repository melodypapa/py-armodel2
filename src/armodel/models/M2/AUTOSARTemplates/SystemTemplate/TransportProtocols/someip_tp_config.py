"""SomeipTpConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 619)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_config import (
    TpConfig,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.someip_tp_channel import (
    SomeipTpChannel,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.someip_tp_connection import (
    SomeipTpConnection,
)


class SomeipTpConfig(TpConfig):
    """AUTOSAR SomeipTpConfig."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    tp_channels: list[SomeipTpChannel]
    tp_connections: list[SomeipTpConnection]
    def __init__(self) -> None:
        """Initialize SomeipTpConfig."""
        super().__init__()
        self.tp_channels: list[SomeipTpChannel] = []
        self.tp_connections: list[SomeipTpConnection] = []


class SomeipTpConfigBuilder:
    """Builder for SomeipTpConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SomeipTpConfig = SomeipTpConfig()

    def build(self) -> SomeipTpConfig:
        """Build and return SomeipTpConfig object.

        Returns:
            SomeipTpConfig instance
        """
        # TODO: Add validation
        return self._obj
