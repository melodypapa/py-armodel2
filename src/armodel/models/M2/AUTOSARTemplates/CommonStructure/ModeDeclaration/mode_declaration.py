"""ModeDeclaration AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class ModeDeclaration(Identifiable):
    """AUTOSAR ModeDeclaration."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("value", None, True, False, None),  # value
    ]

    def __init__(self) -> None:
        """Initialize ModeDeclaration."""
        super().__init__()
        self.value: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ModeDeclaration to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ModeDeclaration":
        """Create ModeDeclaration from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ModeDeclaration instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ModeDeclaration since parent returns ARObject
        return cast("ModeDeclaration", obj)


class ModeDeclarationBuilder:
    """Builder for ModeDeclaration."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeDeclaration = ModeDeclaration()

    def build(self) -> ModeDeclaration:
        """Build and return ModeDeclaration object.

        Returns:
            ModeDeclaration instance
        """
        # TODO: Add validation
        return self._obj
