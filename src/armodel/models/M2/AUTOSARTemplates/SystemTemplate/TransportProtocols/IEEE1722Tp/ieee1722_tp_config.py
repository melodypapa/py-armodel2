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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "IEEE1722TpConfig":
        """Deserialize XML element to IEEE1722TpConfig object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IEEE1722TpConfig object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse tp_connections (list)
        obj.tp_connections = []
        for child in ARObject._find_all_child_elements(element, "TP-CONNECTIONS"):
            tp_connections_value = ARObject._deserialize_by_tag(child, "IEEE1722TpConnection")
            obj.tp_connections.append(tp_connections_value)

        return obj



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
