"""AUTOSAR ShowResourceTypeEnum enumeration.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 324)

JSON Source: packages/M2_MSR_Documentation_TextModel_InlineAttributeEnums.enums.json"""

from enum import Enum


class ShowResourceTypeEnum(Enum):
    """AUTOSAR ShowResourceTypeEnum enumeration."""

    NOSHOWTYPE = "noShowType"
    SHOWTYPE = "showType"
