"""DataByIdentifier module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.DataByIdentifier.diagnostic_read_data_by_identifier import (
        DiagnosticReadDataByIdentifier,
    )
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.DataByIdentifier.diagnostic_write_data_by_identifier import (
        DiagnosticWriteDataByIdentifier,
    )
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.DataByIdentifier.diagnostic_write_data_by_identifier_class import (
        DiagnosticWriteDataByIdentifierClass,
    )
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.DataByIdentifier.diagnostic_data_by_identifier import (
        DiagnosticDataByIdentifier,
    )
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.DataByIdentifier.diagnostic_read_data_by_identifier_class import (
        DiagnosticReadDataByIdentifierClass,
    )
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.DataByIdentifier.diagnostic_read_scaling_data_by_identifier import (
        DiagnosticReadScalingDataByIdentifier,
    )
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.DataByIdentifier.diagnostic_read_scaling_data_by_identifier_class import (
        DiagnosticReadScalingDataByIdentifierClass,
    )

__all__ = [
    "DiagnosticDataByIdentifier",
    "DiagnosticReadDataByIdentifier",
    "DiagnosticReadDataByIdentifierClass",
    "DiagnosticReadScalingDataByIdentifier",
    "DiagnosticReadScalingDataByIdentifierClass",
    "DiagnosticWriteDataByIdentifier",
    "DiagnosticWriteDataByIdentifierClass",
]
