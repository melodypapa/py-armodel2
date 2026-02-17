"""AUTOSAR IPsecPolicyEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 574)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.enums.json"""

from enum import Enum


class IPsecPolicyEnum(Enum):
    """AUTOSAR IPsecPolicyEnum enumeration."""

    DROP = "drop"
    IPSEC = "ipsec"
    PASSTHROUGH = "passthrough"
    REJECT = "reject"
