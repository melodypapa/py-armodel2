"""RoughEstimateOfExecutionTime AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 167)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ResourceConsumption_ExecutionTime.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.ExecutionTime.execution_time import (
    ExecutionTime,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)


class RoughEstimateOfExecutionTime(ExecutionTime):
    """AUTOSAR RoughEstimateOfExecutionTime."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    additional: Optional[String]
    estimated_execution_time: Optional[MultidimensionalTime]
    def __init__(self) -> None:
        """Initialize RoughEstimateOfExecutionTime."""
        super().__init__()
        self.additional: Optional[String] = None
        self.estimated_execution_time: Optional[MultidimensionalTime] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "RoughEstimateOfExecutionTime":
        """Deserialize XML element to RoughEstimateOfExecutionTime object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RoughEstimateOfExecutionTime object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse additional
        child = ARObject._find_child_element(element, "ADDITIONAL")
        if child is not None:
            additional_value = child.text
            obj.additional = additional_value

        # Parse estimated_execution_time
        child = ARObject._find_child_element(element, "ESTIMATED-EXECUTION-TIME")
        if child is not None:
            estimated_execution_time_value = ARObject._deserialize_by_tag(child, "MultidimensionalTime")
            obj.estimated_execution_time = estimated_execution_time_value

        return obj



class RoughEstimateOfExecutionTimeBuilder:
    """Builder for RoughEstimateOfExecutionTime."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RoughEstimateOfExecutionTime = RoughEstimateOfExecutionTime()

    def build(self) -> RoughEstimateOfExecutionTime:
        """Build and return RoughEstimateOfExecutionTime object.

        Returns:
            RoughEstimateOfExecutionTime instance
        """
        # TODO: Add validation
        return self._obj
