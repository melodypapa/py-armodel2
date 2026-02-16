"""Chapter AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
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
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("chapter_model", None, False, False, ChapterModel),  # chapterModel
        ("help_entry", None, True, False, None),  # helpEntry
    ]

    def __init__(self) -> None:
        """Initialize Chapter."""
        super().__init__()
        self.chapter_model: ChapterModel = None
        self.help_entry: Optional[String] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert Chapter to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Chapter":
        """Create Chapter from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            Chapter instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to Chapter since parent returns ARObject
        return cast("Chapter", obj)


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
