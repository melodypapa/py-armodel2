"""DynamicallyDefineDataIdentifier module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.DynamicallyDefineDataIdentifier.diagnostic_dynamically_define_data_identifier import (
        DiagnosticDynamicallyDefineDataIdentifier,
    )
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.DynamicallyDefineDataIdentifier.diagnostic_dynamically_define_data_identifier_class import (
        DiagnosticDynamicallyDefineDataIdentifierClass,
    )

__all__ = [
    "DiagnosticDynamicallyDefineDataIdentifier",
    "DiagnosticDynamicallyDefineDataIdentifierClass",
]
