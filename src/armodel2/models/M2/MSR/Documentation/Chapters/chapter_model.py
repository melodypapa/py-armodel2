"""ChapterModel AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 699)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 329)

JSON Source: docs/json/packages/M2_MSR_Documentation_Chapters.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.MSR.Documentation.Chapters.chapter_content import (
    ChapterContent,
)
from armodel2.models.M2.MSR.Documentation.Chapters.topic_or_msr_query import (
    TopicOrMsrQuery,
)

if TYPE_CHECKING:
    from armodel2.models.M2.MSR.Documentation.Chapters.chapter_or_msr_query import (
        ChapterOrMsrQuery,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class ChapterModel(ARObject):
    """AUTOSAR ChapterModel."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "CHAPTER-MODEL"


    chapter: Optional[ChapterOrMsrQuery]
    chapter_content: Optional[ChapterContent]
    topic1: Optional[TopicOrMsrQuery]
    _DESERIALIZE_DISPATCH = {
        "CHAPTER": lambda obj, elem: setattr(obj, "chapter", SerializationHelper.deserialize_by_tag(elem, "ChapterOrMsrQuery")),
        "CHAPTER-CONTENT": lambda obj, elem: setattr(obj, "chapter_content", SerializationHelper.deserialize_by_tag(elem, "ChapterContent")),
        "TOPIC1": lambda obj, elem: setattr(obj, "topic1", SerializationHelper.deserialize_by_tag(elem, "TopicOrMsrQuery")),
    }


    def __init__(self) -> None:
        """Initialize ChapterModel."""
        super().__init__()
        self.chapter: Optional[ChapterOrMsrQuery] = None
        self.chapter_content: Optional[ChapterContent] = None
        self.topic1: Optional[TopicOrMsrQuery] = None

    def serialize(self) -> ET.Element:
        """Serialize ChapterModel to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ChapterModel, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize chapter (atp_mixed - append children directly)
        if self.chapter is not None:
            serialized = SerializationHelper.serialize_item(self.chapter, "ChapterOrMsrQuery")
            if serialized is not None:
                # atpMixed type: append children directly without wrapper
                if hasattr(serialized, 'attrib'):
                    elem.attrib.update(serialized.attrib)
                # Only copy text if it's a non-empty string (not None or whitespace)
                if serialized.text and serialized.text.strip():
                    elem.text = serialized.text
                for child in serialized:
                    elem.append(child)

        # Serialize chapter_content (atp_mixed - append children directly)
        if self.chapter_content is not None:
            serialized = SerializationHelper.serialize_item(self.chapter_content, "ChapterContent")
            if serialized is not None:
                # atpMixed type: append children directly without wrapper
                if hasattr(serialized, 'attrib'):
                    elem.attrib.update(serialized.attrib)
                # Only copy text if it's a non-empty string (not None or whitespace)
                if serialized.text and serialized.text.strip():
                    elem.text = serialized.text
                for child in serialized:
                    elem.append(child)

        # Serialize topic1 (atp_mixed - append children directly)
        if self.topic1 is not None:
            serialized = SerializationHelper.serialize_item(self.topic1, "TopicOrMsrQuery")
            if serialized is not None:
                # atpMixed type: append children directly without wrapper
                if hasattr(serialized, 'attrib'):
                    elem.attrib.update(serialized.attrib)
                # Only copy text if it's a non-empty string (not None or whitespace)
                if serialized.text and serialized.text.strip():
                    elem.text = serialized.text
                for child in serialized:
                    elem.append(child)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ChapterModel":
        """Deserialize XML element to ChapterModel object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ChapterModel object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ChapterModel, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "CHAPTER":
                setattr(obj, "chapter", SerializationHelper.deserialize_by_tag(child, "ChapterOrMsrQuery"))
            elif tag == "CHAPTER-CONTENT":
                setattr(obj, "chapter_content", SerializationHelper.deserialize_by_tag(child, "ChapterContent"))
            elif tag == "TOPIC1":
                setattr(obj, "topic1", SerializationHelper.deserialize_by_tag(child, "TopicOrMsrQuery"))

        return obj



class ChapterModelBuilder(BuilderBase):
    """Builder for ChapterModel with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ChapterModel = ChapterModel()


    def with_chapter(self, value: Optional[ChapterOrMsrQuery]) -> "ChapterModelBuilder":
        """Set chapter attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.chapter = value
        return self

    def with_chapter_content(self, value: Optional[ChapterContent]) -> "ChapterModelBuilder":
        """Set chapter_content attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.chapter_content = value
        return self

    def with_topic1(self, value: Optional[TopicOrMsrQuery]) -> "ChapterModelBuilder":
        """Set topic1 attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.topic1 = value
        return self




    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Get type hints for the class
        try:
            type_hints_dict = get_type_hints(type(self._obj))
        except Exception:
            # Cannot resolve type hints (e.g., forward references), skip validation
            return

        for attr_name, attr_type in type_hints_dict.items():
            if attr_name.startswith("_"):
                continue

            value = getattr(self._obj, attr_name)

            # Check required fields (not Optional)
            if value is None and not self._is_optional_type(attr_type):
                if mode == BuilderValidationMode.STRICT:
                    raise ValueError(
                        f"Required attribute '{attr_name}' is None"
                    )
                elif mode == BuilderValidationMode.LENIENT:
                    import warnings
                    warnings.warn(
                        f"Required attribute '{attr_name}' is None",
                        UserWarning
                    )

    @staticmethod
    def _is_optional_type(type_hint: Any) -> bool:
        """Check if a type hint is Optional.

        Args:
            type_hint: Type hint to check

        Returns:
            True if type is Optional, False otherwise
        """
        origin = getattr(type_hint, "__origin__", None)
        return origin is Union

    @staticmethod
    def _get_expected_type(type_hint: Any) -> type:
        """Extract expected type from type hint.

        Args:
            type_hint: Type hint to extract from

        Returns:
            Expected type
        """
        if isinstance(type_hint, str):
            return object
        origin = getattr(type_hint, "__origin__", None)
        if origin is Union:
            args = getattr(type_hint, "__args__", [])
            for arg in args:
                if arg is not type(None):
                    return arg
        elif origin is list:
            args = getattr(type_hint, "__args__", [object])
            return args[0] if args else object
        return type_hint if isinstance(type_hint, type) else object


    def build(self) -> ChapterModel:
        """Build and return the ChapterModel instance with validation."""
        self._validate_instance()
        pass
        return self._obj