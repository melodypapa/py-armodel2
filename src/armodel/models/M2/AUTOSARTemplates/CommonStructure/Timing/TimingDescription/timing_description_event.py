"""TimingDescriptionEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 253)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description import (
    TimingDescription,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingClock.timing_clock import (
    TimingClock,
)
from abc import ABC, abstractmethod


class TimingDescriptionEvent(TimingDescription, ABC):
    """AUTOSAR TimingDescriptionEvent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    clock_reference: Optional[TimingClock]
    occurrence: Optional[Any]
    def __init__(self) -> None:
        """Initialize TimingDescriptionEvent."""
        super().__init__()
        self.clock_reference: Optional[TimingClock] = None
        self.occurrence: Optional[Any] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "TimingDescriptionEvent":
        """Deserialize XML element to TimingDescriptionEvent object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TimingDescriptionEvent object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TimingDescriptionEvent, cls).deserialize(element)

        # Parse clock_reference
        child = ARObject._find_child_element(element, "CLOCK-REFERENCE")
        if child is not None:
            clock_reference_value = ARObject._deserialize_by_tag(child, "TimingClock")
            obj.clock_reference = clock_reference_value

        # Parse occurrence
        child = ARObject._find_child_element(element, "OCCURRENCE")
        if child is not None:
            occurrence_value = child.text
            obj.occurrence = occurrence_value

        return obj



class TimingDescriptionEventBuilder:
    """Builder for TimingDescriptionEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TimingDescriptionEvent = TimingDescriptionEvent()

    def build(self) -> TimingDescriptionEvent:
        """Build and return TimingDescriptionEvent object.

        Returns:
            TimingDescriptionEvent instance
        """
        # TODO: Add validation
        return self._obj
