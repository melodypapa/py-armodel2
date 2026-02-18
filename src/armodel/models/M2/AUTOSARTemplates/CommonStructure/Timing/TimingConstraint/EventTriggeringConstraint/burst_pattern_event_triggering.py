"""BurstPatternEventTriggering AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 109)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingConstraint_EventTriggeringConstraint.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.EventTriggeringConstraint.event_triggering_constraint import (
    EventTriggeringConstraint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)


class BurstPatternEventTriggering(EventTriggeringConstraint):
    """AUTOSAR BurstPatternEventTriggering."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    max_number_of: Optional[PositiveInteger]
    minimum_inter: Optional[MultidimensionalTime]
    min_number_of: Optional[PositiveInteger]
    pattern_jitter: Optional[MultidimensionalTime]
    pattern_length: Optional[MultidimensionalTime]
    pattern_period: Optional[MultidimensionalTime]
    def __init__(self) -> None:
        """Initialize BurstPatternEventTriggering."""
        super().__init__()
        self.max_number_of: Optional[PositiveInteger] = None
        self.minimum_inter: Optional[MultidimensionalTime] = None
        self.min_number_of: Optional[PositiveInteger] = None
        self.pattern_jitter: Optional[MultidimensionalTime] = None
        self.pattern_length: Optional[MultidimensionalTime] = None
        self.pattern_period: Optional[MultidimensionalTime] = None


class BurstPatternEventTriggeringBuilder:
    """Builder for BurstPatternEventTriggering."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BurstPatternEventTriggering = BurstPatternEventTriggering()

    def build(self) -> BurstPatternEventTriggering:
        """Build and return BurstPatternEventTriggering object.

        Returns:
            BurstPatternEventTriggering instance
        """
        # TODO: Add validation
        return self._obj
