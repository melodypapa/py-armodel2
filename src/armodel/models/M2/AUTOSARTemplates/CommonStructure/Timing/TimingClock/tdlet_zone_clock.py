"""TDLETZoneClock AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 252)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingClock.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingClock.timing_clock import (
    TimingClock,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)


class TDLETZoneClock(TimingClock):
    """AUTOSAR TDLETZoneClock."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    accuracy_ext: Optional[MultidimensionalTime]
    accuracy_int: Optional[MultidimensionalTime]
    def __init__(self) -> None:
        """Initialize TDLETZoneClock."""
        super().__init__()
        self.accuracy_ext: Optional[MultidimensionalTime] = None
        self.accuracy_int: Optional[MultidimensionalTime] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDLETZoneClock":
        """Deserialize XML element to TDLETZoneClock object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TDLETZoneClock object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TDLETZoneClock, cls).deserialize(element)

        # Parse accuracy_ext
        child = ARObject._find_child_element(element, "ACCURACY-EXT")
        if child is not None:
            accuracy_ext_value = ARObject._deserialize_by_tag(child, "MultidimensionalTime")
            obj.accuracy_ext = accuracy_ext_value

        # Parse accuracy_int
        child = ARObject._find_child_element(element, "ACCURACY-INT")
        if child is not None:
            accuracy_int_value = ARObject._deserialize_by_tag(child, "MultidimensionalTime")
            obj.accuracy_int = accuracy_int_value

        return obj



class TDLETZoneClockBuilder:
    """Builder for TDLETZoneClock."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDLETZoneClock = TDLETZoneClock()

    def build(self) -> TDLETZoneClock:
        """Build and return TDLETZoneClock object.

        Returns:
            TDLETZoneClock instance
        """
        # TODO: Add validation
        return self._obj
