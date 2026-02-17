"""TimingCondition AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 35)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingCondition.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)


class TimingCondition(Identifiable):
    """AUTOSAR TimingCondition."""

    timing_condition: Optional[TimingCondition]
    def __init__(self) -> None:
        """Initialize TimingCondition."""
        super().__init__()
        self.timing_condition: Optional[TimingCondition] = None


class TimingConditionBuilder:
    """Builder for TimingCondition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TimingCondition = TimingCondition()

    def build(self) -> TimingCondition:
        """Build and return TimingCondition object.

        Returns:
            TimingCondition instance
        """
        # TODO: Add validation
        return self._obj
