"""SporadicEventTriggering AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 105)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingConstraint_EventTriggeringConstraint.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.EventTriggeringConstraint.event_triggering_constraint import (
    EventTriggeringConstraint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)


class SporadicEventTriggering(EventTriggeringConstraint):
    """AUTOSAR SporadicEventTriggering."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    jitter: Optional[MultidimensionalTime]
    maximum_inter: Optional[MultidimensionalTime]
    minimum_inter: Optional[MultidimensionalTime]
    period: Optional[MultidimensionalTime]
    def __init__(self) -> None:
        """Initialize SporadicEventTriggering."""
        super().__init__()
        self.jitter: Optional[MultidimensionalTime] = None
        self.maximum_inter: Optional[MultidimensionalTime] = None
        self.minimum_inter: Optional[MultidimensionalTime] = None
        self.period: Optional[MultidimensionalTime] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SporadicEventTriggering":
        """Deserialize XML element to SporadicEventTriggering object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SporadicEventTriggering object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse jitter
        child = ARObject._find_child_element(element, "JITTER")
        if child is not None:
            jitter_value = ARObject._deserialize_by_tag(child, "MultidimensionalTime")
            obj.jitter = jitter_value

        # Parse maximum_inter
        child = ARObject._find_child_element(element, "MAXIMUM-INTER")
        if child is not None:
            maximum_inter_value = ARObject._deserialize_by_tag(child, "MultidimensionalTime")
            obj.maximum_inter = maximum_inter_value

        # Parse minimum_inter
        child = ARObject._find_child_element(element, "MINIMUM-INTER")
        if child is not None:
            minimum_inter_value = ARObject._deserialize_by_tag(child, "MultidimensionalTime")
            obj.minimum_inter = minimum_inter_value

        # Parse period
        child = ARObject._find_child_element(element, "PERIOD")
        if child is not None:
            period_value = ARObject._deserialize_by_tag(child, "MultidimensionalTime")
            obj.period = period_value

        return obj



class SporadicEventTriggeringBuilder:
    """Builder for SporadicEventTriggering."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SporadicEventTriggering = SporadicEventTriggering()

    def build(self) -> SporadicEventTriggering:
        """Build and return SporadicEventTriggering object.

        Returns:
            SporadicEventTriggering instance
        """
        # TODO: Add validation
        return self._obj
