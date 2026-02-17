"""AUTOSAR GlobalTimeIcvSupportEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 880)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_GlobalTime.enums.json"""

from enum import Enum


class GlobalTimeIcvSupportEnum(Enum):
    """AUTOSAR GlobalTimeIcvSupportEnum enumeration."""

    ICVNOTSUPPORTED = "icvNotSupported"
    ICVSUPPORTED = "icvSupported"
