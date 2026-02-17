"""TDEventOccurrenceExpressionFormula AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 84)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.autosar_operation_argument_instance import (
    AutosarOperationArgumentInstance,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description_event import (
    TimingDescriptionEvent,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition.timing_mode_instance import (
    TimingModeInstance,
)


class TDEventOccurrenceExpressionFormula(ARObject):
    """AUTOSAR TDEventOccurrenceExpressionFormula."""

    def __init__(self) -> None:
        """Initialize TDEventOccurrenceExpressionFormula."""
        super().__init__()
        self.argument: Optional[AutosarOperationArgumentInstance] = None
        self.event: Optional[TimingDescriptionEvent] = None
        self.mode: Optional[TimingModeInstance] = None
        self.variable: Optional[Any] = None


class TDEventOccurrenceExpressionFormulaBuilder:
    """Builder for TDEventOccurrenceExpressionFormula."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventOccurrenceExpressionFormula = TDEventOccurrenceExpressionFormula()

    def build(self) -> TDEventOccurrenceExpressionFormula:
        """Build and return TDEventOccurrenceExpressionFormula object.

        Returns:
            TDEventOccurrenceExpressionFormula instance
        """
        # TODO: Add validation
        return self._obj
