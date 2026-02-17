"""AUTOSAR DiagnosticEventWindowTimeEnum enumeration.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 133)

JSON Source: packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_ResponseOnEvent.enums.json"""

from enum import Enum


class DiagnosticEventWindowTimeEnum(Enum):
    """AUTOSAR DiagnosticEventWindowTimeEnum enumeration."""

    INFINITETIMETO = "infiniteTimeTo"
    POWERWINDOWTIMEDOWN = "powerWindowTimedown"
