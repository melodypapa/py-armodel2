"""ModeDrivenTransmissionModeCondition AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 393)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication_Timing.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)


class ModeDrivenTransmissionModeCondition(ARObject):
    """AUTOSAR ModeDrivenTransmissionModeCondition."""

    def __init__(self) -> None:
        """Initialize ModeDrivenTransmissionModeCondition."""
        super().__init__()
        self.modes: list[ModeDeclaration] = []


class ModeDrivenTransmissionModeConditionBuilder:
    """Builder for ModeDrivenTransmissionModeCondition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeDrivenTransmissionModeCondition = ModeDrivenTransmissionModeCondition()

    def build(self) -> ModeDrivenTransmissionModeCondition:
        """Build and return ModeDrivenTransmissionModeCondition object.

        Returns:
            ModeDrivenTransmissionModeCondition instance
        """
        # TODO: Add validation
        return self._obj
