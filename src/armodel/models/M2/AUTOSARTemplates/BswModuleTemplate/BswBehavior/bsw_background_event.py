"""BswBackgroundEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 89)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_schedule_event import (
    BswScheduleEvent,
)


class BswBackgroundEvent(BswScheduleEvent):
    """AUTOSAR BswBackgroundEvent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize BswBackgroundEvent."""
        super().__init__()


class BswBackgroundEventBuilder:
    """Builder for BswBackgroundEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswBackgroundEvent = BswBackgroundEvent()

    def build(self) -> BswBackgroundEvent:
        """Build and return BswBackgroundEvent object.

        Returns:
            BswBackgroundEvent instance
        """
        # TODO: Add validation
        return self._obj
