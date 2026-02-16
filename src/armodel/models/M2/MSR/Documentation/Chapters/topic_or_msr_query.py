"""TopicOrMsrQuery AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.MsrQuery.msr_query_topic1 import (
    MsrQueryTopic1,
)
from armodel.models.M2.MSR.Documentation.Chapters.topic1 import (
    Topic1,
)


class TopicOrMsrQuery(ARObject):
    """AUTOSAR TopicOrMsrQuery."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("msr_query", None, False, False, MsrQueryTopic1),  # msrQuery
        ("topic1", None, False, False, Topic1),  # topic1
    ]

    def __init__(self) -> None:
        """Initialize TopicOrMsrQuery."""
        super().__init__()
        self.msr_query: MsrQueryTopic1 = None
        self.topic1: Topic1 = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TopicOrMsrQuery to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TopicOrMsrQuery":
        """Create TopicOrMsrQuery from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TopicOrMsrQuery instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TopicOrMsrQuery since parent returns ARObject
        return cast("TopicOrMsrQuery", obj)


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
