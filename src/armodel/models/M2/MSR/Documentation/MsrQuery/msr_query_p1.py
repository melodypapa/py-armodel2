"""MsrQueryP1 AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel.models.M2.MSR.Documentation.MsrQuery.msr_query_props import (
    MsrQueryProps,
)
from armodel.models.M2.MSR.Documentation.Chapters.topic_content import (
    TopicContent,
)


class MsrQueryP1(Paginateable):
    """AUTOSAR MsrQueryP1."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("msr_query_props", None, False, False, MsrQueryProps),  # msrQueryProps
        ("msr_query_result", None, False, False, TopicContent),  # msrQueryResult
    ]

    def __init__(self) -> None:
        """Initialize MsrQueryP1."""
        super().__init__()
        self.msr_query_props: MsrQueryProps = None
        self.msr_query_result: Optional[TopicContent] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert MsrQueryP1 to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MsrQueryP1":
        """Create MsrQueryP1 from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            MsrQueryP1 instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to MsrQueryP1 since parent returns ARObject
        return cast("MsrQueryP1", obj)


class MsrQueryP1Builder:
    """Builder for MsrQueryP1."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MsrQueryP1 = MsrQueryP1()

    def build(self) -> MsrQueryP1:
        """Build and return MsrQueryP1 object.

        Returns:
            MsrQueryP1 instance
        """
        # TODO: Add validation
        return self._obj
