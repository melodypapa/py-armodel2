"""BswDataReceivedEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 99)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_schedule_event import (
    BswScheduleEvent,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class BswDataReceivedEvent(BswScheduleEvent):
    """AUTOSAR BswDataReceivedEvent."""

    data: Optional[VariableDataPrototype]
    def __init__(self) -> None:
        """Initialize BswDataReceivedEvent."""
        super().__init__()
        self.data: Optional[VariableDataPrototype] = None


class BswDataReceivedEventBuilder:
    """Builder for BswDataReceivedEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswDataReceivedEvent = BswDataReceivedEvent()

    def build(self) -> BswDataReceivedEvent:
        """Build and return BswDataReceivedEvent object.

        Returns:
            BswDataReceivedEvent instance
        """
        # TODO: Add validation
        return self._obj
