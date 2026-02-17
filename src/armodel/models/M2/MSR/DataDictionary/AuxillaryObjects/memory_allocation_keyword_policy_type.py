"""AUTOSAR MemoryAllocationKeywordPolicyType enumeration.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 145)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 418)

JSON Source: packages/M2_MSR_DataDictionary_AuxillaryObjects.enums.json"""

from enum import Enum


class MemoryAllocationKeywordPolicyType(Enum):
    """AUTOSAR MemoryAllocationKeywordPolicyType enumeration."""

    ADDRMETHODSHORT = "addrMethodShort"
    NAME = "Name"
    ADDRMETHODSHORT = "addrMethodShort"
    NAMEANDALIGNMENT = "NameAndAlignment"
