"""StaticSocketConnection AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.so_con_i_pdu_identifier import (
    SoConIPduIdentifier,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.socket_address import (
    SocketAddress,
)


class StaticSocketConnection(Identifiable):
    """AUTOSAR StaticSocketConnection."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("i_pdu_identifiers", None, False, True, SoConIPduIdentifier),  # iPduIdentifiers
        ("remote_address", None, False, False, SocketAddress),  # remoteAddress
        ("tcp_connect", None, True, False, None),  # tcpConnect
        ("tcp_role", None, False, False, TcpRoleEnum),  # tcpRole
    ]

    def __init__(self) -> None:
        """Initialize StaticSocketConnection."""
        super().__init__()
        self.i_pdu_identifiers: list[SoConIPduIdentifier] = []
        self.remote_address: Optional[SocketAddress] = None
        self.tcp_connect: Optional[TimeValue] = None
        self.tcp_role: Optional[TcpRoleEnum] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert StaticSocketConnection to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "StaticSocketConnection":
        """Create StaticSocketConnection from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            StaticSocketConnection instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to StaticSocketConnection since parent returns ARObject
        return cast("StaticSocketConnection", obj)


class StaticSocketConnectionBuilder:
    """Builder for StaticSocketConnection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: StaticSocketConnection = StaticSocketConnection()

    def build(self) -> StaticSocketConnection:
        """Build and return StaticSocketConnection object.

        Returns:
            StaticSocketConnection instance
        """
        # TODO: Add validation
        return self._obj
