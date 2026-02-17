"""AUTOSAR ShowSeeEnum enumeration.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 325)

JSON Source: packages/M2_MSR_Documentation_TextModel_InlineAttributeEnums.enums.json"""

from enum import Enum


class ShowSeeEnum(Enum):
    """AUTOSAR ShowSeeEnum enumeration."""

    NOSHOWSEE = "noShowSee"
    SHOWSEE = "showSee"
