"""IPsecPolicyEnum enumeration."""

from enum import Enum


class IPsecPolicyEnum(Enum):
    """AUTOSAR IPsecPolicyEnum enumeration."""

    DROP = "drop"
    IPSEC = "ipsec"
    PASSTHROUGH = "passthrough"
    REJECT = "reject"
