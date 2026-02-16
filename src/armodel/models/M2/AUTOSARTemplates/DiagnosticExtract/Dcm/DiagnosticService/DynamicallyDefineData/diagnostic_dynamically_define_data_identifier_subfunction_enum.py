"""DiagnosticDynamicallyDefineDataIdentifierSubfunctionEnum enumeration."""

from enum import Enum


class DiagnosticDynamicallyDefineDataIdentifierSubfunctionEnum(Enum):
    """AUTOSAR DiagnosticDynamicallyDefineDataIdentifierSubfunctionEnum enumeration."""

    CLEARDYNAMICALLYDEFINEDATAIDENTIFIER = "clearDynamicallyDefineDataIdentifier"
    DEFINEBYIDENTIFIER = "defineByIdentifier"
    DEFINEBYMEMORYADDRESS = "defineByMemoryAddress"
