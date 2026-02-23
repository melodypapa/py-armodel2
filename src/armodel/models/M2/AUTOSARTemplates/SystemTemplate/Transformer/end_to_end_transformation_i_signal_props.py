"""EndToEndTransformationISignalProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 808)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization.decorators import atp_variant

from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


@atp_variant()

class EndToEndTransformationISignalProps(ARObject):
    """AUTOSAR EndToEndTransformationISignalProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_length: Optional[PositiveInteger]
    max_data_length: Optional[PositiveInteger]
    min_data_length: Optional[PositiveInteger]
    source_id: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize EndToEndTransformationISignalProps."""
        super().__init__()
        self.data_length: Optional[PositiveInteger] = None
        self.max_data_length: Optional[PositiveInteger] = None
        self.min_data_length: Optional[PositiveInteger] = None
        self.source_id: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize EndToEndTransformationISignalProps to XML element with atp_variant wrapper.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EndToEndTransformationISignalProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Create inner element to hold attributes before wrapping
        inner_elem = ET.Element("INNER")

        # Serialize data_length
        if self.data_length is not None:
            serialized = SerializationHelper.serialize_item(self.data_length, "PositiveInteger")
            if serialized is not None:
                wrapped = ET.Element("DATA-LENGTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize max_data_length
        if self.max_data_length is not None:
            serialized = SerializationHelper.serialize_item(self.max_data_length, "PositiveInteger")
            if serialized is not None:
                wrapped = ET.Element("MAX-DATA-LENGTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize min_data_length
        if self.min_data_length is not None:
            serialized = SerializationHelper.serialize_item(self.min_data_length, "PositiveInteger")
            if serialized is not None:
                wrapped = ET.Element("MIN-DATA-LENGTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize source_id
        if self.source_id is not None:
            serialized = SerializationHelper.serialize_item(self.source_id, "PositiveInteger")
            if serialized is not None:
                wrapped = ET.Element("SOURCE-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Wrap inner element in atp_variant VARIANTS/CONDITIONAL structure
        wrapped = SerializationHelper.serialize_with_atp_variant(inner_elem, "EndToEndTransformationISignalProps")
        elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EndToEndTransformationISignalProps":
        """Deserialize XML element to EndToEndTransformationISignalProps object with atp_variant unwrapping.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EndToEndTransformationISignalProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EndToEndTransformationISignalProps, cls).deserialize(element)

        # Unwrap atp_variant VARIANTS/CONDITIONAL structure
        inner_elem = SerializationHelper.deserialize_from_atp_variant(element, "EndToEndTransformationISignalProps")
        if inner_elem is None:
            # No wrapper structure found, return object with default values
            return obj

        # Parse data_length
        child = SerializationHelper.find_child_element(inner_elem, "DATA-LENGTH")
        if child is not None:
            data_length_value = child.text
            obj.data_length = data_length_value

        # Parse max_data_length
        child = SerializationHelper.find_child_element(inner_elem, "MAX-DATA-LENGTH")
        if child is not None:
            max_data_length_value = child.text
            obj.max_data_length = max_data_length_value

        # Parse min_data_length
        child = SerializationHelper.find_child_element(inner_elem, "MIN-DATA-LENGTH")
        if child is not None:
            min_data_length_value = child.text
            obj.min_data_length = min_data_length_value

        # Parse source_id
        child = SerializationHelper.find_child_element(inner_elem, "SOURCE-ID")
        if child is not None:
            source_id_value = child.text
            obj.source_id = source_id_value

        return obj



class EndToEndTransformationISignalPropsBuilder(BuilderBase):
    """Builder for EndToEndTransformationISignalProps with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EndToEndTransformationISignalProps = EndToEndTransformationISignalProps()


    def with_data_length(self, value: Optional[PositiveInteger]) -> "EndToEndTransformationISignalPropsBuilder":
        """Set data_length attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.data_length = value
        return self

    def with_max_data_length(self, value: Optional[PositiveInteger]) -> "EndToEndTransformationISignalPropsBuilder":
        """Set max_data_length attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.max_data_length = value
        return self

    def with_min_data_length(self, value: Optional[PositiveInteger]) -> "EndToEndTransformationISignalPropsBuilder":
        """Set min_data_length attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.min_data_length = value
        return self

    def with_source_id(self, value: Optional[PositiveInteger]) -> "EndToEndTransformationISignalPropsBuilder":
        """Set source_id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.source_id = value
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


    def build(self) -> EndToEndTransformationISignalProps:
        """Build and return the EndToEndTransformationISignalProps instance with validation."""
        self._validate_instance()
        pass
        return self._obj