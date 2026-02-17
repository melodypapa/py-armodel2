"""ModeDeclarationGroupPrototypeMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 130)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ModeDeclaration.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class ModeDeclarationGroupPrototypeMapping(ARObject):
    """AUTOSAR ModeDeclarationGroupPrototypeMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "first_mode_group_prototype": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ModeDeclarationGroup,
        ),  # firstModeGroupPrototype
        "mode": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ModeDeclaration,
        ),  # mode
        "second_mode": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ModeDeclarationGroup,
        ),  # secondMode
    }

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
