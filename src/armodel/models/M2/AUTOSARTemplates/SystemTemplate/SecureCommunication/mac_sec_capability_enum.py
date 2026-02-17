"""AUTOSAR MacSecCapabilityEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 177)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.enums.json"""

from enum import Enum


class MacSecCapabilityEnum(Enum):
    """AUTOSAR MacSecCapabilityEnum enumeration."""

    INTERGRITYANDCONFIDENTIALITYINTERGRITYWITHOUT = "intergrityAndConfidentialityintergrityWithout"
    CONFIDENTIALITY = "Confidentiality"
