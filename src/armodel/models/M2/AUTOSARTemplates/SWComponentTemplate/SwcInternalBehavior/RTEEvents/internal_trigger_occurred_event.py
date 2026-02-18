"""InternalTriggerOccurredEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 546)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_RTEEvents.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import (
    RTEEvent,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.Trigger.internal_triggering_point import (
    InternalTriggeringPoint,
)


class InternalTriggerOccurredEvent(RTEEvent):
    """AUTOSAR InternalTriggerOccurredEvent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    event_source_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize InternalTriggerOccurredEvent."""
        super().__init__()
        self.event_source_ref: Optional[ARRef] = None


class InternalTriggerOccurredEventBuilder:
    """Builder for InternalTriggerOccurredEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: InternalTriggerOccurredEvent = InternalTriggerOccurredEvent()

    def build(self) -> InternalTriggerOccurredEvent:
        """Build and return InternalTriggerOccurredEvent object.

        Returns:
            InternalTriggerOccurredEvent instance
        """
        # TODO: Add validation
        return self._obj
