"""LinSlave AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 97)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization.decorators import atp_variant

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
    PositiveInteger,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_error_response import (
    LinErrorResponse,
)


@atp_variant()

class LinSlave(ARObject):
    """AUTOSAR LinSlave."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    assign_nad: Optional[Boolean]
    configured_nad: Optional[Integer]
    function_id: Optional[PositiveInteger]
    initial_nad: Optional[Integer]
    lin_error_response: Optional[LinErrorResponse]
    nas_timeout: Optional[TimeValue]
    supplier_id: Optional[PositiveInteger]
    variant_id: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize LinSlave."""
        super().__init__()
        self.assign_nad: Optional[Boolean] = None
        self.configured_nad: Optional[Integer] = None
        self.function_id: Optional[PositiveInteger] = None
        self.initial_nad: Optional[Integer] = None
        self.lin_error_response: Optional[LinErrorResponse] = None
        self.nas_timeout: Optional[TimeValue] = None
        self.supplier_id: Optional[PositiveInteger] = None
        self.variant_id: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize LinSlave to XML element with atp_variant wrapper.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(LinSlave, self).serialize()

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

        # Serialize assign_nad
        if self.assign_nad is not None:
            serialized = SerializationHelper.serialize_item(self.assign_nad, "Boolean")
            if serialized is not None:
                wrapped = ET.Element("ASSIGN-NAD")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize configured_nad
        if self.configured_nad is not None:
            serialized = SerializationHelper.serialize_item(self.configured_nad, "Integer")
            if serialized is not None:
                wrapped = ET.Element("CONFIGURED-NAD")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize function_id
        if self.function_id is not None:
            serialized = SerializationHelper.serialize_item(self.function_id, "PositiveInteger")
            if serialized is not None:
                wrapped = ET.Element("FUNCTION-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize initial_nad
        if self.initial_nad is not None:
            serialized = SerializationHelper.serialize_item(self.initial_nad, "Integer")
            if serialized is not None:
                wrapped = ET.Element("INITIAL-NAD")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize lin_error_response
        if self.lin_error_response is not None:
            serialized = SerializationHelper.serialize_item(self.lin_error_response, "LinErrorResponse")
            if serialized is not None:
                wrapped = ET.Element("LIN-ERROR-RESPONSE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize nas_timeout
        if self.nas_timeout is not None:
            serialized = SerializationHelper.serialize_item(self.nas_timeout, "TimeValue")
            if serialized is not None:
                wrapped = ET.Element("NAS-TIMEOUT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize supplier_id
        if self.supplier_id is not None:
            serialized = SerializationHelper.serialize_item(self.supplier_id, "PositiveInteger")
            if serialized is not None:
                wrapped = ET.Element("SUPPLIER-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize variant_id
        if self.variant_id is not None:
            serialized = SerializationHelper.serialize_item(self.variant_id, "PositiveInteger")
            if serialized is not None:
                wrapped = ET.Element("VARIANT-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Wrap inner element in atp_variant VARIANTS/CONDITIONAL structure
        wrapped = SerializationHelper.serialize_with_atp_variant(inner_elem, "LinSlave")
        elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LinSlave":
        """Deserialize XML element to LinSlave object with atp_variant unwrapping.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LinSlave object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(LinSlave, cls).deserialize(element)

        # Unwrap atp_variant VARIANTS/CONDITIONAL structure
        inner_elem = SerializationHelper.deserialize_from_atp_variant(element, "LinSlave")
        if inner_elem is None:
            # No wrapper structure found, return object with default values
            return obj

        # Parse assign_nad
        child = SerializationHelper.find_child_element(inner_elem, "ASSIGN-NAD")
        if child is not None:
            assign_nad_value = child.text
            obj.assign_nad = assign_nad_value

        # Parse configured_nad
        child = SerializationHelper.find_child_element(inner_elem, "CONFIGURED-NAD")
        if child is not None:
            configured_nad_value = child.text
            obj.configured_nad = configured_nad_value

        # Parse function_id
        child = SerializationHelper.find_child_element(inner_elem, "FUNCTION-ID")
        if child is not None:
            function_id_value = child.text
            obj.function_id = function_id_value

        # Parse initial_nad
        child = SerializationHelper.find_child_element(inner_elem, "INITIAL-NAD")
        if child is not None:
            initial_nad_value = child.text
            obj.initial_nad = initial_nad_value

        # Parse lin_error_response
        child = SerializationHelper.find_child_element(inner_elem, "LIN-ERROR-RESPONSE")
        if child is not None:
            lin_error_response_value = SerializationHelper.deserialize_by_tag(child, "LinErrorResponse")
            obj.lin_error_response = lin_error_response_value

        # Parse nas_timeout
        child = SerializationHelper.find_child_element(inner_elem, "NAS-TIMEOUT")
        if child is not None:
            nas_timeout_value = child.text
            obj.nas_timeout = nas_timeout_value

        # Parse supplier_id
        child = SerializationHelper.find_child_element(inner_elem, "SUPPLIER-ID")
        if child is not None:
            supplier_id_value = child.text
            obj.supplier_id = supplier_id_value

        # Parse variant_id
        child = SerializationHelper.find_child_element(inner_elem, "VARIANT-ID")
        if child is not None:
            variant_id_value = child.text
            obj.variant_id = variant_id_value

        return obj



