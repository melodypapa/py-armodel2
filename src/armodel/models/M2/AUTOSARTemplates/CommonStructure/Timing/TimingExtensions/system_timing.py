"""SystemTiming AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 26)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingExtensions.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions.timing_extension import (
    TimingExtension,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.system import (
    System,
)


class SystemTiming(TimingExtension):
    """AUTOSAR SystemTiming."""

    def __init__(self) -> None:
        """Initialize SystemTiming."""
        super().__init__()
        self.system: Optional[System] = None


class SystemTimingBuilder:
    """Builder for SystemTiming."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SystemTiming = SystemTiming()

    def build(self) -> SystemTiming:
        """Build and return SystemTiming object.

        Returns:
            SystemTiming instance
        """
        # TODO: Add validation
        return self._obj
