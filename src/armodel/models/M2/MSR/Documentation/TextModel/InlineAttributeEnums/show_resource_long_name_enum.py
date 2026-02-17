"""AUTOSAR ShowResourceLongNameEnum enumeration.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 323)

JSON Source: packages/M2_MSR_Documentation_TextModel_InlineAttributeEnums.enums.json"""

from enum import Enum


class ShowResourceLongNameEnum(Enum):
    """AUTOSAR ShowResourceLongNameEnum enumeration."""

    NOSHOWLONGNAME = "noShowLongName"
    SHOWLONGNAME = "showLongName"
