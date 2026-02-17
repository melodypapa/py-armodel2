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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)


class RoughEstimateOfExecutionTime(ExecutionTime):
    """AUTOSAR RoughEstimateOfExecutionTime."""

    additional: Optional[String]
    estimated_execution_time: Optional[MultidimensionalTime]
    def __init__(self) -> None:
        """Initialize RoughEstimateOfExecutionTime."""
        super().__init__()
        self.additional: Optional[String] = None
        self.estimated_execution_time: Optional[MultidimensionalTime] = None


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
