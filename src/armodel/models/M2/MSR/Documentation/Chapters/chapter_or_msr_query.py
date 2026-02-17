"""ChapterOrMsrQuery AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 342)

JSON Source: docs/json/packages/M2_MSR_Documentation_Chapters.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject

if TYPE_CHECKING:
    from armodel.models.M2.MSR.Documentation.Chapters.chapter import (
        Chapter,
    )
    from armodel.models.M2.MSR.Documentation.MsrQuery.msr_query_chapter import (
        MsrQueryChapter,
    )



class ChapterOrMsrQuery(ARObject):
    """AUTOSAR ChapterOrMsrQuery."""

    chapter: Chapter
    msr_query_chapter: MsrQueryChapter
    def __init__(self) -> None:
        """Initialize ChapterOrMsrQuery."""
        super().__init__()
        self.chapter: Chapter = None
        self.msr_query_chapter: MsrQueryChapter = None


class ChapterOrMsrQueryBuilder:
    """Builder for ChapterOrMsrQuery."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ChapterOrMsrQuery = ChapterOrMsrQuery()

    def build(self) -> ChapterOrMsrQuery:
        """Build and return ChapterOrMsrQuery object.

        Returns:
            ChapterOrMsrQuery instance
        """
        # TODO: Add validation
        return self._obj
