"""InterpolationRoutine module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.MeasurementAndCalibration.InterpolationRoutine.interpolation_routine_mapping_set import (
        InterpolationRoutineMappingSet,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.MeasurementAndCalibration.InterpolationRoutine.interpolation_routine_mapping import (
        InterpolationRoutineMapping,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.MeasurementAndCalibration.InterpolationRoutine.interpolation_routine import (
        InterpolationRoutine,
    )

__all__ = [
    "InterpolationRoutine",
    "InterpolationRoutineMapping",
    "InterpolationRoutineMappingSet",
]
