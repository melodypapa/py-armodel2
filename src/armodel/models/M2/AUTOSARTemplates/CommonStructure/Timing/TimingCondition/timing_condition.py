"""TimingCondition AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 35)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingCondition.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class TimingCondition(Identifiable):
    """AUTOSAR TimingCondition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    timing_condition: Optional[TimingCondition]
    def __init__(self) -> None:
        """Initialize TimingCondition."""
        super().__init__()
        self.timing_condition: Optional[TimingCondition] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "TimingCondition":
        """Deserialize XML element to TimingCondition object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TimingCondition object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse timing_condition
        child = ARObject._find_child_element(element, "TIMING-CONDITION")
        if child is not None:
            timing_condition_value = ARObject._deserialize_by_tag(child, "TimingCondition")
            obj.timing_condition = timing_condition_value

        return obj



class TimingConditionBuilder:
    """Builder for TimingCondition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TimingCondition = TimingCondition()

    def build(self) -> TimingCondition:
        """Build and return TimingCondition object.

        Returns:
            TimingCondition instance
        """
        # TODO: Add validation
        return self._obj
