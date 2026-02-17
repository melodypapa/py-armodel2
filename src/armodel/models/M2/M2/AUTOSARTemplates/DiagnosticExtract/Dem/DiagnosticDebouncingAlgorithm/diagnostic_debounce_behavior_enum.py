"""AUTOSAR DiagnosticDebounceBehaviorEnum enumeration.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 199)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 438)

JSON Source: packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticDebouncingAlgorithm.enums.json"""

from enum import Enum


class DiagnosticDebounceBehaviorEnum(Enum):
    """AUTOSAR DiagnosticDebounceBehaviorEnum enumeration."""

    FREEZE = "freeze"
    RESET = "reset"
