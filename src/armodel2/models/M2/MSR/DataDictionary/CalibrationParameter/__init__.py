"""CalibrationParameter module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.MSR.DataDictionary.CalibrationParameter.sw_calprm_axis_set import (
        SwCalprmAxisSet,
    )
    from armodel2.models.M2.MSR.DataDictionary.CalibrationParameter.sw_calprm_axis import (
        SwCalprmAxis,
    )
    from armodel2.models.M2.MSR.DataDictionary.CalibrationParameter.sw_calprm_axis_type_props import (
        SwCalprmAxisTypeProps,
    )

from armodel2.models.M2.MSR.DataDictionary.CalibrationParameter.calprm_axis_category_enum import (
    CalprmAxisCategoryEnum,
)

__all__ = [
    "CalprmAxisCategoryEnum",
    "SwCalprmAxis",
    "SwCalprmAxisSet",
    "SwCalprmAxisTypeProps",
]
