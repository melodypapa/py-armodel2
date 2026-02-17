"""SporadicEventTriggering AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 105)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingConstraint_EventTriggeringConstraint.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.EventTriggeringConstraint.event_triggering_constraint import (
    EventTriggeringConstraint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)


class SporadicEventTriggering(EventTriggeringConstraint):
    """AUTOSAR SporadicEventTriggering."""

    jitter: Optional[MultidimensionalTime]
    maximum_inter: Optional[MultidimensionalTime]
    minimum_inter: Optional[MultidimensionalTime]
    period: Optional[MultidimensionalTime]
    def __init__(self) -> None:
        """Initialize SporadicEventTriggering."""
        super().__init__()
        self.jitter: Optional[MultidimensionalTime] = None
        self.maximum_inter: Optional[MultidimensionalTime] = None
        self.minimum_inter: Optional[MultidimensionalTime] = None
        self.period: Optional[MultidimensionalTime] = None


class SporadicEventTriggeringBuilder:
    """Builder for SporadicEventTriggering."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SporadicEventTriggering = SporadicEventTriggering()

    def build(self) -> SporadicEventTriggering:
        """Build and return SporadicEventTriggering object.

        Returns:
            SporadicEventTriggering instance
        """
        # TODO: Add validation
        return self._obj
