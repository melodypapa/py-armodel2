"""AUTOSAR DiagnosticDenominatorConditionEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 803)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.enums.json"""

from enum import Enum


class DiagnosticDenominatorConditionEnum(Enum):
    """AUTOSAR DiagnosticDenominatorConditionEnum enumeration."""

    _500MILES = "_500miles"
    COLDSTART = "coldstart"
    CSERS = "csers"
    EVAP = "evap"
    EVAPPURGEFLOWINDIVIDUAL = "evappurgeflowindividual"
    OBD = "obd"
