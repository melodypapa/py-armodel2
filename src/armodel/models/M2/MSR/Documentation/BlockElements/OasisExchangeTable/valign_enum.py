"""AUTOSAR ValignEnum enumeration.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 336)

JSON Source: packages/M2_MSR_Documentation_BlockElements_OasisExchangeTable.enums.json"""

from enum import Enum


class ValignEnum(Enum):
    """AUTOSAR ValignEnum enumeration."""

    BOTTOM = "bottom"
    MIDDLE = "middle"
    TOP = "top"
