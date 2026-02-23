"""CanControllerFdConfigurationRequirements AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 66)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Can_CanTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Float,
    PositiveInteger,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class CanControllerFdConfigurationRequirements(ARObject):
    """AUTOSAR CanControllerFdConfigurationRequirements."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    max_number_of_time_quanta_per: Optional[Any]
    max_sample: Optional[Float]
    max_sync_jump: Optional[Float]
    max_trcv_delay: Optional[TimeValue]
    min_number_of_time_quanta_per: Optional[Any]
    min_sample_point: Optional[Float]
    min_sync_jump: Optional[Float]
    min_trcv_delay: Optional[TimeValue]
    padding_value: Optional[PositiveInteger]
    tx_bit_rate_switch: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize CanControllerFdConfigurationRequirements."""
        super().__init__()
        self.max_number_of_time_quanta_per: Optional[Any] = None
        self.max_sample: Optional[Float] = None
        self.max_sync_jump: Optional[Float] = None
        self.max_trcv_delay: Optional[TimeValue] = None
        self.min_number_of_time_quanta_per: Optional[Any] = None
        self.min_sample_point: Optional[Float] = None
        self.min_sync_jump: Optional[Float] = None
        self.min_trcv_delay: Optional[TimeValue] = None
        self.padding_value: Optional[PositiveInteger] = None
        self.tx_bit_rate_switch: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize CanControllerFdConfigurationRequirements to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CanControllerFdConfigurationRequirements, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize max_number_of_time_quanta_per
        if self.max_number_of_time_quanta_per is not None:
            serialized = SerializationHelper.serialize_item(self.max_number_of_time_quanta_per, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-NUMBER-OF-TIME-QUANTA-PER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_sample
        if self.max_sample is not None:
            serialized = SerializationHelper.serialize_item(self.max_sample, "Float")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-SAMPLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_sync_jump
        if self.max_sync_jump is not None:
            serialized = SerializationHelper.serialize_item(self.max_sync_jump, "Float")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-SYNC-JUMP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_trcv_delay
        if self.max_trcv_delay is not None:
            serialized = SerializationHelper.serialize_item(self.max_trcv_delay, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-TRCV-DELAY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize min_number_of_time_quanta_per
        if self.min_number_of_time_quanta_per is not None:
            serialized = SerializationHelper.serialize_item(self.min_number_of_time_quanta_per, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MIN-NUMBER-OF-TIME-QUANTA-PER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize min_sample_point
        if self.min_sample_point is not None:
            serialized = SerializationHelper.serialize_item(self.min_sample_point, "Float")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MIN-SAMPLE-POINT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize min_sync_jump
        if self.min_sync_jump is not None:
            serialized = SerializationHelper.serialize_item(self.min_sync_jump, "Float")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MIN-SYNC-JUMP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize min_trcv_delay
        if self.min_trcv_delay is not None:
            serialized = SerializationHelper.serialize_item(self.min_trcv_delay, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MIN-TRCV-DELAY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

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
    def deserialize(cls, element: ET.Element) -> "CanControllerFdConfigurationRequirements":
        """Deserialize XML element to CanControllerFdConfigurationRequirements object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CanControllerFdConfigurationRequirements object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CanControllerFdConfigurationRequirements, cls).deserialize(element)

        # Parse max_number_of_time_quanta_per
        child = SerializationHelper.find_child_element(element, "MAX-NUMBER-OF-TIME-QUANTA-PER")
        if child is not None:
            max_number_of_time_quanta_per_value = child.text
            obj.max_number_of_time_quanta_per = max_number_of_time_quanta_per_value

        # Parse max_sample
        child = SerializationHelper.find_child_element(element, "MAX-SAMPLE")
        if child is not None:
            max_sample_value = child.text
            obj.max_sample = max_sample_value

        # Parse max_sync_jump
        child = SerializationHelper.find_child_element(element, "MAX-SYNC-JUMP")
        if child is not None:
            max_sync_jump_value = child.text
            obj.max_sync_jump = max_sync_jump_value

        # Parse max_trcv_delay
        child = SerializationHelper.find_child_element(element, "MAX-TRCV-DELAY")
        if child is not None:
            max_trcv_delay_value = child.text
            obj.max_trcv_delay = max_trcv_delay_value

        # Parse min_number_of_time_quanta_per
        child = SerializationHelper.find_child_element(element, "MIN-NUMBER-OF-TIME-QUANTA-PER")
        if child is not None:
            min_number_of_time_quanta_per_value = child.text
            obj.min_number_of_time_quanta_per = min_number_of_time_quanta_per_value

        # Parse min_sample_point
        child = SerializationHelper.find_child_element(element, "MIN-SAMPLE-POINT")
        if child is not None:
            min_sample_point_value = child.text
            obj.min_sample_point = min_sample_point_value

        # Parse min_sync_jump
        child = SerializationHelper.find_child_element(element, "MIN-SYNC-JUMP")
        if child is not None:
            min_sync_jump_value = child.text
            obj.min_sync_jump = min_sync_jump_value

        # Parse min_trcv_delay
        child = SerializationHelper.find_child_element(element, "MIN-TRCV-DELAY")
        if child is not None:
            min_trcv_delay_value = child.text
            obj.min_trcv_delay = min_trcv_delay_value

        # Parse padding_value
        child = SerializationHelper.find_child_element(element, "PADDING-VALUE")
        if child is not None:
            padding_value_value = child.text
            obj.padding_value = padding_value_value

        # Parse tx_bit_rate_switch
        child = SerializationHelper.find_child_element(element, "TX-BIT-RATE-SWITCH")
        if child is not None:
            tx_bit_rate_switch_value = child.text
            obj.tx_bit_rate_switch = tx_bit_rate_switch_value

        return obj



