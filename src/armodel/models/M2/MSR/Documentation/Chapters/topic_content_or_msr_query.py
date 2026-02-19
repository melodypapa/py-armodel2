"""TopicContentOrMsrQuery AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 342)

JSON Source: docs/json/packages/M2_MSR_Documentation_Chapters.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.MsrQuery.msr_query_p1 import (
    MsrQueryP1,
)
from armodel.models.M2.MSR.Documentation.Chapters.topic_content import (
    TopicContent,
)


class TopicContentOrMsrQuery(ARObject):
    """AUTOSAR TopicContentOrMsrQuery."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    msr_query_p1: MsrQueryP1
    topic_content: TopicContent
    def __init__(self) -> None:
        """Initialize TopicContentOrMsrQuery."""
        super().__init__()
        self.msr_query_p1: MsrQueryP1 = None
        self.topic_content: TopicContent = None
    def serialize(self) -> ET.Element:
        """Serialize TopicContentOrMsrQuery to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize msr_query_p1
        if self.msr_query_p1 is not None:
            serialized = ARObject._serialize_item(self.msr_query_p1, "MsrQueryP1")
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

        # Serialize topic_content
        if self.topic_content is not None:
            serialized = ARObject._serialize_item(self.topic_content, "TopicContent")
            if serialized is not None:
                # Wrap with correct tag
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
    def deserialize(cls, element: ET.Element) -> "TopicContentOrMsrQuery":
        """Deserialize XML element to TopicContentOrMsrQuery object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TopicContentOrMsrQuery object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse msr_query_p1
        child = ARObject._find_child_element(element, "MSR-QUERY-P1")
        if child is not None:
            msr_query_p1_value = ARObject._deserialize_by_tag(child, "MsrQueryP1")
            obj.msr_query_p1 = msr_query_p1_value

        # Parse topic_content
        child = ARObject._find_child_element(element, "TOPIC-CONTENT")
        if child is not None:
            topic_content_value = ARObject._deserialize_by_tag(child, "TopicContent")
            obj.topic_content = topic_content_value

        return obj



class TopicContentOrMsrQueryBuilder:
    """Builder for TopicContentOrMsrQuery."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TopicContentOrMsrQuery = TopicContentOrMsrQuery()

    def build(self) -> TopicContentOrMsrQuery:
        """Build and return TopicContentOrMsrQuery object.

        Returns:
            TopicContentOrMsrQuery instance
        """
        # TODO: Add validation
        return self._obj
