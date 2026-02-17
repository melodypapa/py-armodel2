"""BswInternalTriggerOccurredEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 91)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_schedule_event import (
    BswScheduleEvent,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_internal_triggering_point import (
    BswInternalTriggeringPoint,
)


class BswInternalTriggerOccurredEvent(BswScheduleEvent):
    """AUTOSAR BswInternalTriggerOccurredEvent."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "event_source_point": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=BswInternalTriggeringPoint,
        ),  # eventSourcePoint
    }

    def __init__(self) -> None:
        """Initialize BswInternalTriggerOccurredEvent."""
        super().__init__()
        self.event_source_point: Optional[BswInternalTriggeringPoint] = None


class BswInternalTriggerOccurredEventBuilder:
    """Builder for BswInternalTriggerOccurredEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswInternalTriggerOccurredEvent = BswInternalTriggerOccurredEvent()

    def build(self) -> BswInternalTriggerOccurredEvent:
        """Build and return BswInternalTriggerOccurredEvent object.

        Returns:
            BswInternalTriggerOccurredEvent instance
        """
        # TODO: Add validation
        return self._obj
