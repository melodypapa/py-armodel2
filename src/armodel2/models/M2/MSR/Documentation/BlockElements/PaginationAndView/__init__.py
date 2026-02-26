"""PaginationAndView module."""

from __future__ import annotations
from typing import TYPE_CHECKING

from armodel2.models.M2.MSR.Documentation.BlockElements.PaginationAndView.view_tokens import (
    ViewTokens,
)

if TYPE_CHECKING:
    from armodel2.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
        Paginateable,
    )
    from armodel2.models.M2.MSR.Documentation.BlockElements.PaginationAndView.document_view_selectable import (
        DocumentViewSelectable,
    )

from armodel2.models.M2.MSR.Documentation.BlockElements.PaginationAndView.chapter_enum_break import (
    ChapterEnumBreak,
)
from armodel2.models.M2.MSR.Documentation.BlockElements.PaginationAndView.keep_with_previous_enum import (
    KeepWithPreviousEnum,
)

__all__ = [
    "ChapterEnumBreak",
    "DocumentViewSelectable",
    "KeepWithPreviousEnum",
    "Paginateable",
    "ViewTokens",
]
