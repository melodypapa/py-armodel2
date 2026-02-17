"""TimingCondition module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition.timing_condition import (
        TimingCondition,
    )
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition.timing_condition_formula import (
        TimingConditionFormula,
    )
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition.timing_extension_resource import (
        TimingExtensionResource,
    )
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition.timing_mode_instance import (
        TimingModeInstance,
    )
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition.mode_in_bsw_instance_ref import (
        ModeInBswInstanceRef,
    )
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition.mode_in_swc_instance_ref import (
        ModeInSwcInstanceRef,
    )

__all__ = [
    "ModeInBswInstanceRef",
    "ModeInSwcInstanceRef",
    "TimingCondition",
    "TimingConditionFormula",
    "TimingExtensionResource",
    "TimingModeInstance",
]
