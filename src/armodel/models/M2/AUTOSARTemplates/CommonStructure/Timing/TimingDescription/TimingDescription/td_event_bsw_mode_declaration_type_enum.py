"""AUTOSAR TDEventBswModeDeclarationTypeEnum enumeration.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 77)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.enums.json"""

from enum import Enum


class TDEventBswModeDeclarationTypeEnum(Enum):
    """AUTOSAR TDEventBswModeDeclarationTypeEnum enumeration."""

    # Note: 1 duplicate literal(s) found and removed: modeDeclaration
    MODEDECLARATIONREQUESTED = "modeDeclarationRequested"
    MODEDECLARATION = "modeDeclaration"
