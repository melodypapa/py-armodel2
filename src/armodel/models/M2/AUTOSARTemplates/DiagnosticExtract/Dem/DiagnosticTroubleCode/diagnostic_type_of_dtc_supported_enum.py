"""AUTOSAR DiagnosticTypeOfDtcSupportedEnum enumeration.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 66)

JSON Source: packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticTroubleCode.enums.json"""

from enum import Enum


class DiagnosticTypeOfDtcSupportedEnum(Enum):
    """AUTOSAR DiagnosticTypeOfDtcSupportedEnum enumeration."""

    ISO11992_4 = "iso11992_4"
    ISO14229_1 = "iso14229_1"
    ISO15031_6 = "iso15031_6"
    SAEJ1939_73 = "saeJ1939_73"
    SAEJ2012_DA = "saeJ2012_da"
