"""ChapterContent AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 330)

JSON Source: docs/json/packages/M2_MSR_Documentation_Chapters.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.BlockElements.GerneralParameters.prms import (
    Prms,
)
from armodel.models.M2.MSR.Documentation.Chapters.topic_content_or_msr_query import (
    TopicContentOrMsrQuery,
)


class ChapterContent(ARObject):
    """AUTOSAR ChapterContent."""

    prms: Prms
    topic_content_or_msr: Optional[TopicContentOrMsrQuery]
    def __init__(self) -> None:
        """Initialize ChapterContent."""
        super().__init__()
        self.prms: Prms = None
        self.topic_content_or_msr: Optional[TopicContentOrMsrQuery] = None


class ChapterContentBuilder:
    """Builder for ChapterContent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ChapterContent = ChapterContent()

    def build(self) -> ChapterContent:
        """Build and return ChapterContent object.

        Returns:
            ChapterContent instance
        """
        # TODO: Add validation
        return self._obj
