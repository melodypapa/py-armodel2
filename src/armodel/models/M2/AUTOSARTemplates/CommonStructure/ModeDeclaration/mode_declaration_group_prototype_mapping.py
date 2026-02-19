"""ModeDeclarationGroupPrototypeMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 130)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ModeDeclaration.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class ModeDeclarationGroupPrototypeMapping(ARObject):
    """AUTOSAR ModeDeclarationGroupPrototypeMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    first_mode_group_prototype_ref: Optional[ARRef]
    mode: Optional[ModeDeclaration]
    second_mode_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize ModeDeclarationGroupPrototypeMapping."""
        super().__init__()
        self.first_mode_group_prototype_ref: Optional[ARRef] = None
        self.mode: Optional[ModeDeclaration] = None
        self.second_mode_ref: Optional[ARRef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ModeDeclarationGroupPrototypeMapping":
        """Deserialize XML element to ModeDeclarationGroupPrototypeMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ModeDeclarationGroupPrototypeMapping object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse first_mode_group_prototype_ref
        child = ARObject._find_child_element(element, "FIRST-MODE-GROUP-PROTOTYPE")
        if child is not None:
            first_mode_group_prototype_ref_value = ARObject._deserialize_by_tag(child, "ModeDeclarationGroup")
            obj.first_mode_group_prototype_ref = first_mode_group_prototype_ref_value

        # Parse mode
        child = ARObject._find_child_element(element, "MODE")
        if child is not None:
            mode_value = ARObject._deserialize_by_tag(child, "ModeDeclaration")
            obj.mode = mode_value

        # Parse second_mode_ref
        child = ARObject._find_child_element(element, "SECOND-MODE")
        if child is not None:
            second_mode_ref_value = ARObject._deserialize_by_tag(child, "ModeDeclarationGroup")
            obj.second_mode_ref = second_mode_ref_value

        return obj



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
