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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    chapter: Optional[ChapterOrMsrQuery]
    chapter_content: Optional[ChapterContent]
    topic1: Optional[TopicOrMsrQuery]
    def __init__(self) -> None:
        """Initialize ChapterModel."""
        super().__init__()
        self.chapter: Optional[ChapterOrMsrQuery] = None
        self.chapter_content: Optional[ChapterContent] = None
        self.topic1: Optional[TopicOrMsrQuery] = None
    def serialize(self) -> ET.Element:
        """Serialize ChapterModel to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # Serialize chapter
        if self.chapter is not None:
            serialized = ARObject._serialize_item(self.chapter, "ChapterOrMsrQuery")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CHAPTER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize chapter_content
        if self.chapter_content is not None:
            serialized = ARObject._serialize_item(self.chapter_content, "ChapterContent")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CHAPTER-CONTENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize topic1
        if self.topic1 is not None:
            serialized = ARObject._serialize_item(self.topic1, "TopicOrMsrQuery")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TOPIC1")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ChapterModel":
        """Deserialize XML element to ChapterModel object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ChapterModel object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse chapter
        child = ARObject._find_child_element(element, "CHAPTER")
        if child is not None:
            chapter_value = ARObject._deserialize_by_tag(child, "ChapterOrMsrQuery")
            obj.chapter = chapter_value

        # Parse chapter_content
        child = ARObject._find_child_element(element, "CHAPTER-CONTENT")
        if child is not None:
            chapter_content_value = ARObject._deserialize_by_tag(child, "ChapterContent")
            obj.chapter_content = chapter_content_value

        # Parse topic1
        child = ARObject._find_child_element(element, "TOPIC1")
        if child is not None:
            topic1_value = ARObject._deserialize_by_tag(child, "TopicOrMsrQuery")
            obj.topic1 = topic1_value

        return obj



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
