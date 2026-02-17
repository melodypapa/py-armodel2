"""ArbitraryEventTriggering AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 111)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingConstraint_EventTriggeringConstraint.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.EventTriggeringConstraint.event_triggering_constraint import (
    EventTriggeringConstraint,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.EventTriggeringConstraint.confidence_interval import (
    ConfidenceInterval,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)


class ArbitraryEventTriggering(EventTriggeringConstraint):
    """AUTOSAR ArbitraryEventTriggering."""

    confidence_intervals: list[ConfidenceInterval]
    maximums: list[MultidimensionalTime]
    minimums: list[MultidimensionalTime]
    def __init__(self) -> None:
        """Initialize ArbitraryEventTriggering."""
        super().__init__()
        self.confidence_intervals: list[ConfidenceInterval] = []
        self.maximums: list[MultidimensionalTime] = []
        self.minimums: list[MultidimensionalTime] = []


class ArbitraryEventTriggeringBuilder:
    """Builder for ArbitraryEventTriggering."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ArbitraryEventTriggering = ArbitraryEventTriggering()

    def build(self) -> ArbitraryEventTriggering:
        """Build and return ArbitraryEventTriggering object.

        Returns:
            ArbitraryEventTriggering instance
        """
        # TODO: Add validation
        return self._obj
