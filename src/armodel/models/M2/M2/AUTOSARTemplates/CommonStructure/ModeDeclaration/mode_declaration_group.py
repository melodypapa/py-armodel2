"""ModeDeclarationGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 42)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 322)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 628)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2038)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 197)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ModeDeclaration.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_error_behavior import (
    ModeErrorBehavior,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_transition import (
    ModeTransition,
)


class ModeDeclarationGroup(ARElement):
    """AUTOSAR ModeDeclarationGroup."""

    def __init__(self) -> None:
        """Initialize ModeDeclarationGroup."""
        super().__init__()
        self.initial_mode: Optional[ModeDeclaration] = None
        self.modes: list[ModeDeclaration] = []
        self.mode_manager: Optional[ModeErrorBehavior] = None
        self.mode_transition_mode_declaration_groups: list[ModeTransition] = []
        self.mode_user_error: Optional[ModeErrorBehavior] = None
        self.on_transition: Optional[PositiveInteger] = None


class ModeDeclarationGroupBuilder:
    """Builder for ModeDeclarationGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeDeclarationGroup = ModeDeclarationGroup()

    def build(self) -> ModeDeclarationGroup:
        """Build and return ModeDeclarationGroup object.

        Returns:
            ModeDeclarationGroup instance
        """
        # TODO: Add validation
        return self._obj
