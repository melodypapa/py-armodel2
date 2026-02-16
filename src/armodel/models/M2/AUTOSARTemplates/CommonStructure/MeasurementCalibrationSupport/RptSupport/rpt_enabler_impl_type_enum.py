"""RptEnablerImplTypeEnum enumeration."""

from enum import Enum


class RptEnablerImplTypeEnum(Enum):
    """AUTOSAR RptEnablerImplTypeEnum enumeration."""

    NONE = "none"
    RPTENABLERRAM = "rptEnablerRam"
    RPTENABLERRAMANDROM = "rptEnablerRamAndRom"
    RPTENABLERROM = "rptEnablerRom"
