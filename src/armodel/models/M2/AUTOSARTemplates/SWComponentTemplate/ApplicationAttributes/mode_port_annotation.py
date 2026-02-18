"""ModePortAnnotation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 159)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_ApplicationAttributes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.GeneralAnnotation.general_annotation import (
    GeneralAnnotation,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class ModePortAnnotation(GeneralAnnotation):
    """AUTOSAR ModePortAnnotation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    mode_group_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize ModePortAnnotation."""
        super().__init__()
        self.mode_group_ref: Optional[ARRef] = None


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
