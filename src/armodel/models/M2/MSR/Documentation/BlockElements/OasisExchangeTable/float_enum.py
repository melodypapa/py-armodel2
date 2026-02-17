"""AUTOSAR FloatEnum enumeration.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 333)

JSON Source: packages/M2_MSR_Documentation_BlockElements_OasisExchangeTable.enums.json"""

from enum import Enum


class FloatEnum(Enum):
    """AUTOSAR FloatEnum enumeration."""

    FLOAT = "float"
    NOFLOAT = "noFloat"
