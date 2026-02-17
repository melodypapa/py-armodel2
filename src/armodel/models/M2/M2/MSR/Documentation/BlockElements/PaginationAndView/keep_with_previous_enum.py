"""AUTOSAR KeepWithPreviousEnum enumeration.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 339)

JSON Source: packages/M2_MSR_Documentation_BlockElements_PaginationAndView.enums.json"""

from enum import Enum


class KeepWithPreviousEnum(Enum):
    """AUTOSAR KeepWithPreviousEnum enumeration."""

    KEEP = "keep"
    NOKEEP = "noKeep"
