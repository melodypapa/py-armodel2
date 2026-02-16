"""ModeDeclarationGroupPrototypeMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class ModeDeclarationGroupPrototypeMapping(ARObject):
    """AUTOSAR ModeDeclarationGroupPrototypeMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("first_mode_group_prototype", None, False, False, ModeDeclarationGroup),  # firstModeGroupPrototype
        ("mode", None, False, False, ModeDeclaration),  # mode
        ("second_mode", None, False, False, ModeDeclarationGroup),  # secondMode
    ]

    def __init__(self) -> None:
        """Initialize ModeDeclarationGroupPrototypeMapping."""
        super().__init__()
        self.first_mode_group_prototype: Optional[ModeDeclarationGroup] = None
        self.mode: Optional[ModeDeclaration] = None
        self.second_mode: Optional[ModeDeclarationGroup] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ModeDeclarationGroupPrototypeMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ModeDeclarationGroupPrototypeMapping":
        """Create ModeDeclarationGroupPrototypeMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ModeDeclarationGroupPrototypeMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ModeDeclarationGroupPrototypeMapping since parent returns ARObject
        return cast("ModeDeclarationGroupPrototypeMapping", obj)


class ModeDeclarationGroupPrototypeMappingBuilder:
    """Builder for ModeDeclarationGroupPrototypeMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeDeclarationGroupPrototypeMapping = ModeDeclarationGroupPrototypeMapping()

    def build(self) -> ModeDeclarationGroupPrototypeMapping:
        """Build and return ModeDeclarationGroupPrototypeMapping object.

        Returns:
            ModeDeclarationGroupPrototypeMapping instance
        """
        # TODO: Add validation
        return self._obj
