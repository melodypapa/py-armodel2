"""TimeRangeType AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 398)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication_Timing.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class TimeRangeType(ARObject):
    """AUTOSAR TimeRangeType."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    tolerance_tolerance: Optional[TimeRangeType]
    value: Optional[TimeValue]
    def __init__(self) -> None:
        """Initialize TimeRangeType."""
        super().__init__()
        self.tolerance_tolerance: Optional[TimeRangeType] = None
        self.value: Optional[TimeValue] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "TimeRangeType":
        """Deserialize XML element to TimeRangeType object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TimeRangeType object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse tolerance_tolerance
        child = ARObject._find_child_element(element, "TOLERANCE-TOLERANCE")
        if child is not None:
            tolerance_tolerance_value = ARObject._deserialize_by_tag(child, "TimeRangeType")
            obj.tolerance_tolerance = tolerance_tolerance_value

        # Parse value
        child = ARObject._find_child_element(element, "VALUE")
        if child is not None:
            value_value = child.text
            obj.value = value_value

        return obj



class TimeRangeTypeBuilder:
    """Builder for TimeRangeType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TimeRangeType = TimeRangeType()

    def build(self) -> TimeRangeType:
        """Build and return TimeRangeType object.

        Returns:
            TimeRangeType instance
        """
        # TODO: Add validation
        return self._obj
