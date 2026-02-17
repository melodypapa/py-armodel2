"""AUTOSAR FrameEnum enumeration.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 334)

JSON Source: packages/M2_MSR_Documentation_BlockElements_OasisExchangeTable.enums.json"""

from enum import Enum


class FrameEnum(Enum):
    """AUTOSAR FrameEnum enumeration."""

    ALL = "all"
    BOTTOM = "bottom"
    NONE = "none"
    SIDES = "sides"
    TOP = "top"
    TOPBOT = "topbot"
