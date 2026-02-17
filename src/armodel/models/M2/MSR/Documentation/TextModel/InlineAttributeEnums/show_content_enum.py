"""AUTOSAR ShowContentEnum enumeration.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 322)

JSON Source: packages/M2_MSR_Documentation_TextModel_InlineAttributeEnums.enums.json"""

from enum import Enum


class ShowContentEnum(Enum):
    """AUTOSAR ShowContentEnum enumeration."""

    NOSHOWCONTENT = "noShowContent"
    SHOWCONTENT = "showContent"
