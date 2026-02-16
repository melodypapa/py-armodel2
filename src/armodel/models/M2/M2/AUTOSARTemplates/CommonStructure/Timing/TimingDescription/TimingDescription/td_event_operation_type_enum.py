"""TDEventOperationTypeEnum enumeration."""

from enum import Enum


class TDEventOperationTypeEnum(Enum):
    """AUTOSAR TDEventOperationTypeEnum enumeration."""

    OPERATIONCALLED = "operationCalled"
    OPERATIONCALLRECEIVED = "operationCallReceived"
    OPERATIONCALLRESPONSERECEIVED = "operationCallResponseReceived"
    OPERATIONCALL = "operationCall"
