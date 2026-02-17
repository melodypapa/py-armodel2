"""DiagnosticTestResult module."""
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTestResult.diagnostic_test_result import (
    DiagnosticTestResult,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTestResult.diagnostic_test_identifier import (
    DiagnosticTestIdentifier,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTestResult.diagnostic_measurement_identifier import (
    DiagnosticMeasurementIdentifier,
)

__all__ = [
    "DiagnosticMeasurementIdentifier",
    "DiagnosticTestIdentifier",
    "DiagnosticTestResult",
]
