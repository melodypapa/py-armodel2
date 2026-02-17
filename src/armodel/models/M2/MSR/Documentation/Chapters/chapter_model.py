"""ChapterModel AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 699)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 329)

JSON Source: docs/json/packages/M2_MSR_Documentation_Chapters.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.Chapters.chapter_content import (
    ChapterContent,
)
from armodel.models.M2.MSR.Documentation.Chapters.topic_or_msr_query import (
    TopicOrMsrQuery,
)

if TYPE_CHECKING:
    from armodel.models.M2.MSR.Documentation.Chapters.chapter_or_msr_query import (
        ChapterOrMsrQuery,
    )



class ChapterModel(ARObject):
    """AUTOSAR ChapterModel."""

    def __init__(self) -> None:
        """Initialize ChapterModel."""
        super().__init__()
        self.chapter: Optional[ChapterOrMsrQuery] = None
        self.chapter_content: Optional[ChapterContent] = None
        self.topic1: Optional[TopicOrMsrQuery] = None


class ChapterModelBuilder:
    """Builder for ChapterModel."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ChapterModel = ChapterModel()

    def build(self) -> ChapterModel:
        """Build and return ChapterModel object.

        Returns:
            ChapterModel instance
        """
        # TODO: Add validation
        return self._obj
