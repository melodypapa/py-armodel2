"""TpConnection AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection.tp_connection_ident import (
    TpConnectionIdent,
)


class TpConnection(ARObject):
    """AUTOSAR TpConnection."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("ident", None, False, False, TpConnectionIdent),  # ident
    ]

    def __init__(self) -> None:
        """Initialize TpConnection."""
        super().__init__()
        self.ident: Optional[TpConnectionIdent] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TpConnection to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TpConnection":
        """Create TpConnection from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TpConnection instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TpConnection since parent returns ARObject
        return cast("TpConnection", obj)


class TpConnectionBuilder:
    """Builder for TpConnection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TpConnection = TpConnection()

    def build(self) -> TpConnection:
        """Build and return TpConnection object.

        Returns:
            TpConnection instance
        """
        # TODO: Add validation
        return self._obj
