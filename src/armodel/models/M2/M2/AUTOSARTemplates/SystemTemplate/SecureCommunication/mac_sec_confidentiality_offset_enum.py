"""AUTOSAR MacSecConfidentialityOffsetEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 176)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.enums.json"""

from enum import Enum


class MacSecConfidentialityOffsetEnum(Enum):
    """AUTOSAR MacSecConfidentialityOffsetEnum enumeration."""

    CONFIDENTIALITYOFFSET_0OFFSET_30 = "ConfidentialityOffset_0Offset_30"
    SYSTEM = "System"
    AUTOSAROFFSET_50 = "AUTOSAROffset_50"
