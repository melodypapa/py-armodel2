"""CommonService module."""
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_custom_service_class import (
    DiagnosticCustomServiceClass,
)

__all__ = [
    "DiagnosticCustomServiceClass",
    "DiagnosticServiceClass",
    "DiagnosticServiceInstance",
]
