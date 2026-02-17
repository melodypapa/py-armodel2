"""ControlDTCSetting module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.ControlDTCSetting.diagnostic_control_dtc_setting import (
        DiagnosticControlDTCSetting,
    )
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.ControlDTCSetting.diagnostic_control_dtc_setting_class import (
        DiagnosticControlDTCSettingClass,
    )

__all__ = [
    "DiagnosticControlDTCSetting",
    "DiagnosticControlDTCSettingClass",
]
