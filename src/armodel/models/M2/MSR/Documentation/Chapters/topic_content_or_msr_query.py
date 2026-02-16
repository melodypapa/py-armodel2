"""TopicContentOrMsrQuery AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.MsrQuery.msr_query_p1 import (
    MsrQueryP1,
)
from armodel.models.M2.MSR.Documentation.Chapters.topic_content import (
    TopicContent,
)


class TopicContentOrMsrQuery(ARObject):
    """AUTOSAR TopicContentOrMsrQuery."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("msr_query_p1", None, False, False, MsrQueryP1),  # msrQueryP1
        ("topic_content", None, False, False, TopicContent),  # topicContent
    ]

    def __init__(self) -> None:
        """Initialize TopicContentOrMsrQuery."""
        super().__init__()
        self.msr_query_p1: MsrQueryP1 = None
        self.topic_content: TopicContent = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TopicContentOrMsrQuery to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TopicContentOrMsrQuery":
        """Create TopicContentOrMsrQuery from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TopicContentOrMsrQuery instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TopicContentOrMsrQuery since parent returns ARObject
        return cast("TopicContentOrMsrQuery", obj)


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
