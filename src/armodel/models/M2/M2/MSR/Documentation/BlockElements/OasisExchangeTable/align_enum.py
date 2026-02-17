"""AUTOSAR AlignEnum enumeration.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 335)

JSON Source: packages/M2_MSR_Documentation_BlockElements_OasisExchangeTable.enums.json"""

from enum import Enum


class AlignEnum(Enum):
    """AUTOSAR AlignEnum enumeration."""

    CENTER = "center"
    JUSTIFY = "justify"
    LEFTRIGHT = "leftright"
