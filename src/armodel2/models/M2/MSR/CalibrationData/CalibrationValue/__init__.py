"""CalibrationValue module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.MSR.CalibrationData.CalibrationValue.sw_value_cont import (
        SwValueCont,
    )
    from armodel2.models.M2.MSR.CalibrationData.CalibrationValue.sw_axis_cont import (
        SwAxisCont,
    )
    from armodel2.models.M2.MSR.CalibrationData.CalibrationValue.sw_values import (
        SwValues,
    )
    from armodel2.models.M2.MSR.CalibrationData.CalibrationValue.value_group import (
        ValueGroup,
    )

__all__ = [
    "SwAxisCont",
    "SwValueCont",
    "SwValues",
    "ValueGroup",
]
