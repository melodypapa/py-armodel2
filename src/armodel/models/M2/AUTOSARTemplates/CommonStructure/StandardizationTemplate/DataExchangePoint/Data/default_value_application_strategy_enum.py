"""AUTOSAR DefaultValueApplicationStrategyEnum enumeration.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 112)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint_Data.enums.json"""

from enum import Enum


class DefaultValueApplicationStrategyEnum(Enum):
    """AUTOSAR DefaultValueApplicationStrategyEnum enumeration."""

    FURTHER = "further"
    DEFAULTIFUNDEFINED = "defaultIfUndefined"
