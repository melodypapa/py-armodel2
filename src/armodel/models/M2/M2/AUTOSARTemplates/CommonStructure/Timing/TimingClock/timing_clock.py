"""TimingClock AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 252)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingClock.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.global_time_domain import (
    GlobalTimeDomain,
)


class TimingClock(Identifiable):
    """AUTOSAR TimingClock."""
    """Abstract base class - do not instantiate directly."""

    def __init__(self) -> None:
        """Initialize TimingClock."""
        super().__init__()
        self.platform_time: Optional[GlobalTimeDomain] = None


class TimingClockBuilder:
    """Builder for TimingClock."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TimingClock = TimingClock()

    def build(self) -> TimingClock:
        """Build and return TimingClock object.

        Returns:
            TimingClock instance
        """
        # TODO: Add validation
        return self._obj