class LinSlaveBuilder:
    """Builder for LinSlave with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: LinSlave = LinSlave()


    def with_assign_nad(self, value: Optional[Boolean]) -> "LinSlaveBuilder":
        """Set assign_nad attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.assign_nad = value
        return self

    def with_configured_nad(self, value: Optional[Integer]) -> "LinSlaveBuilder":
        """Set configured_nad attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.configured_nad = value
        return self

    def with_function_id(self, value: Optional[PositiveInteger]) -> "LinSlaveBuilder":
        """Set function_id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.function_id = value
        return self

    def with_initial_nad(self, value: Optional[Integer]) -> "LinSlaveBuilder":
        """Set initial_nad attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.initial_nad = value
        return self

    def with_lin_error_response(self, value: Optional[LinErrorResponse]) -> "LinSlaveBuilder":
        """Set lin_error_response attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.lin_error_response = value
        return self

    def with_nas_timeout(self, value: Optional[TimeValue]) -> "LinSlaveBuilder":
        """Set nas_timeout attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.nas_timeout = value
        return self

    def with_supplier_id(self, value: Optional[PositiveInteger]) -> "LinSlaveBuilder":
        """Set supplier_id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.supplier_id = value
        return self

    def with_variant_id(self, value: Optional[PositiveInteger]) -> "LinSlaveBuilder":
        """Set variant_id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.variant_id = value
        return self



    @staticmethod
    def _coerce_to_int(value: Any) -> int:
        """Coerce value to int.

        Args:
            value: Value to coerce

        Returns:
            Integer value

        Raises:
            ValueError: If value cannot be coerced to int
        """
        if isinstance(value, int):
            return value
        if isinstance(value, str) and value.isdigit():
            return int(value)
        if isinstance(value, float):
            return int(value)
        if isinstance(value, bool):
            return int(value)
        raise ValueError(f"Cannot coerce {type(value).__name__} to int: {value}")

    @staticmethod
    def _coerce_to_float(value: Any) -> float:
        """Coerce value to float.

        Args:
            value: Value to coerce

        Returns:
            Float value

        Raises:
            ValueError: If value cannot be coerced to float
        """
        if isinstance(value, float):
            return value
        if isinstance(value, int):
            return float(value)
        if isinstance(value, str):
            try:
                return float(value)
            except ValueError:
                pass
        raise ValueError(f"Cannot coerce {type(value).__name__} to float: {value}")

    @staticmethod
    def _coerce_to_bool(value: Any) -> bool:
        """Coerce value to bool.

        Args:
            value: Value to coerce

        Returns:
            Boolean value

        Raises:
            ValueError: If value cannot be coerced to bool
        """
        if isinstance(value, bool):
            return value
        if isinstance(value, int):
            return bool(value)
        if isinstance(value, str):
            if value.lower() in ("true", "1", "yes"):
                return True
            if value.lower() in ("false", "0", "no"):
                return False
        raise ValueError(f"Cannot coerce {type(value).__name__} to bool: {value}")

    @staticmethod
    def _coerce_to_str(value: Any) -> str:
        """Coerce value to str.

        Args:
            value: Value to coerce

        Returns:
            String value
        """
        return str(value)


    @staticmethod
    def _coerce_to_list(value: Any, item_type: str) -> list:
        """Coerce value to list.

        Args:
            value: Value to coerce
            item_type: Expected item type (for error messages)

        Returns:
            List value

        Raises:
            ValueError: If value cannot be coerced to list
        """
        if isinstance(value, list):
            return value
        if isinstance(value, tuple):
            return list(value)
        raise ValueError(f"Cannot coerce {type(value).__name__} to list[{item_type}]: {value}")


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


    def build(self) -> LinSlave:
        """Build and return the LinSlave instance with validation."""
        self._validate_instance()
        pass
        return self._obj