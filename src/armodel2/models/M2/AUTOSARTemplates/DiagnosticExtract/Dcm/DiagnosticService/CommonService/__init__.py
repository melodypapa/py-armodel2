"""CommonService module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
        DiagnosticServiceClass,
    )
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
        DiagnosticServiceInstance,
    )
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_custom_service_class import (
        DiagnosticCustomServiceClass,
    )

__all__ = [
    "DiagnosticCustomServiceClass",
    "DiagnosticServiceClass",
    "DiagnosticServiceInstance",
]
