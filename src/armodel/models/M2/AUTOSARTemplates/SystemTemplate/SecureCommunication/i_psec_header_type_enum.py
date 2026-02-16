"""IPsecHeaderTypeEnum enumeration."""

from enum import Enum


class IPsecHeaderTypeEnum(Enum):
    """AUTOSAR IPsecHeaderTypeEnum enumeration."""

    AH = "ah"
    ESP = "esp"
    NONE = "none"
