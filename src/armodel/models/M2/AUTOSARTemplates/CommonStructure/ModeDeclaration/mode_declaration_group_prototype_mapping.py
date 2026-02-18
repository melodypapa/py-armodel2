"""ModeDeclarationGroupPrototypeMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 130)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ModeDeclaration.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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

    first_mode_group_prototype: Optional[ModeDeclarationGroup]
    mode: Optional[ModeDeclaration]
    second_mode: Optional[ModeDeclarationGroup]
    def __init__(self) -> None:
        """Initialize ModeDeclarationGroupPrototypeMapping."""
        super().__init__()
        self.first_mode_group_prototype: Optional[ModeDeclarationGroup] = None
        self.mode: Optional[ModeDeclaration] = None
        self.second_mode: Optional[ModeDeclarationGroup] = None


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
