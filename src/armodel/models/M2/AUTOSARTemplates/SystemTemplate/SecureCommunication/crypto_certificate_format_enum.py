"""AUTOSAR CryptoCertificateFormatEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 565)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.enums.json"""

from enum import Enum


class CryptoCertificateFormatEnum(Enum):
    """AUTOSAR CryptoCertificateFormatEnum enumeration."""

    CVC = "cvc"
    X509 = "x509"
