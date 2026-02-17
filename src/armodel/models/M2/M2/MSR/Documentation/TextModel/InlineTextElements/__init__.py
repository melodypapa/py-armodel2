"""InlineTextElements module."""

from __future__ import annotations
from typing import TYPE_CHECKING

from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements.superscript import (
    Superscript,
)

if TYPE_CHECKING:
    from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements.br import (
        Br,
    )
    from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements.emphasis_text import (
        EmphasisText,
    )
    from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements.index_entry import (
        IndexEntry,
    )
    from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements.std import (
        Std,
    )
    from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements.tt import (
        Tt,
    )
    from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements.xdoc import (
        Xdoc,
    )
    from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements.xfile import (
        Xfile,
    )
    from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements.xref import (
        Xref,
    )
    from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements.xref_target import (
        XrefTarget,
    )

__all__ = [
    "Br",
    "EmphasisText",
    "IndexEntry",
    "Std",
    "Superscript",
    "Tt",
    "Xdoc",
    "Xfile",
    "Xref",
    "XrefTarget",
]