class CanControllerFdConfigurationRequirementsBuilder(BuilderBase):
    """Builder for CanControllerFdConfigurationRequirements with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: CanControllerFdConfigurationRequirements = CanControllerFdConfigurationRequirements()


    def with_max_number_of_time_quanta_per(self, value: Optional[any (IntegerBit)]) -> "CanControllerFdConfigurationRequirementsBuilder":
        """Set max_number_of_time_quanta_per attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.max_number_of_time_quanta_per = value
        return self

    def with_max_sample(self, value: Optional[Float]) -> "CanControllerFdConfigurationRequirementsBuilder":
        """Set max_sample attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.max_sample = value
        return self

    def with_max_sync_jump(self, value: Optional[Float]) -> "CanControllerFdConfigurationRequirementsBuilder":
        """Set max_sync_jump attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.max_sync_jump = value
        return self

    def with_max_trcv_delay(self, value: Optional[TimeValue]) -> "CanControllerFdConfigurationRequirementsBuilder":
        """Set max_trcv_delay attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.max_trcv_delay = value
        return self

    def with_min_number_of_time_quanta_per(self, value: Optional[any (IntegerBit)]) -> "CanControllerFdConfigurationRequirementsBuilder":
        """Set min_number_of_time_quanta_per attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.min_number_of_time_quanta_per = value
        return self

    def with_min_sample_point(self, value: Optional[Float]) -> "CanControllerFdConfigurationRequirementsBuilder":
        """Set min_sample_point attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.min_sample_point = value
        return self

    def with_min_sync_jump(self, value: Optional[Float]) -> "CanControllerFdConfigurationRequirementsBuilder":
        """Set min_sync_jump attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.min_sync_jump = value
        return self

    def with_min_trcv_delay(self, value: Optional[TimeValue]) -> "CanControllerFdConfigurationRequirementsBuilder":
        """Set min_trcv_delay attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.min_trcv_delay = value
        return self

    def with_padding_value(self, value: Optional[PositiveInteger]) -> "CanControllerFdConfigurationRequirementsBuilder":
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

    def with_tx_bit_rate_switch(self, value: Optional[Boolean]) -> "CanControllerFdConfigurationRequirementsBuilder":
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


    def build(self) -> CanControllerFdConfigurationRequirements:
        """Build and return the CanControllerFdConfigurationRequirements instance with validation."""
        self._validate_instance()
        pass
        return self._obj