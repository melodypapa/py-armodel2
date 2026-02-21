"""PredefinedChapter AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 330)

JSON Source: docs/json/packages/M2_MSR_Documentation_Chapters.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.MSR.Documentation.Chapters.chapter_model import (
    ChapterModel,
)


class PredefinedChapter(ARObject):
    """AUTOSAR PredefinedChapter."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    chapter_model: ChapterModel
    def __init__(self) -> None:
        """Initialize PredefinedChapter."""
        super().__init__()
        self.chapter_model: ChapterModel = None

    def serialize(self) -> ET.Element:
        """Serialize PredefinedChapter to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(PredefinedChapter, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize chapter_model
        if self.chapter_model is not None:
            serialized = SerializationHelper.serialize_item(self.chapter_model, "ChapterModel")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CHAPTER-MODEL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PredefinedChapter":
        """Deserialize XML element to PredefinedChapter object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PredefinedChapter object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PredefinedChapter, cls).deserialize(element)

        # Parse chapter_model
        child = SerializationHelper.find_child_element(element, "CHAPTER-MODEL")
        if child is not None:
            chapter_model_value = SerializationHelper.deserialize_by_tag(child, "ChapterModel")
            obj.chapter_model = chapter_model_value

        return obj



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
