"""MeasuredExecutionTime AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 166)

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


class MeasuredExecutionTime(ExecutionTime):
    """AUTOSAR MeasuredExecutionTime."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    maximum_execution_time: Optional[MultidimensionalTime]
    minimum_execution_time: Optional[MultidimensionalTime]
    nominal_execution_time: Optional[MultidimensionalTime]
    def __init__(self) -> None:
        """Initialize MeasuredExecutionTime."""
        super().__init__()
        self.maximum_execution_time: Optional[MultidimensionalTime] = None
        self.minimum_execution_time: Optional[MultidimensionalTime] = None
        self.nominal_execution_time: Optional[MultidimensionalTime] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "MeasuredExecutionTime":
        """Deserialize XML element to MeasuredExecutionTime object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MeasuredExecutionTime object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse maximum_execution_time
        child = ARObject._find_child_element(element, "MAXIMUM-EXECUTION-TIME")
        if child is not None:
            maximum_execution_time_value = ARObject._deserialize_by_tag(child, "MultidimensionalTime")
            obj.maximum_execution_time = maximum_execution_time_value

        # Parse minimum_execution_time
        child = ARObject._find_child_element(element, "MINIMUM-EXECUTION-TIME")
        if child is not None:
            minimum_execution_time_value = ARObject._deserialize_by_tag(child, "MultidimensionalTime")
            obj.minimum_execution_time = minimum_execution_time_value

        # Parse nominal_execution_time
        child = ARObject._find_child_element(element, "NOMINAL-EXECUTION-TIME")
        if child is not None:
            nominal_execution_time_value = ARObject._deserialize_by_tag(child, "MultidimensionalTime")
            obj.nominal_execution_time = nominal_execution_time_value

        return obj



class MeasuredExecutionTimeBuilder:
    """Builder for MeasuredExecutionTime."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MeasuredExecutionTime = MeasuredExecutionTime()

    def build(self) -> MeasuredExecutionTime:
        """Build and return MeasuredExecutionTime object.

        Returns:
            MeasuredExecutionTime instance
        """
        # TODO: Add validation
        return self._obj
