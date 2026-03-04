"""ChapterContent AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 330)

JSON Source: docs/json/packages/M2_MSR_Documentation_Chapters.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel2.serialization.decorators import atp_mixed

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.MSR.Documentation.MsrQuery.msr_query_p1 import (
    MsrQueryP1,
)
from armodel2.models.M2.MSR.Documentation.BlockElements.GerneralParameters.prms import (
    Prms,
)
from armodel2.models.M2.MSR.Documentation.Chapters.topic_content import (
    TopicContent,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


@atp_mixed()

class ChapterContent(ARObject):
    """AUTOSAR ChapterContent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "CHAPTER-CONTENT"


    prms: Prms
    msr_query_p1: MsrQueryP1
    topic_content: TopicContent
    _DESERIALIZE_DISPATCH = {
        "PRMS": lambda obj, elem: setattr(obj, "prms", SerializationHelper.deserialize_by_tag(elem, "Prms")),
        "MSR-QUERY-P1": lambda obj, elem: setattr(obj, "msr_query_p1", SerializationHelper.deserialize_by_tag(elem, "MsrQueryP1")),
        "TOPIC-CONTENT": lambda obj, elem: setattr(obj, "topic_content", SerializationHelper.deserialize_by_tag(elem, "TopicContent")),
    }


    def __init__(self) -> None:
        """Initialize ChapterContent."""
        super().__init__()
        self.prms: Prms = None
        self.msr_query_p1: MsrQueryP1 = None
        self.topic_content: TopicContent = None

    def serialize(self) -> ET.Element:
        """Serialize ChapterContent to XML element (atp_mixed - no wrapping).

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ChapterContent, self).serialize()

        # Copy all attributes from parent element to current element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element to current element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element to current element
        for child in parent_elem:
            elem.append(child)

        # Serialize prms (complex type)
        if self.prms is not None:
            serialized = SerializationHelper.serialize_item(self.prms, "Prms")
            if serialized is not None:
                wrapped = ET.Element("PRMS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize msr_query_p1 (complex type)
        if self.msr_query_p1 is not None:
            serialized = SerializationHelper.serialize_item(self.msr_query_p1, "MsrQueryP1")
            if serialized is not None:
                wrapped = ET.Element("MSR-QUERY-P1")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize topic_content (complex type)
        if self.topic_content is not None:
            serialized = SerializationHelper.serialize_item(self.topic_content, "TopicContent")
            if serialized is not None:
                wrapped = ET.Element("TOPIC-CONTENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ChapterContent":
        """Deserialize XML element to ChapterContent object (atp_mixed - no unwrapping).

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ChapterContent object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ChapterContent, cls).deserialize(element)

        # Parse prms
        child = SerializationHelper.find_child_element(element, "PRMS")
        if child is not None:
            prms_value = SerializationHelper.deserialize_by_tag(child, "Prms")
            obj.prms = prms_value

        # Parse msr_query_p1
        child = SerializationHelper.find_child_element(element, "MSR-QUERY-P1")
        if child is not None:
            msr_query_p1_value = SerializationHelper.deserialize_by_tag(child, "MsrQueryP1")
            obj.msr_query_p1 = msr_query_p1_value

        # Parse topic_content
        child = SerializationHelper.find_child_element(element, "TOPIC-CONTENT")
        if child is not None:
            topic_content_value = SerializationHelper.deserialize_by_tag(child, "TopicContent")
            obj.topic_content = topic_content_value

        return obj



class ChapterContentBuilder(BuilderBase):
    """Builder for ChapterContent with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ChapterContent = ChapterContent()


    def with_prms(self, value: Prms) -> "ChapterContentBuilder":
        """Set prms attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.prms = value
        return self

    def with_msr_query_p1(self, value: MsrQueryP1) -> "ChapterContentBuilder":
        """Set msr_query_p1 attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.msr_query_p1 = value
        return self

    def with_topic_content(self, value: TopicContent) -> "ChapterContentBuilder":
        """Set topic_content attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.topic_content = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _REQUIRED_ATTRIBUTES = {
        "prms",
    }
    _OPTIONAL_ATTRIBUTES = {
        "topicContentOrMsr",
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
        if getattr(self._obj, "prms", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError("Required attribute 'prms' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn("Required attribute 'prms' is None", UserWarning)


    def build(self) -> ChapterContent:
        """Build and return the ChapterContent instance with validation."""
        self._validate_instance()
        return self._obj