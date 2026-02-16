"""ChapterModel AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.Chapters.chapter_content import (
    ChapterContent,
)
from armodel.models.M2.MSR.Documentation.Chapters.chapter_or_msr_query import (
    ChapterOrMsrQuery,
)
from armodel.models.M2.MSR.Documentation.Chapters.topic_or_msr_query import (
    TopicOrMsrQuery,
)


class ChapterModel(ARObject):
    """AUTOSAR ChapterModel."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("chapter", None, False, False, ChapterOrMsrQuery),  # chapter
        ("chapter_content", None, False, False, ChapterContent),  # chapterContent
        ("topic1", None, False, False, TopicOrMsrQuery),  # topic1
    ]

    def __init__(self) -> None:
        """Initialize ChapterModel."""
        super().__init__()
        self.chapter: Optional[ChapterOrMsrQuery] = None
        self.chapter_content: Optional[ChapterContent] = None
        self.topic1: Optional[TopicOrMsrQuery] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ChapterModel to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ChapterModel":
        """Create ChapterModel from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ChapterModel instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ChapterModel since parent returns ARObject
        return cast("ChapterModel", obj)


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
