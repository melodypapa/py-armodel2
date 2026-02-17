"""AUTOSAR DiagnosticIumprKindEnum enumeration.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 210)

JSON Source: packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticEvent.enums.json"""

from enum import Enum


class DiagnosticIumprKindEnum(Enum):
    """AUTOSAR DiagnosticIumprKindEnum enumeration."""

    APIBASED = "apiBased"
    OBSERVERBASED = "observerBased"
