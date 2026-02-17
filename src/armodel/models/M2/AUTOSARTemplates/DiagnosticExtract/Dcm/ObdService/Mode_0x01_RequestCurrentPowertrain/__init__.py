"""Mode_0x01_RequestCurrentPowertrain module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.ObdService.Mode_0x01_RequestCurrentPowertrain.diagnostic_request_current_powertrain_data import (
        DiagnosticRequestCurrentPowertrainData,
    )
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.ObdService.Mode_0x01_RequestCurrentPowertrain.diagnostic_request_current_powertrain_data_class import (
        DiagnosticRequestCurrentPowertrainDataClass,
    )

__all__ = [
    "DiagnosticRequestCurrentPowertrainData",
    "DiagnosticRequestCurrentPowertrainDataClass",
]
