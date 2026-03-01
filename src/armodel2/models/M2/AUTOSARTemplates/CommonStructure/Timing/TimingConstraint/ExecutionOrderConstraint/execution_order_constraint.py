"""ExecutionOrderConstraint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 118)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingConstraint_ExecutionOrderConstraint.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.timing_constraint import (
    TimingConstraint,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.timing_constraint import TimingConstraintBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.composition_sw_component_type import (
    CompositionSwComponentType,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ExecutionOrderConstraint(TimingConstraint):
    """AUTOSAR ExecutionOrderConstraint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "EXECUTION-ORDER-CONSTRAINT"


    base_ref: Optional[ARRef]
    execution_order: Optional[Any]
    ignore_order: Optional[Boolean]
    is_event: Optional[Boolean]
    ordered_elements: list[Any]
    permit_multiple: Optional[Boolean]
    _DESERIALIZE_DISPATCH = {
        "BASE-REF": lambda obj, elem: setattr(obj, "base_ref", ARRef.deserialize(elem)),
        "EXECUTION-ORDER": lambda obj, elem: setattr(obj, "execution_order", SerializationHelper.deserialize_by_tag(elem, "any (ExecutionOrder)")),
        "IGNORE-ORDER": lambda obj, elem: setattr(obj, "ignore_order", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "IS-EVENT": lambda obj, elem: setattr(obj, "is_event", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "ORDERED-ELEMENTS": lambda obj, elem: obj.ordered_elements.append(SerializationHelper.deserialize_by_tag(elem, "any (EOCExecutableEntity)")),
        "PERMIT-MULTIPLE": lambda obj, elem: setattr(obj, "permit_multiple", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
    }


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
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "BASE-REF":
                setattr(obj, "base_ref", ARRef.deserialize(child))
            elif tag == "EXECUTION-ORDER":
                setattr(obj, "execution_order", SerializationHelper.deserialize_by_tag(child, "any (ExecutionOrder)"))
            elif tag == "IGNORE-ORDER":
                setattr(obj, "ignore_order", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "IS-EVENT":
                setattr(obj, "is_event", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "ORDERED-ELEMENTS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.ordered_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "any (EOCExecutableEntity)"))
            elif tag == "PERMIT-MULTIPLE":
                setattr(obj, "permit_multiple", SerializationHelper.deserialize_by_tag(child, "Boolean"))

        return obj



class ExecutionOrderConstraintBuilder(TimingConstraintBuilder):
    """Builder for ExecutionOrderConstraint with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ExecutionOrderConstraint = ExecutionOrderConstraint()


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


    def build(self) -> ExecutionOrderConstraint:
        """Build and return the ExecutionOrderConstraint instance with validation."""
        self._validate_instance()
        pass
        return self._obj