"""ChapterOrMsrQuery AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.Chapters.chapter import (
    Chapter,
)
from armodel.models.M2.MSR.Documentation.MsrQuery.msr_query_chapter import (
    MsrQueryChapter,
)


class ChapterOrMsrQuery(ARObject):
    """AUTOSAR ChapterOrMsrQuery."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("chapter", None, False, False, Chapter),  # chapter
        ("msr_query_chapter", None, False, False, MsrQueryChapter),  # msrQueryChapter
    ]

    def __init__(self) -> None:
        """Initialize ChapterOrMsrQuery."""
        super().__init__()
        self.chapter: Chapter = None
        self.msr_query_chapter: MsrQueryChapter = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ChapterOrMsrQuery to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ChapterOrMsrQuery":
        """Create ChapterOrMsrQuery from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ChapterOrMsrQuery instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ChapterOrMsrQuery since parent returns ARObject
        return cast("ChapterOrMsrQuery", obj)


class ChapterOrMsrQueryBuilder:
    """Builder for ChapterOrMsrQuery."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ChapterOrMsrQuery = ChapterOrMsrQuery()

    def build(self) -> ChapterOrMsrQuery:
        """Build and return ChapterOrMsrQuery object.

        Returns:
            ChapterOrMsrQuery instance
        """
        # TODO: Add validation
        return self._obj
