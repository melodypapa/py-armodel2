"""ChapterOrMsrQuery AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 342)

JSON Source: docs/json/packages/M2_MSR_Documentation_Chapters.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "chapter": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class="Chapter",
        ),  # chapter
        "msr_query_chapter": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class="MsrQueryChapter",
        ),  # msrQueryChapter
    }

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
