"""SomeipTpConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 619)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "tp_channels": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=SomeipTpChannel,
        ),  # tpChannels
        "tp_connections": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=SomeipTpConnection,
        ),  # tpConnections
    }

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
