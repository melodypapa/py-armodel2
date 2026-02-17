"""AUTOSAR CryptoServiceKeyGenerationEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 378)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.enums.json"""

from enum import Enum


class CryptoServiceKeyGenerationEnum(Enum):
    """AUTOSAR CryptoServiceKeyGenerationEnum enumeration."""

    KEYDERIVATION = "keyDerivation"
    KEYSTORAGE = "keyStorage"
