"""AUTOSAR DiagnosticLogicalOperatorEnum enumeration.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 80)

JSON Source: packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_EnvironmentalCondition.enums.json"""

from enum import Enum


class DiagnosticLogicalOperatorEnum(Enum):
    """AUTOSAR DiagnosticLogicalOperatorEnum enumeration."""

    LOGICALAND = "logicalAnd"
    LOGICALOR = "logicalOr"
