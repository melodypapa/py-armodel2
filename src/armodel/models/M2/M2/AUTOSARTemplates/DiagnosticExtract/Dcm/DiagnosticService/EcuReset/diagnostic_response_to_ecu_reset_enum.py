"""AUTOSAR DiagnosticResponseToEcuResetEnum enumeration.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 102)

JSON Source: packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_EcuReset.enums.json"""

from enum import Enum


class DiagnosticResponseToEcuResetEnum(Enum):
    """AUTOSAR DiagnosticResponseToEcuResetEnum enumeration."""

    RESPONDAFTERRESET = "respondAfterReset"
    RESPONDBEFORERESET = "respondBeforeReset"
