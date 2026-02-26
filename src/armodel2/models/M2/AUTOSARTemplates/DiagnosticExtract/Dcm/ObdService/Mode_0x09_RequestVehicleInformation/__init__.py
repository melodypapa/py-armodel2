"""Mode_0x09_RequestVehicleInformation module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.ObdService.Mode_0x09_RequestVehicleInformation.diagnostic_request_vehicle_info import (
        DiagnosticRequestVehicleInfo,
    )
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.ObdService.Mode_0x09_RequestVehicleInformation.diagnostic_request_vehicle_info_class import (
        DiagnosticRequestVehicleInfoClass,
    )

__all__ = [
    "DiagnosticRequestVehicleInfo",
    "DiagnosticRequestVehicleInfoClass",
]
