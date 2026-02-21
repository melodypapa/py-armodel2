"""SegmentPosition AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 412)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ByteOrderEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)


class SegmentPosition(ARObject):
    """AUTOSAR SegmentPosition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    segment_byte: Optional[ByteOrderEnum]
    segment_length: Optional[Integer]
    segment: Optional[Integer]
    def __init__(self) -> None:
        """Initialize SegmentPosition."""
        super().__init__()
        self.segment_byte: Optional[ByteOrderEnum] = None
        self.segment_length: Optional[Integer] = None
        self.segment: Optional[Integer] = None

    def serialize(self) -> ET.Element:
        """Serialize SegmentPosition to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SegmentPosition, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize segment_byte
        if self.segment_byte is not None:
            serialized = SerializationHelper.serialize_item(self.segment_byte, "ByteOrderEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SEGMENT-BYTE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize segment_length
        if self.segment_length is not None:
            serialized = SerializationHelper.serialize_item(self.segment_length, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SEGMENT-LENGTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize segment
        if self.segment is not None:
            serialized = SerializationHelper.serialize_item(self.segment, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SEGMENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SegmentPosition":
        """Deserialize XML element to SegmentPosition object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SegmentPosition object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SegmentPosition, cls).deserialize(element)

        # Parse segment_byte
        child = SerializationHelper.find_child_element(element, "SEGMENT-BYTE")
        if child is not None:
            segment_byte_value = ByteOrderEnum.deserialize(child)
            obj.segment_byte = segment_byte_value

        # Parse segment_length
        child = SerializationHelper.find_child_element(element, "SEGMENT-LENGTH")
        if child is not None:
            segment_length_value = child.text
            obj.segment_length = segment_length_value

        # Parse segment
        child = SerializationHelper.find_child_element(element, "SEGMENT")
        if child is not None:
            segment_value = child.text
            obj.segment = segment_value

        return obj



class SegmentPositionBuilder:
    """Builder for SegmentPosition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SegmentPosition = SegmentPosition()

    def build(self) -> SegmentPosition:
        """Build and return SegmentPosition object.

        Returns:
            SegmentPosition instance
        """
        # TODO: Add validation
        return self._obj
