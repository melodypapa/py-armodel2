"""HandleInvalidEnum enumeration."""

from enum import Enum


class HandleInvalidEnum(Enum):
    """AUTOSAR HandleInvalidEnum enumeration."""

    DONTINVALIDATE = "dontInvalidate"
    EXTERNAL = "external"
    KEEP = "keep"
    REPLACE = "replace"
