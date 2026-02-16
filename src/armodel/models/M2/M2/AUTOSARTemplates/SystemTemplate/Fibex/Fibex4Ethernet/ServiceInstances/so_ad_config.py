"""SoAdConfig AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.socket_address import (
    SocketAddress,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ObsoleteModel.socket_connection import (
    SocketConnection,
)


class SoAdConfig(ARObject):
    """AUTOSAR SoAdConfig."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "connections": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=SocketConnection,
        ),  # connections
        "socket_addresses": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=SocketAddress,
        ),  # socketAddresses
    }

    def __init__(self) -> None:
        """Initialize SoAdConfig."""
        super().__init__()
        self.connections: list[SocketConnection] = []
        self.socket_addresses: list[SocketAddress] = []


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
