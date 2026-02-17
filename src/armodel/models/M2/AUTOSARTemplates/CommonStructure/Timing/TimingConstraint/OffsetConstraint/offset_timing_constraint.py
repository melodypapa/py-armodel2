"""OffsetTimingConstraint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 114)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingConstraint_OffsetConstraint.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.timing_constraint import (
    TimingConstraint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description_event import (
    TimingDescriptionEvent,
)


class OffsetTimingConstraint(TimingConstraint):
    """AUTOSAR OffsetTimingConstraint."""

    maximum: Optional[MultidimensionalTime]
    minimum: Optional[MultidimensionalTime]
    source: Optional[TimingDescriptionEvent]
    target: Optional[TimingDescriptionEvent]
    def __init__(self) -> None:
        """Initialize OffsetTimingConstraint."""
        super().__init__()
        self.maximum: Optional[MultidimensionalTime] = None
        self.minimum: Optional[MultidimensionalTime] = None
        self.source: Optional[TimingDescriptionEvent] = None
        self.target: Optional[TimingDescriptionEvent] = None


class OffsetTimingConstraintBuilder:
    """Builder for OffsetTimingConstraint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: OffsetTimingConstraint = OffsetTimingConstraint()

    def build(self) -> OffsetTimingConstraint:
        """Build and return OffsetTimingConstraint object.

        Returns:
            OffsetTimingConstraint instance
        """
        # TODO: Add validation
        return self._obj
