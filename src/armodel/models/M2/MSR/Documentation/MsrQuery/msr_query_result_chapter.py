"""MsrQueryResultChapter AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.Chapters.chapter import (
    Chapter,
)


class MsrQueryResultChapter(ARObject):
    """AUTOSAR MsrQueryResultChapter."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("chapters", None, False, True, Chapter),  # chapters
    ]

    def __init__(self) -> None:
        """Initialize MsrQueryResultChapter."""
        super().__init__()
        self.chapters: list[Chapter] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert MsrQueryResultChapter to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MsrQueryResultChapter":
        """Create MsrQueryResultChapter from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            MsrQueryResultChapter instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to MsrQueryResultChapter since parent returns ARObject
        return cast("MsrQueryResultChapter", obj)


class MsrQueryResultChapterBuilder:
    """Builder for MsrQueryResultChapter."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MsrQueryResultChapter = MsrQueryResultChapter()

    def build(self) -> MsrQueryResultChapter:
        """Build and return MsrQueryResultChapter object.

        Returns:
            MsrQueryResultChapter instance
        """
        # TODO: Add validation
        return self._obj
