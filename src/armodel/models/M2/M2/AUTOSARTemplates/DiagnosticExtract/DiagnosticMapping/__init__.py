"""DiagnosticMapping module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_trouble_code_uds_to_trouble_code_obd_mapping import (
        DiagnosticTroubleCodeUdsToTroubleCodeObdMapping,
    )
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import (
        DiagnosticMapping,
    )
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_sw_mapping import (
        DiagnosticSwMapping,
    )
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_auth_transmit_certificate_mapping import (
        DiagnosticAuthTransmitCertificateMapping,
    )
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_event_to_trouble_code_uds_mapping import (
        DiagnosticEventToTroubleCodeUdsMapping,
    )
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_event_to_operation_cycle_mapping import (
        DiagnosticEventToOperationCycleMapping,
    )
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_event_to_debounce_algorithm_mapping import (
        DiagnosticEventToDebounceAlgorithmMapping,
    )
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_event_to_enable_condition_group_mapping import (
        DiagnosticEventToEnableConditionGroupMapping,
    )
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_event_to_storage_condition_group_mapping import (
        DiagnosticEventToStorageConditionGroupMapping,
    )
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_event_port_mapping import (
        DiagnosticEventPortMapping,
    )
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_operation_cycle_port_mapping import (
        DiagnosticOperationCyclePortMapping,
    )
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_enable_condition_port_mapping import (
        DiagnosticEnableConditionPortMapping,
    )
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_storage_condition_port_mapping import (
        DiagnosticStorageConditionPortMapping,
    )
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_master_to_slave_event_mapping import (
        DiagnosticMasterToSlaveEventMapping,
    )
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_event_to_security_event_mapping import (
        DiagnosticEventToSecurityEventMapping,
    )
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_iumpr_to_function_identifier_mapping import (
        DiagnosticIumprToFunctionIdentifierMapping,
    )
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_secure_coding_mapping import (
        DiagnosticSecureCodingMapping,
    )

__all__ = [
    "DiagnosticAuthTransmitCertificateMapping",
    "DiagnosticEnableConditionPortMapping",
    "DiagnosticEventPortMapping",
    "DiagnosticEventToDebounceAlgorithmMapping",
    "DiagnosticEventToEnableConditionGroupMapping",
    "DiagnosticEventToOperationCycleMapping",
    "DiagnosticEventToSecurityEventMapping",
    "DiagnosticEventToStorageConditionGroupMapping",
    "DiagnosticEventToTroubleCodeUdsMapping",
    "DiagnosticIumprToFunctionIdentifierMapping",
    "DiagnosticMapping",
    "DiagnosticMasterToSlaveEventMapping",
    "DiagnosticOperationCyclePortMapping",
    "DiagnosticSecureCodingMapping",
    "DiagnosticStorageConditionPortMapping",
    "DiagnosticSwMapping",
    "DiagnosticTroubleCodeUdsToTroubleCodeObdMapping",
]
