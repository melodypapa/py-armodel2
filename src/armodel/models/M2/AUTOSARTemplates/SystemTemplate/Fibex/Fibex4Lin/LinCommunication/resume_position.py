"""AUTOSAR ResumePosition enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 432)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinCommunication.enums.json"""

from enum import Enum


class ResumePosition(Enum):
    """AUTOSAR ResumePosition enumeration."""

    CONTINUEATITPOSITION = "continueAtItPosition"
    STARTFROMBEGINNING = "startFromBeginning"
