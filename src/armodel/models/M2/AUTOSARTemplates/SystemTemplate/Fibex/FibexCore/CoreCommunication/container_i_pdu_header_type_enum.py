"""ContainerIPduHeaderTypeEnum enumeration."""

from enum import Enum


class ContainerIPduHeaderTypeEnum(Enum):
    """AUTOSAR ContainerIPduHeaderTypeEnum enumeration."""

    LONGHEADER = "longHeader"
    NOHEADER = "noHeader"
    SHORTHEADER = "shortHeader"
