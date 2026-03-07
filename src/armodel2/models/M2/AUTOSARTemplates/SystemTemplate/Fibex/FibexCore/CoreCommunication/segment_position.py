"""SegmentPosition AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 412)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ByteOrderEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SegmentPosition(ARObject):
    """AUTOSAR SegmentPosition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SEGMENT-POSITION"


    segment_byte: Optional[ByteOrderEnum]
    segment_length: Optional[Integer]
    segment: Optional[Integer]
    _DESERIALIZE_DISPATCH = {
        "SEGMENT-BYTE": lambda obj, elem: setattr(obj, "segment_byte", ByteOrderEnum.deserialize(elem)),
        "SEGMENT-LENGTH": lambda obj, elem: setattr(obj, "segment_length", SerializationHelper.deserialize_by_tag(elem, "Integer")),
        "SEGMENT": lambda obj, elem: setattr(obj, "segment", SerializationHelper.deserialize_by_tag(elem, "Integer")),
    }


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
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "SEGMENT-BYTE":
                setattr(obj, "segment_byte", ByteOrderEnum.deserialize(child))
            elif tag == "SEGMENT-LENGTH":
                setattr(obj, "segment_length", SerializationHelper.deserialize_by_tag(child, "Integer"))
            elif tag == "SEGMENT":
                setattr(obj, "segment", SerializationHelper.deserialize_by_tag(child, "Integer"))

        return obj



class SegmentPositionBuilder(BuilderBase):
    """Builder for SegmentPosition with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SegmentPosition = SegmentPosition()


    def with_segment_byte(self, value: Optional[ByteOrderEnum]) -> "SegmentPositionBuilder":
        """Set segment_byte attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'segment_byte' is required and cannot be None")
        self._obj.segment_byte = value
        return self

    def with_segment_length(self, value: Optional[Integer]) -> "SegmentPositionBuilder":
        """Set segment_length attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'segment_length' is required and cannot be None")
        self._obj.segment_length = value
        return self

    def with_segment(self, value: Optional[Integer]) -> "SegmentPositionBuilder":
        """Set segment attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'segment' is required and cannot be None")
        self._obj.segment = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "segment",
        "segmentByte",
        "segmentLength",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> SegmentPosition:
        """Build and return the SegmentPosition instance with validation."""
        self._validate_instance()
        return self._obj