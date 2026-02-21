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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_schedule_table import (
    LinScheduleTable,
)


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



class LinPhysicalChannelBuilder:
    """Builder for LinPhysicalChannel."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LinPhysicalChannel = LinPhysicalChannel()

    def build(self) -> LinPhysicalChannel:
        """Build and return LinPhysicalChannel object.

        Returns:
            LinPhysicalChannel instance
        """
        # TODO: Add validation
        return self._obj
