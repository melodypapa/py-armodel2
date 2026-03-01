"""ExecutableEntity AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 70)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 538)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2024)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 222)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_InternalBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel2.serialization.decorators import xml_element_name

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior import (
    ReentrancyLevelEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.exclusive_area import (
    ExclusiveArea,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.exclusive_area_nesting_order import (
    ExclusiveAreaNestingOrder,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.executable_entity_activation_reason import (
    ExecutableEntityActivationReason,
)
from armodel2.models.M2.MSR.DataDictionary.AuxillaryObjects.sw_addr_method import (
    SwAddrMethod,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ExecutableEntity(Identifiable, ABC):
    """AUTOSAR ExecutableEntity."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    activation_reasons: list[ExecutableEntityActivationReason]
    _can_enter_refs: list[ARRef]
    exclusive_area_nesting_order_refs: list[ARRef]
    minimum_start_interval: Optional[TimeValue]
    reentrancy_level: Optional[ReentrancyLevelEnum]
    runs_inside_refs: list[ARRef]
    sw_addr_method_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "ACTIVATION-REASONS": lambda obj, elem: obj.activation_reasons.append(SerializationHelper.deserialize_by_tag(elem, "ExecutableEntityActivationReason")),
        "CAN-ENTERS": lambda obj, elem: obj._can_enter_refs.append(ARRef.deserialize(elem)),
        "EXCLUSIVE-AREA-NESTING-ORDERS": lambda obj, elem: obj.exclusive_area_nesting_order_refs.append(ARRef.deserialize(elem)),
        "MINIMUM-START-INTERVAL": lambda obj, elem: setattr(obj, "minimum_start_interval", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "REENTRANCY-LEVEL": lambda obj, elem: setattr(obj, "reentrancy_level", ReentrancyLevelEnum.deserialize(elem)),
        "RUNS-INSIDES": lambda obj, elem: obj.runs_inside_refs.append(ARRef.deserialize(elem)),
        "SW-ADDR-METHOD-REF": lambda obj, elem: setattr(obj, "sw_addr_method_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize ExecutableEntity."""
        super().__init__()
        self.activation_reasons: list[ExecutableEntityActivationReason] = []
        self._can_enter_refs: list[ARRef] = []
        self.exclusive_area_nesting_order_refs: list[ARRef] = []
        self.minimum_start_interval: Optional[TimeValue] = None
        self.reentrancy_level: Optional[ReentrancyLevelEnum] = None
        self.runs_inside_refs: list[ARRef] = []
        self.sw_addr_method_ref: Optional[ARRef] = None
    @property
    @xml_element_name("CAN-ENTER-EXCLUSIVE-AREA-REFS/CAN-ENTER-EXCLUSIVE-AREA-REF")
    def can_enter_refs(self) -> list[ARRef]:
        """Get can_enter_refs with custom XML element name."""
        return self._can_enter_refs

    @can_enter_refs.setter
    def can_enter_refs(self, value: list[ARRef]) -> None:
        """Set can_enter_refs with custom XML element name."""
        self._can_enter_refs = value


    def serialize(self) -> ET.Element:
        """Serialize ExecutableEntity to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ExecutableEntity, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize activation_reasons (list to container "ACTIVATION-REASONS")
        if self.activation_reasons:
            wrapper = ET.Element("ACTIVATION-REASONS")
            for item in self.activation_reasons:
                serialized = SerializationHelper.serialize_item(item, "ExecutableEntityActivationReason")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize can_enter_refs (list to container "CAN-ENTER-EXCLUSIVE-AREA-REFS")
        if self.can_enter_refs:
            wrapper = ET.Element("CAN-ENTER-EXCLUSIVE-AREA-REFS")
            for item in self.can_enter_refs:
                serialized = SerializationHelper.serialize_item(item, "ExclusiveArea")
                if serialized is not None:
                    child_elem = ET.Element("CAN-ENTER-EXCLUSIVE-AREA-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize exclusive_area_nesting_order_refs (list to container "EXCLUSIVE-AREA-NESTING-ORDER-REFS")
        if self.exclusive_area_nesting_order_refs:
            wrapper = ET.Element("EXCLUSIVE-AREA-NESTING-ORDER-REFS")
            for item in self.exclusive_area_nesting_order_refs:
                serialized = SerializationHelper.serialize_item(item, "ExclusiveAreaNestingOrder")
                if serialized is not None:
                    child_elem = ET.Element("EXCLUSIVE-AREA-NESTING-ORDER-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize minimum_start_interval
        if self.minimum_start_interval is not None:
            serialized = SerializationHelper.serialize_item(self.minimum_start_interval, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MINIMUM-START-INTERVAL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize reentrancy_level
        if self.reentrancy_level is not None:
            serialized = SerializationHelper.serialize_item(self.reentrancy_level, "ReentrancyLevelEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REENTRANCY-LEVEL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize runs_inside_refs (list to container "RUNS-INSIDE-REFS")
        if self.runs_inside_refs:
            wrapper = ET.Element("RUNS-INSIDE-REFS")
            for item in self.runs_inside_refs:
                serialized = SerializationHelper.serialize_item(item, "ExclusiveArea")
                if serialized is not None:
                    child_elem = ET.Element("RUNS-INSIDE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize sw_addr_method_ref
        if self.sw_addr_method_ref is not None:
            serialized = SerializationHelper.serialize_item(self.sw_addr_method_ref, "SwAddrMethod")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-ADDR-METHOD-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ExecutableEntity":
        """Deserialize XML element to ExecutableEntity object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ExecutableEntity object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ExecutableEntity, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ACTIVATION-REASONS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.activation_reasons.append(SerializationHelper.deserialize_by_tag(item_elem, "ExecutableEntityActivationReason"))
            elif tag == "CAN-ENTERS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj._can_enter_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "ExclusiveArea"))
            elif tag == "EXCLUSIVE-AREA-NESTING-ORDERS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.exclusive_area_nesting_order_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "ExclusiveAreaNestingOrder"))
            elif tag == "MINIMUM-START-INTERVAL":
                setattr(obj, "minimum_start_interval", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "REENTRANCY-LEVEL":
                setattr(obj, "reentrancy_level", ReentrancyLevelEnum.deserialize(child))
            elif tag == "RUNS-INSIDES":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.runs_inside_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "ExclusiveArea"))
            elif tag == "SW-ADDR-METHOD-REF":
                setattr(obj, "sw_addr_method_ref", ARRef.deserialize(child))

        return obj



class ExecutableEntityBuilder(IdentifiableBuilder):
    """Builder for ExecutableEntity with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ExecutableEntity = ExecutableEntity()


    def with_activation_reasons(self, items: list[ExecutableEntityActivationReason]) -> "ExecutableEntityBuilder":
        """Set activation_reasons list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.activation_reasons = list(items) if items else []
        return self

    def with_can_enters(self, items: list[ExclusiveArea]) -> "ExecutableEntityBuilder":
        """Set can_enters list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.can_enters = list(items) if items else []
        return self

    def with_exclusive_area_nesting_orders(self, items: list[ExclusiveAreaNestingOrder]) -> "ExecutableEntityBuilder":
        """Set exclusive_area_nesting_orders list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.exclusive_area_nesting_orders = list(items) if items else []
        return self

    def with_minimum_start_interval(self, value: Optional[TimeValue]) -> "ExecutableEntityBuilder":
        """Set minimum_start_interval attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.minimum_start_interval = value
        return self

    def with_reentrancy_level(self, value: Optional[ReentrancyLevelEnum]) -> "ExecutableEntityBuilder":
        """Set reentrancy_level attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.reentrancy_level = value
        return self

    def with_runs_insides(self, items: list[ExclusiveArea]) -> "ExecutableEntityBuilder":
        """Set runs_insides list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.runs_insides = list(items) if items else []
        return self

    def with_sw_addr_method(self, value: Optional[SwAddrMethod]) -> "ExecutableEntityBuilder":
        """Set sw_addr_method attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_addr_method = value
        return self


    def add_activation_reason(self, item: ExecutableEntityActivationReason) -> "ExecutableEntityBuilder":
        """Add a single item to activation_reasons list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.activation_reasons.append(item)
        return self

    def clear_activation_reasons(self) -> "ExecutableEntityBuilder":
        """Clear all items from activation_reasons list.

        Returns:
            self for method chaining
        """
        self._obj.activation_reasons = []
        return self

    def add_can_enter(self, item: ExclusiveArea) -> "ExecutableEntityBuilder":
        """Add a single item to can_enters list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.can_enters.append(item)
        return self

    def clear_can_enters(self) -> "ExecutableEntityBuilder":
        """Clear all items from can_enters list.

        Returns:
            self for method chaining
        """
        self._obj.can_enters = []
        return self

    def add_exclusive_area_nesting_order(self, item: ExclusiveAreaNestingOrder) -> "ExecutableEntityBuilder":
        """Add a single item to exclusive_area_nesting_orders list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.exclusive_area_nesting_orders.append(item)
        return self

    def clear_exclusive_area_nesting_orders(self) -> "ExecutableEntityBuilder":
        """Clear all items from exclusive_area_nesting_orders list.

        Returns:
            self for method chaining
        """
        self._obj.exclusive_area_nesting_orders = []
        return self

    def add_runs_inside(self, item: ExclusiveArea) -> "ExecutableEntityBuilder":
        """Add a single item to runs_insides list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.runs_insides.append(item)
        return self

    def clear_runs_insides(self) -> "ExecutableEntityBuilder":
        """Clear all items from runs_insides list.

        Returns:
            self for method chaining
        """
        self._obj.runs_insides = []
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


    @abstractmethod
    def build(self) -> ExecutableEntity:
        """Build and return the ExecutableEntity instance (abstract)."""
        raise NotImplementedError