"""NoteTypeEnum enumeration."""

from enum import Enum


class NoteTypeEnum(Enum):
    """AUTOSAR NoteTypeEnum enumeration."""

    CAUTION = "caution"
    EXAMPLE = "example"
    EXERCISE = "exercise"
    HINTINSTRUCTION = "hintinstruction"
    OTHERIN = "otherin"
    TIP = "tip"
