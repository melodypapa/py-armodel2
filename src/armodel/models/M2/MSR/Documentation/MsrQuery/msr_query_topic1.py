"""MsrQueryTopic1 AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel.models.M2.MSR.Documentation.MsrQuery.msr_query_props import (
    MsrQueryProps,
)
from armodel.models.M2.MSR.Documentation.MsrQuery.msr_query_result_topic1 import (
    MsrQueryResultTopic1,
)


class MsrQueryTopic1(Paginateable):
    """AUTOSAR MsrQueryTopic1."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("msr_query_props", None, False, False, MsrQueryProps),  # msrQueryProps
        ("msr_query_result_topic1", None, False, False, MsrQueryResultTopic1),  # msrQueryResultTopic1
    ]

    def __init__(self) -> None:
        """Initialize MsrQueryTopic1."""
        super().__init__()
        self.msr_query_props: MsrQueryProps = None
        self.msr_query_result_topic1: Optional[MsrQueryResultTopic1] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert MsrQueryTopic1 to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MsrQueryTopic1":
        """Create MsrQueryTopic1 from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            MsrQueryTopic1 instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to MsrQueryTopic1 since parent returns ARObject
        return cast("MsrQueryTopic1", obj)


class MsrQueryTopic1Builder:
    """Builder for MsrQueryTopic1."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MsrQueryTopic1 = MsrQueryTopic1()

    def build(self) -> MsrQueryTopic1:
        """Build and return MsrQueryTopic1 object.

        Returns:
            MsrQueryTopic1 instance
        """
        # TODO: Add validation
        return self._obj
