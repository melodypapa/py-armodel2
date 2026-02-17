"""AUTOSAR CryptoCertificateAlgorithmFamilyEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 565)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.enums.json"""

from enum import Enum


class CryptoCertificateAlgorithmFamilyEnum(Enum):
    """AUTOSAR CryptoCertificateAlgorithmFamilyEnum enumeration."""

    ECC = "ecc"
    RSA = "rsa"
