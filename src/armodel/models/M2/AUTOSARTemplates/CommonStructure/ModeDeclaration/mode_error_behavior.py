"""ModeErrorBehavior AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 44)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 637)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ModeDeclaration.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration import (
    ModeErrorReactionPolicyEnum,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)


class ModeErrorBehavior(ARObject):
    """AUTOSAR ModeErrorBehavior."""

    def __init__(self) -> None:
        """Initialize ModeErrorBehavior."""
        super().__init__()
        self.default_mode: Optional[ModeDeclaration] = None
        self.error_reaction: Optional[ModeErrorReactionPolicyEnum] = None


class ModeErrorBehaviorBuilder:
    """Builder for ModeErrorBehavior."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeErrorBehavior = ModeErrorBehavior()

    def build(self) -> ModeErrorBehavior:
        """Build and return ModeErrorBehavior object.

        Returns:
            ModeErrorBehavior instance
        """
        # TODO: Add validation
        return self._obj
