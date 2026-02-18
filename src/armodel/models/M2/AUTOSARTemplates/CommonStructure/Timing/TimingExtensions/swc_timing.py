"""SwcTiming AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 25)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingExtensions.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions.timing_extension import (
    TimingExtension,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.swc_internal_behavior import (
    SwcInternalBehavior,
)


class SwcTiming(TimingExtension):
    """AUTOSAR SwcTiming."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    behavior: Optional[SwcInternalBehavior]
    def __init__(self) -> None:
        """Initialize SwcTiming."""
        super().__init__()
        self.behavior: Optional[SwcInternalBehavior] = None


class SwcTimingBuilder:
    """Builder for SwcTiming."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwcTiming = SwcTiming()

    def build(self) -> SwcTiming:
        """Build and return SwcTiming object.

        Returns:
            SwcTiming instance
        """
        # TODO: Add validation
        return self._obj
