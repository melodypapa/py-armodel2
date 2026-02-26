"""SwCalprmAxis AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 352)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_CalibrationParameter.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.MSR.DataDictionary.CalibrationParameter import (
    CalprmAxisCategoryEnum,
)
from armodel2.models.M2.MSR.DataDictionary.DataDefProperties import (
    SwCalibrationAccessEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    DisplayFormatString,
)
from armodel2.models.M2.MSR.DataDictionary.RecordLayout import (
    AxisIndexType,
)
from armodel2.models.M2.MSR.DataDictionary.CalibrationParameter.sw_calprm_axis_type_props import (
    SwCalprmAxisTypeProps,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SwCalprmAxis(ARObject):
    """AUTOSAR SwCalprmAxis."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    category: Optional[CalprmAxisCategoryEnum]
    display_format_string: Optional[DisplayFormatString]
    sw_axis_index: Optional[AxisIndexType]
    sw_calibration_access: Optional[SwCalibrationAccessEnum]
    sw_calprm_axis: Optional[SwCalprmAxisTypeProps]
    def __init__(self) -> None:
        """Initialize SwCalprmAxis."""
        super().__init__()
        self.category: Optional[CalprmAxisCategoryEnum] = None
        self.display_format_string: Optional[DisplayFormatString] = None
        self.sw_axis_index: Optional[AxisIndexType] = None
        self.sw_calibration_access: Optional[SwCalibrationAccessEnum] = None
        self.sw_calprm_axis: Optional[SwCalprmAxisTypeProps] = None

    def serialize(self) -> ET.Element:
        """Serialize SwCalprmAxis to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwCalprmAxis, self).serialize()

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
            serialized = SerializationHelper.serialize_item(self.category, "CalprmAxisCategoryEnum")
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

        # Serialize display_format_string
        if self.display_format_string is not None:
            serialized = SerializationHelper.serialize_item(self.display_format_string, "DisplayFormatString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DISPLAY-FORMAT-STRING")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_axis_index
        if self.sw_axis_index is not None:
            serialized = SerializationHelper.serialize_item(self.sw_axis_index, "AxisIndexType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-AXIS-INDEX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_calibration_access
        if self.sw_calibration_access is not None:
            serialized = SerializationHelper.serialize_item(self.sw_calibration_access, "SwCalibrationAccessEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-CALIBRATION-ACCESS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_calprm_axis
        if self.sw_calprm_axis is not None:
            serialized = SerializationHelper.serialize_item(self.sw_calprm_axis, "SwCalprmAxisTypeProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-CALPRM-AXIS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwCalprmAxis":
        """Deserialize XML element to SwCalprmAxis object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwCalprmAxis object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwCalprmAxis, cls).deserialize(element)

        # Parse category
        child = SerializationHelper.find_child_element(element, "CATEGORY")
        if child is not None:
            category_value = CalprmAxisCategoryEnum.deserialize(child)
            obj.category = category_value

        # Parse display_format_string
        child = SerializationHelper.find_child_element(element, "DISPLAY-FORMAT-STRING")
        if child is not None:
            display_format_string_value = child.text
            obj.display_format_string = display_format_string_value

        # Parse sw_axis_index
        child = SerializationHelper.find_child_element(element, "SW-AXIS-INDEX")
        if child is not None:
            sw_axis_index_value = child.text
            obj.sw_axis_index = sw_axis_index_value

        # Parse sw_calibration_access
        child = SerializationHelper.find_child_element(element, "SW-CALIBRATION-ACCESS")
        if child is not None:
            sw_calibration_access_value = SwCalibrationAccessEnum.deserialize(child)
            obj.sw_calibration_access = sw_calibration_access_value

        # Parse sw_calprm_axis
        child = SerializationHelper.find_child_element(element, "SW-CALPRM-AXIS")
        if child is not None:
            sw_calprm_axis_value = SerializationHelper.deserialize_by_tag(child, "SwCalprmAxisTypeProps")
            obj.sw_calprm_axis = sw_calprm_axis_value

        return obj



class SwCalprmAxisBuilder(BuilderBase):
    """Builder for SwCalprmAxis with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SwCalprmAxis = SwCalprmAxis()


    def with_category(self, value: Optional[CalprmAxisCategoryEnum]) -> "SwCalprmAxisBuilder":
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

    def with_display_format_string(self, value: Optional[DisplayFormatString]) -> "SwCalprmAxisBuilder":
        """Set display_format_string attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.display_format_string = value
        return self

    def with_sw_axis_index(self, value: Optional[AxisIndexType]) -> "SwCalprmAxisBuilder":
        """Set sw_axis_index attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_axis_index = value
        return self

    def with_sw_calibration_access(self, value: Optional[SwCalibrationAccessEnum]) -> "SwCalprmAxisBuilder":
        """Set sw_calibration_access attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_calibration_access = value
        return self

    def with_sw_calprm_axis(self, value: Optional[SwCalprmAxisTypeProps]) -> "SwCalprmAxisBuilder":
        """Set sw_calprm_axis attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_calprm_axis = value
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


    def build(self) -> SwCalprmAxis:
        """Build and return the SwCalprmAxis instance with validation."""
        self._validate_instance()
        pass
        return self._obj