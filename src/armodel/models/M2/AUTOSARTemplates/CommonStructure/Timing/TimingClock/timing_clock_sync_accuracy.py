"""TimingClockSyncAccuracy AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 252)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingClock.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingClock.timing_clock import (
    TimingClock,
)


class TimingClockSyncAccuracy(Identifiable):
    """AUTOSAR TimingClockSyncAccuracy."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    accuracy: Optional[MultidimensionalTime]
    lower: Optional[TimingClock]
    upper: Optional[TimingClock]
    def __init__(self) -> None:
        """Initialize TimingClockSyncAccuracy."""
        super().__init__()
        self.accuracy: Optional[MultidimensionalTime] = None
        self.lower: Optional[TimingClock] = None
        self.upper: Optional[TimingClock] = None
    def serialize(self) -> ET.Element:
        """Serialize TimingClockSyncAccuracy to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TimingClockSyncAccuracy, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize accuracy
        if self.accuracy is not None:
            serialized = ARObject._serialize_item(self.accuracy, "MultidimensionalTime")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ACCURACY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize lower
        if self.lower is not None:
            serialized = ARObject._serialize_item(self.lower, "TimingClock")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LOWER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize upper
        if self.upper is not None:
            serialized = ARObject._serialize_item(self.upper, "TimingClock")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("UPPER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TimingClockSyncAccuracy":
        """Deserialize XML element to TimingClockSyncAccuracy object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TimingClockSyncAccuracy object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TimingClockSyncAccuracy, cls).deserialize(element)

        # Parse accuracy
        child = ARObject._find_child_element(element, "ACCURACY")
        if child is not None:
            accuracy_value = ARObject._deserialize_by_tag(child, "MultidimensionalTime")
            obj.accuracy = accuracy_value

        # Parse lower
        child = ARObject._find_child_element(element, "LOWER")
        if child is not None:
            lower_value = ARObject._deserialize_by_tag(child, "TimingClock")
            obj.lower = lower_value

        # Parse upper
        child = ARObject._find_child_element(element, "UPPER")
        if child is not None:
            upper_value = ARObject._deserialize_by_tag(child, "TimingClock")
            obj.upper = upper_value

        return obj



class TimingClockSyncAccuracyBuilder:
    """Builder for TimingClockSyncAccuracy."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TimingClockSyncAccuracy = TimingClockSyncAccuracy()

    def build(self) -> TimingClockSyncAccuracy:
        """Build and return TimingClockSyncAccuracy object.

        Returns:
            TimingClockSyncAccuracy instance
        """
        # TODO: Add validation
        return self._obj
