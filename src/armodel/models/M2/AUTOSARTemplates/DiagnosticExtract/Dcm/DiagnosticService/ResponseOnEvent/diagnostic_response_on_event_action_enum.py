"""AUTOSAR DiagnosticResponseOnEventActionEnum enumeration.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 134)

JSON Source: packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_ResponseOnEvent.enums.json"""

from enum import Enum


class DiagnosticResponseOnEventActionEnum(Enum):
    """AUTOSAR DiagnosticResponseOnEventActionEnum enumeration."""

    CLEARONCHANGEOFDATA = "clearonChangeOfData"
    IDENTIFIERONCOMPARISONOFVALUESONDTCSTATUSCHANGE = "IdentifieronComparisonOfValuesonDTCStatusChange"
    REPORT = "report"
    REPORTDTCRECORDINFORMATIONONDTC = "reportDTCRecordInformationOnDtc"
    REPORTMOSTRECENTDTCONSTATUS = "reportMostRecentDtcOnStatus"
    START = "start"
    STOP = "stop"
