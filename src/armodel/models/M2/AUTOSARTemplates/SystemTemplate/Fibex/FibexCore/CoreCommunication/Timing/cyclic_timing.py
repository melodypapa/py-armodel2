"""CyclicTiming AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 396)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication_Timing.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.describable import (
    Describable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.Timing.time_range_type import (
    TimeRangeType,
)


class CyclicTiming(Describable):
    """AUTOSAR CyclicTiming."""

    time_offset: Optional[TimeRangeType]
    time_period: Optional[TimeRangeType]
    def __init__(self) -> None:
        """Initialize CyclicTiming."""
        super().__init__()
        self.time_offset: Optional[TimeRangeType] = None
        self.time_period: Optional[TimeRangeType] = None


class CyclicTimingBuilder:
    """Builder for CyclicTiming."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CyclicTiming = CyclicTiming()

    def build(self) -> CyclicTiming:
        """Build and return CyclicTiming object.

        Returns:
            CyclicTiming instance
        """
        # TODO: Add validation
        return self._obj
