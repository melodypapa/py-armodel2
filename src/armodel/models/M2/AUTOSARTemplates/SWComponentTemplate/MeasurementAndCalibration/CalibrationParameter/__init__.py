"""CalibrationParameter module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.MeasurementAndCalibration.CalibrationParameter.calibration_parameter_value_set import (
        CalibrationParameterValueSet,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.MeasurementAndCalibration.CalibrationParameter.calibration_parameter_value import (
        CalibrationParameterValue,
    )

__all__ = [
    "CalibrationParameterValue",
    "CalibrationParameterValueSet",
]
