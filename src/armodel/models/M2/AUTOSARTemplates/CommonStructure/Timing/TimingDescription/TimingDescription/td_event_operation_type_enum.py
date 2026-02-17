"""AUTOSAR TDEventOperationTypeEnum enumeration.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 56)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.enums.json"""

from enum import Enum


class TDEventOperationTypeEnum(Enum):
    """AUTOSAR TDEventOperationTypeEnum enumeration."""

    OPERATIONCALLED = "operationCalled"
    OPERATIONCALLRECEIVED = "operationCallReceived"
    OPERATIONCALLRESPONSERECEIVED = "operationCallResponseReceived"
    OPERATIONCALL = "operationCall"
