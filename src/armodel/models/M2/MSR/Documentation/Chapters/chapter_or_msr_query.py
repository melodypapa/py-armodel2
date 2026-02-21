"""ChapterOrMsrQuery AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 342)

JSON Source: docs/json/packages/M2_MSR_Documentation_Chapters.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper

if TYPE_CHECKING:
    from armodel.models.M2.MSR.Documentation.Chapters.chapter import (
        Chapter,
    )
    from armodel.models.M2.MSR.Documentation.MsrQuery.msr_query_chapter import (
        MsrQueryChapter,
    )



class ChapterOrMsrQuery(ARObject):
    """AUTOSAR ChapterOrMsrQuery."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    chapter: Chapter
    msr_query_chapter: MsrQueryChapter
    def __init__(self) -> None:
        """Initialize ChapterOrMsrQuery."""
        super().__init__()
        self.chapter: Chapter = None
        self.msr_query_chapter: MsrQueryChapter = None

    def serialize(self) -> ET.Element:
        """Serialize ChapterOrMsrQuery to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ChapterOrMsrQuery, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize chapter
        if self.chapter is not None:
            serialized = SerializationHelper.serialize_item(self.chapter, "Chapter")
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

        # Serialize msr_query_chapter
        if self.msr_query_chapter is not None:
            serialized = SerializationHelper.serialize_item(self.msr_query_chapter, "MsrQueryChapter")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MSR-QUERY-CHAPTER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ChapterOrMsrQuery":
        """Deserialize XML element to ChapterOrMsrQuery object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ChapterOrMsrQuery object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ChapterOrMsrQuery, cls).deserialize(element)

        # Parse chapter
        child = SerializationHelper.find_child_element(element, "CHAPTER")
        if child is not None:
            chapter_value = SerializationHelper.deserialize_by_tag(child, "Chapter")
            obj.chapter = chapter_value

        # Parse msr_query_chapter
        child = SerializationHelper.find_child_element(element, "MSR-QUERY-CHAPTER")
        if child is not None:
            msr_query_chapter_value = SerializationHelper.deserialize_by_tag(child, "MsrQueryChapter")
            obj.msr_query_chapter = msr_query_chapter_value

        return obj



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
