"""HandleOutOfRangeEnum enumeration."""

from enum import Enum


class HandleOutOfRangeEnum(Enum):
    """AUTOSAR HandleOutOfRangeEnum enumeration."""

    DEFAULT = "default"
    EXTERNALREPLACEMENT = "externalReplacement"
    IGNOREINVALID = "ignoreinvalid"
    NONE = "none"
    SATURATE = "saturate"
