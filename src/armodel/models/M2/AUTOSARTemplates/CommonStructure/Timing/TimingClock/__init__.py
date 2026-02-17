"""TimingClock module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingClock.tdlet_zone_clock import (
        TDLETZoneClock,
    )
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingClock.timing_clock import (
        TimingClock,
    )
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingClock.timing_clock_sync_accuracy import (
        TimingClockSyncAccuracy,
    )

__all__ = [
    "TDLETZoneClock",
    "TimingClock",
    "TimingClockSyncAccuracy",
]
