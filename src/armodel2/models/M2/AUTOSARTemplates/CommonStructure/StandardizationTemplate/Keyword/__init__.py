"""Keyword module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.Keyword.keyword import (
        Keyword,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.Keyword.keyword_set import (
        KeywordSet,
    )

__all__ = [
    "Keyword",
    "KeywordSet",
]
