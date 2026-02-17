"""Chapter AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 698)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 329)

JSON Source: docs/json/packages/M2_MSR_Documentation_Chapters.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.MSR.Documentation.Chapters.chapter_model import (
    ChapterModel,
)


class Chapter(Paginateable):
    """AUTOSAR Chapter."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "chapter_model": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=ChapterModel,
        ),  # chapterModel
        "help_entry": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # helpEntry
    }

    def __init__(self) -> None:
        """Initialize Chapter."""
        super().__init__()
        self.chapter_model: ChapterModel = None
        self.help_entry: Optional[String] = None


class ChapterBuilder:
    """Builder for Chapter."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Chapter = Chapter()

    def build(self) -> Chapter:
        """Build and return Chapter object.

        Returns:
            Chapter instance
        """
        # TODO: Add validation
        return self._obj
