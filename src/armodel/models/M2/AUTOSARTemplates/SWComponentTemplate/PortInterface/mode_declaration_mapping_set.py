"""ModeDeclarationMappingSet AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)


class ModeDeclarationMappingSet(ARElement):
    """AUTOSAR ModeDeclarationMappingSet."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("modes", None, False, True, ModeDeclaration),  # modes
    ]

    def __init__(self) -> None:
        """Initialize ModeDeclarationMappingSet."""
        super().__init__()
        self.modes: list[ModeDeclaration] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ModeDeclarationMappingSet to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ModeDeclarationMappingSet":
        """Create ModeDeclarationMappingSet from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ModeDeclarationMappingSet instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ModeDeclarationMappingSet since parent returns ARObject
        return cast("ModeDeclarationMappingSet", obj)


class ModeDeclarationMappingSetBuilder:
    """Builder for ModeDeclarationMappingSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeDeclarationMappingSet = ModeDeclarationMappingSet()

    def build(self) -> ModeDeclarationMappingSet:
        """Build and return ModeDeclarationMappingSet object.

        Returns:
            ModeDeclarationMappingSet instance
        """
        # TODO: Add validation
        return self._obj
