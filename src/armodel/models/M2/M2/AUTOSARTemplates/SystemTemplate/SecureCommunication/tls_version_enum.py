"""AUTOSAR TlsVersionEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 563)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.enums.json"""

from enum import Enum


class TlsVersionEnum(Enum):
    """AUTOSAR TlsVersionEnum enumeration."""

    TLS12 = "tls12"
    TLS13 = "tls13"
