"""FreeFormatEntry AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 433)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.schedule_table_entry import (
    ScheduleTableEntry,
)


class FreeFormatEntry(ScheduleTableEntry):
    """AUTOSAR FreeFormatEntry."""
    """Abstract base class - do not instantiate directly."""

    def __init__(self) -> None:
        """Initialize FreeFormatEntry."""
        super().__init__()


class FreeFormatEntryBuilder:
    """Builder for FreeFormatEntry."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FreeFormatEntry = FreeFormatEntry()

    def build(self) -> FreeFormatEntry:
        """Build and return FreeFormatEntry object.

        Returns:
            FreeFormatEntry instance
        """
        # TODO: Add validation
        return self._obj
