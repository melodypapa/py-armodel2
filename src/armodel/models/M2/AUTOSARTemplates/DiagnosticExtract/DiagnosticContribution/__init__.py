"""DiagnosticContribution module."""
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

__all__ = [
    "DiagnosticContributionSet",
    "DiagnosticEcuInstanceProps",
    "DiagnosticProtocol",
    "DiagnosticServiceTable",
]
