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
from armodel.serialization import SerializationHelper
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

    def serialize(self) -> ET.Element:
        """Serialize LinScheduleTable to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(LinScheduleTable, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize resume_position
        if self.resume_position is not None:
            serialized = SerializationHelper.serialize_item(self.resume_position, "ResumePosition")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RESUME-POSITION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize run_mode
        if self.run_mode is not None:
            serialized = SerializationHelper.serialize_item(self.run_mode, "RunMode")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RUN-MODE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize table_entries (list to container "TABLE-ENTRIES")
        if self.table_entries:
            wrapper = ET.Element("TABLE-ENTRIES")
            for item in self.table_entries:
                serialized = SerializationHelper.serialize_item(item, "ScheduleTableEntry")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LinScheduleTable":
        """Deserialize XML element to LinScheduleTable object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LinScheduleTable object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(LinScheduleTable, cls).deserialize(element)

        # Parse resume_position
        child = SerializationHelper.find_child_element(element, "RESUME-POSITION")
        if child is not None:
            resume_position_value = ResumePosition.deserialize(child)
            obj.resume_position = resume_position_value

        # Parse run_mode
        child = SerializationHelper.find_child_element(element, "RUN-MODE")
        if child is not None:
            run_mode_value = RunMode.deserialize(child)
            obj.run_mode = run_mode_value

        # Parse table_entries (list from container "TABLE-ENTRIES")
        obj.table_entries = []
        container = SerializationHelper.find_child_element(element, "TABLE-ENTRIES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.table_entries.append(child_value)

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
