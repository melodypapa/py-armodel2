"""Chapters module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.MSR.Documentation.Chapters.chapter import (
        Chapter,
    )
    from armodel.models.M2.MSR.Documentation.Chapters.chapter_model import (
        ChapterModel,
    )
    from armodel.models.M2.MSR.Documentation.Chapters.chapter_content import (
        ChapterContent,
    )
    from armodel.models.M2.MSR.Documentation.Chapters.predefined_chapter import (
        PredefinedChapter,
    )
    from armodel.models.M2.MSR.Documentation.Chapters.topic1 import (
        Topic1,
    )
    from armodel.models.M2.MSR.Documentation.Chapters.topic_content_or_msr_query import (
        TopicContentOrMsrQuery,
    )
    from armodel.models.M2.MSR.Documentation.Chapters.topic_or_msr_query import (
        TopicOrMsrQuery,
    )
    from armodel.models.M2.MSR.Documentation.Chapters.chapter_or_msr_query import (
        ChapterOrMsrQuery,
    )
    from armodel.models.M2.MSR.Documentation.Chapters.topic_content import (
        TopicContent,
    )

__all__ = [
    "Chapter",
    "ChapterContent",
    "ChapterModel",
    "ChapterOrMsrQuery",
    "PredefinedChapter",
    "Topic1",
    "TopicContent",
    "TopicContentOrMsrQuery",
    "TopicOrMsrQuery",
]
