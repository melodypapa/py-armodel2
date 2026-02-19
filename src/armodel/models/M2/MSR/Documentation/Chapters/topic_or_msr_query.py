"""TopicOrMsrQuery AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 342)

JSON Source: docs/json/packages/M2_MSR_Documentation_Chapters.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.MsrQuery.msr_query_topic1 import (
    MsrQueryTopic1,
)
from armodel.models.M2.MSR.Documentation.Chapters.topic1 import (
    Topic1,
)


class TopicOrMsrQuery(ARObject):
    """AUTOSAR TopicOrMsrQuery."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    msr_query: MsrQueryTopic1
    topic1: Topic1
    def __init__(self) -> None:
        """Initialize TopicOrMsrQuery."""
        super().__init__()
        self.msr_query: MsrQueryTopic1 = None
        self.topic1: Topic1 = None
    def serialize(self) -> ET.Element:
        """Serialize TopicOrMsrQuery to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize msr_query
        if self.msr_query is not None:
            serialized = ARObject._serialize_item(self.msr_query, "MsrQueryTopic1")
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
            serialized = ARObject._serialize_item(self.topic1, "Topic1")
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
    def deserialize(cls, element: ET.Element) -> "TopicOrMsrQuery":
        """Deserialize XML element to TopicOrMsrQuery object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TopicOrMsrQuery object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse msr_query
        child = ARObject._find_child_element(element, "MSR-QUERY")
        if child is not None:
            msr_query_value = ARObject._deserialize_by_tag(child, "MsrQueryTopic1")
            obj.msr_query = msr_query_value

        # Parse topic1
        child = ARObject._find_child_element(element, "TOPIC1")
        if child is not None:
            topic1_value = ARObject._deserialize_by_tag(child, "Topic1")
            obj.topic1 = topic1_value

        return obj



class TopicOrMsrQueryBuilder:
    """Builder for TopicOrMsrQuery."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TopicOrMsrQuery = TopicOrMsrQuery()

    def build(self) -> TopicOrMsrQuery:
        """Build and return TopicOrMsrQuery object.

        Returns:
            TopicOrMsrQuery instance
        """
        # TODO: Add validation
        return self._obj
