"""PredefinedChapter AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.Chapters.chapter_model import (
    ChapterModel,
)


class PredefinedChapter(ARObject):
    """AUTOSAR PredefinedChapter."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("chapter_model", None, False, False, ChapterModel),  # chapterModel
    ]

    def __init__(self) -> None:
        """Initialize PredefinedChapter."""
        super().__init__()
        self.chapter_model: ChapterModel = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert PredefinedChapter to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PredefinedChapter":
        """Create PredefinedChapter from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            PredefinedChapter instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to PredefinedChapter since parent returns ARObject
        return cast("PredefinedChapter", obj)


class PredefinedChapterBuilder:
    """Builder for PredefinedChapter."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PredefinedChapter = PredefinedChapter()

    def build(self) -> PredefinedChapter:
        """Build and return PredefinedChapter object.

        Returns:
            PredefinedChapter instance
        """
        # TODO: Add validation
        return self._obj
