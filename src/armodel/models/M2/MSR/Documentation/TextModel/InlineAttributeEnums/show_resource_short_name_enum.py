"""AUTOSAR ShowResourceShortNameEnum enumeration.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 324)

JSON Source: packages/M2_MSR_Documentation_TextModel_InlineAttributeEnums.enums.json"""

from enum import Enum


class ShowResourceShortNameEnum(Enum):
    """AUTOSAR ShowResourceShortNameEnum enumeration."""

    NOSHOWSHORTNAME = "noShowShortName"
    SHOWSHORTNAME = "showShortName"
