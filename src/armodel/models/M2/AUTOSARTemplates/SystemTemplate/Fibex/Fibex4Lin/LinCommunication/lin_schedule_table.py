"""LinScheduleTable AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 432)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication import (
    ResumePosition,
    RunMode,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.schedule_table_entry import (
    ScheduleTableEntry,
)


class LinScheduleTable(Identifiable):
    """AUTOSAR LinScheduleTable."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    resume_position: Optional[ResumePosition]
    run_mode: Optional[RunMode]
    table_entries: list[ScheduleTableEntry]
    def __init__(self) -> None:
        """Initialize LinScheduleTable."""
        super().__init__()
        self.resume_position: Optional[ResumePosition] = None
        self.run_mode: Optional[RunMode] = None
        self.table_entries: list[ScheduleTableEntry] = []


class LinScheduleTableBuilder:
    """Builder for LinScheduleTable."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LinScheduleTable = LinScheduleTable()

    def build(self) -> LinScheduleTable:
        """Build and return LinScheduleTable object.

        Returns:
            LinScheduleTable instance
        """
        # TODO: Add validation
        return self._obj
