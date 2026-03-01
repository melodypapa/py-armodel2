"""MsrQueryTopic1 AUTOSAR element.

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
from armodel2.models.M2.MSR.Documentation.MsrQuery.msr_query_result_topic1 import (
    MsrQueryResultTopic1,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class MsrQueryTopic1(Paginateable):
    """AUTOSAR MsrQueryTopic1."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "MSR-QUERY-TOPIC1"


    msr_query_props: MsrQueryProps
    msr_query_result_topic1: Optional[MsrQueryResultTopic1]
    _DESERIALIZE_DISPATCH = {
        "MSR-QUERY-PROPS": lambda obj, elem: setattr(obj, "msr_query_props", SerializationHelper.deserialize_by_tag(elem, "MsrQueryProps")),
        "MSR-QUERY-RESULT-TOPIC1": lambda obj, elem: setattr(obj, "msr_query_result_topic1", SerializationHelper.deserialize_by_tag(elem, "MsrQueryResultTopic1")),
    }


    def __init__(self) -> None:
        """Initialize MsrQueryTopic1."""
        super().__init__()
        self.msr_query_props: MsrQueryProps = None
        self.msr_query_result_topic1: Optional[MsrQueryResultTopic1] = None

    def serialize(self) -> ET.Element:
        """Serialize MsrQueryTopic1 to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(MsrQueryTopic1, self).serialize()

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

        # Serialize msr_query_result_topic1
        if self.msr_query_result_topic1 is not None:
            serialized = SerializationHelper.serialize_item(self.msr_query_result_topic1, "MsrQueryResultTopic1")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MSR-QUERY-RESULT-TOPIC1")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MsrQueryTopic1":
        """Deserialize XML element to MsrQueryTopic1 object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MsrQueryTopic1 object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(MsrQueryTopic1, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "MSR-QUERY-PROPS":
                setattr(obj, "msr_query_props", SerializationHelper.deserialize_by_tag(child, "MsrQueryProps"))
            elif tag == "MSR-QUERY-RESULT-TOPIC1":
                setattr(obj, "msr_query_result_topic1", SerializationHelper.deserialize_by_tag(child, "MsrQueryResultTopic1"))

        return obj



class MsrQueryTopic1Builder(PaginateableBuilder):
    """Builder for MsrQueryTopic1 with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: MsrQueryTopic1 = MsrQueryTopic1()


    def with_msr_query_props(self, value: MsrQueryProps) -> "MsrQueryTopic1Builder":
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

    def with_msr_query_result_topic1(self, value: Optional[MsrQueryResultTopic1]) -> "MsrQueryTopic1Builder":
        """Set msr_query_result_topic1 attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.msr_query_result_topic1 = value
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


    def build(self) -> MsrQueryTopic1:
        """Build and return the MsrQueryTopic1 instance with validation."""
        self._validate_instance()
        pass
        return self._obj