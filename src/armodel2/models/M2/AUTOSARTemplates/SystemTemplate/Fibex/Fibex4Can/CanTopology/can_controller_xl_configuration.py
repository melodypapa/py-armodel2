"""CanControllerXlConfiguration AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 70)

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


class CanControllerXlConfiguration(ARObject):
    """AUTOSAR CanControllerXlConfiguration."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "CAN-CONTROLLER-XL-CONFIGURATION"


    error_signaling: Optional[Boolean]
    prop_seg: Optional[PositiveInteger]
    pwm_l: Optional[PositiveInteger]
    pwm_o: Optional[PositiveInteger]
    pwm_s: Optional[PositiveInteger]
    ssp_offset: Optional[PositiveInteger]
    sync_jump_width: Optional[PositiveInteger]
    time_seg1: Optional[PositiveInteger]
    time_seg2: Optional[PositiveInteger]
    trcv_pwm_mode: Optional[Boolean]
    _DESERIALIZE_DISPATCH = {
        "ERROR-SIGNALING": lambda obj, elem: setattr(obj, "error_signaling", elem.text),
        "PROP-SEG": lambda obj, elem: setattr(obj, "prop_seg", elem.text),
        "PWM-L": lambda obj, elem: setattr(obj, "pwm_l", elem.text),
        "PWM-O": lambda obj, elem: setattr(obj, "pwm_o", elem.text),
        "PWM-S": lambda obj, elem: setattr(obj, "pwm_s", elem.text),
        "SSP-OFFSET": lambda obj, elem: setattr(obj, "ssp_offset", elem.text),
        "SYNC-JUMP-WIDTH": lambda obj, elem: setattr(obj, "sync_jump_width", elem.text),
        "TIME-SEG1": lambda obj, elem: setattr(obj, "time_seg1", elem.text),
        "TIME-SEG2": lambda obj, elem: setattr(obj, "time_seg2", elem.text),
        "TRCV-PWM-MODE": lambda obj, elem: setattr(obj, "trcv_pwm_mode", elem.text),
    }


    def __init__(self) -> None:
        """Initialize CanControllerXlConfiguration."""
        super().__init__()
        self.error_signaling: Optional[Boolean] = None
        self.prop_seg: Optional[PositiveInteger] = None
        self.pwm_l: Optional[PositiveInteger] = None
        self.pwm_o: Optional[PositiveInteger] = None
        self.pwm_s: Optional[PositiveInteger] = None
        self.ssp_offset: Optional[PositiveInteger] = None
        self.sync_jump_width: Optional[PositiveInteger] = None
        self.time_seg1: Optional[PositiveInteger] = None
        self.time_seg2: Optional[PositiveInteger] = None
        self.trcv_pwm_mode: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize CanControllerXlConfiguration to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CanControllerXlConfiguration, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize error_signaling
        if self.error_signaling is not None:
            serialized = SerializationHelper.serialize_item(self.error_signaling, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ERROR-SIGNALING")
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

        # Serialize pwm_l
        if self.pwm_l is not None:
            serialized = SerializationHelper.serialize_item(self.pwm_l, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PWM-L")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize pwm_o
        if self.pwm_o is not None:
            serialized = SerializationHelper.serialize_item(self.pwm_o, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PWM-O")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize pwm_s
        if self.pwm_s is not None:
            serialized = SerializationHelper.serialize_item(self.pwm_s, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PWM-S")
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

        # Serialize trcv_pwm_mode
        if self.trcv_pwm_mode is not None:
            serialized = SerializationHelper.serialize_item(self.trcv_pwm_mode, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRCV-PWM-MODE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CanControllerXlConfiguration":
        """Deserialize XML element to CanControllerXlConfiguration object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CanControllerXlConfiguration object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CanControllerXlConfiguration, cls).deserialize(element)

        # Parse error_signaling
        child = SerializationHelper.find_child_element(element, "ERROR-SIGNALING")
        if child is not None:
            error_signaling_value = child.text
            obj.error_signaling = error_signaling_value

        # Parse prop_seg
        child = SerializationHelper.find_child_element(element, "PROP-SEG")
        if child is not None:
            prop_seg_value = child.text
            obj.prop_seg = prop_seg_value

        # Parse pwm_l
        child = SerializationHelper.find_child_element(element, "PWM-L")
        if child is not None:
            pwm_l_value = child.text
            obj.pwm_l = pwm_l_value

        # Parse pwm_o
        child = SerializationHelper.find_child_element(element, "PWM-O")
        if child is not None:
            pwm_o_value = child.text
            obj.pwm_o = pwm_o_value

        # Parse pwm_s
        child = SerializationHelper.find_child_element(element, "PWM-S")
        if child is not None:
            pwm_s_value = child.text
            obj.pwm_s = pwm_s_value

        # Parse ssp_offset
        child = SerializationHelper.find_child_element(element, "SSP-OFFSET")
        if child is not None:
            ssp_offset_value = child.text
            obj.ssp_offset = ssp_offset_value

        # Parse sync_jump_width
        child = SerializationHelper.find_child_element(element, "SYNC-JUMP-WIDTH")
        if child is not None:
            sync_jump_width_value = child.text
            obj.sync_jump_width = sync_jump_width_value

        # Parse time_seg1
        child = SerializationHelper.find_child_element(element, "TIME-SEG1")
        if child is not None:
            time_seg1_value = child.text
            obj.time_seg1 = time_seg1_value

        # Parse time_seg2
        child = SerializationHelper.find_child_element(element, "TIME-SEG2")
        if child is not None:
            time_seg2_value = child.text
            obj.time_seg2 = time_seg2_value

        # Parse trcv_pwm_mode
        child = SerializationHelper.find_child_element(element, "TRCV-PWM-MODE")
        if child is not None:
            trcv_pwm_mode_value = child.text
            obj.trcv_pwm_mode = trcv_pwm_mode_value

        return obj



class CanControllerXlConfigurationBuilder(BuilderBase):
    """Builder for CanControllerXlConfiguration with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: CanControllerXlConfiguration = CanControllerXlConfiguration()


    def with_error_signaling(self, value: Optional[Boolean]) -> "CanControllerXlConfigurationBuilder":
        """Set error_signaling attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.error_signaling = value
        return self

    def with_prop_seg(self, value: Optional[PositiveInteger]) -> "CanControllerXlConfigurationBuilder":
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

    def with_pwm_l(self, value: Optional[PositiveInteger]) -> "CanControllerXlConfigurationBuilder":
        """Set pwm_l attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.pwm_l = value
        return self

    def with_pwm_o(self, value: Optional[PositiveInteger]) -> "CanControllerXlConfigurationBuilder":
        """Set pwm_o attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.pwm_o = value
        return self

    def with_pwm_s(self, value: Optional[PositiveInteger]) -> "CanControllerXlConfigurationBuilder":
        """Set pwm_s attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.pwm_s = value
        return self

    def with_ssp_offset(self, value: Optional[PositiveInteger]) -> "CanControllerXlConfigurationBuilder":
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

    def with_sync_jump_width(self, value: Optional[PositiveInteger]) -> "CanControllerXlConfigurationBuilder":
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

    def with_time_seg1(self, value: Optional[PositiveInteger]) -> "CanControllerXlConfigurationBuilder":
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

    def with_time_seg2(self, value: Optional[PositiveInteger]) -> "CanControllerXlConfigurationBuilder":
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

    def with_trcv_pwm_mode(self, value: Optional[Boolean]) -> "CanControllerXlConfigurationBuilder":
        """Set trcv_pwm_mode attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.trcv_pwm_mode = value
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


    def build(self) -> CanControllerXlConfiguration:
        """Build and return the CanControllerXlConfiguration instance with validation."""
        self._validate_instance()
        pass
        return self._obj