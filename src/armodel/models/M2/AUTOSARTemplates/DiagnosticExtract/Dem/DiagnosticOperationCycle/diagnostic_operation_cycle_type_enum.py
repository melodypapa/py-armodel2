"""AUTOSAR DiagnosticOperationCycleTypeEnum enumeration.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 201)

JSON Source: packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticOperationCycle.enums.json"""

from enum import Enum


class DiagnosticOperationCycleTypeEnum(Enum):
    """AUTOSAR DiagnosticOperationCycleTypeEnum enumeration."""

    IGNITION = "ignition"
    OBDDRIVINGCYCLE = "obdDrivingCycle"
    WARMUP = "warmup"
