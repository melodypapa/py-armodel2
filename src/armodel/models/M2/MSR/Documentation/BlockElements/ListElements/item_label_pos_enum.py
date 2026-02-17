"""AUTOSAR ItemLabelPosEnum enumeration.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 297)

JSON Source: packages/M2_MSR_Documentation_BlockElements_ListElements.enums.json"""

from enum import Enum


class ItemLabelPosEnum(Enum):
    """AUTOSAR ItemLabelPosEnum enumeration."""

    NEWLINE = "newline"
    NEWLINEIFNECESSARY = "newlineIfNecessary"
    NONEWLINE = "noNewline"
