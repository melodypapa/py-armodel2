"""MultiplexedPart AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 411)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.segment_position import (
    SegmentPosition,
)
from abc import ABC, abstractmethod


class MultiplexedPart(ARObject, ABC):
    """AUTOSAR MultiplexedPart."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    segment_positions: list[SegmentPosition]
    def __init__(self) -> None:
        """Initialize MultiplexedPart."""
        super().__init__()
        self.segment_positions: list[SegmentPosition] = []

    def serialize(self) -> ET.Element:
        """Serialize MultiplexedPart to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(MultiplexedPart, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize segment_positions (list to container "SEGMENT-POSITIONS")
        if self.segment_positions:
            wrapper = ET.Element("SEGMENT-POSITIONS")
            for item in self.segment_positions:
                serialized = SerializationHelper.serialize_item(item, "SegmentPosition")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MultiplexedPart":
        """Deserialize XML element to MultiplexedPart object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MultiplexedPart object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(MultiplexedPart, cls).deserialize(element)

        # Parse segment_positions (list from container "SEGMENT-POSITIONS")
        obj.segment_positions = []
        container = SerializationHelper.find_child_element(element, "SEGMENT-POSITIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.segment_positions.append(child_value)

        return obj



