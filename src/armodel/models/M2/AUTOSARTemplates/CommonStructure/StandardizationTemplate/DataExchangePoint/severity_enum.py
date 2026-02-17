"""AUTOSAR SeverityEnum enumeration.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 87)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint.enums.json"""

from enum import Enum


class SeverityEnum(Enum):
    """AUTOSAR SeverityEnum enumeration."""

    ERRORINFO = "errorinfo"
    WARNING = "warning"
