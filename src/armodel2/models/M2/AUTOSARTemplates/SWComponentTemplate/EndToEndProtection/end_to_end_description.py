"""EndToEndDescription AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 205)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 385)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_EndToEndProtection.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class EndToEndDescription(ARObject):
    """AUTOSAR EndToEndDescription."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    category: Optional[NameToken]
    counter_offset: Optional[PositiveInteger]
    crc_offset: Optional[PositiveInteger]
    data_id_mode: Optional[PositiveInteger]
    data_id_nibble: Optional[PositiveInteger]
    data_length: Optional[PositiveInteger]
    max_delta: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize EndToEndDescription."""
        super().__init__()
        self.category: Optional[NameToken] = None
        self.counter_offset: Optional[PositiveInteger] = None
        self.crc_offset: Optional[PositiveInteger] = None
        self.data_id_mode: Optional[PositiveInteger] = None
        self.data_id_nibble: Optional[PositiveInteger] = None
        self.data_length: Optional[PositiveInteger] = None
        self.max_delta: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize EndToEndDescription to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EndToEndDescription, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize category
        if self.category is not None:
            serialized = SerializationHelper.serialize_item(self.category, "NameToken")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CATEGORY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize counter_offset
        if self.counter_offset is not None:
            serialized = SerializationHelper.serialize_item(self.counter_offset, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COUNTER-OFFSET")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize crc_offset
        if self.crc_offset is not None:
            serialized = SerializationHelper.serialize_item(self.crc_offset, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CRC-OFFSET")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize data_id_mode
        if self.data_id_mode is not None:
            serialized = SerializationHelper.serialize_item(self.data_id_mode, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-ID-MODE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize data_id_nibble
        if self.data_id_nibble is not None:
            serialized = SerializationHelper.serialize_item(self.data_id_nibble, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-ID-NIBBLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize data_length
        if self.data_length is not None:
            serialized = SerializationHelper.serialize_item(self.data_length, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-LENGTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_delta
        if self.max_delta is not None:
            serialized = SerializationHelper.serialize_item(self.max_delta, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-DELTA")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EndToEndDescription":
        """Deserialize XML element to EndToEndDescription object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EndToEndDescription object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EndToEndDescription, cls).deserialize(element)

        # Parse category
        child = SerializationHelper.find_child_element(element, "CATEGORY")
        if child is not None:
            category_value = child.text
            obj.category = category_value

        # Parse counter_offset
        child = SerializationHelper.find_child_element(element, "COUNTER-OFFSET")
        if child is not None:
            counter_offset_value = child.text
            obj.counter_offset = counter_offset_value

        # Parse crc_offset
        child = SerializationHelper.find_child_element(element, "CRC-OFFSET")
        if child is not None:
            crc_offset_value = child.text
            obj.crc_offset = crc_offset_value

        # Parse data_id_mode
        child = SerializationHelper.find_child_element(element, "DATA-ID-MODE")
        if child is not None:
            data_id_mode_value = child.text
            obj.data_id_mode = data_id_mode_value

        # Parse data_id_nibble
        child = SerializationHelper.find_child_element(element, "DATA-ID-NIBBLE")
        if child is not None:
            data_id_nibble_value = child.text
            obj.data_id_nibble = data_id_nibble_value

        # Parse data_length
        child = SerializationHelper.find_child_element(element, "DATA-LENGTH")
        if child is not None:
            data_length_value = child.text
            obj.data_length = data_length_value

        # Parse max_delta
        child = SerializationHelper.find_child_element(element, "MAX-DELTA")
        if child is not None:
            max_delta_value = child.text
            obj.max_delta = max_delta_value

        return obj



class EndToEndDescriptionBuilder(BuilderBase):
    """Builder for EndToEndDescription with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EndToEndDescription = EndToEndDescription()


    def with_category(self, value: Optional[NameToken]) -> "EndToEndDescriptionBuilder":
        """Set category attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.category = value
        return self

    def with_counter_offset(self, value: Optional[PositiveInteger]) -> "EndToEndDescriptionBuilder":
        """Set counter_offset attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.counter_offset = value
        return self

    def with_crc_offset(self, value: Optional[PositiveInteger]) -> "EndToEndDescriptionBuilder":
        """Set crc_offset attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.crc_offset = value
        return self

    def with_data_id_mode(self, value: Optional[PositiveInteger]) -> "EndToEndDescriptionBuilder":
        """Set data_id_mode attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.data_id_mode = value
        return self

    def with_data_id_nibble(self, value: Optional[PositiveInteger]) -> "EndToEndDescriptionBuilder":
        """Set data_id_nibble attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.data_id_nibble = value
        return self

    def with_data_length(self, value: Optional[PositiveInteger]) -> "EndToEndDescriptionBuilder":
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

    def with_max_delta(self, value: Optional[PositiveInteger]) -> "EndToEndDescriptionBuilder":
        """Set max_delta attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.max_delta = value
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


    def build(self) -> EndToEndDescription:
        """Build and return the EndToEndDescription instance with validation."""
        self._validate_instance()
        pass
        return self._obj