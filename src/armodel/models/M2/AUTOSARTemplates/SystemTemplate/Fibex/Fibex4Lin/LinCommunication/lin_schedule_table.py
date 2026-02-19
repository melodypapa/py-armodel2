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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "LinScheduleTable":
        """Deserialize XML element to LinScheduleTable object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LinScheduleTable object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse resume_position
        child = ARObject._find_child_element(element, "RESUME-POSITION")
        if child is not None:
            resume_position_value = child.text
            obj.resume_position = resume_position_value

        # Parse run_mode
        child = ARObject._find_child_element(element, "RUN-MODE")
        if child is not None:
            run_mode_value = child.text
            obj.run_mode = run_mode_value

        # Parse table_entries (list)
        obj.table_entries = []
        for child in ARObject._find_all_child_elements(element, "TABLE-ENTRIES"):
            table_entries_value = ARObject._deserialize_by_tag(child, "ScheduleTableEntry")
            obj.table_entries.append(table_entries_value)

        return obj



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
