"""Topic1 AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 338)

JSON Source: docs/json/packages/M2_MSR_Documentation_Chapters.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import PaginateableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel2.models.M2.MSR.Documentation.MsrQuery.msr_query_p1 import (
    MsrQueryP1,
)
from armodel2.models.M2.MSR.Documentation.Chapters.topic_content import (
    TopicContent,
)
from armodel2.models.M2.MSR.Documentation.Chapters.topic_content_or_msr_query import (
    TopicContentOrMsrQuery,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class Topic1(Paginateable):
    """AUTOSAR Topic1."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "TOPIC1"


    help_entry: Optional[String]
    topic_content_or_msr: Optional[TopicContentOrMsrQuery]
    msr_query_p1: MsrQueryP1
    topic_content: TopicContent
    _DESERIALIZE_DISPATCH = {
        "HELP-ENTRY": lambda obj, elem: setattr(obj, "help_entry", SerializationHelper.deserialize_by_tag(elem, "String")),
        "TOPIC-CONTENT-OR-MSR": lambda obj, elem: setattr(obj, "topic_content_or_msr", SerializationHelper.deserialize_by_tag(elem, "TopicContentOrMsrQuery")),
        "MSR-QUERY-P1": lambda obj, elem: setattr(obj, "msr_query_p1", SerializationHelper.deserialize_by_tag(elem, "MsrQueryP1")),
        "TOPIC-CONTENT": lambda obj, elem: setattr(obj, "topic_content", SerializationHelper.deserialize_by_tag(elem, "TopicContent")),
    }


    def __init__(self) -> None:
        """Initialize Topic1."""
        super().__init__()
        self.help_entry: Optional[String] = None
        self.topic_content_or_msr: Optional[TopicContentOrMsrQuery] = None
        self.msr_query_p1: MsrQueryP1 = None
        self.topic_content: TopicContent = None

    def serialize(self) -> ET.Element:
        """Serialize Topic1 to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Topic1, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize help_entry
        if self.help_entry is not None:
            serialized = SerializationHelper.serialize_item(self.help_entry, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HELP-ENTRY")
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

        # Serialize msr_query_p1
        if self.msr_query_p1 is not None:
            serialized = SerializationHelper.serialize_item(self.msr_query_p1, "MsrQueryP1")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MSR-QUERY-P1")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize topic_content (atp_mixed - append children directly)
        if self.topic_content is not None:
            serialized = SerializationHelper.serialize_item(self.topic_content, "TopicContent")
            if serialized is not None:
                # atpMixed type: append children directly without wrapper
                if hasattr(serialized, 'attrib'):
                    elem.attrib.update(serialized.attrib)
                # Only copy text if it's a non-empty string (not None or whitespace)
                if serialized.text and serialized.text.strip():
                    elem.text = serialized.text
                for child in serialized:
                    elem.append(child)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Topic1":
        """Deserialize XML element to Topic1 object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Topic1 object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Topic1, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "HELP-ENTRY":
                setattr(obj, "help_entry", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "TOPIC-CONTENT-OR-MSR":
                setattr(obj, "topic_content_or_msr", SerializationHelper.deserialize_by_tag(child, "TopicContentOrMsrQuery"))
            elif tag == "MSR-QUERY-P1":
                setattr(obj, "msr_query_p1", SerializationHelper.deserialize_by_tag(child, "MsrQueryP1"))
            elif tag == "TOPIC-CONTENT":
                setattr(obj, "topic_content", SerializationHelper.deserialize_by_tag(child, "TopicContent"))

        return obj



class Topic1Builder(PaginateableBuilder):
    """Builder for Topic1 with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: Topic1 = Topic1()


    def with_help_entry(self, value: Optional[String]) -> "Topic1Builder":
        """Set help_entry attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'help_entry' is required and cannot be None")
        self._obj.help_entry = value
        return self

    def with_topic_content_or_msr(self, value: Optional[TopicContentOrMsrQuery]) -> "Topic1Builder":
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

    def with_msr_query_p1(self, value: MsrQueryP1) -> "Topic1Builder":
        """Set msr_query_p1 attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute 'msr_query_p1' is required and cannot be None")
        self._obj.msr_query_p1 = value
        return self

    def with_topic_content(self, value: TopicContent) -> "Topic1Builder":
        """Set topic_content attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute 'topic_content' is required and cannot be None")
        self._obj.topic_content = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "helpEntry",
        "topicContentOrMsr",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> Topic1:
        """Build and return the Topic1 instance with validation."""
        self._validate_instance()
        return self._obj