"""LanguageDataModel module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.MSR.Documentation.TextModel.LanguageDataModel.l_long_name import (
        LLongName,
    )
    from armodel2.models.M2.MSR.Documentation.TextModel.LanguageDataModel.whitespace_controlled import (
        WhitespaceControlled,
    )
    from armodel2.models.M2.MSR.Documentation.TextModel.LanguageDataModel.l_verbatim import (
        LVerbatim,
    )
    from armodel2.models.M2.MSR.Documentation.TextModel.LanguageDataModel.l_overview_paragraph import (
        LOverviewParagraph,
    )
    from armodel2.models.M2.MSR.Documentation.TextModel.LanguageDataModel.l_paragraph import (
        LParagraph,
    )
    from armodel2.models.M2.MSR.Documentation.TextModel.LanguageDataModel.l_plain_text import (
        LPlainText,
    )
    from armodel2.models.M2.MSR.Documentation.TextModel.LanguageDataModel.language_specific import (
        LanguageSpecific,
    )

from armodel2.models.M2.MSR.Documentation.TextModel.LanguageDataModel.l_enum import (
    LEnum,
)

__all__ = [
    "LEnum",
    "LLongName",
    "LOverviewParagraph",
    "LParagraph",
    "LPlainText",
    "LVerbatim",
    "LanguageSpecific",
    "WhitespaceControlled",
]
