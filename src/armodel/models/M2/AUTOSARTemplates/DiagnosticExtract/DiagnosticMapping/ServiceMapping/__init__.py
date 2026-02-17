"""ServiceMapping module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.ServiceMapping.diagnostic_service_data_mapping import (
        DiagnosticServiceDataMapping,
    )
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.ServiceMapping.diagnostic_parameter_element_access import (
        DiagnosticParameterElementAccess,
    )
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.ServiceMapping.diagnostic_service_mapping_diag_target import (
        DiagnosticServiceMappingDiagTarget,
    )
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.ServiceMapping.diagnostic_service_sw_mapping import (
        DiagnosticServiceSwMapping,
    )
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.ServiceMapping.bsw_service_dependency_ident import (
        BswServiceDependencyIdent,
    )
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.ServiceMapping.diagnostic_security_event_reporting_mode_mapping import (
        DiagnosticSecurityEventReportingModeMapping,
    )
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.ServiceMapping.diagnostic_dem_provided_data_mapping import (
        DiagnosticDemProvidedDataMapping,
    )
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.ServiceMapping.diagnostic_fim_function_mapping import (
        DiagnosticFimFunctionMapping,
    )

__all__ = [
    "BswServiceDependencyIdent",
    "DiagnosticDemProvidedDataMapping",
    "DiagnosticFimFunctionMapping",
    "DiagnosticParameterElementAccess",
    "DiagnosticSecurityEventReportingModeMapping",
    "DiagnosticServiceDataMapping",
    "DiagnosticServiceMappingDiagTarget",
    "DiagnosticServiceSwMapping",
]
