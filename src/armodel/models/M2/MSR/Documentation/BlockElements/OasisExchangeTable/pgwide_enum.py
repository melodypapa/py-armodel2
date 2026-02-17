"""AUTOSAR PgwideEnum enumeration.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 348)

JSON Source: packages/M2_MSR_Documentation_BlockElements_OasisExchangeTable.enums.json"""

from enum import Enum


class PgwideEnum(Enum):
    """AUTOSAR PgwideEnum enumeration."""

    NOPGWIDE = "noPgwide"
    GENERIC = "Generic"
    AUTOSAR = "AUTOSAR"
    PGWIDE = "pgwide"
