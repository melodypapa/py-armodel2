"""AUTOSAR DataExchangePointKind enumeration.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 79)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint.enums.json"""

from enum import Enum


class DataExchangePointKind(Enum):
    """AUTOSAR DataExchangePointKind enumeration."""

    AGREED = "agreed"
