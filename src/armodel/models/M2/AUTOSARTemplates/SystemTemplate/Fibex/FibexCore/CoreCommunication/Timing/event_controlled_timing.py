"""EventControlledTiming AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 397)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication_Timing.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.describable import (
    Describable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.Timing.time_range_type import (
    TimeRangeType,
)


class EventControlledTiming(Describable):
    """AUTOSAR EventControlledTiming."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    number_of: Optional[Integer]
    repetition_period: Optional[TimeRangeType]
    def __init__(self) -> None:
        """Initialize EventControlledTiming."""
        super().__init__()
        self.number_of: Optional[Integer] = None
        self.repetition_period: Optional[TimeRangeType] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "EventControlledTiming":
        """Deserialize XML element to EventControlledTiming object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EventControlledTiming object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EventControlledTiming, cls).deserialize(element)

        # Parse number_of
        child = ARObject._find_child_element(element, "NUMBER-OF")
        if child is not None:
            number_of_value = child.text
            obj.number_of = number_of_value

        # Parse repetition_period
        child = ARObject._find_child_element(element, "REPETITION-PERIOD")
        if child is not None:
            repetition_period_value = ARObject._deserialize_by_tag(child, "TimeRangeType")
            obj.repetition_period = repetition_period_value

        return obj



class EventControlledTimingBuilder:
    """Builder for EventControlledTiming."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EventControlledTiming = EventControlledTiming()

    def build(self) -> EventControlledTiming:
        """Build and return EventControlledTiming object.

        Returns:
            EventControlledTiming instance
        """
        # TODO: Add validation
        return self._obj
