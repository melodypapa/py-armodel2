"""CanControllerFdConfiguration AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 66)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Can_CanTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class CanControllerFdConfiguration(ARObject):
    """AUTOSAR CanControllerFdConfiguration."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "CAN-CONTROLLER-FD-CONFIGURATION"


    padding_value: Optional[PositiveInteger]
    prop_seg: Optional[PositiveInteger]
    ssp_offset: Optional[PositiveInteger]
    sync_jump_width: Optional[PositiveInteger]
    time_seg1: Optional[PositiveInteger]
    time_seg2: Optional[PositiveInteger]
    tx_bit_rate_switch: Optional[Boolean]
    _DESERIALIZE_DISPATCH = {
        "PADDING-VALUE": lambda obj, elem: setattr(obj, "padding_value", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "PROP-SEG": lambda obj, elem: setattr(obj, "prop_seg", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "SSP-OFFSET": lambda obj, elem: setattr(obj, "ssp_offset", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "SYNC-JUMP-WIDTH": lambda obj, elem: setattr(obj, "sync_jump_width", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "TIME-SEG1": lambda obj, elem: setattr(obj, "time_seg1", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "TIME-SEG2": lambda obj, elem: setattr(obj, "time_seg2", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "TX-BIT-RATE-SWITCH": lambda obj, elem: setattr(obj, "tx_bit_rate_switch", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
    }


    def __init__(self) -> None:
        """Initialize CanControllerFdConfiguration."""
        super().__init__()
        self.padding_value: Optional[PositiveInteger] = None
        self.prop_seg: Optional[PositiveInteger] = None
        self.ssp_offset: Optional[PositiveInteger] = None
        self.sync_jump_width: Optional[PositiveInteger] = None
        self.time_seg1: Optional[PositiveInteger] = None
        self.time_seg2: Optional[PositiveInteger] = None
        self.tx_bit_rate_switch: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize CanControllerFdConfiguration to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CanControllerFdConfiguration, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize padding_value
        if self.padding_value is not None:
            serialized = SerializationHelper.serialize_item(self.padding_value, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PADDING-VALUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize prop_seg
        if self.prop_seg is not None:
            serialized = SerializationHelper.serialize_item(self.prop_seg, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PROP-SEG")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ssp_offset
        if self.ssp_offset is not None:
            serialized = SerializationHelper.serialize_item(self.ssp_offset, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SSP-OFFSET")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sync_jump_width
        if self.sync_jump_width is not None:
            serialized = SerializationHelper.serialize_item(self.sync_jump_width, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SYNC-JUMP-WIDTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize time_seg1
        if self.time_seg1 is not None:
            serialized = SerializationHelper.serialize_item(self.time_seg1, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIME-SEG1")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize time_seg2
        if self.time_seg2 is not None:
            serialized = SerializationHelper.serialize_item(self.time_seg2, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIME-SEG2")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tx_bit_rate_switch
        if self.tx_bit_rate_switch is not None:
            serialized = SerializationHelper.serialize_item(self.tx_bit_rate_switch, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TX-BIT-RATE-SWITCH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CanControllerFdConfiguration":
        """Deserialize XML element to CanControllerFdConfiguration object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CanControllerFdConfiguration object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CanControllerFdConfiguration, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "PADDING-VALUE":
                setattr(obj, "padding_value", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "PROP-SEG":
                setattr(obj, "prop_seg", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "SSP-OFFSET":
                setattr(obj, "ssp_offset", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "SYNC-JUMP-WIDTH":
                setattr(obj, "sync_jump_width", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "TIME-SEG1":
                setattr(obj, "time_seg1", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "TIME-SEG2":
                setattr(obj, "time_seg2", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "TX-BIT-RATE-SWITCH":
                setattr(obj, "tx_bit_rate_switch", SerializationHelper.deserialize_by_tag(child, "Boolean"))

        return obj



class CanControllerFdConfigurationBuilder(BuilderBase):
    """Builder for CanControllerFdConfiguration with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: CanControllerFdConfiguration = CanControllerFdConfiguration()


    def with_padding_value(self, value: Optional[PositiveInteger]) -> "CanControllerFdConfigurationBuilder":
        """Set padding_value attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.padding_value = value
        return self

    def with_prop_seg(self, value: Optional[PositiveInteger]) -> "CanControllerFdConfigurationBuilder":
        """Set prop_seg attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.prop_seg = value
        return self

    def with_ssp_offset(self, value: Optional[PositiveInteger]) -> "CanControllerFdConfigurationBuilder":
        """Set ssp_offset attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ssp_offset = value
        return self

    def with_sync_jump_width(self, value: Optional[PositiveInteger]) -> "CanControllerFdConfigurationBuilder":
        """Set sync_jump_width attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sync_jump_width = value
        return self

    def with_time_seg1(self, value: Optional[PositiveInteger]) -> "CanControllerFdConfigurationBuilder":
        """Set time_seg1 attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.time_seg1 = value
        return self

    def with_time_seg2(self, value: Optional[PositiveInteger]) -> "CanControllerFdConfigurationBuilder":
        """Set time_seg2 attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.time_seg2 = value
        return self

    def with_tx_bit_rate_switch(self, value: Optional[Boolean]) -> "CanControllerFdConfigurationBuilder":
        """Set tx_bit_rate_switch attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tx_bit_rate_switch = value
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


    def build(self) -> CanControllerFdConfiguration:
        """Build and return the CanControllerFdConfiguration instance with validation."""
        self._validate_instance()
        pass
        return self._obj