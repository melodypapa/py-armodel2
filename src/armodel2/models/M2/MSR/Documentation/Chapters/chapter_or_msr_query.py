"""ChapterOrMsrQuery AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 342)

JSON Source: docs/json/packages/M2_MSR_Documentation_Chapters.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel2.serialization.decorators import atp_mixed

from armodel2.models.M2.builder_base import BuilderBase

if TYPE_CHECKING:
    from armodel2.models.M2.MSR.Documentation.Chapters.chapter import (
        Chapter,
    )
    from armodel2.models.M2.MSR.Documentation.MsrQuery.msr_query_chapter import (
        MsrQueryChapter,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
@atp_mixed()

class ChapterOrMsrQuery(ARObject):
    """AUTOSAR ChapterOrMsrQuery."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "CHAPTER-OR-MSR-QUERY"


    chapter: Chapter
    msr_query_chapter: MsrQueryChapter
    _DESERIALIZE_DISPATCH = {
        "CHAPTER": lambda obj, elem: setattr(obj, "chapter", SerializationHelper.deserialize_by_tag(elem, "Chapter")),
        "MSR-QUERY-CHAPTER": lambda obj, elem: setattr(obj, "msr_query_chapter", SerializationHelper.deserialize_by_tag(elem, "MsrQueryChapter")),
    }


    def __init__(self) -> None:
        """Initialize ChapterOrMsrQuery."""
        super().__init__()
        self.chapter: Chapter = None
        self.msr_query_chapter: MsrQueryChapter = None

    def serialize(self) -> ET.Element:
        """Serialize ChapterOrMsrQuery to XML element (atp_mixed - no wrapping).

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ChapterOrMsrQuery, self).serialize()

        # Copy all attributes from parent element to current element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element to current element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element to current element
        for child in parent_elem:
            elem.append(child)

        # Serialize chapter (complex type)
        if self.chapter is not None:
            serialized = SerializationHelper.serialize_item(self.chapter, "Chapter")
            if serialized is not None:
                wrapped = ET.Element("CHAPTER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize msr_query_chapter (complex type)
        if self.msr_query_chapter is not None:
            serialized = SerializationHelper.serialize_item(self.msr_query_chapter, "MsrQueryChapter")
            if serialized is not None:
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
        """Deserialize XML element to ChapterOrMsrQuery object (atp_mixed - no unwrapping).

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



class ChapterOrMsrQueryBuilder(BuilderBase):
    """Builder for ChapterOrMsrQuery with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ChapterOrMsrQuery = ChapterOrMsrQuery()


    def with_chapter(self, value: Chapter) -> "ChapterOrMsrQueryBuilder":
        """Set chapter attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute 'chapter' is required and cannot be None")
        self._obj.chapter = value
        return self

    def with_msr_query_chapter(self, value: MsrQueryChapter) -> "ChapterOrMsrQueryBuilder":
        """Set msr_query_chapter attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute 'msr_query_chapter' is required and cannot be None")
        self._obj.msr_query_chapter = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _REQUIRED_ATTRIBUTES = {
        "chapter",
        "msrQueryChapter",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Validate required attributes using pre-computed constants (O(1) lookup)
        # This is much faster than calling get_type_hints() at runtime
        if getattr(self._obj, "chapter", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError("Required attribute 'chapter' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn("Required attribute 'chapter' is None", UserWarning)
        if getattr(self._obj, "msrQueryChapter", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError("Required attribute 'msrQueryChapter' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn("Required attribute 'msrQueryChapter' is None", UserWarning)


    def build(self) -> ChapterOrMsrQuery:
        """Build and return the ChapterOrMsrQuery instance with validation."""
        self._validate_instance()
        return self._obj