"""MsrQueryChapter AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 343)

JSON Source: docs/json/packages/M2_MSR_Documentation_MsrQuery.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import PaginateableBuilder
from armodel2.models.M2.MSR.Documentation.MsrQuery.msr_query_props import (
    MsrQueryProps,
)

if TYPE_CHECKING:
    from armodel2.models.M2.MSR.Documentation.MsrQuery.msr_query_result_chapter import (
        MsrQueryResultChapter,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class MsrQueryChapter(Paginateable):
    """AUTOSAR MsrQueryChapter."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "MSR-QUERY-CHAPTER"


    msr_query_props: MsrQueryProps
    msr_query_result_chapter: Optional[MsrQueryResultChapter]
    _DESERIALIZE_DISPATCH = {
        "MSR-QUERY-PROPS": lambda obj, elem: setattr(obj, "msr_query_props", SerializationHelper.deserialize_by_tag(elem, "MsrQueryProps")),
        "MSR-QUERY-RESULT-CHAPTER": lambda obj, elem: setattr(obj, "msr_query_result_chapter", SerializationHelper.deserialize_by_tag(elem, "MsrQueryResultChapter")),
    }


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
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "MSR-QUERY-PROPS":
                setattr(obj, "msr_query_props", SerializationHelper.deserialize_by_tag(child, "MsrQueryProps"))
            elif tag == "MSR-QUERY-RESULT-CHAPTER":
                setattr(obj, "msr_query_result_chapter", SerializationHelper.deserialize_by_tag(child, "MsrQueryResultChapter"))

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
            raise ValueError("Attribute 'msr_query_props' is required and cannot be None")
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
            raise ValueError("Attribute 'msr_query_result_chapter' is required and cannot be None")
        self._obj.msr_query_result_chapter = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _REQUIRED_ATTRIBUTES = {
        "msrQueryProps",
    }
    _OPTIONAL_ATTRIBUTES = {
        "msrQueryResultChapter",
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
        if getattr(self._obj, "msrQueryProps", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError("Required attribute 'msrQueryProps' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn("Required attribute 'msrQueryProps' is None", UserWarning)


    def build(self) -> MsrQueryChapter:
        """Build and return the MsrQueryChapter instance with validation."""
        self._validate_instance()
        return self._obj