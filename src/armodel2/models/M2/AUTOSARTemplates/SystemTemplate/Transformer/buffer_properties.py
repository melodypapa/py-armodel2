"""BufferProperties AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 199)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 767)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class BufferProperties(ARObject):
    """AUTOSAR BufferProperties."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "BUFFER-PROPERTIES"


    header_length: Optional[Integer]
    in_place: Optional[Boolean]
    _DESERIALIZE_DISPATCH = {
        "HEADER-LENGTH": lambda obj, elem: setattr(obj, "header_length", SerializationHelper.deserialize_by_tag(elem, "Integer")),
        "IN-PLACE": lambda obj, elem: setattr(obj, "in_place", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
    }


    def __init__(self) -> None:
        """Initialize BufferProperties."""
        super().__init__()
        self.header_length: Optional[Integer] = None
        self.in_place: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize BufferProperties to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BufferProperties, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize header_length
        if self.header_length is not None:
            serialized = SerializationHelper.serialize_item(self.header_length, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HEADER-LENGTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize in_place
        if self.in_place is not None:
            serialized = SerializationHelper.serialize_item(self.in_place, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IN-PLACE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BufferProperties":
        """Deserialize XML element to BufferProperties object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BufferProperties object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BufferProperties, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "HEADER-LENGTH":
                setattr(obj, "header_length", SerializationHelper.deserialize_by_tag(child, "Integer"))
            elif tag == "IN-PLACE":
                setattr(obj, "in_place", SerializationHelper.deserialize_by_tag(child, "Boolean"))

        return obj



class BufferPropertiesBuilder(BuilderBase):
    """Builder for BufferProperties with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: BufferProperties = BufferProperties()


    def with_header_length(self, value: Optional[Integer]) -> "BufferPropertiesBuilder":
        """Set header_length attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.header_length = value
        return self

    def with_in_place(self, value: Optional[Boolean]) -> "BufferPropertiesBuilder":
        """Set in_place attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.in_place = value
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


    def build(self) -> BufferProperties:
        """Build and return the BufferProperties instance with validation."""
        self._validate_instance()
        pass
        return self._obj