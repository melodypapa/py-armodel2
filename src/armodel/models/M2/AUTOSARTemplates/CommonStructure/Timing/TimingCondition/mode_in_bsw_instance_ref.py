"""ModeInBswInstanceRef AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswImplementation.bsw_implementation import (
    BswImplementation,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class ModeInBswInstanceRef(ARObject):
    """AUTOSAR ModeInBswInstanceRef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("context_bsw", None, False, False, BswImplementation),  # contextBsw
        ("context_mode", None, False, False, ModeDeclarationGroup),  # contextMode
        ("target_mode", None, False, False, ModeDeclaration),  # targetMode
    ]

    def __init__(self) -> None:
        """Initialize ModeInBswInstanceRef."""
        super().__init__()
        self.context_bsw: Optional[BswImplementation] = None
        self.context_mode: Optional[ModeDeclarationGroup] = None
        self.target_mode: Optional[ModeDeclaration] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ModeInBswInstanceRef to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ModeInBswInstanceRef":
        """Create ModeInBswInstanceRef from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ModeInBswInstanceRef instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ModeInBswInstanceRef since parent returns ARObject
        return cast("ModeInBswInstanceRef", obj)


class ModeInBswInstanceRefBuilder:
    """Builder for ModeInBswInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeInBswInstanceRef = ModeInBswInstanceRef()

    def build(self) -> ModeInBswInstanceRef:
        """Build and return ModeInBswInstanceRef object.

        Returns:
            ModeInBswInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
