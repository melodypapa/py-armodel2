"""MsrQueryChapter AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel.models.M2.MSR.Documentation.MsrQuery.msr_query_props import (
    MsrQueryProps,
)
from armodel.models.M2.MSR.Documentation.MsrQuery.msr_query_result_chapter import (
    MsrQueryResultChapter,
)


class MsrQueryChapter(Paginateable):
    """AUTOSAR MsrQueryChapter."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("msr_query_props", None, False, False, MsrQueryProps),  # msrQueryProps
        ("msr_query_result_chapter", None, False, False, MsrQueryResultChapter),  # msrQueryResultChapter
    ]

    def __init__(self) -> None:
        """Initialize MsrQueryChapter."""
        super().__init__()
        self.msr_query_props: MsrQueryProps = None
        self.msr_query_result_chapter: Optional[MsrQueryResultChapter] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert MsrQueryChapter to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MsrQueryChapter":
        """Create MsrQueryChapter from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            MsrQueryChapter instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to MsrQueryChapter since parent returns ARObject
        return cast("MsrQueryChapter", obj)


class MsrQueryChapterBuilder:
    """Builder for MsrQueryChapter."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MsrQueryChapter = MsrQueryChapter()

    def build(self) -> MsrQueryChapter:
        """Build and return MsrQueryChapter object.

        Returns:
            MsrQueryChapter instance
        """
        # TODO: Add validation
        return self._obj
