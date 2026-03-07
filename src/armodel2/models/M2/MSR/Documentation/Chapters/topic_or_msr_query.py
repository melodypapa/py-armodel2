"""TopicOrMsrQuery AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 342)

JSON Source: docs/json/packages/M2_MSR_Documentation_Chapters.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel2.serialization.decorators import atp_mixed

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.MSR.Documentation.MsrQuery.msr_query_topic1 import (
    MsrQueryTopic1,
)
from armodel2.models.M2.MSR.Documentation.Chapters.topic1 import (
    Topic1,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


@atp_mixed()

class TopicOrMsrQuery(ARObject):
    """AUTOSAR TopicOrMsrQuery."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "TOPIC-OR-MSR-QUERY"


    msr_query: MsrQueryTopic1
    topic1: Topic1
    _DESERIALIZE_DISPATCH = {
        "MSR-QUERY": lambda obj, elem: setattr(obj, "msr_query", SerializationHelper.deserialize_by_tag(elem, "MsrQueryTopic1")),
        "TOPIC1": lambda obj, elem: setattr(obj, "topic1", SerializationHelper.deserialize_by_tag(elem, "Topic1")),
    }


    def __init__(self) -> None:
        """Initialize TopicOrMsrQuery."""
        super().__init__()
        self.msr_query: MsrQueryTopic1 = None
        self.topic1: Topic1 = None

    def serialize(self) -> ET.Element:
        """Serialize TopicOrMsrQuery to XML element (atp_mixed - no wrapping).

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TopicOrMsrQuery, self).serialize()

        # Copy all attributes from parent element to current element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element to current element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element to current element
        for child in parent_elem:
            elem.append(child)

        # Serialize msr_query (complex type)
        if self.msr_query is not None:
            serialized = SerializationHelper.serialize_item(self.msr_query, "MsrQueryTopic1")
            if serialized is not None:
                wrapped = ET.Element("MSR-QUERY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize topic1 (complex type)
        if self.topic1 is not None:
            serialized = SerializationHelper.serialize_item(self.topic1, "Topic1")
            if serialized is not None:
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
    def deserialize(cls, element: ET.Element) -> "TopicOrMsrQuery":
        """Deserialize XML element to TopicOrMsrQuery object (atp_mixed - no unwrapping).

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TopicOrMsrQuery object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TopicOrMsrQuery, cls).deserialize(element)

        # Parse msr_query
        child = SerializationHelper.find_child_element(element, "MSR-QUERY")
        if child is not None:
            msr_query_value = SerializationHelper.deserialize_by_tag(child, "MsrQueryTopic1")
            obj.msr_query = msr_query_value

        # Parse topic1
        child = SerializationHelper.find_child_element(element, "TOPIC1")
        if child is not None:
            topic1_value = SerializationHelper.deserialize_by_tag(child, "Topic1")
            obj.topic1 = topic1_value

        return obj



class TopicOrMsrQueryBuilder(BuilderBase):
    """Builder for TopicOrMsrQuery with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TopicOrMsrQuery = TopicOrMsrQuery()


    def with_msr_query(self, value: MsrQueryTopic1) -> "TopicOrMsrQueryBuilder":
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

    def with_topic1(self, value: Topic1) -> "TopicOrMsrQueryBuilder":
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
    _REQUIRED_ATTRIBUTES = {
        "msrQuery",
        "topic1",
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
        if getattr(self._obj, "msrQuery", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError("Required attribute 'msrQuery' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn("Required attribute 'msrQuery' is None", UserWarning)
        if getattr(self._obj, "topic1", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError("Required attribute 'topic1' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn("Required attribute 'topic1' is None", UserWarning)


    def build(self) -> TopicOrMsrQuery:
        """Build and return the TopicOrMsrQuery instance with validation."""
        self._validate_instance()
        return self._obj