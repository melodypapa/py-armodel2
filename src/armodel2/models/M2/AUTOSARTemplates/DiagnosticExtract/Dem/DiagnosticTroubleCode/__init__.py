"""DiagnosticTroubleCode module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTroubleCode.diagnostic_trouble_code_uds import (
        DiagnosticTroubleCodeUds,
    )
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTroubleCode.diagnostic_trouble_code_obd import (
        DiagnosticTroubleCodeObd,
    )
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTroubleCode.event_obd_readiness_group import (
        EventObdReadinessGroup,
    )
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTroubleCode.diagnostic_trouble_code import (
        DiagnosticTroubleCode,
    )
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTroubleCode.diagnostic_trouble_code_group import (
        DiagnosticTroubleCodeGroup,
    )
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTroubleCode.diagnostic_trouble_code_props import (
        DiagnosticTroubleCodeProps,
    )
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTroubleCode.diagnostic_data_identifier_set import (
        DiagnosticDataIdentifierSet,
    )
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTroubleCode.diagnostic_trouble_code_j1939 import (
        DiagnosticTroubleCodeJ1939,
    )

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTroubleCode.diagnostic_type_of_dtc_supported_enum import (
    DiagnosticTypeOfDtcSupportedEnum,
)
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTroubleCode.diagnostic_status_bit_handling_test_failed_since_last_clear_enum import (
    DiagnosticStatusBitHandlingTestFailedSinceLastClearEnum,
)
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTroubleCode.diagnostic_significance_enum import (
    DiagnosticSignificanceEnum,
)
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTroubleCode.diagnostic_uds_severity_enum import (
    DiagnosticUdsSeverityEnum,
)
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTroubleCode.diagnostic_wwh_obd_dtc_class_enum import (
    DiagnosticWwhObdDtcClassEnum,
)
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTroubleCode.diagnostic_trouble_code_j1939_dtc_kind_enum import (
    DiagnosticTroubleCodeJ1939DtcKindEnum,
)

__all__ = [
    "DiagnosticDataIdentifierSet",
    "DiagnosticSignificanceEnum",
    "DiagnosticStatusBitHandlingTestFailedSinceLastClearEnum",
    "DiagnosticTroubleCode",
    "DiagnosticTroubleCodeGroup",
    "DiagnosticTroubleCodeJ1939",
    "DiagnosticTroubleCodeJ1939DtcKindEnum",
    "DiagnosticTroubleCodeObd",
    "DiagnosticTroubleCodeProps",
    "DiagnosticTroubleCodeUds",
    "DiagnosticTypeOfDtcSupportedEnum",
    "DiagnosticUdsSeverityEnum",
    "DiagnosticWwhObdDtcClassEnum",
    "EventObdReadinessGroup",
]
