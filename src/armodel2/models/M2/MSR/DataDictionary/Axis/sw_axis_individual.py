"""SwAxisIndividual AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 354)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_Axis.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.MSR.DataDictionary.CalibrationParameter.sw_calprm_axis_type_props import (
    SwCalprmAxisTypeProps,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.MSR.DataDictionary.CalibrationParameter.sw_calprm_axis_type_props import SwCalprmAxisTypePropsBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel2.models.M2.MSR.AsamHdo.ComputationMethod.compu_method import (
    CompuMethod,
)
from armodel2.models.M2.MSR.AsamHdo.Constraints.GlobalConstraints.data_constr import (
    DataConstr,
)
from armodel2.models.M2.MSR.DataDictionary.Axis.sw_axis_generic import (
    SwAxisGeneric,
)
from armodel2.models.M2.MSR.DataDictionary.DatadictionaryProxies.sw_variable_ref_proxy import (
    SwVariableRefProxy,
)
from armodel2.models.M2.MSR.AsamHdo.Units.unit import (
    Unit,
)

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.application_primitive_data_type import (
        ApplicationPrimitiveDataType,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class SwAxisIndividual(SwCalprmAxisTypeProps):
    """AUTOSAR SwAxisIndividual."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SW-AXIS-INDIVIDUAL"


    compu_method_ref: Optional[ARRef]
    data_constr_ref: Optional[ARRef]
    input_variable_ref: Optional[ARRef]
    sw_axis_generic: Optional[SwAxisGeneric]
    sw_max_axis: Optional[Integer]
    sw_min_axis: Optional[Integer]
    sw_variable_ref_proxy_refs: list[ARRef]
    unit_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "COMPU-METHOD-REF": lambda obj, elem: setattr(obj, "compu_method_ref", ARRef.deserialize(elem)),
        "DATA-CONSTR-REF": lambda obj, elem: setattr(obj, "data_constr_ref", ARRef.deserialize(elem)),
        "INPUT-VARIABLE-REF": lambda obj, elem: setattr(obj, "input_variable_ref", ARRef.deserialize(elem)),
        "SW-AXIS-GENERIC": lambda obj, elem: setattr(obj, "sw_axis_generic", SerializationHelper.deserialize_by_tag(elem, "SwAxisGeneric")),
        "SW-MAX-AXIS": lambda obj, elem: setattr(obj, "sw_max_axis", SerializationHelper.deserialize_by_tag(elem, "Integer")),
        "SW-MIN-AXIS": lambda obj, elem: setattr(obj, "sw_min_axis", SerializationHelper.deserialize_by_tag(elem, "Integer")),
        "SW-VARIABLE-REF-PROXIES": lambda obj, elem: obj.sw_variable_ref_proxy_refs.append(ARRef.deserialize(elem)),
        "UNIT-REF": lambda obj, elem: setattr(obj, "unit_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize SwAxisIndividual."""
        super().__init__()
        self.compu_method_ref: Optional[ARRef] = None
        self.data_constr_ref: Optional[ARRef] = None
        self.input_variable_ref: Optional[ARRef] = None
        self.sw_axis_generic: Optional[SwAxisGeneric] = None
        self.sw_max_axis: Optional[Integer] = None
        self.sw_min_axis: Optional[Integer] = None
        self.sw_variable_ref_proxy_refs: list[ARRef] = []
        self.unit_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize SwAxisIndividual to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

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

        # Serialize sw_variable_ref_proxy_refs (list to container "SW-VARIABLE-REF-PROXY-REFS")
        if self.sw_variable_ref_proxy_refs:
            wrapper = ET.Element("SW-VARIABLE-REF-PROXY-REFS")
            for item in self.sw_variable_ref_proxy_refs:
                serialized = SerializationHelper.serialize_item(item, "SwVariableRefProxy")
                if serialized is not None:
                    child_elem = ET.Element("SW-VARIABLE-REF-PROXY-REF")
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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "COMPU-METHOD-REF":
                setattr(obj, "compu_method_ref", ARRef.deserialize(child))
            elif tag == "DATA-CONSTR-REF":
                setattr(obj, "data_constr_ref", ARRef.deserialize(child))
            elif tag == "INPUT-VARIABLE-REF":
                setattr(obj, "input_variable_ref", ARRef.deserialize(child))
            elif tag == "SW-AXIS-GENERIC":
                setattr(obj, "sw_axis_generic", SerializationHelper.deserialize_by_tag(child, "SwAxisGeneric"))
            elif tag == "SW-MAX-AXIS":
                setattr(obj, "sw_max_axis", SerializationHelper.deserialize_by_tag(child, "Integer"))
            elif tag == "SW-MIN-AXIS":
                setattr(obj, "sw_min_axis", SerializationHelper.deserialize_by_tag(child, "Integer"))
            elif tag == "SW-VARIABLE-REF-PROXIES":
                obj.sw_variable_ref_proxy_refs.append(ARRef.deserialize(child))
            elif tag == "UNIT-REF":
                setattr(obj, "unit_ref", ARRef.deserialize(child))

        return obj



class SwAxisIndividualBuilder(SwCalprmAxisTypePropsBuilder):
    """Builder for SwAxisIndividual with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SwAxisIndividual = SwAxisIndividual()


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


    def add_sw_variable_ref_proxy(self, item: SwVariableRefProxy) -> "SwAxisIndividualBuilder":
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


    def build(self) -> SwAxisIndividual:
        """Build and return the SwAxisIndividual instance with validation."""
        self._validate_instance()
        pass
        return self._obj