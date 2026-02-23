"""LinPhysicalChannel AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 99)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.physical_channel import (
    PhysicalChannel,
)
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.physical_channel import PhysicalChannelBuilder
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_schedule_table import (
    LinScheduleTable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class LinPhysicalChannel(PhysicalChannel):
    """AUTOSAR LinPhysicalChannel."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    bus_idle_timeout: Optional[TimeValue]
    schedule_tables: list[LinScheduleTable]
    def __init__(self) -> None:
        """Initialize LinPhysicalChannel."""
        super().__init__()
        self.bus_idle_timeout: Optional[TimeValue] = None
        self.schedule_tables: list[LinScheduleTable] = []

    def serialize(self) -> ET.Element:
        """Serialize LinPhysicalChannel to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(LinPhysicalChannel, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize bus_idle_timeout
        if self.bus_idle_timeout is not None:
            serialized = SerializationHelper.serialize_item(self.bus_idle_timeout, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BUS-IDLE-TIMEOUT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize schedule_tables (list to container "SCHEDULE-TABLES")
        if self.schedule_tables:
            wrapper = ET.Element("SCHEDULE-TABLES")
            for item in self.schedule_tables:
                serialized = SerializationHelper.serialize_item(item, "LinScheduleTable")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LinPhysicalChannel":
        """Deserialize XML element to LinPhysicalChannel object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LinPhysicalChannel object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(LinPhysicalChannel, cls).deserialize(element)

        # Parse bus_idle_timeout
        child = SerializationHelper.find_child_element(element, "BUS-IDLE-TIMEOUT")
        if child is not None:
            bus_idle_timeout_value = child.text
            obj.bus_idle_timeout = bus_idle_timeout_value

        # Parse schedule_tables (list from container "SCHEDULE-TABLES")
        obj.schedule_tables = []
        container = SerializationHelper.find_child_element(element, "SCHEDULE-TABLES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.schedule_tables.append(child_value)

        return obj



class LinPhysicalChannelBuilder(PhysicalChannelBuilder):
    """Builder for LinPhysicalChannel with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: LinPhysicalChannel = LinPhysicalChannel()


    def with_bus_idle_timeout(self, value: Optional[TimeValue]) -> "LinPhysicalChannelBuilder":
        """Set bus_idle_timeout attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.bus_idle_timeout = value
        return self

    def with_schedule_tables(self, items: list[LinScheduleTable]) -> "LinPhysicalChannelBuilder":
        """Set schedule_tables list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.schedule_tables = list(items) if items else []
        return self


    def add_schedule_table(self, item: LinScheduleTable) -> "LinPhysicalChannelBuilder":
        """Add a single item to schedule_tables list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.schedule_tables.append(item)
        return self

    def clear_schedule_tables(self) -> "LinPhysicalChannelBuilder":
        """Clear all items from schedule_tables list.

        Returns:
            self for method chaining
        """
        self._obj.schedule_tables = []
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


    def build(self) -> LinPhysicalChannel:
        """Build and return the LinPhysicalChannel instance with validation."""
        self._validate_instance()
        pass
        return self._obj