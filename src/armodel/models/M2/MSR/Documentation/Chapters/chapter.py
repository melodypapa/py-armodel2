"""Chapter AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 698)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 329)

JSON Source: docs/json/packages/M2_MSR_Documentation_Chapters.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)

if TYPE_CHECKING:
    from armodel.models.M2.MSR.Documentation.Chapters.chapter_model import (
        ChapterModel,
    )



class Chapter(Paginateable):
    """AUTOSAR Chapter."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    chapter_model: ChapterModel
    help_entry: Optional[String]
    def __init__(self) -> None:
        """Initialize Chapter."""
        super().__init__()
        self.chapter_model: ChapterModel = None
        self.help_entry: Optional[String] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "Chapter":
        """Deserialize XML element to Chapter object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Chapter object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse chapter_model
        child = ARObject._find_child_element(element, "CHAPTER-MODEL")
        if child is not None:
            chapter_model_value = ARObject._deserialize_by_tag(child, "ChapterModel")
            obj.chapter_model = chapter_model_value

        # Parse help_entry
        child = ARObject._find_child_element(element, "HELP-ENTRY")
        if child is not None:
            help_entry_value = child.text
            obj.help_entry = help_entry_value

        return obj



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
