"""AUTOSAR DiagnosticDynamicallyDefineDataIdentifierSubfunctionEnum enumeration.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 129)

JSON Source: packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_DynamicallyDefineData.enums.json"""

from enum import Enum


class DiagnosticDynamicallyDefineDataIdentifierSubfunctionEnum(Enum):
    """AUTOSAR DiagnosticDynamicallyDefineDataIdentifierSubfunctionEnum enumeration."""

    CLEARDYNAMICALLYDEFINEDATAIDENTIFIER = "clearDynamicallyDefineDataIdentifier"
    DEFINEBYIDENTIFIER = "defineByIdentifier"
    DEFINEBYMEMORYADDRESS = "defineByMemoryAddress"
