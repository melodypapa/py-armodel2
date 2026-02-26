"""MultilanguageData module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_overview_paragraph import (
        MultiLanguageOverviewParagraph,
    )
    from armodel2.models.M2.MSR.Documentation.TextModel.MultilanguageData.multilanguage_long_name import (
        MultilanguageLongName,
    )
    from armodel2.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_paragraph import (
        MultiLanguageParagraph,
    )
    from armodel2.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_verbatim import (
        MultiLanguageVerbatim,
    )
    from armodel2.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_plain_text import (
        MultiLanguagePlainText,
    )

__all__ = [
    "MultiLanguageOverviewParagraph",
    "MultiLanguageParagraph",
    "MultiLanguagePlainText",
    "MultiLanguageVerbatim",
    "MultilanguageLongName",
]
