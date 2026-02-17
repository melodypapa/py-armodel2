"""ApplicationEntry AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 433)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.schedule_table_entry import (
    ScheduleTableEntry,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_frame_triggering import (
    LinFrameTriggering,
)


class ApplicationEntry(ScheduleTableEntry):
    """AUTOSAR ApplicationEntry."""

    frame_triggering: Optional[LinFrameTriggering]
    def __init__(self) -> None:
        """Initialize ApplicationEntry."""
        super().__init__()
        self.frame_triggering: Optional[LinFrameTriggering] = None


class ApplicationEntryBuilder:
    """Builder for ApplicationEntry."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ApplicationEntry = ApplicationEntry()

    def build(self) -> ApplicationEntry:
        """Build and return ApplicationEntry object.

        Returns:
            ApplicationEntry instance
        """
        # TODO: Add validation
        return self._obj
