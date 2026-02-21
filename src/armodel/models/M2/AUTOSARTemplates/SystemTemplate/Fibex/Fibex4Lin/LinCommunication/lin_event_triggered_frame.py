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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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

    collision_schedule_ref: Optional[ARRef]
    lin_unconditional_frame_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize LinEventTriggeredFrame."""
        super().__init__()
        self.collision_schedule_ref: Optional[ARRef] = None
        self.lin_unconditional_frame_refs: list[ARRef] = []

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

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize collision_schedule_ref
        if self.collision_schedule_ref is not None:
            serialized = ARObject._serialize_item(self.collision_schedule_ref, "LinScheduleTable")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COLLISION-SCHEDULE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize lin_unconditional_frame_refs (list to container "LIN-UNCONDITIONAL-FRAME-REFS")
        if self.lin_unconditional_frame_refs:
            wrapper = ET.Element("LIN-UNCONDITIONAL-FRAME-REFS")
            for item in self.lin_unconditional_frame_refs:
                serialized = ARObject._serialize_item(item, "LinUnconditionalFrame")
                if serialized is not None:
                    child_elem = ET.Element("LIN-UNCONDITIONAL-FRAME-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
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

        # Parse collision_schedule_ref
        child = ARObject._find_child_element(element, "COLLISION-SCHEDULE-REF")
        if child is not None:
            collision_schedule_ref_value = ARRef.deserialize(child)
            obj.collision_schedule_ref = collision_schedule_ref_value

        # Parse lin_unconditional_frame_refs (list from container "LIN-UNCONDITIONAL-FRAME-REFS")
        obj.lin_unconditional_frame_refs = []
        container = ARObject._find_child_element(element, "LIN-UNCONDITIONAL-FRAME-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.lin_unconditional_frame_refs.append(child_value)

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
