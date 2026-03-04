"""TimeRangeType AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 398)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication_Timing.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class TimeRangeType(ARObject):
    """AUTOSAR TimeRangeType."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "TIME-RANGE-TYPE"


    tolerance: Optional[TimeRangeTypeTolerance]
    value: Optional[TimeValue]
    _DESERIALIZE_DISPATCH = {
        "TOLERANCE": lambda obj, elem: setattr(obj, "tolerance", SerializationHelper.deserialize_by_tag(elem, "TimeRangeTypeTolerance")),
        "VALUE": lambda obj, elem: setattr(obj, "value", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
    }


    def __init__(self) -> None:
        """Initialize TimeRangeType."""
        super().__init__()
        self.tolerance: Optional[TimeRangeTypeTolerance] = None
        self.value: Optional[TimeValue] = None

    def serialize(self) -> ET.Element:
        """Serialize TimeRangeType to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TimeRangeType, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize tolerance
        if self.tolerance is not None:
            serialized = SerializationHelper.serialize_item(self.tolerance, "TimeRangeTypeTolerance")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TOLERANCE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize value
        if self.value is not None:
            serialized = SerializationHelper.serialize_item(self.value, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VALUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TimeRangeType":
        """Deserialize XML element to TimeRangeType object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TimeRangeType object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TimeRangeType, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "TOLERANCE":
                setattr(obj, "tolerance", SerializationHelper.deserialize_by_tag(child, "TimeRangeTypeTolerance"))
            elif tag == "VALUE":
                setattr(obj, "value", SerializationHelper.deserialize_by_tag(child, "TimeValue"))

        return obj



class TimeRangeTypeBuilder(BuilderBase):
    """Builder for TimeRangeType with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TimeRangeType = TimeRangeType()


    def with_tolerance(self, value: Optional[TimeRangeTypeTolerance]) -> "TimeRangeTypeBuilder":
        """Set tolerance attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tolerance = value
        return self

    def with_value(self, value: Optional[TimeValue]) -> "TimeRangeTypeBuilder":
        """Set value attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.value = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "tolerance",
        "value",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> TimeRangeType:
        """Build and return the TimeRangeType instance with validation."""
        self._validate_instance()
        return self._obj