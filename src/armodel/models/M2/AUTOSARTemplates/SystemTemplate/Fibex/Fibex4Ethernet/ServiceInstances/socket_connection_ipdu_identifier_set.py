"""SocketConnectionIpduIdentifierSet AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.so_con_i_pdu_identifier import (
    SoConIPduIdentifier,
)


class SocketConnectionIpduIdentifierSet(FibexElement):
    """AUTOSAR SocketConnectionIpduIdentifierSet."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("i_pdu_identifiers", None, False, True, SoConIPduIdentifier),  # iPduIdentifiers
    ]

    def __init__(self) -> None:
        """Initialize SocketConnectionIpduIdentifierSet."""
        super().__init__()
        self.i_pdu_identifiers: list[SoConIPduIdentifier] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SocketConnectionIpduIdentifierSet to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SocketConnectionIpduIdentifierSet":
        """Create SocketConnectionIpduIdentifierSet from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SocketConnectionIpduIdentifierSet instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SocketConnectionIpduIdentifierSet since parent returns ARObject
        return cast("SocketConnectionIpduIdentifierSet", obj)


class SocketConnectionIpduIdentifierSetBuilder:
    """Builder for SocketConnectionIpduIdentifierSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SocketConnectionIpduIdentifierSet = SocketConnectionIpduIdentifierSet()

    def build(self) -> SocketConnectionIpduIdentifierSet:
        """Build and return SocketConnectionIpduIdentifierSet object.

        Returns:
            SocketConnectionIpduIdentifierSet instance
        """
        # TODO: Add validation
        return self._obj
