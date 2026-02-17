"""AUTOSAR DdsDurabilityKindEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 530)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_Dds.enums.json"""

from enum import Enum


class DdsDurabilityKindEnum(Enum):
    """AUTOSAR DdsDurabilityKindEnum enumeration."""

    PERSISTENTTRANSIENTTRANSIENTLOCALVOLATILE = "persistenttransienttransientLocalvolatile"
