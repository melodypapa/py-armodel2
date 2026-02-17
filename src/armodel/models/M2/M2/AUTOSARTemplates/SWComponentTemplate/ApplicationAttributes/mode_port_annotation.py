"""ModePortAnnotation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 159)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_ApplicationAttributes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.GeneralAnnotation.general_annotation import (
    GeneralAnnotation,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class ModePortAnnotation(GeneralAnnotation):
    """AUTOSAR ModePortAnnotation."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "mode_group": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ModeDeclarationGroup,
        ),  # modeGroup
    }

    def __init__(self) -> None:
        """Initialize ModePortAnnotation."""
        super().__init__()
        self.mode_group: Optional[ModeDeclarationGroup] = None


class ModePortAnnotationBuilder:
    """Builder for ModePortAnnotation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModePortAnnotation = ModePortAnnotation()

    def build(self) -> ModePortAnnotation:
        """Build and return ModePortAnnotation object.

        Returns:
            ModePortAnnotation instance
        """
        # TODO: Add validation
        return self._obj
