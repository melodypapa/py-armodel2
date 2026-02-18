"""ModeTransition AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 43)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 630)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ModeDeclaration.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)


class ModeTransition(Identifiable):
    """AUTOSAR ModeTransition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    entered_mode: Optional[ModeDeclaration]
    exited_mode: Optional[ModeDeclaration]
    def __init__(self) -> None:
        """Initialize ModeTransition."""
        super().__init__()
        self.entered_mode: Optional[ModeDeclaration] = None
        self.exited_mode: Optional[ModeDeclaration] = None


class ModeTransitionBuilder:
    """Builder for ModeTransition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeTransition = ModeTransition()

    def build(self) -> ModeTransition:
        """Build and return ModeTransition object.

        Returns:
            ModeTransition instance
        """
        # TODO: Add validation
        return self._obj
