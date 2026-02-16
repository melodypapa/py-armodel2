"""ModeAccessPointIdent AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario.ident_caption import (
    IdentCaption,
)


class ModeAccessPointIdent(IdentCaption):
    """AUTOSAR ModeAccessPointIdent."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize ModeAccessPointIdent."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ModeAccessPointIdent to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ModeAccessPointIdent":
        """Create ModeAccessPointIdent from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ModeAccessPointIdent instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ModeAccessPointIdent since parent returns ARObject
        return cast("ModeAccessPointIdent", obj)


class ModeAccessPointIdentBuilder:
    """Builder for ModeAccessPointIdent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeAccessPointIdent = ModeAccessPointIdent()

    def build(self) -> ModeAccessPointIdent:
        """Build and return ModeAccessPointIdent object.

        Returns:
            ModeAccessPointIdent instance
        """
        # TODO: Add validation
        return self._obj
