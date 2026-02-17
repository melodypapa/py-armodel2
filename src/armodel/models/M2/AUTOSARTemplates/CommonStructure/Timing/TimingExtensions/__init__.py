"""TimingExtensions module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions.vfb_timing import (
        VfbTiming,
    )
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions.swc_timing import (
        SwcTiming,
    )
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions.system_timing import (
        SystemTiming,
    )
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions.bsw_module_timing import (
        BswModuleTiming,
    )
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions.bsw_composition_timing import (
        BswCompositionTiming,
    )
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions.ecu_timing import (
        EcuTiming,
    )
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions.timing_extension import (
        TimingExtension,
    )

__all__ = [
    "BswCompositionTiming",
    "BswModuleTiming",
    "EcuTiming",
    "SwcTiming",
    "SystemTiming",
    "TimingExtension",
    "VfbTiming",
]
