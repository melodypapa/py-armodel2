"""MultiplexedPart AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 411)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.segment_position import (
    SegmentPosition,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


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
    _DESERIALIZE_DISPATCH = {
        "SEGMENT-POSITIONS": lambda obj, elem: obj.segment_positions.append(SerializationHelper.deserialize_by_tag(elem, "SegmentPosition")),
    }


    def __init__(self) -> None:
        """Initialize MultiplexedPart."""
        super().__init__()
        self.segment_positions: list[SegmentPosition] = []

    def serialize(self) -> ET.Element:
        """Serialize MultiplexedPart to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "SEGMENT-POSITIONS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.segment_positions.append(SerializationHelper.deserialize_by_tag(item_elem, "SegmentPosition"))

        return obj



class MultiplexedPartBuilder(BuilderBase, ABC):
    """Builder for MultiplexedPart with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: MultiplexedPart = MultiplexedPart()


    def with_segment_positions(self, items: list[SegmentPosition]) -> "MultiplexedPartBuilder":
        """Set segment_positions list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.segment_positions = list(items) if items else []
        return self


    def add_segment_position(self, item: SegmentPosition) -> "MultiplexedPartBuilder":
        """Add a single item to segment_positions list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.segment_positions.append(item)
        return self

    def clear_segment_positions(self) -> "MultiplexedPartBuilder":
        """Clear all items from segment_positions list.

        Returns:
            self for method chaining
        """
        self._obj.segment_positions = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "segmentPosition",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    @abstractmethod
    def build(self) -> MultiplexedPart:
        """Build and return the MultiplexedPart instance (abstract)."""
        raise NotImplementedError