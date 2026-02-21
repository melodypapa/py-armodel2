"""ArbitraryEventTriggering AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 111)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingConstraint_EventTriggeringConstraint.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.EventTriggeringConstraint.event_triggering_constraint import (
    EventTriggeringConstraint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.EventTriggeringConstraint.confidence_interval import (
    ConfidenceInterval,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)


class ArbitraryEventTriggering(EventTriggeringConstraint):
    """AUTOSAR ArbitraryEventTriggering."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    confidence_intervals: list[ConfidenceInterval]
    maximums: list[MultidimensionalTime]
    minimums: list[MultidimensionalTime]
    def __init__(self) -> None:
        """Initialize ArbitraryEventTriggering."""
        super().__init__()
        self.confidence_intervals: list[ConfidenceInterval] = []
        self.maximums: list[MultidimensionalTime] = []
        self.minimums: list[MultidimensionalTime] = []

    def serialize(self) -> ET.Element:
        """Serialize ArbitraryEventTriggering to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ArbitraryEventTriggering, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize confidence_intervals (list to container "CONFIDENCE-INTERVALS")
        if self.confidence_intervals:
            wrapper = ET.Element("CONFIDENCE-INTERVALS")
            for item in self.confidence_intervals:
                serialized = SerializationHelper.serialize_item(item, "ConfidenceInterval")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize maximums (list to container "MAXIMUMS")
        if self.maximums:
            wrapper = ET.Element("MAXIMUMS")
            for item in self.maximums:
                serialized = SerializationHelper.serialize_item(item, "MultidimensionalTime")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize minimums (list to container "MINIMUMS")
        if self.minimums:
            wrapper = ET.Element("MINIMUMS")
            for item in self.minimums:
                serialized = SerializationHelper.serialize_item(item, "MultidimensionalTime")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ArbitraryEventTriggering":
        """Deserialize XML element to ArbitraryEventTriggering object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ArbitraryEventTriggering object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ArbitraryEventTriggering, cls).deserialize(element)

        # Parse confidence_intervals (list from container "CONFIDENCE-INTERVALS")
        obj.confidence_intervals = []
        container = SerializationHelper.find_child_element(element, "CONFIDENCE-INTERVALS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.confidence_intervals.append(child_value)

        # Parse maximums (list from container "MAXIMUMS")
        obj.maximums = []
        container = SerializationHelper.find_child_element(element, "MAXIMUMS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.maximums.append(child_value)

        # Parse minimums (list from container "MINIMUMS")
        obj.minimums = []
        container = SerializationHelper.find_child_element(element, "MINIMUMS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.minimums.append(child_value)

        return obj



class ArbitraryEventTriggeringBuilder:
    """Builder for ArbitraryEventTriggering."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ArbitraryEventTriggering = ArbitraryEventTriggering()

    def build(self) -> ArbitraryEventTriggering:
        """Build and return ArbitraryEventTriggering object.

        Returns:
            ArbitraryEventTriggering instance
        """
        # TODO: Add validation
        return self._obj
