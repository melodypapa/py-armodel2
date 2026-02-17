"""BswScheduleEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 88)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_event import (
    BswEvent,
)


class BswScheduleEvent(BswEvent):
    """AUTOSAR BswScheduleEvent."""
    """Abstract base class - do not instantiate directly."""

    def __init__(self) -> None:
        """Initialize BswScheduleEvent."""
        super().__init__()


class BswScheduleEventBuilder:
    """Builder for BswScheduleEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswScheduleEvent = BswScheduleEvent()

    def build(self) -> BswScheduleEvent:
        """Build and return BswScheduleEvent object.

        Returns:
            BswScheduleEvent instance
        """
        # TODO: Add validation
        return self._obj
