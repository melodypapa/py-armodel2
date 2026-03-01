"""SOMEIPTransformationProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 783)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.transformation_props import (
    TransformationProps,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.transformation_props import TransformationPropsBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SOMEIPTransformationProps(TransformationProps):
    """AUTOSAR SOMEIPTransformationProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "S-O-M-E-I-P-TRANSFORMATION-PROPS"


    alignment: Optional[PositiveInteger]
    size_of_array: Optional[PositiveInteger]
    size_of_string: Optional[PositiveInteger]
    size_of_struct: Optional[PositiveInteger]
    size_of_union: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "ALIGNMENT": lambda obj, elem: setattr(obj, "alignment", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "SIZE-OF-ARRAY": lambda obj, elem: setattr(obj, "size_of_array", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "SIZE-OF-STRING": lambda obj, elem: setattr(obj, "size_of_string", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "SIZE-OF-STRUCT": lambda obj, elem: setattr(obj, "size_of_struct", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "SIZE-OF-UNION": lambda obj, elem: setattr(obj, "size_of_union", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize SOMEIPTransformationProps."""
        super().__init__()
        self.alignment: Optional[PositiveInteger] = None
        self.size_of_array: Optional[PositiveInteger] = None
        self.size_of_string: Optional[PositiveInteger] = None
        self.size_of_struct: Optional[PositiveInteger] = None
        self.size_of_union: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize SOMEIPTransformationProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SOMEIPTransformationProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize alignment
        if self.alignment is not None:
            serialized = SerializationHelper.serialize_item(self.alignment, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ALIGNMENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize size_of_array
        if self.size_of_array is not None:
            serialized = SerializationHelper.serialize_item(self.size_of_array, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SIZE-OF-ARRAY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize size_of_string
        if self.size_of_string is not None:
            serialized = SerializationHelper.serialize_item(self.size_of_string, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SIZE-OF-STRING")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize size_of_struct
        if self.size_of_struct is not None:
            serialized = SerializationHelper.serialize_item(self.size_of_struct, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SIZE-OF-STRUCT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize size_of_union
        if self.size_of_union is not None:
            serialized = SerializationHelper.serialize_item(self.size_of_union, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SIZE-OF-UNION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SOMEIPTransformationProps":
        """Deserialize XML element to SOMEIPTransformationProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SOMEIPTransformationProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SOMEIPTransformationProps, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ALIGNMENT":
                setattr(obj, "alignment", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "SIZE-OF-ARRAY":
                setattr(obj, "size_of_array", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "SIZE-OF-STRING":
                setattr(obj, "size_of_string", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "SIZE-OF-STRUCT":
                setattr(obj, "size_of_struct", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "SIZE-OF-UNION":
                setattr(obj, "size_of_union", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class SOMEIPTransformationPropsBuilder(TransformationPropsBuilder):
    """Builder for SOMEIPTransformationProps with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SOMEIPTransformationProps = SOMEIPTransformationProps()


    def with_alignment(self, value: Optional[PositiveInteger]) -> "SOMEIPTransformationPropsBuilder":
        """Set alignment attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.alignment = value
        return self

    def with_size_of_array(self, value: Optional[PositiveInteger]) -> "SOMEIPTransformationPropsBuilder":
        """Set size_of_array attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.size_of_array = value
        return self

    def with_size_of_string(self, value: Optional[PositiveInteger]) -> "SOMEIPTransformationPropsBuilder":
        """Set size_of_string attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.size_of_string = value
        return self

    def with_size_of_struct(self, value: Optional[PositiveInteger]) -> "SOMEIPTransformationPropsBuilder":
        """Set size_of_struct attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.size_of_struct = value
        return self

    def with_size_of_union(self, value: Optional[PositiveInteger]) -> "SOMEIPTransformationPropsBuilder":
        """Set size_of_union attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.size_of_union = value
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


    def build(self) -> SOMEIPTransformationProps:
        """Build and return the SOMEIPTransformationProps instance with validation."""
        self._validate_instance()
        pass
        return self._obj