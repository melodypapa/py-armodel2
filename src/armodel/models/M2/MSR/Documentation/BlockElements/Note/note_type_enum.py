"""AUTOSAR NoteTypeEnum enumeration.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 311)

JSON Source: packages/M2_MSR_Documentation_BlockElements_Note.enums.json"""

from enum import Enum


class NoteTypeEnum(Enum):
    """AUTOSAR NoteTypeEnum enumeration."""

    CAUTION = "caution"
    EXAMPLE = "example"
    EXERCISE = "exercise"
    HINTINSTRUCTION = "hintinstruction"
    OTHERIN = "otherin"
    TIP = "tip"
