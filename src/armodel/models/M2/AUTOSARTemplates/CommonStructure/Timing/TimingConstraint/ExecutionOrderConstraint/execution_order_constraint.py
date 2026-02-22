"""ExecutionOrderConstraint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 118)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingConstraint_ExecutionOrderConstraint.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.timing_constraint import (
    TimingConstraint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.composition_sw_component_type import (
    CompositionSwComponentType,
)


class ExecutionOrderConstraint(TimingConstraint):
    """AUTOSAR ExecutionOrderConstraint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    base_ref: Optional[ARRef]
    execution_order: Optional[Any]
    ignore_order: Optional[Boolean]
    is_event: Optional[Boolean]
    ordered_elements: list[Any]
    permit_multiple: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize ExecutionOrderConstraint."""
        super().__init__()
        self.base_ref: Optional[ARRef] = None
        self.execution_order: Optional[Any] = None
        self.ignore_order: Optional[Boolean] = None
        self.is_event: Optional[Boolean] = None
        self.ordered_elements: list[Any] = []
        self.permit_multiple: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize ExecutionOrderConstraint to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ExecutionOrderConstraint, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize base_ref
        if self.base_ref is not None:
            serialized = SerializationHelper.serialize_item(self.base_ref, "CompositionSwComponentType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BASE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize execution_order
        if self.execution_order is not None:
            serialized = SerializationHelper.serialize_item(self.execution_order, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EXECUTION-ORDER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ignore_order
        if self.ignore_order is not None:
            serialized = SerializationHelper.serialize_item(self.ignore_order, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IGNORE-ORDER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize is_event
        if self.is_event is not None:
            serialized = SerializationHelper.serialize_item(self.is_event, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IS-EVENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ordered_elements (list to container "ORDERED-ELEMENTS")
        if self.ordered_elements:
            wrapper = ET.Element("ORDERED-ELEMENTS")
            for item in self.ordered_elements:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize permit_multiple
        if self.permit_multiple is not None:
            serialized = SerializationHelper.serialize_item(self.permit_multiple, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PERMIT-MULTIPLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ExecutionOrderConstraint":
        """Deserialize XML element to ExecutionOrderConstraint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ExecutionOrderConstraint object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ExecutionOrderConstraint, cls).deserialize(element)

        # Parse base_ref
        child = SerializationHelper.find_child_element(element, "BASE-REF")
        if child is not None:
            base_ref_value = ARRef.deserialize(child)
            obj.base_ref = base_ref_value

        # Parse execution_order
        child = SerializationHelper.find_child_element(element, "EXECUTION-ORDER")
        if child is not None:
            execution_order_value = child.text
            obj.execution_order = execution_order_value

        # Parse ignore_order
        child = SerializationHelper.find_child_element(element, "IGNORE-ORDER")
        if child is not None:
            ignore_order_value = child.text
            obj.ignore_order = ignore_order_value

        # Parse is_event
        child = SerializationHelper.find_child_element(element, "IS-EVENT")
        if child is not None:
            is_event_value = child.text
            obj.is_event = is_event_value

        # Parse ordered_elements (list from container "ORDERED-ELEMENTS")
        obj.ordered_elements = []
        container = SerializationHelper.find_child_element(element, "ORDERED-ELEMENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.ordered_elements.append(child_value)

        # Parse permit_multiple
        child = SerializationHelper.find_child_element(element, "PERMIT-MULTIPLE")
        if child is not None:
            permit_multiple_value = child.text
            obj.permit_multiple = permit_multiple_value

        return obj



class ExecutionOrderConstraintBuilder:
    """Builder for ExecutionOrderConstraint with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: ExecutionOrderConstraint = ExecutionOrderConstraint()


    def with_short_name(self, value: Identifier) -> "ExecutionOrderConstraintBuilder":
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

    def with_short_name_fragments(self, items: list[ShortNameFragment]) -> "ExecutionOrderConstraintBuilder":
        """Set short_name_fragments list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = list(items) if items else []
        return self

    def with_long_name(self, value: Optional[MultilanguageLongName]) -> "ExecutionOrderConstraintBuilder":
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

    def with_traces(self, items: list[Traceable]) -> "ExecutionOrderConstraintBuilder":
        """Set traces list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.traces = list(items) if items else []
        return self

    def with_timing_condition(self, value: Optional[TimingCondition]) -> "ExecutionOrderConstraintBuilder":
        """Set timing_condition attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.timing_condition = value
        return self

    def with_base(self, value: Optional[CompositionSwComponentType]) -> "ExecutionOrderConstraintBuilder":
        """Set base attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.base = value
        return self

    def with_execution_order(self, value: Optional[any (ExecutionOrder)]) -> "ExecutionOrderConstraintBuilder":
        """Set execution_order attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.execution_order = value
        return self

    def with_ignore_order(self, value: Optional[Boolean]) -> "ExecutionOrderConstraintBuilder":
        """Set ignore_order attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ignore_order = value
        return self

    def with_is_event(self, value: Optional[Boolean]) -> "ExecutionOrderConstraintBuilder":
        """Set is_event attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.is_event = value
        return self

    def with_ordered_elements(self, items: list[any (EOCExecutableEntity)]) -> "ExecutionOrderConstraintBuilder":
        """Set ordered_elements list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.ordered_elements = list(items) if items else []
        return self

    def with_permit_multiple(self, value: Optional[Boolean]) -> "ExecutionOrderConstraintBuilder":
        """Set permit_multiple attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.permit_multiple = value
        return self


    def add_short_name_fragment(self, item: ShortNameFragment) -> "ExecutionOrderConstraintBuilder":
        """Add a single item to short_name_fragments list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments.append(item)
        return self

    def clear_short_name_fragments(self) -> "ExecutionOrderConstraintBuilder":
        """Clear all items from short_name_fragments list.

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = []
        return self

    def add_trace(self, item: Traceable) -> "ExecutionOrderConstraintBuilder":
        """Add a single item to traces list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.traces.append(item)
        return self

    def clear_traces(self) -> "ExecutionOrderConstraintBuilder":
        """Clear all items from traces list.

        Returns:
            self for method chaining
        """
        self._obj.traces = []
        return self

    def add_ordered_element(self, item: any (EOCExecutableEntity)) -> "ExecutionOrderConstraintBuilder":
        """Add a single item to ordered_elements list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.ordered_elements.append(item)
        return self

    def clear_ordered_elements(self) -> "ExecutionOrderConstraintBuilder":
        """Clear all items from ordered_elements list.

        Returns:
            self for method chaining
        """
        self._obj.ordered_elements = []
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


    def build(self) -> ExecutionOrderConstraint:
        """Build and return the ExecutionOrderConstraint instance with validation."""
        self._validate_instance()
        pass
        return self._obj