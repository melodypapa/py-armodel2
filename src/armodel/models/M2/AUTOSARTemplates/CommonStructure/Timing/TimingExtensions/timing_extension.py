"""TimingExtension AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 254)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingExtensions.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingClock.timing_clock import (
    TimingClock,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingClock.timing_clock_sync_accuracy import (
    TimingClockSyncAccuracy,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition.timing_condition import (
    TimingCondition,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.timing_constraint import (
    TimingConstraint,
)
from abc import ABC, abstractmethod


class TimingExtension(ARElement, ABC):
    """AUTOSAR TimingExtension."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    timing_clocks: list[TimingClock]
    timing_clock_syncs: list[TimingClockSyncAccuracy]
    timing_conditions: list[TimingCondition]
    timings: list[TimingConstraint]
    timing_resource: Optional[TimingExtension]
    def __init__(self) -> None:
        """Initialize TimingExtension."""
        super().__init__()
        self.timing_clocks: list[TimingClock] = []
        self.timing_clock_syncs: list[TimingClockSyncAccuracy] = []
        self.timing_conditions: list[TimingCondition] = []
        self.timings: list[TimingConstraint] = []
        self.timing_resource: Optional[TimingExtension] = None

    def serialize(self) -> ET.Element:
        """Serialize TimingExtension to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TimingExtension, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize timing_clocks (list to container "TIMING-CLOCKS")
        if self.timing_clocks:
            wrapper = ET.Element("TIMING-CLOCKS")
            for item in self.timing_clocks:
                serialized = SerializationHelper.serialize_item(item, "TimingClock")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize timing_clock_syncs (list to container "TIMING-CLOCK-SYNCS")
        if self.timing_clock_syncs:
            wrapper = ET.Element("TIMING-CLOCK-SYNCS")
            for item in self.timing_clock_syncs:
                serialized = SerializationHelper.serialize_item(item, "TimingClockSyncAccuracy")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize timing_conditions (list to container "TIMING-CONDITIONS")
        if self.timing_conditions:
            wrapper = ET.Element("TIMING-CONDITIONS")
            for item in self.timing_conditions:
                serialized = SerializationHelper.serialize_item(item, "TimingCondition")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize timings (list to container "TIMINGS")
        if self.timings:
            wrapper = ET.Element("TIMINGS")
            for item in self.timings:
                serialized = SerializationHelper.serialize_item(item, "TimingConstraint")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize timing_resource
        if self.timing_resource is not None:
            serialized = SerializationHelper.serialize_item(self.timing_resource, "TimingExtension")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIMING-RESOURCE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TimingExtension":
        """Deserialize XML element to TimingExtension object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TimingExtension object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TimingExtension, cls).deserialize(element)

        # Parse timing_clocks (list from container "TIMING-CLOCKS")
        obj.timing_clocks = []
        container = SerializationHelper.find_child_element(element, "TIMING-CLOCKS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.timing_clocks.append(child_value)

        # Parse timing_clock_syncs (list from container "TIMING-CLOCK-SYNCS")
        obj.timing_clock_syncs = []
        container = SerializationHelper.find_child_element(element, "TIMING-CLOCK-SYNCS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.timing_clock_syncs.append(child_value)

        # Parse timing_conditions (list from container "TIMING-CONDITIONS")
        obj.timing_conditions = []
        container = SerializationHelper.find_child_element(element, "TIMING-CONDITIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.timing_conditions.append(child_value)

        # Parse timings (list from container "TIMINGS")
        obj.timings = []
        container = SerializationHelper.find_child_element(element, "TIMINGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.timings.append(child_value)

        # Parse timing_resource
        child = SerializationHelper.find_child_element(element, "TIMING-RESOURCE")
        if child is not None:
            timing_resource_value = SerializationHelper.deserialize_by_tag(child, "TimingExtension")
            obj.timing_resource = timing_resource_value

        return obj



