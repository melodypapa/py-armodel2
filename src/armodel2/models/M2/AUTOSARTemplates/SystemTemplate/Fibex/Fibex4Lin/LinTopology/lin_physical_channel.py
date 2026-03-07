"""LinPhysicalChannel AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 99)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.physical_channel import (
    PhysicalChannel,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.physical_channel import PhysicalChannelBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_schedule_table import (
    LinScheduleTable,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class LinPhysicalChannel(PhysicalChannel):
    """AUTOSAR LinPhysicalChannel."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "LIN-PHYSICAL-CHANNEL"


    bus_idle_timeout: Optional[TimeValue]
    schedule_tables: list[LinScheduleTable]
    _DESERIALIZE_DISPATCH = {
        "BUS-IDLE-TIMEOUT": lambda obj, elem: setattr(obj, "bus_idle_timeout", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "SCHEDULE-TABLES": lambda obj, elem: obj.schedule_tables.append(SerializationHelper.deserialize_by_tag(elem, "LinScheduleTable")),
    }


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
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "BUS-IDLE-TIMEOUT":
                setattr(obj, "bus_idle_timeout", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "SCHEDULE-TABLES":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.schedule_tables.append(SerializationHelper.deserialize_by_tag(item_elem, "LinScheduleTable"))

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
            raise ValueError("Attribute 'bus_idle_timeout' is required and cannot be None")
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


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "busIdleTimeout",
        "scheduleTable",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> LinPhysicalChannel:
        """Build and return the LinPhysicalChannel instance with validation."""
        self._validate_instance()
        return self._obj