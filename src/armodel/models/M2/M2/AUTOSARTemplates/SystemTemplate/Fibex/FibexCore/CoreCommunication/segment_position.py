"""SegmentPosition AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)


class SegmentPosition(ARObject):
    """AUTOSAR SegmentPosition."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "segment_byte": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ByteOrderEnum,
        ),  # segmentByte
        "segment_length": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # segmentLength
        "segment": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # segment
    }

    def __init__(self) -> None:
        """Initialize SegmentPosition."""
        super().__init__()
        self.segment_byte: Optional[ByteOrderEnum] = None
        self.segment_length: Optional[Integer] = None
        self.segment: Optional[Integer] = None


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
