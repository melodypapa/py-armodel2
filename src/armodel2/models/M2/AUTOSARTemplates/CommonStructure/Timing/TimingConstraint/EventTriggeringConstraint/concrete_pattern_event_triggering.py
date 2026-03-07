"""ConcretePatternEventTriggering AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 106)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingConstraint_EventTriggeringConstraint.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.EventTriggeringConstraint.event_triggering_constraint import (
    EventTriggeringConstraint,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.EventTriggeringConstraint.event_triggering_constraint import EventTriggeringConstraintBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ConcretePatternEventTriggering(EventTriggeringConstraint):
    """AUTOSAR ConcretePatternEventTriggering."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "CONCRETE-PATTERN-EVENT-TRIGGERING"


    offsets: list[MultidimensionalTime]
    pattern_jitter: Optional[MultidimensionalTime]
    pattern_length: Optional[MultidimensionalTime]
    pattern_period: Optional[MultidimensionalTime]
    _DESERIALIZE_DISPATCH = {
        "OFFSETS": lambda obj, elem: obj.offsets.append(SerializationHelper.deserialize_by_tag(elem, "MultidimensionalTime")),
        "PATTERN-JITTER": lambda obj, elem: setattr(obj, "pattern_jitter", SerializationHelper.deserialize_by_tag(elem, "MultidimensionalTime")),
        "PATTERN-LENGTH": lambda obj, elem: setattr(obj, "pattern_length", SerializationHelper.deserialize_by_tag(elem, "MultidimensionalTime")),
        "PATTERN-PERIOD": lambda obj, elem: setattr(obj, "pattern_period", SerializationHelper.deserialize_by_tag(elem, "MultidimensionalTime")),
    }


    def __init__(self) -> None:
        """Initialize ConcretePatternEventTriggering."""
        super().__init__()
        self.offsets: list[MultidimensionalTime] = []
        self.pattern_jitter: Optional[MultidimensionalTime] = None
        self.pattern_length: Optional[MultidimensionalTime] = None
        self.pattern_period: Optional[MultidimensionalTime] = None

    def serialize(self) -> ET.Element:
        """Serialize ConcretePatternEventTriggering to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ConcretePatternEventTriggering, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize offsets (list to container "OFFSETS")
        if self.offsets:
            wrapper = ET.Element("OFFSETS")
            for item in self.offsets:
                serialized = SerializationHelper.serialize_item(item, "MultidimensionalTime")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize pattern_jitter
        if self.pattern_jitter is not None:
            serialized = SerializationHelper.serialize_item(self.pattern_jitter, "MultidimensionalTime")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PATTERN-JITTER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize pattern_length
        if self.pattern_length is not None:
            serialized = SerializationHelper.serialize_item(self.pattern_length, "MultidimensionalTime")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PATTERN-LENGTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize pattern_period
        if self.pattern_period is not None:
            serialized = SerializationHelper.serialize_item(self.pattern_period, "MultidimensionalTime")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PATTERN-PERIOD")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ConcretePatternEventTriggering":
        """Deserialize XML element to ConcretePatternEventTriggering object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ConcretePatternEventTriggering object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ConcretePatternEventTriggering, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "OFFSETS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.offsets.append(SerializationHelper.deserialize_by_tag(item_elem, "MultidimensionalTime"))
            elif tag == "PATTERN-JITTER":
                setattr(obj, "pattern_jitter", SerializationHelper.deserialize_by_tag(child, "MultidimensionalTime"))
            elif tag == "PATTERN-LENGTH":
                setattr(obj, "pattern_length", SerializationHelper.deserialize_by_tag(child, "MultidimensionalTime"))
            elif tag == "PATTERN-PERIOD":
                setattr(obj, "pattern_period", SerializationHelper.deserialize_by_tag(child, "MultidimensionalTime"))

        return obj



class ConcretePatternEventTriggeringBuilder(EventTriggeringConstraintBuilder):
    """Builder for ConcretePatternEventTriggering with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ConcretePatternEventTriggering = ConcretePatternEventTriggering()


    def with_offsets(self, items: list[MultidimensionalTime]) -> "ConcretePatternEventTriggeringBuilder":
        """Set offsets list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.offsets = list(items) if items else []
        return self

    def with_pattern_jitter(self, value: Optional[MultidimensionalTime]) -> "ConcretePatternEventTriggeringBuilder":
        """Set pattern_jitter attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'pattern_jitter' is required and cannot be None")
        self._obj.pattern_jitter = value
        return self

    def with_pattern_length(self, value: Optional[MultidimensionalTime]) -> "ConcretePatternEventTriggeringBuilder":
        """Set pattern_length attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'pattern_length' is required and cannot be None")
        self._obj.pattern_length = value
        return self

    def with_pattern_period(self, value: Optional[MultidimensionalTime]) -> "ConcretePatternEventTriggeringBuilder":
        """Set pattern_period attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'pattern_period' is required and cannot be None")
        self._obj.pattern_period = value
        return self


    def add_offset(self, item: MultidimensionalTime) -> "ConcretePatternEventTriggeringBuilder":
        """Add a single item to offsets list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.offsets.append(item)
        return self

    def clear_offsets(self) -> "ConcretePatternEventTriggeringBuilder":
        """Clear all items from offsets list.

        Returns:
            self for method chaining
        """
        self._obj.offsets = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "offset",
        "patternJitter",
        "patternLength",
        "patternPeriod",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> ConcretePatternEventTriggering:
        """Build and return the ConcretePatternEventTriggering instance with validation."""
        self._validate_instance()
        return self._obj