"""PredefinedChapter AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 330)

JSON Source: docs/json/packages/M2_MSR_Documentation_Chapters.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.MSR.Documentation.Chapters.chapter_model import (
    ChapterModel,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class PredefinedChapter(ARObject):
    """AUTOSAR PredefinedChapter."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "PREDEFINED-CHAPTER"


    chapter_model: ChapterModel
    _DESERIALIZE_DISPATCH = {
        "CHAPTER-MODEL": lambda obj, elem: setattr(obj, "chapter_model", SerializationHelper.deserialize_by_tag(elem, "ChapterModel")),
    }


    def __init__(self) -> None:
        """Initialize PredefinedChapter."""
        super().__init__()
        self.chapter_model: ChapterModel = None

    def serialize(self) -> ET.Element:
        """Serialize PredefinedChapter to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CHAPTER-MODEL":
                setattr(obj, "chapter_model", SerializationHelper.deserialize_by_tag(child, "ChapterModel"))

        return obj



class PredefinedChapterBuilder(BuilderBase):
    """Builder for PredefinedChapter with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: PredefinedChapter = PredefinedChapter()


    def with_chapter_model(self, value: ChapterModel) -> "PredefinedChapterBuilder":
        """Set chapter_model attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.chapter_model = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _REQUIRED_ATTRIBUTES = {
        "chapterModel",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Validate required attributes using pre-computed constants (O(1) lookup)
        # This is much faster than calling get_type_hints() at runtime
        if getattr(self._obj, "chapterModel", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError("Required attribute 'chapterModel' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn("Required attribute 'chapterModel' is None", UserWarning)


    def build(self) -> PredefinedChapter:
        """Build and return the PredefinedChapter instance with validation."""
        self._validate_instance()
        return self._obj