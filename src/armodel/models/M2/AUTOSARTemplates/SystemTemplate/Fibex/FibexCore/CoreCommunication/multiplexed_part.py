"""MultiplexedPart AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.segment_position import (
    SegmentPosition,
)


class MultiplexedPart(ARObject):
    """AUTOSAR MultiplexedPart."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("segment_positions", None, False, True, SegmentPosition),  # segmentPositions
    ]

    def __init__(self) -> None:
        """Initialize MultiplexedPart."""
        super().__init__()
        self.segment_positions: list[SegmentPosition] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert MultiplexedPart to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MultiplexedPart":
        """Create MultiplexedPart from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            MultiplexedPart instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to MultiplexedPart since parent returns ARObject
        return cast("MultiplexedPart", obj)


class MultiplexedPartBuilder:
    """Builder for MultiplexedPart."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MultiplexedPart = MultiplexedPart()

    def build(self) -> MultiplexedPart:
        """Build and return MultiplexedPart object.

        Returns:
            MultiplexedPart instance
        """
        # TODO: Add validation
        return self._obj
