"""ModeSwitchedAckEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 545)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_RTEEvents.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import (
    RTEEvent,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ModeDeclarationGroup.mode_switch_point import (
    ModeSwitchPoint,
)


class ModeSwitchedAckEvent(RTEEvent):
    """AUTOSAR ModeSwitchedAckEvent."""

    def __init__(self) -> None:
        """Initialize ModeSwitchedAckEvent."""
        super().__init__()
        self.event_source: Optional[ModeSwitchPoint] = None


class ModeSwitchedAckEventBuilder:
    """Builder for ModeSwitchedAckEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeSwitchedAckEvent = ModeSwitchedAckEvent()

    def build(self) -> ModeSwitchedAckEvent:
        """Build and return ModeSwitchedAckEvent object.

        Returns:
            ModeSwitchedAckEvent instance
        """
        # TODO: Add validation
        return self._obj
