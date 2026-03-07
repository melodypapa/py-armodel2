"""CyclicTiming AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 396)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication_Timing.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.describable import (
    Describable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.describable import DescribableBuilder
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.Timing.time_range_type import (
    TimeRangeType,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class CyclicTiming(Describable):
    """AUTOSAR CyclicTiming."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "CYCLIC-TIMING"


    time_offset: Optional[TimeRangeType]
    time_period: Optional[TimeRangeType]
    _DESERIALIZE_DISPATCH = {
        "TIME-OFFSET": lambda obj, elem: setattr(obj, "time_offset", SerializationHelper.deserialize_by_tag(elem, "TimeRangeType")),
        "TIME-PERIOD": lambda obj, elem: setattr(obj, "time_period", SerializationHelper.deserialize_by_tag(elem, "TimeRangeType")),
    }


    def __init__(self) -> None:
        """Initialize CyclicTiming."""
        super().__init__()
        self.time_offset: Optional[TimeRangeType] = None
        self.time_period: Optional[TimeRangeType] = None

    def serialize(self) -> ET.Element:
        """Serialize CyclicTiming to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CyclicTiming, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize time_offset
        if self.time_offset is not None:
            serialized = SerializationHelper.serialize_item(self.time_offset, "TimeRangeType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIME-OFFSET")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize time_period
        if self.time_period is not None:
            serialized = SerializationHelper.serialize_item(self.time_period, "TimeRangeType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIME-PERIOD")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CyclicTiming":
        """Deserialize XML element to CyclicTiming object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CyclicTiming object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CyclicTiming, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "TIME-OFFSET":
                setattr(obj, "time_offset", SerializationHelper.deserialize_by_tag(child, "TimeRangeType"))
            elif tag == "TIME-PERIOD":
                setattr(obj, "time_period", SerializationHelper.deserialize_by_tag(child, "TimeRangeType"))

        return obj



class CyclicTimingBuilder(DescribableBuilder):
    """Builder for CyclicTiming with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: CyclicTiming = CyclicTiming()


    def with_time_offset(self, value: Optional[TimeRangeType]) -> "CyclicTimingBuilder":
        """Set time_offset attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'time_offset' is required and cannot be None")
        self._obj.time_offset = value
        return self

    def with_time_period(self, value: Optional[TimeRangeType]) -> "CyclicTimingBuilder":
        """Set time_period attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'time_period' is required and cannot be None")
        self._obj.time_period = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "timeOffset",
        "timePeriod",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> CyclicTiming:
        """Build and return the CyclicTiming instance with validation."""
        self._validate_instance()
        return self._obj