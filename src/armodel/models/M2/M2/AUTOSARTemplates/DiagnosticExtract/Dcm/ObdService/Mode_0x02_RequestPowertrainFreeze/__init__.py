"""Mode_0x02_RequestPowertrainFreeze module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.ObdService.Mode_0x02_RequestPowertrainFreeze.diagnostic_request_powertrain_freeze_frame_data import (
        DiagnosticRequestPowertrainFreezeFrameData,
    )
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.ObdService.Mode_0x02_RequestPowertrainFreeze.diagnostic_request_powertrain_freeze_frame_data_class import (
        DiagnosticRequestPowertrainFreezeFrameDataClass,
    )
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.ObdService.Mode_0x02_RequestPowertrainFreeze.diagnostic_powertrain_freeze_frame import (
        DiagnosticPowertrainFreezeFrame,
    )

__all__ = [
    "DiagnosticPowertrainFreezeFrame",
    "DiagnosticRequestPowertrainFreezeFrameData",
    "DiagnosticRequestPowertrainFreezeFrameDataClass",
]
