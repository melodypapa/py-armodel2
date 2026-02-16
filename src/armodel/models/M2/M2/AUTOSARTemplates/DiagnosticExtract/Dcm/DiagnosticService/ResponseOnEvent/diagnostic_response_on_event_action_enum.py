"""DiagnosticResponseOnEventActionEnum enumeration."""

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
