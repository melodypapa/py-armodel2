"""OsTaskExecutionEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 547)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_RTEEvents.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import (
    RTEEvent,
)


class OsTaskExecutionEvent(RTEEvent):
    """AUTOSAR OsTaskExecutionEvent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize OsTaskExecutionEvent."""
        super().__init__()


class OsTaskExecutionEventBuilder:
    """Builder for OsTaskExecutionEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: OsTaskExecutionEvent = OsTaskExecutionEvent()

    def build(self) -> OsTaskExecutionEvent:
        """Build and return OsTaskExecutionEvent object.

        Returns:
            OsTaskExecutionEvent instance
        """
        # TODO: Add validation
        return self._obj
