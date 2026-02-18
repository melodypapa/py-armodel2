"""PeriodicEventTriggering AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 101)

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


class PeriodicEventTriggering(EventTriggeringConstraint):
    """AUTOSAR PeriodicEventTriggering."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    jitter: Optional[MultidimensionalTime]
    minimum_inter: Optional[MultidimensionalTime]
    period: Optional[MultidimensionalTime]
    def __init__(self) -> None:
        """Initialize PeriodicEventTriggering."""
        super().__init__()
        self.jitter: Optional[MultidimensionalTime] = None
        self.minimum_inter: Optional[MultidimensionalTime] = None
        self.period: Optional[MultidimensionalTime] = None


class PeriodicEventTriggeringBuilder:
    """Builder for PeriodicEventTriggering."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PeriodicEventTriggering = PeriodicEventTriggering()

    def build(self) -> PeriodicEventTriggering:
        """Build and return PeriodicEventTriggering object.

        Returns:
            PeriodicEventTriggering instance
        """
        # TODO: Add validation
        return self._obj
