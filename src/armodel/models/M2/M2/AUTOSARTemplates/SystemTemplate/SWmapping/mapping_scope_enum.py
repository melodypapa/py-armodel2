"""AUTOSAR MappingScopeEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 203)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_SWmapping.enums.json"""

from enum import Enum


class MappingScopeEnum(Enum):
    """AUTOSAR MappingScopeEnum enumeration."""

    MAPPINGSCOPECORE = "mappingScopeCore"
    SYSTEM = "System"
    AUTOSAR = "AUTOSAR"
    MAPPINGSCOPEECU = "mappingScopeEcu"
    MAPPINGSCOPEPARTITION = "mappingScopePartition"
