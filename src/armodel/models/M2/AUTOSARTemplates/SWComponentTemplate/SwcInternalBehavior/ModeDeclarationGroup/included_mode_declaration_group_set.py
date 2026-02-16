"""IncludedModeDeclarationGroupSet AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class IncludedModeDeclarationGroupSet(ARObject):
    """AUTOSAR IncludedModeDeclarationGroupSet."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("modes", None, False, True, ModeDeclarationGroup),  # modes
        ("prefix", None, True, False, None),  # prefix
    ]

    def __init__(self) -> None:
        """Initialize IncludedModeDeclarationGroupSet."""
        super().__init__()
        self.modes: list[ModeDeclarationGroup] = []
        self.prefix: Optional[Identifier] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert IncludedModeDeclarationGroupSet to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IncludedModeDeclarationGroupSet":
        """Create IncludedModeDeclarationGroupSet from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            IncludedModeDeclarationGroupSet instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to IncludedModeDeclarationGroupSet since parent returns ARObject
        return cast("IncludedModeDeclarationGroupSet", obj)


class IncludedModeDeclarationGroupSetBuilder:
    """Builder for IncludedModeDeclarationGroupSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IncludedModeDeclarationGroupSet = IncludedModeDeclarationGroupSet()

    def build(self) -> IncludedModeDeclarationGroupSet:
        """Build and return IncludedModeDeclarationGroupSet object.

        Returns:
            IncludedModeDeclarationGroupSet instance
        """
        # TODO: Add validation
        return self._obj
