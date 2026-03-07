"""ChapterModel AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 699)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 329)

JSON Source: docs/json/packages/M2_MSR_Documentation_Chapters.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.MSR.Documentation.MsrQuery.msr_query_topic1 import (
    MsrQueryTopic1,
)
from armodel2.models.M2.MSR.Documentation.BlockElements.GerneralParameters.prms import (
    Prms,
)
from armodel2.models.M2.MSR.Documentation.Chapters.topic1 import (
    Topic1,
)
from armodel2.models.M2.MSR.Documentation.Chapters.topic_content_or_msr_query import (
    TopicContentOrMsrQuery,
)

if TYPE_CHECKING:
    from armodel2.models.M2.MSR.Documentation.Chapters.chapter import (
        Chapter,
    )
    from armodel2.models.M2.MSR.Documentation.MsrQuery.msr_query_chapter import (
        MsrQueryChapter,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class ChapterModel(ARObject):
    """AUTOSAR ChapterModel."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "CHAPTER-MODEL"


    chapter: Chapter
    msr_query_chapter: MsrQueryChapter
    prms: Prms
    topic_content_or_msr: Optional[TopicContentOrMsrQuery]
    msr_query: MsrQueryTopic1
    topic1: Topic1
    _DESERIALIZE_DISPATCH = {
        "CHAPTER": lambda obj, elem: setattr(obj, "chapter", SerializationHelper.deserialize_by_tag(elem, "Chapter")),
        "MSR-QUERY-CHAPTER": lambda obj, elem: setattr(obj, "msr_query_chapter", SerializationHelper.deserialize_by_tag(elem, "MsrQueryChapter")),
        "PRMS": lambda obj, elem: setattr(obj, "prms", SerializationHelper.deserialize_by_tag(elem, "Prms")),
        "TOPIC-CONTENT-OR-MSR": lambda obj, elem: setattr(obj, "topic_content_or_msr", SerializationHelper.deserialize_by_tag(elem, "TopicContentOrMsrQuery")),
        "MSR-QUERY": lambda obj, elem: setattr(obj, "msr_query", SerializationHelper.deserialize_by_tag(elem, "MsrQueryTopic1")),
        "TOPIC1": lambda obj, elem: setattr(obj, "topic1", SerializationHelper.deserialize_by_tag(elem, "Topic1")),
    }


    def __init__(self) -> None:
        """Initialize ChapterModel."""
        super().__init__()
        self.chapter: Chapter = None
        self.msr_query_chapter: MsrQueryChapter = None
        self.prms: Prms = None
        self.topic_content_or_msr: Optional[TopicContentOrMsrQuery] = None
        self.msr_query: MsrQueryTopic1 = None
        self.topic1: Topic1 = None

    def serialize(self) -> ET.Element:
        """Serialize ChapterModel to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ChapterModel, self).serialize()

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

        # Serialize prms
        if self.prms is not None:
            serialized = SerializationHelper.serialize_item(self.prms, "Prms")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PRMS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize topic_content_or_msr (atp_mixed - append children directly)
        if self.topic_content_or_msr is not None:
            serialized = SerializationHelper.serialize_item(self.topic_content_or_msr, "TopicContentOrMsrQuery")
            if serialized is not None:
                # atpMixed type: append children directly without wrapper
                if hasattr(serialized, 'attrib'):
                    elem.attrib.update(serialized.attrib)
                # Only copy text if it's a non-empty string (not None or whitespace)
                if serialized.text and serialized.text.strip():
                    elem.text = serialized.text
                for child in serialized:
                    elem.append(child)

        # Serialize msr_query
        if self.msr_query is not None:
            serialized = SerializationHelper.serialize_item(self.msr_query, "MsrQueryTopic1")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MSR-QUERY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize topic1
        if self.topic1 is not None:
            serialized = SerializationHelper.serialize_item(self.topic1, "Topic1")
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
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ChapterModel, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CHAPTER":
                setattr(obj, "chapter", SerializationHelper.deserialize_by_tag(child, "Chapter"))
            elif tag == "MSR-QUERY-CHAPTER":
                setattr(obj, "msr_query_chapter", SerializationHelper.deserialize_by_tag(child, "MsrQueryChapter"))
            elif tag == "PRMS":
                setattr(obj, "prms", SerializationHelper.deserialize_by_tag(child, "Prms"))
            elif tag == "TOPIC-CONTENT-OR-MSR":
                setattr(obj, "topic_content_or_msr", SerializationHelper.deserialize_by_tag(child, "TopicContentOrMsrQuery"))
            elif tag == "MSR-QUERY":
                setattr(obj, "msr_query", SerializationHelper.deserialize_by_tag(child, "MsrQueryTopic1"))
            elif tag == "TOPIC1":
                setattr(obj, "topic1", SerializationHelper.deserialize_by_tag(child, "Topic1"))

        return obj



class ChapterModelBuilder(BuilderBase):
    """Builder for ChapterModel with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ChapterModel = ChapterModel()


    def with_chapter(self, value: Chapter) -> "ChapterModelBuilder":
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

    def with_msr_query_chapter(self, value: MsrQueryChapter) -> "ChapterModelBuilder":
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

    def with_prms(self, value: Prms) -> "ChapterModelBuilder":
        """Set prms attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute 'prms' is required and cannot be None")
        self._obj.prms = value
        return self

    def with_topic_content_or_msr(self, value: Optional[TopicContentOrMsrQuery]) -> "ChapterModelBuilder":
        """Set topic_content_or_msr attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'topic_content_or_msr' is required and cannot be None")
        self._obj.topic_content_or_msr = value
        return self

    def with_msr_query(self, value: MsrQueryTopic1) -> "ChapterModelBuilder":
        """Set msr_query attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute 'msr_query' is required and cannot be None")
        self._obj.msr_query = value
        return self

    def with_topic1(self, value: Topic1) -> "ChapterModelBuilder":
        """Set topic1 attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute 'topic1' is required and cannot be None")
        self._obj.topic1 = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "chapter",
        "chapterContent",
        "topic1",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> ChapterModel:
        """Build and return the ChapterModel instance with validation."""
        self._validate_instance()
        return self._obj