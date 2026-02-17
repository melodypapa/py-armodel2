"""AUTOSAR DiagnosticClearEventAllowedBehaviorEnum enumeration.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 166)

JSON Source: packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticEvent.enums.json"""

from enum import Enum


class DiagnosticClearEventAllowedBehaviorEnum(Enum):
    """AUTOSAR DiagnosticClearEventAllowedBehaviorEnum enumeration."""

    NOSTATUSBYTECHANGEONLYTHISCYCLEAND = "noStatusByteChangeonlyThisCycleAnd"
    READINESS = "Readiness"
