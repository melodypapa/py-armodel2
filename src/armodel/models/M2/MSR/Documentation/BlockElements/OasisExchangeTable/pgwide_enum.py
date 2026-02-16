"""PgwideEnum enumeration."""

from enum import Enum


class PgwideEnum(Enum):
    """AUTOSAR PgwideEnum enumeration."""

    NOPGWIDE = "noPgwide"
    GENERIC = "Generic"
    AUTOSAR = "AUTOSAR"
    PGWIDE = "pgwide"
