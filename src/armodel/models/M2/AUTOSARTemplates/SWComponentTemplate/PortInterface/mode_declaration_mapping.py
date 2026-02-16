"""ModeDeclarationMapping AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)


class ModeDeclarationMapping(Identifiable):
    """AUTOSAR ModeDeclarationMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "first_modes": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=ModeDeclaration,
        ),  # firstModes
        "second_mode": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ModeDeclaration,
        ),  # secondMode
    }

    def __init__(self) -> None:
        """Initialize ModeDeclarationMapping."""
        super().__init__()
        self.first_modes: list[ModeDeclaration] = []
        self.second_mode: Optional[ModeDeclaration] = None


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
