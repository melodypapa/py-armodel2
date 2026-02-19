"""TimingDescriptionEventChain AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 40)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description import (
    TimingDescription,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description_event import (
    TimingDescriptionEvent,
)


class TimingDescriptionEventChain(TimingDescription):
    """AUTOSAR TimingDescriptionEventChain."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    is_pipelining: Optional[Boolean]
    response: Optional[TimingDescriptionEvent]
    segments: list[TimingDescriptionEvent]
    stimulus: Optional[TimingDescriptionEvent]
    def __init__(self) -> None:
        """Initialize TimingDescriptionEventChain."""
        super().__init__()
        self.is_pipelining: Optional[Boolean] = None
        self.response: Optional[TimingDescriptionEvent] = None
        self.segments: list[TimingDescriptionEvent] = []
        self.stimulus: Optional[TimingDescriptionEvent] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "TimingDescriptionEventChain":
        """Deserialize XML element to TimingDescriptionEventChain object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TimingDescriptionEventChain object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse is_pipelining
        child = ARObject._find_child_element(element, "IS-PIPELINING")
        if child is not None:
            is_pipelining_value = child.text
            obj.is_pipelining = is_pipelining_value

        # Parse response
        child = ARObject._find_child_element(element, "RESPONSE")
        if child is not None:
            response_value = ARObject._deserialize_by_tag(child, "TimingDescriptionEvent")
            obj.response = response_value

        # Parse segments (list)
        obj.segments = []
        for child in ARObject._find_all_child_elements(element, "SEGMENTS"):
            segments_value = ARObject._deserialize_by_tag(child, "TimingDescriptionEvent")
            obj.segments.append(segments_value)

        # Parse stimulus
        child = ARObject._find_child_element(element, "STIMULUS")
        if child is not None:
            stimulus_value = ARObject._deserialize_by_tag(child, "TimingDescriptionEvent")
            obj.stimulus = stimulus_value

        return obj



class TimingDescriptionEventChainBuilder:
    """Builder for TimingDescriptionEventChain."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TimingDescriptionEventChain = TimingDescriptionEventChain()

    def build(self) -> TimingDescriptionEventChain:
        """Build and return TimingDescriptionEventChain object.

        Returns:
            TimingDescriptionEventChain instance
        """
        # TODO: Add validation
        return self._obj
