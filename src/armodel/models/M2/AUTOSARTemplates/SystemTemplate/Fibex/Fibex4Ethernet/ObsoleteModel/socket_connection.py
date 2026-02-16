"""SocketConnection AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.describable import (
    Describable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Identifier,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.socket_address import (
    SocketAddress,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.socket_connection_ipdu_identifier_set import (
    SocketConnectionIpduIdentifierSet,
)


class SocketConnection(Describable):
    """AUTOSAR SocketConnection."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("client_ip_addr", None, True, False, None),  # clientIpAddr
        ("client_port", None, False, False, SocketAddress),  # clientPort
        ("client_port_from", None, True, False, None),  # clientPortFrom
        ("pdus", None, False, True, SocketConnectionIpduIdentifierSet),  # pdus
        ("pdu_collection", None, True, False, None),  # pduCollection
        ("runtime_ip", None, False, False, any (RuntimeAddress)),  # runtimeIp
        ("runtime_port", None, False, False, any (RuntimeAddress)),  # runtimePort
        ("short_label", None, True, False, None),  # shortLabel
    ]

    def __init__(self) -> None:
        """Initialize SocketConnection."""
        super().__init__()
        self.client_ip_addr: Optional[Boolean] = None
        self.client_port: Optional[SocketAddress] = None
        self.client_port_from: Optional[Boolean] = None
        self.pdus: list[SocketConnectionIpduIdentifierSet] = []
        self.pdu_collection: Optional[TimeValue] = None
        self.runtime_ip: Optional[Any] = None
        self.runtime_port: Optional[Any] = None
        self.short_label: Optional[Identifier] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SocketConnection to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SocketConnection":
        """Create SocketConnection from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SocketConnection instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SocketConnection since parent returns ARObject
        return cast("SocketConnection", obj)


class SocketConnectionBuilder:
    """Builder for SocketConnection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SocketConnection = SocketConnection()

    def build(self) -> SocketConnection:
        """Build and return SocketConnection object.

        Returns:
            SocketConnection instance
        """
        # TODO: Add validation
        return self._obj
