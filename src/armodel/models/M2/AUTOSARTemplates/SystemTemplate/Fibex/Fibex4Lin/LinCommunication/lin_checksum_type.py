"""AUTOSAR LinChecksumType enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 428)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinCommunication.enums.json"""

from enum import Enum


class LinChecksumType(Enum):
    """AUTOSAR LinChecksumType enumeration."""

    CLASSIC = "classic"
    ENHANCED = "enhanced"
