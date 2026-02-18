"""TimingConstraint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 253)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingConstraint.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.BlockElements.RequirementsTracing.traceable import (
    Traceable,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition.timing_condition import (
    TimingCondition,
)
from abc import ABC, abstractmethod


class TimingConstraint(Traceable, ABC):
    """AUTOSAR TimingConstraint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    timing_condition: Optional[TimingCondition]
    def __init__(self) -> None:
        """Initialize TimingConstraint."""
        super().__init__()
        self.timing_condition: Optional[TimingCondition] = None


class TimingConstraintBuilder:
    """Builder for TimingConstraint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TimingConstraint = TimingConstraint()

    def build(self) -> TimingConstraint:
        """Build and return TimingConstraint object.

        Returns:
            TimingConstraint instance
        """
        # TODO: Add validation
        return self._obj
