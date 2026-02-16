"""ModeInBswModuleDescriptionInstanceRef AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswOverview.bsw_module_description import (
    BswModuleDescription,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class ModeInBswModuleDescriptionInstanceRef(ARObject):
    """AUTOSAR ModeInBswModuleDescriptionInstanceRef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("base", None, False, False, BswModuleDescription),  # base
        ("context_mode_group", None, False, False, ModeDeclarationGroup),  # contextModeGroup
        ("target_mode", None, False, False, ModeDeclaration),  # targetMode
    ]

    def __init__(self) -> None:
        """Initialize ModeInBswModuleDescriptionInstanceRef."""
        super().__init__()
        self.base: Optional[BswModuleDescription] = None
        self.context_mode_group: Optional[ModeDeclarationGroup] = None
        self.target_mode: Optional[ModeDeclaration] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ModeInBswModuleDescriptionInstanceRef to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ModeInBswModuleDescriptionInstanceRef":
        """Create ModeInBswModuleDescriptionInstanceRef from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ModeInBswModuleDescriptionInstanceRef instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ModeInBswModuleDescriptionInstanceRef since parent returns ARObject
        return cast("ModeInBswModuleDescriptionInstanceRef", obj)


class ModeInBswModuleDescriptionInstanceRefBuilder:
    """Builder for ModeInBswModuleDescriptionInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeInBswModuleDescriptionInstanceRef = ModeInBswModuleDescriptionInstanceRef()

    def build(self) -> ModeInBswModuleDescriptionInstanceRef:
        """Build and return ModeInBswModuleDescriptionInstanceRef object.

        Returns:
            ModeInBswModuleDescriptionInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
