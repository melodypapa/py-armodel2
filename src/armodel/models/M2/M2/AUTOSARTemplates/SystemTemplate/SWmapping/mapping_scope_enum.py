"""MappingScopeEnum enumeration."""

from enum import Enum


class MappingScopeEnum(Enum):
    """AUTOSAR MappingScopeEnum enumeration."""

    MAPPINGSCOPECORE = "mappingScopeCore"
    SYSTEM = "System"
    AUTOSAR = "AUTOSAR"
    MAPPINGSCOPEECU = "mappingScopeEcu"
    MAPPINGSCOPEPARTITION = "mappingScopePartition"
