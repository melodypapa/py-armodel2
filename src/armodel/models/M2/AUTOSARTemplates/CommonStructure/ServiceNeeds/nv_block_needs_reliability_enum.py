"""AUTOSAR NvBlockNeedsReliabilityEnum enumeration.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 233)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 680)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.enums.json"""

from enum import Enum


class NvBlockNeedsReliabilityEnum(Enum):
    """AUTOSAR NvBlockNeedsReliabilityEnum enumeration."""

    ERRORCORRECTION = "errorCorrection"
    ERRORDETECTION = "errorDetection"
    NOPROTECTION = "noProtection"
