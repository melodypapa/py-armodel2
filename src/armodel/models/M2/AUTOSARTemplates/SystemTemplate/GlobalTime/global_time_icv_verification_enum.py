"""AUTOSAR GlobalTimeIcvVerificationEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 881)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_GlobalTime.enums.json"""

from enum import Enum


class GlobalTimeIcvVerificationEnum(Enum):
    """AUTOSAR GlobalTimeIcvVerificationEnum enumeration."""

    ICVIGNORED = "icvIgnored"
    ICVNOTVERIFIED = "icvNotVerified"
    ICVOPTIONAL = "icvOptional"
    ICVVERIFIED = "icvVerified"
