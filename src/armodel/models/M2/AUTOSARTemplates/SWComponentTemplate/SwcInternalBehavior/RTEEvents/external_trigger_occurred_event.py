"""ExternalTriggerOccurredEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 545)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_RTEEvents.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import (
    RTEEvent,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger import (
    Trigger,
)


class ExternalTriggerOccurredEvent(RTEEvent):
    """AUTOSAR ExternalTriggerOccurredEvent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    trigger: Optional[Trigger]
    def __init__(self) -> None:
        """Initialize ExternalTriggerOccurredEvent."""
        super().__init__()
        self.trigger: Optional[Trigger] = None


class ExternalTriggerOccurredEventBuilder:
    """Builder for ExternalTriggerOccurredEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ExternalTriggerOccurredEvent = ExternalTriggerOccurredEvent()

    def build(self) -> ExternalTriggerOccurredEvent:
        """Build and return ExternalTriggerOccurredEvent object.

        Returns:
            ExternalTriggerOccurredEvent instance
        """
        # TODO: Add validation
        return self._obj
