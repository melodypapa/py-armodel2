"""BswModeManagerErrorEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 95)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_schedule_event import (
    BswScheduleEvent,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class BswModeManagerErrorEvent(BswScheduleEvent):
    """AUTOSAR BswModeManagerErrorEvent."""

    def __init__(self) -> None:
        """Initialize BswModeManagerErrorEvent."""
        super().__init__()
        self.mode_group: Optional[ModeDeclarationGroup] = None


class BswModeManagerErrorEventBuilder:
    """Builder for BswModeManagerErrorEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswModeManagerErrorEvent = BswModeManagerErrorEvent()

    def build(self) -> BswModeManagerErrorEvent:
        """Build and return BswModeManagerErrorEvent object.

        Returns:
            BswModeManagerErrorEvent instance
        """
        # TODO: Add validation
        return self._obj
