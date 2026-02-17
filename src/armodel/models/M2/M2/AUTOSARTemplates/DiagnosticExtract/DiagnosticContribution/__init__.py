"""DiagnosticContribution module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticContribution.diagnostic_contribution_set import (
        DiagnosticContributionSet,
    )
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticContribution.diagnostic_protocol import (
        DiagnosticProtocol,
    )
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticContribution.diagnostic_service_table import (
        DiagnosticServiceTable,
    )
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticContribution.diagnostic_ecu_instance_props import (
        DiagnosticEcuInstanceProps,
    )

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticContribution.diagnostic_obd_support_enum import (
    DiagnosticObdSupportEnum,
)

__all__ = [
    "DiagnosticContributionSet",
    "DiagnosticEcuInstanceProps",
    "DiagnosticObdSupportEnum",
    "DiagnosticProtocol",
    "DiagnosticServiceTable",
]
