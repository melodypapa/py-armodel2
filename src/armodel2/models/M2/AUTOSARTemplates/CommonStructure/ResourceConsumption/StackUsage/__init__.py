"""StackUsage module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.StackUsage.stack_usage import (
        StackUsage,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.StackUsage.worst_case_stack_usage import (
        WorstCaseStackUsage,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.StackUsage.measured_stack_usage import (
        MeasuredStackUsage,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.StackUsage.rough_estimate_stack_usage import (
        RoughEstimateStackUsage,
    )

__all__ = [
    "MeasuredStackUsage",
    "RoughEstimateStackUsage",
    "StackUsage",
    "WorstCaseStackUsage",
]
