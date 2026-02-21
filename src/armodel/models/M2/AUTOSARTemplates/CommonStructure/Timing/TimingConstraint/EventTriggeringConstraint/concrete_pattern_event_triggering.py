"""ConcretePatternEventTriggering AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 106)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingConstraint_EventTriggeringConstraint.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.EventTriggeringConstraint.event_triggering_constraint import (
    EventTriggeringConstraint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)


class ConcretePatternEventTriggering(EventTriggeringConstraint):
    """AUTOSAR ConcretePatternEventTriggering."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    offsets: list[MultidimensionalTime]
    pattern_jitter: Optional[MultidimensionalTime]
    pattern_length: Optional[MultidimensionalTime]
    pattern_period: Optional[MultidimensionalTime]
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
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

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

        # Parse offsets (list from container "OFFSETS")
        obj.offsets = []
        container = SerializationHelper.find_child_element(element, "OFFSETS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.offsets.append(child_value)

        # Parse pattern_jitter
        child = SerializationHelper.find_child_element(element, "PATTERN-JITTER")
        if child is not None:
            pattern_jitter_value = SerializationHelper.deserialize_by_tag(child, "MultidimensionalTime")
            obj.pattern_jitter = pattern_jitter_value

        # Parse pattern_length
        child = SerializationHelper.find_child_element(element, "PATTERN-LENGTH")
        if child is not None:
            pattern_length_value = SerializationHelper.deserialize_by_tag(child, "MultidimensionalTime")
            obj.pattern_length = pattern_length_value

        # Parse pattern_period
        child = SerializationHelper.find_child_element(element, "PATTERN-PERIOD")
        if child is not None:
            pattern_period_value = SerializationHelper.deserialize_by_tag(child, "MultidimensionalTime")
            obj.pattern_period = pattern_period_value

        return obj



class ConcretePatternEventTriggeringBuilder:
    """Builder for ConcretePatternEventTriggering."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ConcretePatternEventTriggering = ConcretePatternEventTriggering()

    def build(self) -> ConcretePatternEventTriggering:
        """Build and return ConcretePatternEventTriggering object.

        Returns:
            ConcretePatternEventTriggering instance
        """
        # TODO: Add validation
        return self._obj
