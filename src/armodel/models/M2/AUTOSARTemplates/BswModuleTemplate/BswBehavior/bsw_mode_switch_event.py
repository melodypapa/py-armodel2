"""BswModeSwitchEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 94)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_schedule_event import (
    BswScheduleEvent,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration import (
    ModeActivationKind,
)


class BswModeSwitchEvent(BswScheduleEvent):
    """AUTOSAR BswModeSwitchEvent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    activation: Optional[ModeActivationKind]
    def __init__(self) -> None:
        """Initialize BswModeSwitchEvent."""
        super().__init__()
        self.activation: Optional[ModeActivationKind] = None


class BswModeSwitchEventBuilder:
    """Builder for BswModeSwitchEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswModeSwitchEvent = BswModeSwitchEvent()

    def build(self) -> BswModeSwitchEvent:
        """Build and return BswModeSwitchEvent object.

        Returns:
            BswModeSwitchEvent instance
        """
        # TODO: Add validation
        return self._obj
