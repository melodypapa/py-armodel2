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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)


class MeasuredExecutionTime(ExecutionTime):
    """AUTOSAR MeasuredExecutionTime."""

    def __init__(self) -> None:
        """Initialize MeasuredExecutionTime."""
        super().__init__()
        self.maximum_execution_time: Optional[MultidimensionalTime] = None
        self.minimum_execution_time: Optional[MultidimensionalTime] = None
        self.nominal_execution_time: Optional[MultidimensionalTime] = None


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
