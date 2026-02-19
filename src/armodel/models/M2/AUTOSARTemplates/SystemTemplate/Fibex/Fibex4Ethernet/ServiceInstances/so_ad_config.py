"""SoAdConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 451)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ServiceInstances.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.socket_address import (
    SocketAddress,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ObsoleteModel.socket_connection import (
    SocketConnection,
)


class SoAdConfig(ARObject):
    """AUTOSAR SoAdConfig."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    connections: list[SocketConnection]
    socket_addresses: list[SocketAddress]
    def __init__(self) -> None:
        """Initialize SoAdConfig."""
        super().__init__()
        self.connections: list[SocketConnection] = []
        self.socket_addresses: list[SocketAddress] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SoAdConfig":
        """Deserialize XML element to SoAdConfig object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SoAdConfig object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse connections (list from container "CONNECTIONS")
        obj.connections = []
        container = ARObject._find_child_element(element, "CONNECTIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.connections.append(child_value)

        # Parse socket_addresses (list from container "SOCKET-ADDRESSES")
        obj.socket_addresses = []
        container = ARObject._find_child_element(element, "SOCKET-ADDRESSES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.socket_addresses.append(child_value)

        return obj



class SoAdConfigBuilder:
    """Builder for SoAdConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SoAdConfig = SoAdConfig()

    def build(self) -> SoAdConfig:
        """Build and return SoAdConfig object.

        Returns:
            SoAdConfig instance
        """
        # TODO: Add validation
        return self._obj
