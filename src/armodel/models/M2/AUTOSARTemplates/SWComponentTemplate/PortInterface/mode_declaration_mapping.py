"""ModeDeclarationMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)


class ModeDeclarationMapping(Identifiable):
    """AUTOSAR ModeDeclarationMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("first_modes", None, False, True, ModeDeclaration),  # firstModes
        ("second_mode", None, False, False, ModeDeclaration),  # secondMode
    ]

    def __init__(self) -> None:
        """Initialize ModeDeclarationMapping."""
        super().__init__()
        self.first_modes: list[ModeDeclaration] = []
        self.second_mode: Optional[ModeDeclaration] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ModeDeclarationMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ModeDeclarationMapping":
        """Create ModeDeclarationMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ModeDeclarationMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ModeDeclarationMapping since parent returns ARObject
        return cast("ModeDeclarationMapping", obj)


class ModeDeclarationMappingBuilder:
    """Builder for ModeDeclarationMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeDeclarationMapping = ModeDeclarationMapping()

    def build(self) -> ModeDeclarationMapping:
        """Build and return ModeDeclarationMapping object.

        Returns:
            ModeDeclarationMapping instance
        """
        # TODO: Add validation
        return self._obj
