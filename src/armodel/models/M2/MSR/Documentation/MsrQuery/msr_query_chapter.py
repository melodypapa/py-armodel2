"""MsrQueryChapter AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 343)

JSON Source: docs/json/packages/M2_MSR_Documentation_MsrQuery.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import PaginateableBuilder
from armodel.models.M2.MSR.Documentation.MsrQuery.msr_query_props import (
    MsrQueryProps,
)

if TYPE_CHECKING:
    from armodel.models.M2.MSR.Documentation.MsrQuery.msr_query_result_chapter import (
        MsrQueryResultChapter,
    )



class MsrQueryChapter(Paginateable):
    """AUTOSAR MsrQueryChapter."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    msr_query_props: MsrQueryProps
    msr_query_result_chapter: Optional[MsrQueryResultChapter]
    def __init__(self) -> None:
        """Initialize MsrQueryChapter."""
        super().__init__()
        self.msr_query_props: MsrQueryProps = None
        self.msr_query_result_chapter: Optional[MsrQueryResultChapter] = None

    def serialize(self) -> ET.Element:
        """Serialize MsrQueryChapter to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(MsrQueryChapter, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize msr_query_props
        if self.msr_query_props is not None:
            serialized = SerializationHelper.serialize_item(self.msr_query_props, "MsrQueryProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MSR-QUERY-PROPS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize msr_query_result_chapter
        if self.msr_query_result_chapter is not None:
            serialized = SerializationHelper.serialize_item(self.msr_query_result_chapter, "MsrQueryResultChapter")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MSR-QUERY-RESULT-CHAPTER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MsrQueryChapter":
        """Deserialize XML element to MsrQueryChapter object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MsrQueryChapter object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(MsrQueryChapter, cls).deserialize(element)

        # Parse msr_query_props
        child = SerializationHelper.find_child_element(element, "MSR-QUERY-PROPS")
        if child is not None:
            msr_query_props_value = SerializationHelper.deserialize_by_tag(child, "MsrQueryProps")
            obj.msr_query_props = msr_query_props_value

        # Parse msr_query_result_chapter
        child = SerializationHelper.find_child_element(element, "MSR-QUERY-RESULT-CHAPTER")
        if child is not None:
            msr_query_result_chapter_value = SerializationHelper.deserialize_by_tag(child, "MsrQueryResultChapter")
            obj.msr_query_result_chapter = msr_query_result_chapter_value

        return obj



class MsrQueryChapterBuilder(PaginateableBuilder):
    """Builder for MsrQueryChapter with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: MsrQueryChapter = MsrQueryChapter()


    def with_msr_query_props(self, value: MsrQueryProps) -> "MsrQueryChapterBuilder":
        """Set msr_query_props attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.msr_query_props = value
        return self

    def with_msr_query_result_chapter(self, value: Optional[MsrQueryResultChapter]) -> "MsrQueryChapterBuilder":
        """Set msr_query_result_chapter attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.msr_query_result_chapter = value
        return self




    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel.core import GlobalSettingsManager, BuilderValidationMode

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


    def build(self) -> MsrQueryChapter:
        """Build and return the MsrQueryChapter instance with validation."""
        self._validate_instance()
        pass
        return self._obj