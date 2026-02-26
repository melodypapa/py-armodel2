"""DiagnosticTestResult module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTestResult.diagnostic_test_result import (
        DiagnosticTestResult,
    )
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTestResult.diagnostic_test_identifier import (
        DiagnosticTestIdentifier,
    )
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTestResult.diagnostic_measurement_identifier import (
        DiagnosticMeasurementIdentifier,
    )

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTestResult.diagnostic_test_result_update_enum import (
    DiagnosticTestResultUpdateEnum,
)

__all__ = [
    "DiagnosticMeasurementIdentifier",
    "DiagnosticTestIdentifier",
    "DiagnosticTestResult",
    "DiagnosticTestResultUpdateEnum",
]
