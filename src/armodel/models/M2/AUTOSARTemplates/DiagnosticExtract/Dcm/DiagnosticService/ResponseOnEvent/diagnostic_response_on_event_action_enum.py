"""AUTOSAR DiagnosticResponseOnEventActionEnum enumeration.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 134)

JSON Source: packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_ResponseOnEvent.enums.json"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class DiagnosticResponseOnEventActionEnum(AREnum):
    """AUTOSAR DiagnosticResponseOnEventActionEnum enumeration.

    This enum inherits from AREnum, which provides:
    - serialize(): XML serialization
    - deserialize(): XML deserialization with automatic member matching
    - Transparent equality comparison with string values
    """

    def __init__(self, value: str) -> None:
        """Initialize enum member.

        Args:
            value: The enum value as a string
        """
        self._value_ = value

    CLEARON_CHANGE_OF_DATA = "clearonChangeOfData"
    IDENTIFIERON_COMPARISON_OF_VALUESON_DTC_STATUS_CHANGE = "IdentifieronComparisonOfValuesonDTCStatusChange"
    REPORT = "report"
    REPORT_DTC_RECORD_INFORMATION_ON_DTC = "reportDTCRecordInformationOnDtc"
    REPORT_MOST_RECENT_DTC_ON_STATUS = "reportMostRecentDtcOnStatus"
    START = "start"
    STOP = "stop"
