"""AUTOSAR ShowResourceNumberEnum enumeration.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 324)

JSON Source: packages/M2_MSR_Documentation_TextModel_InlineAttributeEnums.enums.json"""

from enum import Enum


class ShowResourceNumberEnum(Enum):
    """AUTOSAR ShowResourceNumberEnum enumeration."""

    NOSHOWNUMBER = "noShowNumber"
    SHOWNUMBER = "showNumber"
