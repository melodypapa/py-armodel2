"""SimulatedExecutionTime AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 167)

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


class SimulatedExecutionTime(ExecutionTime):
    """AUTOSAR SimulatedExecutionTime."""

    maximum_execution_time: Optional[MultidimensionalTime]
    minimum_execution_time: Optional[MultidimensionalTime]
    nominal_execution_time: Optional[MultidimensionalTime]
    def __init__(self) -> None:
        """Initialize SimulatedExecutionTime."""
        super().__init__()
        self.maximum_execution_time: Optional[MultidimensionalTime] = None
        self.minimum_execution_time: Optional[MultidimensionalTime] = None
        self.nominal_execution_time: Optional[MultidimensionalTime] = None


class SimulatedExecutionTimeBuilder:
    """Builder for SimulatedExecutionTime."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SimulatedExecutionTime = SimulatedExecutionTime()

    def build(self) -> SimulatedExecutionTime:
        """Build and return SimulatedExecutionTime object.

        Returns:
            SimulatedExecutionTime instance
        """
        # TODO: Add validation
        return self._obj
