"""DiagnosticDenominatorConditionEnum enumeration."""

from enum import Enum


class DiagnosticDenominatorConditionEnum(Enum):
    """AUTOSAR DiagnosticDenominatorConditionEnum enumeration."""

    _500MILES = "_500miles"
    COLDSTART = "coldstart"
    CSERS = "csers"
    EVAP = "evap"
    EVAPPURGEFLOWINDIVIDUAL = "evappurgeflowindividual"
    OBD = "obd"
