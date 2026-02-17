"""ModeDeclaration AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 43)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 322)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 628)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2038)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 233)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ModeDeclaration.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class ModeDeclaration(Identifiable):
    """AUTOSAR ModeDeclaration."""

    def __init__(self) -> None:
        """Initialize ModeDeclaration."""
        super().__init__()
        self.value: Optional[PositiveInteger] = None


class ModeDeclarationBuilder:
    """Builder for ModeDeclaration."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeDeclaration = ModeDeclaration()

    def build(self) -> ModeDeclaration:
        """Build and return ModeDeclaration object.

        Returns:
            ModeDeclaration instance
        """
        # TODO: Add validation
        return self._obj
