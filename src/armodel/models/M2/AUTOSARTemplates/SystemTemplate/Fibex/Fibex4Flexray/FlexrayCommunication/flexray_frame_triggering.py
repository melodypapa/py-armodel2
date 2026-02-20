"""FlexrayFrameTriggering AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 422)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Flexray_FlexrayCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.frame_triggering import (
    FrameTriggering,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayCommunication.flexray_absolutely_scheduled_timing import (
    FlexrayAbsolutelyScheduledTiming,
)


class FlexrayFrameTriggering(FrameTriggering):
    """AUTOSAR FlexrayFrameTriggering."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    absolutelies: list[FlexrayAbsolutelyScheduledTiming]
    allow_dynamic: Optional[Boolean]
    message_id: Optional[PositiveInteger]
    payload_preamble: Optional[Any]
    def __init__(self) -> None:
        """Initialize FlexrayFrameTriggering."""
        super().__init__()
        self.absolutelies: list[FlexrayAbsolutelyScheduledTiming] = []
        self.allow_dynamic: Optional[Boolean] = None
        self.message_id: Optional[PositiveInteger] = None
        self.payload_preamble: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize FlexrayFrameTriggering to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(FlexrayFrameTriggering, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize absolutelies (list to container "ABSOLUTELIES")
        if self.absolutelies:
            wrapper = ET.Element("ABSOLUTELIES")
            for item in self.absolutelies:
                serialized = ARObject._serialize_item(item, "FlexrayAbsolutelyScheduledTiming")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize allow_dynamic
        if self.allow_dynamic is not None:
            serialized = ARObject._serialize_item(self.allow_dynamic, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ALLOW-DYNAMIC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize message_id
        if self.message_id is not None:
            serialized = ARObject._serialize_item(self.message_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MESSAGE-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize payload_preamble
        if self.payload_preamble is not None:
            serialized = ARObject._serialize_item(self.payload_preamble, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PAYLOAD-PREAMBLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlexrayFrameTriggering":
        """Deserialize XML element to FlexrayFrameTriggering object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FlexrayFrameTriggering object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(FlexrayFrameTriggering, cls).deserialize(element)

        # Parse absolutelies (list from container "ABSOLUTELIES")
        obj.absolutelies = []
        container = ARObject._find_child_element(element, "ABSOLUTELIES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.absolutelies.append(child_value)

        # Parse allow_dynamic
        child = ARObject._find_child_element(element, "ALLOW-DYNAMIC")
        if child is not None:
            allow_dynamic_value = child.text
            obj.allow_dynamic = allow_dynamic_value

        # Parse message_id
        child = ARObject._find_child_element(element, "MESSAGE-ID")
        if child is not None:
            message_id_value = child.text
            obj.message_id = message_id_value

        # Parse payload_preamble
        child = ARObject._find_child_element(element, "PAYLOAD-PREAMBLE")
        if child is not None:
            payload_preamble_value = child.text
            obj.payload_preamble = payload_preamble_value

        return obj



class FlexrayFrameTriggeringBuilder:
    """Builder for FlexrayFrameTriggering."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlexrayFrameTriggering = FlexrayFrameTriggering()

    def build(self) -> FlexrayFrameTriggering:
        """Build and return FlexrayFrameTriggering object.

        Returns:
            FlexrayFrameTriggering instance
        """
        # TODO: Add validation
        return self._obj
