"""SegmentPosition AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)


class SegmentPosition(ARObject):
    """AUTOSAR SegmentPosition."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("segment_byte", None, False, False, ByteOrderEnum),  # segmentByte
        ("segment_length", None, True, False, None),  # segmentLength
        ("segment", None, True, False, None),  # segment
    ]

    def __init__(self) -> None:
        """Initialize SegmentPosition."""
        super().__init__()
        self.segment_byte: Optional[ByteOrderEnum] = None
        self.segment_length: Optional[Integer] = None
        self.segment: Optional[Integer] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SegmentPosition to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SegmentPosition":
        """Create SegmentPosition from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SegmentPosition instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SegmentPosition since parent returns ARObject
        return cast("SegmentPosition", obj)


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
