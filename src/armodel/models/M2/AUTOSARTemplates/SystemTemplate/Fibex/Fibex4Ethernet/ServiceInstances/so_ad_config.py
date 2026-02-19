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

        # Parse connections (list)
        obj.connections = []
        for child in ARObject._find_all_child_elements(element, "CONNECTIONS"):
            connections_value = ARObject._deserialize_by_tag(child, "SocketConnection")
            obj.connections.append(connections_value)

        # Parse socket_addresses (list)
        obj.socket_addresses = []
        for child in ARObject._find_all_child_elements(element, "SOCKET-ADDRESSES"):
            socket_addresses_value = ARObject._deserialize_by_tag(child, "SocketAddress")
            obj.socket_addresses.append(socket_addresses_value)

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
