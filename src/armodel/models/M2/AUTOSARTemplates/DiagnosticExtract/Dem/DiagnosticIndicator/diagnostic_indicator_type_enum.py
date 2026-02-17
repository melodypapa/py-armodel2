"""AUTOSAR DiagnosticIndicatorTypeEnum enumeration.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 203)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 766)

JSON Source: packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticIndicator.enums.json"""

from enum import Enum


class DiagnosticIndicatorTypeEnum(Enum):
    """AUTOSAR DiagnosticIndicatorTypeEnum enumeration."""

    AMBERWARNING = "amberWarning"
    MALFUNCTION = "malfunction"
    PROTECTLAMP = "protectLamp"
    REDSTOPLAMP = "redStopLamp"
    WARNING = "warning"
