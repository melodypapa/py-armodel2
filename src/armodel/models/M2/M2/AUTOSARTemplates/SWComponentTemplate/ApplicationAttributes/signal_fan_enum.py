"""AUTOSAR SignalFanEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 162)

JSON Source: packages/M2_AUTOSARTemplates_SWComponentTemplate_ApplicationAttributes.enums.json"""

from enum import Enum


class SignalFanEnum(Enum):
    """AUTOSAR SignalFanEnum enumeration."""

    NFOLDINTERFACE = "nfoldinterface"
    SINGLEINTERFACE = "singleinterface"
