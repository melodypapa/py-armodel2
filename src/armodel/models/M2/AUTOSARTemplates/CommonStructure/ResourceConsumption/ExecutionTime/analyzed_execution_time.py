"""AnalyzedExecutionTime AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 164)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ResourceConsumption_ExecutionTime.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.ExecutionTime.execution_time import (
    ExecutionTime,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)


class AnalyzedExecutionTime(ExecutionTime):
    """AUTOSAR AnalyzedExecutionTime."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    best_case: Optional[MultidimensionalTime]
    worst_case: Optional[MultidimensionalTime]
    def __init__(self) -> None:
        """Initialize AnalyzedExecutionTime."""
        super().__init__()
        self.best_case: Optional[MultidimensionalTime] = None
        self.worst_case: Optional[MultidimensionalTime] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "AnalyzedExecutionTime":
        """Deserialize XML element to AnalyzedExecutionTime object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AnalyzedExecutionTime object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AnalyzedExecutionTime, cls).deserialize(element)

        # Parse best_case
        child = ARObject._find_child_element(element, "BEST-CASE")
        if child is not None:
            best_case_value = ARObject._deserialize_by_tag(child, "MultidimensionalTime")
            obj.best_case = best_case_value

        # Parse worst_case
        child = ARObject._find_child_element(element, "WORST-CASE")
        if child is not None:
            worst_case_value = ARObject._deserialize_by_tag(child, "MultidimensionalTime")
            obj.worst_case = worst_case_value

        return obj



class AnalyzedExecutionTimeBuilder:
    """Builder for AnalyzedExecutionTime."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AnalyzedExecutionTime = AnalyzedExecutionTime()

    def build(self) -> AnalyzedExecutionTime:
        """Build and return AnalyzedExecutionTime object.

        Returns:
            AnalyzedExecutionTime instance
        """
        # TODO: Add validation
        return self._obj
