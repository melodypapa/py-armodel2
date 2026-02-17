"""AUTOSAR DiagnosticEventKindEnum enumeration.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 167)

JSON Source: packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticEvent.enums.json"""

from enum import Enum


class DiagnosticEventKindEnum(Enum):
    """AUTOSAR DiagnosticEventKindEnum enumeration."""

    BSW = "bsw"
    SWC = "swc"
