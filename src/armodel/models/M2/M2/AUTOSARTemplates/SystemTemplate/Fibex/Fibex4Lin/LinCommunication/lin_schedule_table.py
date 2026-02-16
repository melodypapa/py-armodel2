"""LinScheduleTable AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.schedule_table_entry import (
    ScheduleTableEntry,
)


class LinScheduleTable(Identifiable):
    """AUTOSAR LinScheduleTable."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "resume_position": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ResumePosition,
        ),  # resumePosition
        "run_mode": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=RunMode,
        ),  # runMode
        "table_entries": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=ScheduleTableEntry,
        ),  # tableEntries
    }

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
