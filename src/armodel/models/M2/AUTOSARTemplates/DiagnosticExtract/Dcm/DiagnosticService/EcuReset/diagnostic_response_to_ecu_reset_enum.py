"""DiagnosticResponseToEcuResetEnum enumeration."""

from enum import Enum


class DiagnosticResponseToEcuResetEnum(Enum):
    """AUTOSAR DiagnosticResponseToEcuResetEnum enumeration."""

    RESPONDAFTERRESET = "respondAfterReset"
    RESPONDBEFORERESET = "respondBeforeReset"
