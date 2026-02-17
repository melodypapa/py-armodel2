"""TDLETZoneClock AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 252)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingClock.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingClock.timing_clock import (
    TimingClock,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)


class TDLETZoneClock(TimingClock):
    """AUTOSAR TDLETZoneClock."""

    accuracy_ext: Optional[MultidimensionalTime]
    accuracy_int: Optional[MultidimensionalTime]
    def __init__(self) -> None:
        """Initialize TDLETZoneClock."""
        super().__init__()
        self.accuracy_ext: Optional[MultidimensionalTime] = None
        self.accuracy_int: Optional[MultidimensionalTime] = None


class TDLETZoneClockBuilder:
    """Builder for TDLETZoneClock."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDLETZoneClock = TDLETZoneClock()

    def build(self) -> TDLETZoneClock:
        """Build and return TDLETZoneClock object.

        Returns:
            TDLETZoneClock instance
        """
        # TODO: Add validation
        return self._obj
