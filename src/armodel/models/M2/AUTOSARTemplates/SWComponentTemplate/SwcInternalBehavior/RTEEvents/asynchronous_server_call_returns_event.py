"""AsynchronousServerCallReturnsEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 541)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_RTEEvents.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import (
    RTEEvent,
)


class AsynchronousServerCallReturnsEvent(RTEEvent):
    """AUTOSAR AsynchronousServerCallReturnsEvent."""

    event_source: Optional[Any]
    def __init__(self) -> None:
        """Initialize AsynchronousServerCallReturnsEvent."""
        super().__init__()
        self.event_source: Optional[Any] = None


class AsynchronousServerCallReturnsEventBuilder:
    """Builder for AsynchronousServerCallReturnsEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AsynchronousServerCallReturnsEvent = AsynchronousServerCallReturnsEvent()

    def build(self) -> AsynchronousServerCallReturnsEvent:
        """Build and return AsynchronousServerCallReturnsEvent object.

        Returns:
            AsynchronousServerCallReturnsEvent instance
        """
        # TODO: Add validation
        return self._obj
