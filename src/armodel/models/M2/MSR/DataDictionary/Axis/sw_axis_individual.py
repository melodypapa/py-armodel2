"""SwAxisIndividual AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 354)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_Axis.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization.decorators import xml_element_name

from armodel.models.M2.MSR.DataDictionary.CalibrationParameter.sw_calprm_axis_type_props import (
    SwCalprmAxisTypeProps,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_method import (
    CompuMethod,
)
from armodel.models.M2.MSR.AsamHdo.Constraints.GlobalConstraints.data_constr import (
    DataConstr,
)
from armodel.models.M2.MSR.DataDictionary.Axis.sw_axis_generic import (
    SwAxisGeneric,
)
from armodel.models.M2.MSR.DataDictionary.DatadictionaryProxies.sw_variable_ref_proxy import (
    SwVariableRefProxy,
)
from armodel.models.M2.MSR.AsamHdo.Units.unit import (
    Unit,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.application_primitive_data_type import (
        ApplicationPrimitiveDataType,
    )



class SwAxisIndividual(SwCalprmAxisTypeProps):
    """AUTOSAR SwAxisIndividual."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    compu_method_ref: Optional[ARRef]
    data_constr_ref: Optional[ARRef]
    input_variable_ref: Optional[ARRef]
    sw_axis_generic: Optional[SwAxisGeneric]
    sw_max_axis: Optional[Integer]
    sw_min_axis: Optional[Integer]
    _sw_variable_ref_proxie_refs: list[ARRef]
    unit_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize SwAxisIndividual."""
        super().__init__()
        self.compu_method_ref: Optional[ARRef] = None
        self.data_constr_ref: Optional[ARRef] = None
        self.input_variable_ref: Optional[ARRef] = None
        self.sw_axis_generic: Optional[SwAxisGeneric] = None
        self.sw_max_axis: Optional[Integer] = None
        self.sw_min_axis: Optional[Integer] = None
        self._sw_variable_ref_proxie_refs: list[ARRef] = []
        self.unit_ref: Optional[ARRef] = None
    @property
    @xml_element_name("SW-VARIABLE-REF-PROXYS")
    def sw_variable_ref_proxie_refs(self) -> list[ARRef]:
        """Get sw_variable_ref_proxie_refs with custom XML element name."""
        return self._sw_variable_ref_proxie_refs

    @sw_variable_ref_proxie_refs.setter
    def sw_variable_ref_proxie_refs(self, value: list[ARRef]) -> None:
        """Set sw_variable_ref_proxie_refs with custom XML element name."""
        self._sw_variable_ref_proxie_refs = value


    def serialize(self) -> ET.Element:
        """Serialize SwAxisIndividual to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwAxisIndividual, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize compu_method_ref
        if self.compu_method_ref is not None:
            serialized = SerializationHelper.serialize_item(self.compu_method_ref, "CompuMethod")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COMPU-METHOD-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize data_constr_ref
        if self.data_constr_ref is not None:
            serialized = SerializationHelper.serialize_item(self.data_constr_ref, "DataConstr")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-CONSTR-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize input_variable_ref
        if self.input_variable_ref is not None:
            serialized = SerializationHelper.serialize_item(self.input_variable_ref, "ApplicationPrimitiveDataType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INPUT-VARIABLE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_axis_generic
        if self.sw_axis_generic is not None:
            serialized = SerializationHelper.serialize_item(self.sw_axis_generic, "SwAxisGeneric")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-AXIS-GENERIC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_max_axis
        if self.sw_max_axis is not None:
            serialized = SerializationHelper.serialize_item(self.sw_max_axis, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-MAX-AXIS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_min_axis
        if self.sw_min_axis is not None:
            serialized = SerializationHelper.serialize_item(self.sw_min_axis, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-MIN-AXIS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_variable_ref_proxie_refs (list to container "SW-VARIABLE-REF-PROXYS")
        if self.sw_variable_ref_proxie_refs:
            wrapper = ET.Element("SW-VARIABLE-REF-PROXYS")
            for item in self.sw_variable_ref_proxie_refs:
                serialized = SerializationHelper.serialize_item(item, "SwVariableRefProxy")
                if serialized is not None:
                    child_elem = ET.Element("SW-VARIABLE-REF-PROXIE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize unit_ref
        if self.unit_ref is not None:
            serialized = SerializationHelper.serialize_item(self.unit_ref, "Unit")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("UNIT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwAxisIndividual":
        """Deserialize XML element to SwAxisIndividual object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwAxisIndividual object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwAxisIndividual, cls).deserialize(element)

        # Parse compu_method_ref
        child = SerializationHelper.find_child_element(element, "COMPU-METHOD-REF")
        if child is not None:
            compu_method_ref_value = ARRef.deserialize(child)
            obj.compu_method_ref = compu_method_ref_value

        # Parse data_constr_ref
        child = SerializationHelper.find_child_element(element, "DATA-CONSTR-REF")
        if child is not None:
            data_constr_ref_value = ARRef.deserialize(child)
            obj.data_constr_ref = data_constr_ref_value

        # Parse input_variable_ref
        child = SerializationHelper.find_child_element(element, "INPUT-VARIABLE-REF")
        if child is not None:
            input_variable_ref_value = ARRef.deserialize(child)
            obj.input_variable_ref = input_variable_ref_value

        # Parse sw_axis_generic
        child = SerializationHelper.find_child_element(element, "SW-AXIS-GENERIC")
        if child is not None:
            sw_axis_generic_value = SerializationHelper.deserialize_by_tag(child, "SwAxisGeneric")
            obj.sw_axis_generic = sw_axis_generic_value

        # Parse sw_max_axis
        child = SerializationHelper.find_child_element(element, "SW-MAX-AXIS")
        if child is not None:
            sw_max_axis_value = child.text
            obj.sw_max_axis = sw_max_axis_value

        # Parse sw_min_axis
        child = SerializationHelper.find_child_element(element, "SW-MIN-AXIS")
        if child is not None:
            sw_min_axis_value = child.text
            obj.sw_min_axis = sw_min_axis_value

        # Parse sw_variable_ref_proxie_refs (list from container "SW-VARIABLE-REF-PROXYS")
        obj.sw_variable_ref_proxie_refs = []
        container = SerializationHelper.find_child_element(element, "SW-VARIABLE-REF-PROXYS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.sw_variable_ref_proxie_refs.append(child_value)

        # Parse unit_ref
        child = SerializationHelper.find_child_element(element, "UNIT-REF")
        if child is not None:
            unit_ref_value = ARRef.deserialize(child)
            obj.unit_ref = unit_ref_value

        return obj



class SwAxisIndividualBuilder:
    """Builder for SwAxisIndividual with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: SwAxisIndividual = SwAxisIndividual()


    def with_max_gradient(self, value: Optional[Float]) -> "SwAxisIndividualBuilder":
        """Set max_gradient attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.max_gradient = value
        return self

    def with_monotony(self, value: Optional[MonotonyEnum]) -> "SwAxisIndividualBuilder":
        """Set monotony attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.monotony = value
        return self

    def with_compu_method(self, value: Optional[CompuMethod]) -> "SwAxisIndividualBuilder":
        """Set compu_method attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.compu_method = value
        return self

    def with_data_constr(self, value: Optional[DataConstr]) -> "SwAxisIndividualBuilder":
        """Set data_constr attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.data_constr = value
        return self

    def with_input_variable(self, value: Optional[ApplicationPrimitiveDataType]) -> "SwAxisIndividualBuilder":
        """Set input_variable attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.input_variable = value
        return self

    def with_sw_axis_generic(self, value: Optional[SwAxisGeneric]) -> "SwAxisIndividualBuilder":
        """Set sw_axis_generic attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_axis_generic = value
        return self

    def with_sw_max_axis(self, value: Optional[Integer]) -> "SwAxisIndividualBuilder":
        """Set sw_max_axis attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_max_axis = value
        return self

    def with_sw_min_axis(self, value: Optional[Integer]) -> "SwAxisIndividualBuilder":
        """Set sw_min_axis attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_min_axis = value
        return self

    def with_sw_variable_ref_proxies(self, items: list[SwVariableRefProxy]) -> "SwAxisIndividualBuilder":
        """Set sw_variable_ref_proxies list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.sw_variable_ref_proxies = list(items) if items else []
        return self

    def with_unit(self, value: Optional[Unit]) -> "SwAxisIndividualBuilder":
        """Set unit attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.unit = value
        return self


    def add_sw_variable_ref_proxie(self, item: SwVariableRefProxy) -> "SwAxisIndividualBuilder":
        """Add a single item to sw_variable_ref_proxies list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.sw_variable_ref_proxies.append(item)
        return self

    def clear_sw_variable_ref_proxies(self) -> "SwAxisIndividualBuilder":
        """Clear all items from sw_variable_ref_proxies list.

        Returns:
            self for method chaining
        """
        self._obj.sw_variable_ref_proxies = []
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


    def build(self) -> SwAxisIndividual:
        """Build and return the SwAxisIndividual instance with validation."""
        self._validate_instance()
        pass
        return self._obj