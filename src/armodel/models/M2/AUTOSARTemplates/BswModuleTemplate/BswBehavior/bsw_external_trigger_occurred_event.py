"""BswExternalTriggerOccurredEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 91)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_schedule_event import (
    BswScheduleEvent,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger import (
    Trigger,
)


class BswExternalTriggerOccurredEvent(BswScheduleEvent):
    """AUTOSAR BswExternalTriggerOccurredEvent."""

    trigger: Optional[Trigger]
    def __init__(self) -> None:
        """Initialize BswExternalTriggerOccurredEvent."""
        super().__init__()
        self.trigger: Optional[Trigger] = None


class BswExternalTriggerOccurredEventBuilder:
    """Builder for BswExternalTriggerOccurredEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswExternalTriggerOccurredEvent = BswExternalTriggerOccurredEvent()

    def build(self) -> BswExternalTriggerOccurredEvent:
        """Build and return BswExternalTriggerOccurredEvent object.

        Returns:
            BswExternalTriggerOccurredEvent instance
        """
        # TODO: Add validation
        return self._obj
