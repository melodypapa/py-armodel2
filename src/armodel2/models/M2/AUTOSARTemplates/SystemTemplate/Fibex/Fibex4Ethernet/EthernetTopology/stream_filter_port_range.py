"""StreamFilterPortRange AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 139)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class StreamFilterPortRange(ARObject):
    """AUTOSAR StreamFilterPortRange."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "STREAM-FILTER-PORT-RANGE"


    max: Optional[PositiveInteger]
    min: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "MAX": lambda obj, elem: setattr(obj, "max", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "MIN": lambda obj, elem: setattr(obj, "min", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize StreamFilterPortRange."""
        super().__init__()
        self.max: Optional[PositiveInteger] = None
        self.min: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize StreamFilterPortRange to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(StreamFilterPortRange, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize max
        if self.max is not None:
            serialized = SerializationHelper.serialize_item(self.max, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize min
        if self.min is not None:
            serialized = SerializationHelper.serialize_item(self.min, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MIN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "StreamFilterPortRange":
        """Deserialize XML element to StreamFilterPortRange object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized StreamFilterPortRange object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(StreamFilterPortRange, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "MAX":
                setattr(obj, "max", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "MIN":
                setattr(obj, "min", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class StreamFilterPortRangeBuilder(BuilderBase):
    """Builder for StreamFilterPortRange with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: StreamFilterPortRange = StreamFilterPortRange()


    def with_max(self, value: Optional[PositiveInteger]) -> "StreamFilterPortRangeBuilder":
        """Set max attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'max' is required and cannot be None")
        self._obj.max = value
        return self

    def with_min(self, value: Optional[PositiveInteger]) -> "StreamFilterPortRangeBuilder":
        """Set min attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'min' is required and cannot be None")
        self._obj.min = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "max",
        "min",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> StreamFilterPortRange:
        """Build and return the StreamFilterPortRange instance with validation."""
        self._validate_instance()
        return self._obj