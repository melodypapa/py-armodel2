"""LinEventTriggeredFrame AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 430)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_frame import (
    LinFrame,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_schedule_table import (
    LinScheduleTable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_unconditional_frame import (
    LinUnconditionalFrame,
)


class LinEventTriggeredFrame(LinFrame):
    """AUTOSAR LinEventTriggeredFrame."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    collision_schedule: Optional[LinScheduleTable]
    lin_unconditional_frames: list[LinUnconditionalFrame]
    def __init__(self) -> None:
        """Initialize LinEventTriggeredFrame."""
        super().__init__()
        self.collision_schedule: Optional[LinScheduleTable] = None
        self.lin_unconditional_frames: list[LinUnconditionalFrame] = []

    def serialize(self) -> ET.Element:
        """Serialize LinEventTriggeredFrame to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(LinEventTriggeredFrame, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize collision_schedule
        if self.collision_schedule is not None:
            serialized = ARObject._serialize_item(self.collision_schedule, "LinScheduleTable")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COLLISION-SCHEDULE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize lin_unconditional_frames (list to container "LIN-UNCONDITIONAL-FRAMES")
        if self.lin_unconditional_frames:
            wrapper = ET.Element("LIN-UNCONDITIONAL-FRAMES")
            for item in self.lin_unconditional_frames:
                serialized = ARObject._serialize_item(item, "LinUnconditionalFrame")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LinEventTriggeredFrame":
        """Deserialize XML element to LinEventTriggeredFrame object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LinEventTriggeredFrame object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(LinEventTriggeredFrame, cls).deserialize(element)

        # Parse collision_schedule
        child = ARObject._find_child_element(element, "COLLISION-SCHEDULE")
        if child is not None:
            collision_schedule_value = ARObject._deserialize_by_tag(child, "LinScheduleTable")
            obj.collision_schedule = collision_schedule_value

        # Parse lin_unconditional_frames (list from container "LIN-UNCONDITIONAL-FRAMES")
        obj.lin_unconditional_frames = []
        container = ARObject._find_child_element(element, "LIN-UNCONDITIONAL-FRAMES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.lin_unconditional_frames.append(child_value)

        return obj



class LinEventTriggeredFrameBuilder:
    """Builder for LinEventTriggeredFrame."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LinEventTriggeredFrame = LinEventTriggeredFrame()

    def build(self) -> LinEventTriggeredFrame:
        """Build and return LinEventTriggeredFrame object.

        Returns:
            LinEventTriggeredFrame instance
        """
        # TODO: Add validation
        return self._obj
