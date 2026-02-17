"""TimingConditionFormula AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 35)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingCondition.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.autosar_operation_argument_instance import (
    AutosarOperationArgumentInstance,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition.timing_condition import (
    TimingCondition,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description_event import (
    TimingDescriptionEvent,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition.timing_mode_instance import (
    TimingModeInstance,
)


class TimingConditionFormula(ARObject):
    """AUTOSAR TimingConditionFormula."""

    def __init__(self) -> None:
        """Initialize TimingConditionFormula."""
        super().__init__()
        self.timing_argument_argument_instance: Optional[AutosarOperationArgumentInstance] = None
        self.timing_condition: Optional[TimingCondition] = None
        self.timing_event: Optional[TimingDescriptionEvent] = None
        self.timing_mode: Optional[TimingModeInstance] = None
        self.timing_variable_instance: Optional[Any] = None


class TimingConditionFormulaBuilder:
    """Builder for TimingConditionFormula."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TimingConditionFormula = TimingConditionFormula()

    def build(self) -> TimingConditionFormula:
        """Build and return TimingConditionFormula object.

        Returns:
            TimingConditionFormula instance
        """
        # TODO: Add validation
        return self._obj
