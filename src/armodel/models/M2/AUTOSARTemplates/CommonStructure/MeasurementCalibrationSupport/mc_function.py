"""McFunction AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 186)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_MeasurementCalibrationSupport.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport.mc_function_data_ref_set import (
    McFunctionDataRefSet,
)


class McFunction(ARElement):
    """AUTOSAR McFunction."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def_calprm_set_ref: Optional[ARRef]
    in_measurement_ref: Optional[ARRef]
    loc_ref: Optional[ARRef]
    out_ref: Optional[ARRef]
    ref_calprm_set_ref: Optional[ARRef]
    sub_function_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize McFunction."""
        super().__init__()
        self.def_calprm_set_ref: Optional[ARRef] = None
        self.in_measurement_ref: Optional[ARRef] = None
        self.loc_ref: Optional[ARRef] = None
        self.out_ref: Optional[ARRef] = None
        self.ref_calprm_set_ref: Optional[ARRef] = None
        self.sub_function_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize McFunction to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(McFunction, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize def_calprm_set_ref
        if self.def_calprm_set_ref is not None:
            serialized = SerializationHelper.serialize_item(self.def_calprm_set_ref, "McFunctionDataRefSet")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DEF-CALPRM-SET-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize in_measurement_ref
        if self.in_measurement_ref is not None:
            serialized = SerializationHelper.serialize_item(self.in_measurement_ref, "McFunctionDataRefSet")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IN-MEASUREMENT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize loc_ref
        if self.loc_ref is not None:
            serialized = SerializationHelper.serialize_item(self.loc_ref, "McFunctionDataRefSet")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LOC-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize out_ref
        if self.out_ref is not None:
            serialized = SerializationHelper.serialize_item(self.out_ref, "McFunctionDataRefSet")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("OUT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ref_calprm_set_ref
        if self.ref_calprm_set_ref is not None:
            serialized = SerializationHelper.serialize_item(self.ref_calprm_set_ref, "McFunctionDataRefSet")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REF-CALPRM-SET-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sub_function_refs (list to container "SUB-FUNCTION-REFS")
        if self.sub_function_refs:
            wrapper = ET.Element("SUB-FUNCTION-REFS")
            for item in self.sub_function_refs:
                serialized = SerializationHelper.serialize_item(item, "McFunction")
                if serialized is not None:
                    child_elem = ET.Element("SUB-FUNCTION-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "McFunction":
        """Deserialize XML element to McFunction object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized McFunction object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(McFunction, cls).deserialize(element)

        # Parse def_calprm_set_ref
        child = SerializationHelper.find_child_element(element, "DEF-CALPRM-SET-REF")
        if child is not None:
            def_calprm_set_ref_value = ARRef.deserialize(child)
            obj.def_calprm_set_ref = def_calprm_set_ref_value

        # Parse in_measurement_ref
        child = SerializationHelper.find_child_element(element, "IN-MEASUREMENT-REF")
        if child is not None:
            in_measurement_ref_value = ARRef.deserialize(child)
            obj.in_measurement_ref = in_measurement_ref_value

        # Parse loc_ref
        child = SerializationHelper.find_child_element(element, "LOC-REF")
        if child is not None:
            loc_ref_value = ARRef.deserialize(child)
            obj.loc_ref = loc_ref_value

        # Parse out_ref
        child = SerializationHelper.find_child_element(element, "OUT-REF")
        if child is not None:
            out_ref_value = ARRef.deserialize(child)
            obj.out_ref = out_ref_value

        # Parse ref_calprm_set_ref
        child = SerializationHelper.find_child_element(element, "REF-CALPRM-SET-REF")
        if child is not None:
            ref_calprm_set_ref_value = ARRef.deserialize(child)
            obj.ref_calprm_set_ref = ref_calprm_set_ref_value

        # Parse sub_function_refs (list from container "SUB-FUNCTION-REFS")
        obj.sub_function_refs = []
        container = SerializationHelper.find_child_element(element, "SUB-FUNCTION-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.sub_function_refs.append(child_value)

        return obj



class McFunctionBuilder:
    """Builder for McFunction with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: McFunction = McFunction()


    def with_short_name(self, value: Identifier) -> "McFunctionBuilder":
        """Set short_name attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.short_name = value
        return self

    def with_short_name_fragments(self, items: list[ShortNameFragment]) -> "McFunctionBuilder":
        """Set short_name_fragments list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = list(items) if items else []
        return self

    def with_long_name(self, value: Optional[MultilanguageLongName]) -> "McFunctionBuilder":
        """Set long_name attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.long_name = value
        return self

    def with_admin_data(self, value: Optional[AdminData]) -> "McFunctionBuilder":
        """Set admin_data attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.admin_data = value
        return self

    def with_annotations(self, items: list[Annotation]) -> "McFunctionBuilder":
        """Set annotations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.annotations = list(items) if items else []
        return self

    def with_desc(self, value: Optional[MultiLanguageOverviewParagraph]) -> "McFunctionBuilder":
        """Set desc attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.desc = value
        return self

    def with_category(self, value: Optional[CategoryString]) -> "McFunctionBuilder":
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

    def with_introduction(self, value: Optional[DocumentationBlock]) -> "McFunctionBuilder":
        """Set introduction attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.introduction = value
        return self

    def with_uuid(self, value: Optional[String]) -> "McFunctionBuilder":
        """Set uuid attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.uuid = value
        return self

    def with_def_calprm_set(self, value: Optional[McFunctionDataRefSet]) -> "McFunctionBuilder":
        """Set def_calprm_set attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.def_calprm_set = value
        return self

    def with_in_measurement(self, value: Optional[McFunctionDataRefSet]) -> "McFunctionBuilder":
        """Set in_measurement attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.in_measurement = value
        return self

    def with_loc(self, value: Optional[McFunctionDataRefSet]) -> "McFunctionBuilder":
        """Set loc attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.loc = value
        return self

    def with_out(self, value: Optional[McFunctionDataRefSet]) -> "McFunctionBuilder":
        """Set out attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.out = value
        return self

    def with_ref_calprm_set(self, value: Optional[McFunctionDataRefSet]) -> "McFunctionBuilder":
        """Set ref_calprm_set attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ref_calprm_set = value
        return self

    def with_sub_functions(self, items: list[McFunction]) -> "McFunctionBuilder":
        """Set sub_functions list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.sub_functions = list(items) if items else []
        return self


    def add_short_name_fragment(self, item: ShortNameFragment) -> "McFunctionBuilder":
        """Add a single item to short_name_fragments list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments.append(item)
        return self

    def clear_short_name_fragments(self) -> "McFunctionBuilder":
        """Clear all items from short_name_fragments list.

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = []
        return self

    def add_annotation(self, item: Annotation) -> "McFunctionBuilder":
        """Add a single item to annotations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.annotations.append(item)
        return self

    def clear_annotations(self) -> "McFunctionBuilder":
        """Clear all items from annotations list.

        Returns:
            self for method chaining
        """
        self._obj.annotations = []
        return self

    def add_sub_function(self, item: McFunction) -> "McFunctionBuilder":
        """Add a single item to sub_functions list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.sub_functions.append(item)
        return self

    def clear_sub_functions(self) -> "McFunctionBuilder":
        """Clear all items from sub_functions list.

        Returns:
            self for method chaining
        """
        self._obj.sub_functions = []
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


    def build(self) -> McFunction:
        """Build and return the McFunction instance with validation."""
        self._validate_instance()
        pass
        return self._obj