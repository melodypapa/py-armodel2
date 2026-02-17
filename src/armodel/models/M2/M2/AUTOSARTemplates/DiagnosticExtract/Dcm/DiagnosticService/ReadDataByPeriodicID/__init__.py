"""ReadDataByPeriodicID module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.ReadDataByPeriodicID.diagnostic_read_data_by_periodic_id import (
        DiagnosticReadDataByPeriodicID,
    )
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.ReadDataByPeriodicID.diagnostic_read_data_by_periodic_id_class import (
        DiagnosticReadDataByPeriodicIDClass,
    )
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.ReadDataByPeriodicID.diagnostic_periodic_rate import (
        DiagnosticPeriodicRate,
    )

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.ReadDataByPeriodicID.diagnostic_periodic_rate_category_enum import (
    DiagnosticPeriodicRateCategoryEnum,
)

__all__ = [
    "DiagnosticPeriodicRate",
    "DiagnosticPeriodicRateCategoryEnum",
    "DiagnosticReadDataByPeriodicID",
    "DiagnosticReadDataByPeriodicIDClass",
]
