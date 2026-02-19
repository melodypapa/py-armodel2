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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SomeipTpConfig":
        """Deserialize XML element to SomeipTpConfig object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SomeipTpConfig object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse tp_channels (list)
        obj.tp_channels = []
        for child in ARObject._find_all_child_elements(element, "TP-CHANNELS"):
            tp_channels_value = ARObject._deserialize_by_tag(child, "SomeipTpChannel")
            obj.tp_channels.append(tp_channels_value)

        # Parse tp_connections (list)
        obj.tp_connections = []
        for child in ARObject._find_all_child_elements(element, "TP-CONNECTIONS"):
            tp_connections_value = ARObject._deserialize_by_tag(child, "SomeipTpConnection")
            obj.tp_connections.append(tp_connections_value)

        return obj



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
