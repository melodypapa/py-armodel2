"""SingleLanguageData module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.MSR.Documentation.TextModel.SingleLanguageData.single_language_unit_names import (
        SingleLanguageUnitNames,
    )
    from armodel.models.M2.MSR.Documentation.TextModel.SingleLanguageData.single_language_long_name import (
        SingleLanguageLongName,
    )
    from armodel.models.M2.MSR.Documentation.TextModel.SingleLanguageData.sl_overview_paragraph import (
        SlOverviewParagraph,
    )
    from armodel.models.M2.MSR.Documentation.TextModel.SingleLanguageData.sl_paragraph import (
        SlParagraph,
    )

__all__ = [
    "SingleLanguageLongName",
    "SingleLanguageUnitNames",
    "SlOverviewParagraph",
    "SlParagraph",
]
