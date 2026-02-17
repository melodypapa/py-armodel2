"""TransmissionModeDeclaration AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 392)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication_Timing.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.Timing.mode_driven_transmission_mode_condition import (
    ModeDrivenTransmissionModeCondition,
)


class TransmissionModeDeclaration(ARObject):
    """AUTOSAR TransmissionModeDeclaration."""

    mode_drivens: list[ModeDrivenTransmissionModeCondition]
    transmission: Optional[Any]
    def __init__(self) -> None:
        """Initialize TransmissionModeDeclaration."""
        super().__init__()
        self.mode_drivens: list[ModeDrivenTransmissionModeCondition] = []
        self.transmission: Optional[Any] = None


class TransmissionModeDeclarationBuilder:
    """Builder for TransmissionModeDeclaration."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TransmissionModeDeclaration = TransmissionModeDeclaration()

    def build(self) -> TransmissionModeDeclaration:
        """Build and return TransmissionModeDeclaration object.

        Returns:
            TransmissionModeDeclaration instance
        """
        # TODO: Add validation
        return self._obj
