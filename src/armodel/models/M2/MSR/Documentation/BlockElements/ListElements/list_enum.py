"""AUTOSAR ListEnum enumeration.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 295)

JSON Source: packages/M2_MSR_Documentation_BlockElements_ListElements.enums.json"""

from enum import Enum


class ListEnum(Enum):
    """AUTOSAR ListEnum enumeration."""

    NUMBER = "number"
    UNNUMBER = "unnumber"
