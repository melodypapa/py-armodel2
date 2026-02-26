"""ExecutionTime module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.ExecutionTime.execution_time import (
        ExecutionTime,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.ExecutionTime.memory_section_location import (
        MemorySectionLocation,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.ExecutionTime.analyzed_execution_time import (
        AnalyzedExecutionTime,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.ExecutionTime.measured_execution_time import (
        MeasuredExecutionTime,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.ExecutionTime.simulated_execution_time import (
        SimulatedExecutionTime,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.ExecutionTime.rough_estimate_of_execution_time import (
        RoughEstimateOfExecutionTime,
    )

__all__ = [
    "AnalyzedExecutionTime",
    "ExecutionTime",
    "MeasuredExecutionTime",
    "MemorySectionLocation",
    "RoughEstimateOfExecutionTime",
    "SimulatedExecutionTime",
]
