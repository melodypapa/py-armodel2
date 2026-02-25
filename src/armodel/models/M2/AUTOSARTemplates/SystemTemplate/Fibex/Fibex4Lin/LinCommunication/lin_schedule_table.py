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
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication import (
    ResumePosition,
    RunMode,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.schedule_table_entry import (
    ScheduleTableEntry,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


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



    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Get type hints for the class
        try:
            type_hints_dict = get_type_hints(type(self._obj))
        except Exception:
            # Cannot resolve type hints (e.g., forward references), skip validation
            return

        for attr_name, attr_type in type_hints_dict.items():
            if attr_name.startswith("_"):
                continue

            value = getattr(self._obj, attr_name)

            # Check required fields (not Optional)
            if value is None and not self._is_optional_type(attr_type):
                if mode == BuilderValidationMode.STRICT:
                    raise ValueError(
                        f"Required attribute '{attr_name}' is None"
                    )
                elif mode == BuilderValidationMode.LENIENT:
                    import warnings
                    warnings.warn(
                        f"Required attribute '{attr_name}' is None",
                        UserWarning
                    )

    @staticmethod
    def _is_optional_type(type_hint: Any) -> bool:
        """Check if a type hint is Optional.

        Args:
            type_hint: Type hint to check

        Returns:
            True if type is Optional, False otherwise
        """
        origin = getattr(type_hint, "__origin__", None)
        return origin is Union

    @staticmethod
    def _get_expected_type(type_hint: Any) -> type:
        """Extract expected type from type hint.

        Args:
            type_hint: Type hint to extract from

        Returns:
            Expected type
        """
        if isinstance(type_hint, str):
            return object
        origin = getattr(type_hint, "__origin__", None)
        if origin is Union:
            args = getattr(type_hint, "__args__", [])
            for arg in args:
                if arg is not type(None):
                    return arg
        elif origin is list:
            args = getattr(type_hint, "__args__", [object])
            return args[0] if args else object
        return type_hint if isinstance(type_hint, type) else object


    def build(self) -> LinScheduleTable:
        """Build and return the LinScheduleTable instance with validation."""
        self._validate_instance()
        pass
        return self._obj