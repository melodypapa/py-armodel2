"""Note module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.MSR.Documentation.BlockElements.Note.note import (
        Note,
    )

from armodel.models.M2.MSR.Documentation.BlockElements.Note.note_type_enum import (
    NoteTypeEnum,
)

__all__ = [
    "Note",
    "NoteTypeEnum",
]
