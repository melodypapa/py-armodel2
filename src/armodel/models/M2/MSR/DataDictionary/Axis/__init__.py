"""Axis module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.MSR.DataDictionary.Axis.sw_axis_individual import (
        SwAxisIndividual,
    )
    from armodel.models.M2.MSR.DataDictionary.Axis.sw_axis_generic import (
        SwAxisGeneric,
    )
    from armodel.models.M2.MSR.DataDictionary.Axis.sw_axis_type import (
        SwAxisType,
    )
    from armodel.models.M2.MSR.DataDictionary.Axis.sw_generic_axis_param import (
        SwGenericAxisParam,
    )
    from armodel.models.M2.MSR.DataDictionary.Axis.sw_generic_axis_param_type import (
        SwGenericAxisParamType,
    )
    from armodel.models.M2.MSR.DataDictionary.Axis.sw_axis_grouped import (
        SwAxisGrouped,
    )

__all__ = [
    "SwAxisGeneric",
    "SwAxisGrouped",
    "SwAxisIndividual",
    "SwAxisType",
    "SwGenericAxisParam",
    "SwGenericAxisParamType",
]
