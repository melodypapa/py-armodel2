"""SynchronizationPointConstraint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 132)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingConstraint_SynchronizationPointConstraint.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.timing_constraint import (
    TimingConstraint,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.abstract_event import (
    AbstractEvent,
)


class SynchronizationPointConstraint(TimingConstraint):
    """AUTOSAR SynchronizationPointConstraint."""

    source_eecs: list[Any]
    source_events: list[AbstractEvent]
    target_eecs: list[Any]
    target_events: list[AbstractEvent]
    def __init__(self) -> None:
        """Initialize SynchronizationPointConstraint."""
        super().__init__()
        self.source_eecs: list[Any] = []
        self.source_events: list[AbstractEvent] = []
        self.target_eecs: list[Any] = []
        self.target_events: list[AbstractEvent] = []


class SynchronizationPointConstraintBuilder:
    """Builder for SynchronizationPointConstraint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SynchronizationPointConstraint = SynchronizationPointConstraint()

    def build(self) -> SynchronizationPointConstraint:
        """Build and return SynchronizationPointConstraint object.

        Returns:
            SynchronizationPointConstraint instance
        """
        # TODO: Add validation
        return self._obj
