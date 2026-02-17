"""DataDefProperties module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_pointer_target_props import (
        SwPointerTargetProps,
    )
    from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
        SwDataDefProps,
    )
    from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_text_props import (
        SwTextProps,
    )
    from armodel.models.M2.MSR.DataDictionary.DataDefProperties.value_list import (
        ValueList,
    )
    from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_bit_representation import (
        SwBitRepresentation,
    )
    from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_dependency import (
        SwDataDependency,
    )
    from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_dependency_args import (
        SwDataDependencyArgs,
    )

from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_calibration_access_enum import (
    SwCalibrationAccessEnum,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_impl_policy_enum import (
    SwImplPolicyEnum,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties.display_presentation_enum import (
    DisplayPresentationEnum,
)

__all__ = [
    "DisplayPresentationEnum",
    "SwBitRepresentation",
    "SwCalibrationAccessEnum",
    "SwDataDefProps",
    "SwDataDependency",
    "SwDataDependencyArgs",
    "SwImplPolicyEnum",
    "SwPointerTargetProps",
    "SwTextProps",
    "ValueList",
]
