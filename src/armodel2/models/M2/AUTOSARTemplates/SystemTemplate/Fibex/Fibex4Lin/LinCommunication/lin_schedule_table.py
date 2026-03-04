"""LinScheduleTable AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 432)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication import (
    ResumePosition,
    RunMode,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.schedule_table_entry import (
    ScheduleTableEntry,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class LinScheduleTable(Identifiable):
    """AUTOSAR LinScheduleTable."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "LIN-SCHEDULE-TABLE"


    resume_position: Optional[ResumePosition]
    run_mode: Optional[RunMode]
    table_entries: list[ScheduleTableEntry]
    _DESERIALIZE_DISPATCH = {
        "RESUME-POSITION": lambda obj, elem: setattr(obj, "resume_position", ResumePosition.deserialize(elem)),
        "RUN-MODE": lambda obj, elem: setattr(obj, "run_mode", RunMode.deserialize(elem)),
        "TABLE-ENTRYS": ("_POLYMORPHIC_LIST", "table_entries", ["ApplicationEntry", "AssignFrameId", "AssignFrameIdRange", "AssignNad", "ConditionalChangeNad", "DataDumpEntry", "FreeFormat", "FreeFormatEntry", "LinConfigurationEntry", "SaveConfigurationEntry", "UnassignFrameId"]),
    }


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
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

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

        # Serialize table_entries (list to container "TABLE-ENTRYS")
        if self.table_entries:
            wrapper = ET.Element("TABLE-ENTRYS")
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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "RESUME-POSITION":
                setattr(obj, "resume_position", ResumePosition.deserialize(child))
            elif tag == "RUN-MODE":
                setattr(obj, "run_mode", RunMode.deserialize(child))
            elif tag == "TABLE-ENTRYS":
                # Iterate through all child elements and deserialize each based on its concrete type
                for item_elem in child:
                    concrete_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    if concrete_tag == "APPLICATION-ENTRY":
                        obj.table_entries.append(SerializationHelper.deserialize_by_tag(item_elem, "ApplicationEntry"))
                    elif concrete_tag == "ASSIGN-FRAME-ID":
                        obj.table_entries.append(SerializationHelper.deserialize_by_tag(item_elem, "AssignFrameId"))
                    elif concrete_tag == "ASSIGN-FRAME-ID-RANGE":
                        obj.table_entries.append(SerializationHelper.deserialize_by_tag(item_elem, "AssignFrameIdRange"))
                    elif concrete_tag == "ASSIGN-NAD":
                        obj.table_entries.append(SerializationHelper.deserialize_by_tag(item_elem, "AssignNad"))
                    elif concrete_tag == "CONDITIONAL-CHANGE-NAD":
                        obj.table_entries.append(SerializationHelper.deserialize_by_tag(item_elem, "ConditionalChangeNad"))
                    elif concrete_tag == "DATA-DUMP-ENTRY":
                        obj.table_entries.append(SerializationHelper.deserialize_by_tag(item_elem, "DataDumpEntry"))
                    elif concrete_tag == "FREE-FORMAT":
                        obj.table_entries.append(SerializationHelper.deserialize_by_tag(item_elem, "FreeFormat"))
                    elif concrete_tag == "FREE-FORMAT-ENTRY":
                        obj.table_entries.append(SerializationHelper.deserialize_by_tag(item_elem, "FreeFormatEntry"))
                    elif concrete_tag == "LIN-CONFIGURATION-ENTRY":
                        obj.table_entries.append(SerializationHelper.deserialize_by_tag(item_elem, "LinConfigurationEntry"))
                    elif concrete_tag == "SAVE-CONFIGURATION-ENTRY":
                        obj.table_entries.append(SerializationHelper.deserialize_by_tag(item_elem, "SaveConfigurationEntry"))
                    elif concrete_tag == "UNASSIGN-FRAME-ID":
                        obj.table_entries.append(SerializationHelper.deserialize_by_tag(item_elem, "UnassignFrameId"))

        return obj



class LinScheduleTableBuilder(IdentifiableBuilder):
    """Builder for LinScheduleTable with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: LinScheduleTable = LinScheduleTable()


    def with_resume_position(self, value: Optional[ResumePosition]) -> "LinScheduleTableBuilder":
        """Set resume_position attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.resume_position = value
        return self

    def with_run_mode(self, value: Optional[RunMode]) -> "LinScheduleTableBuilder":
        """Set run_mode attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.run_mode = value
        return self

    def with_table_entries(self, items: list[ScheduleTableEntry]) -> "LinScheduleTableBuilder":
        """Set table_entries list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.table_entries = list(items) if items else []
        return self


    def add_table_entry(self, item: ScheduleTableEntry) -> "LinScheduleTableBuilder":
        """Add a single item to table_entries list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.table_entries.append(item)
        return self

    def clear_table_entries(self) -> "LinScheduleTableBuilder":
        """Clear all items from table_entries list.

        Returns:
            self for method chaining
        """
        self._obj.table_entries = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "resumePosition",
        "runMode",
        "tableEntry",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> LinScheduleTable:
        """Build and return the LinScheduleTable instance with validation."""
        self._validate_instance()
        return self._obj