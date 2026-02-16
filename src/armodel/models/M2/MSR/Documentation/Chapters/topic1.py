"""Topic1 AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.MSR.Documentation.Chapters.topic_content_or_msr_query import (
    TopicContentOrMsrQuery,
)


class Topic1(Paginateable):
    """AUTOSAR Topic1."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("help_entry", None, True, False, None),  # helpEntry
        ("topic_content_or_msr", None, False, False, TopicContentOrMsrQuery),  # topicContentOrMsr
    ]

    def __init__(self) -> None:
        """Initialize Topic1."""
        super().__init__()
        self.help_entry: Optional[String] = None
        self.topic_content_or_msr: Optional[TopicContentOrMsrQuery] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert Topic1 to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Topic1":
        """Create Topic1 from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            Topic1 instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to Topic1 since parent returns ARObject
        return cast("Topic1", obj)


class Topic1Builder:
    """Builder for Topic1."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Topic1 = Topic1()

    def build(self) -> Topic1:
        """Build and return Topic1 object.

        Returns:
            Topic1 instance
        """
        # TODO: Add validation
        return self._obj
