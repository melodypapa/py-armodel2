"""ModeInBswInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 38)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingCondition.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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

    context_bsw: Optional[BswImplementation]
    context_mode: Optional[ModeDeclarationGroup]
    target_mode: Optional[ModeDeclaration]
    def __init__(self) -> None:
        """Initialize ModeInBswInstanceRef."""
        super().__init__()
        self.context_bsw: Optional[BswImplementation] = None
        self.context_mode: Optional[ModeDeclarationGroup] = None
        self.target_mode: Optional[ModeDeclaration] = None


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
