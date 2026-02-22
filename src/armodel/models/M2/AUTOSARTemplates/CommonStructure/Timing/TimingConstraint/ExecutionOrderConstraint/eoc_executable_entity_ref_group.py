"""EOCExecutableEntityRefGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 119)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingConstraint_ExecutionOrderConstraint.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.ExecutionOrderConstraint.eoc_executable_entity_ref_abstract import (
    EOCExecutableEntityRefAbstract,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.ExecutionOrderConstraint import (
    LetDataExchangeParadigmEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description_event import (
    TimingDescriptionEvent,
)


class EOCExecutableEntityRefGroup(EOCExecutableEntityRefAbstract):
    """AUTOSAR EOCExecutableEntityRefGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    let_data_exchange: Optional[LetDataExchangeParadigmEnum]
    let_interval_refs: list[ARRef]
    max_cycle: Optional[PositiveInteger]
    max_cycles: Optional[Integer]
    max_slots: Optional[Integer]
    max_slots_per: Optional[PositiveInteger]
    nested_element_refs: list[Any]
    successor_refs: list[Any]
    triggering_event_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize EOCExecutableEntityRefGroup."""
        super().__init__()
        self.let_data_exchange: Optional[LetDataExchangeParadigmEnum] = None
        self.let_interval_refs: list[ARRef] = []
        self.max_cycle: Optional[PositiveInteger] = None
        self.max_cycles: Optional[Integer] = None
        self.max_slots: Optional[Integer] = None
        self.max_slots_per: Optional[PositiveInteger] = None
        self.nested_element_refs: list[Any] = []
        self.successor_refs: list[Any] = []
        self.triggering_event_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize EOCExecutableEntityRefGroup to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EOCExecutableEntityRefGroup, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize let_data_exchange
        if self.let_data_exchange is not None:
            serialized = SerializationHelper.serialize_item(self.let_data_exchange, "LetDataExchangeParadigmEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LET-DATA-EXCHANGE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize let_interval_refs (list to container "LET-INTERVAL-REFS")
        if self.let_interval_refs:
            wrapper = ET.Element("LET-INTERVAL-REFS")
            for item in self.let_interval_refs:
                serialized = SerializationHelper.serialize_item(item, "TimingDescriptionEvent")
                if serialized is not None:
                    child_elem = ET.Element("LET-INTERVAL-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize max_cycle
        if self.max_cycle is not None:
            serialized = SerializationHelper.serialize_item(self.max_cycle, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-CYCLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_cycles
        if self.max_cycles is not None:
            serialized = SerializationHelper.serialize_item(self.max_cycles, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-CYCLES")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_slots
        if self.max_slots is not None:
            serialized = SerializationHelper.serialize_item(self.max_slots, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-SLOTS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_slots_per
        if self.max_slots_per is not None:
            serialized = SerializationHelper.serialize_item(self.max_slots_per, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-SLOTS-PER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nested_element_refs (list to container "NESTED-ELEMENT-REFS")
        if self.nested_element_refs:
            wrapper = ET.Element("NESTED-ELEMENT-REFS")
            for item in self.nested_element_refs:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    child_elem = ET.Element("NESTED-ELEMENT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize successor_refs (list to container "SUCCESSOR-REFS")
        if self.successor_refs:
            wrapper = ET.Element("SUCCESSOR-REFS")
            for item in self.successor_refs:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    child_elem = ET.Element("SUCCESSOR-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize triggering_event_ref
        if self.triggering_event_ref is not None:
            serialized = SerializationHelper.serialize_item(self.triggering_event_ref, "TimingDescriptionEvent")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRIGGERING-EVENT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EOCExecutableEntityRefGroup":
        """Deserialize XML element to EOCExecutableEntityRefGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EOCExecutableEntityRefGroup object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EOCExecutableEntityRefGroup, cls).deserialize(element)

        # Parse let_data_exchange
        child = SerializationHelper.find_child_element(element, "LET-DATA-EXCHANGE")
        if child is not None:
            let_data_exchange_value = LetDataExchangeParadigmEnum.deserialize(child)
            obj.let_data_exchange = let_data_exchange_value

        # Parse let_interval_refs (list from container "LET-INTERVAL-REFS")
        obj.let_interval_refs = []
        container = SerializationHelper.find_child_element(element, "LET-INTERVAL-REFS")
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
                    obj.let_interval_refs.append(child_value)

        # Parse max_cycle
        child = SerializationHelper.find_child_element(element, "MAX-CYCLE")
        if child is not None:
            max_cycle_value = child.text
            obj.max_cycle = max_cycle_value

        # Parse max_cycles
        child = SerializationHelper.find_child_element(element, "MAX-CYCLES")
        if child is not None:
            max_cycles_value = child.text
            obj.max_cycles = max_cycles_value

        # Parse max_slots
        child = SerializationHelper.find_child_element(element, "MAX-SLOTS")
        if child is not None:
            max_slots_value = child.text
            obj.max_slots = max_slots_value

        # Parse max_slots_per
        child = SerializationHelper.find_child_element(element, "MAX-SLOTS-PER")
        if child is not None:
            max_slots_per_value = child.text
            obj.max_slots_per = max_slots_per_value

        # Parse nested_element_refs (list from container "NESTED-ELEMENT-REFS")
        obj.nested_element_refs = []
        container = SerializationHelper.find_child_element(element, "NESTED-ELEMENT-REFS")
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
                    obj.nested_element_refs.append(child_value)

        # Parse successor_refs (list from container "SUCCESSOR-REFS")
        obj.successor_refs = []
        container = SerializationHelper.find_child_element(element, "SUCCESSOR-REFS")
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
                    obj.successor_refs.append(child_value)

        # Parse triggering_event_ref
        child = SerializationHelper.find_child_element(element, "TRIGGERING-EVENT-REF")
        if child is not None:
            triggering_event_ref_value = ARRef.deserialize(child)
            obj.triggering_event_ref = triggering_event_ref_value

        return obj



class EOCExecutableEntityRefGroupBuilder:
    """Builder for EOCExecutableEntityRefGroup with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: EOCExecutableEntityRefGroup = EOCExecutableEntityRefGroup()


    def with_short_name(self, value: Identifier) -> "EOCExecutableEntityRefGroupBuilder":
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

    def with_short_name_fragments(self, items: list[ShortNameFragment]) -> "EOCExecutableEntityRefGroupBuilder":
        """Set short_name_fragments list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = list(items) if items else []
        return self

    def with_long_name(self, value: Optional[MultilanguageLongName]) -> "EOCExecutableEntityRefGroupBuilder":
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

    def with_admin_data(self, value: Optional[AdminData]) -> "EOCExecutableEntityRefGroupBuilder":
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

    def with_annotations(self, items: list[Annotation]) -> "EOCExecutableEntityRefGroupBuilder":
        """Set annotations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.annotations = list(items) if items else []
        return self

    def with_desc(self, value: Optional[MultiLanguageOverviewParagraph]) -> "EOCExecutableEntityRefGroupBuilder":
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

    def with_category(self, value: Optional[CategoryString]) -> "EOCExecutableEntityRefGroupBuilder":
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

    def with_introduction(self, value: Optional[DocumentationBlock]) -> "EOCExecutableEntityRefGroupBuilder":
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

    def with_uuid(self, value: Optional[String]) -> "EOCExecutableEntityRefGroupBuilder":
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

    def with_direct_successors(self, items: list[any (EOCExecutableEntity)]) -> "EOCExecutableEntityRefGroupBuilder":
        """Set direct_successors list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.direct_successors = list(items) if items else []
        return self

    def with_let_data_exchange(self, value: Optional[LetDataExchangeParadigmEnum]) -> "EOCExecutableEntityRefGroupBuilder":
        """Set let_data_exchange attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.let_data_exchange = value
        return self

    def with_let_intervals(self, items: list[TimingDescriptionEvent]) -> "EOCExecutableEntityRefGroupBuilder":
        """Set let_intervals list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.let_intervals = list(items) if items else []
        return self

    def with_max_cycle(self, value: Optional[PositiveInteger]) -> "EOCExecutableEntityRefGroupBuilder":
        """Set max_cycle attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.max_cycle = value
        return self

    def with_max_cycles(self, value: Optional[Integer]) -> "EOCExecutableEntityRefGroupBuilder":
        """Set max_cycles attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.max_cycles = value
        return self

    def with_max_slots(self, value: Optional[Integer]) -> "EOCExecutableEntityRefGroupBuilder":
        """Set max_slots attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.max_slots = value
        return self

    def with_max_slots_per(self, value: Optional[PositiveInteger]) -> "EOCExecutableEntityRefGroupBuilder":
        """Set max_slots_per attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.max_slots_per = value
        return self

    def with_nested_elements(self, items: list[any (EOCExecutableEntity)]) -> "EOCExecutableEntityRefGroupBuilder":
        """Set nested_elements list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.nested_elements = list(items) if items else []
        return self

    def with_successors(self, items: list[any (EOCExecutableEntity)]) -> "EOCExecutableEntityRefGroupBuilder":
        """Set successors list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.successors = list(items) if items else []
        return self

    def with_triggering_event(self, value: Optional[TimingDescriptionEvent]) -> "EOCExecutableEntityRefGroupBuilder":
        """Set triggering_event attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.triggering_event = value
        return self


    def add_short_name_fragment(self, item: ShortNameFragment) -> "EOCExecutableEntityRefGroupBuilder":
        """Add a single item to short_name_fragments list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments.append(item)
        return self

    def clear_short_name_fragments(self) -> "EOCExecutableEntityRefGroupBuilder":
        """Clear all items from short_name_fragments list.

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = []
        return self

    def add_annotation(self, item: Annotation) -> "EOCExecutableEntityRefGroupBuilder":
        """Add a single item to annotations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.annotations.append(item)
        return self

    def clear_annotations(self) -> "EOCExecutableEntityRefGroupBuilder":
        """Clear all items from annotations list.

        Returns:
            self for method chaining
        """
        self._obj.annotations = []
        return self

    def add_direct_successor(self, item: any (EOCExecutableEntity)) -> "EOCExecutableEntityRefGroupBuilder":
        """Add a single item to direct_successors list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.direct_successors.append(item)
        return self

    def clear_direct_successors(self) -> "EOCExecutableEntityRefGroupBuilder":
        """Clear all items from direct_successors list.

        Returns:
            self for method chaining
        """
        self._obj.direct_successors = []
        return self

    def add_let_interval(self, item: TimingDescriptionEvent) -> "EOCExecutableEntityRefGroupBuilder":
        """Add a single item to let_intervals list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.let_intervals.append(item)
        return self

    def clear_let_intervals(self) -> "EOCExecutableEntityRefGroupBuilder":
        """Clear all items from let_intervals list.

        Returns:
            self for method chaining
        """
        self._obj.let_intervals = []
        return self

    def add_nested_element(self, item: any (EOCExecutableEntity)) -> "EOCExecutableEntityRefGroupBuilder":
        """Add a single item to nested_elements list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.nested_elements.append(item)
        return self

    def clear_nested_elements(self) -> "EOCExecutableEntityRefGroupBuilder":
        """Clear all items from nested_elements list.

        Returns:
            self for method chaining
        """
        self._obj.nested_elements = []
        return self

    def add_successor(self, item: any (EOCExecutableEntity)) -> "EOCExecutableEntityRefGroupBuilder":
        """Add a single item to successors list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.successors.append(item)
        return self

    def clear_successors(self) -> "EOCExecutableEntityRefGroupBuilder":
        """Clear all items from successors list.

        Returns:
            self for method chaining
        """
        self._obj.successors = []
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


    def build(self) -> EOCExecutableEntityRefGroup:
        """Build and return the EOCExecutableEntityRefGroup instance with validation."""
        self._validate_instance()
        pass
        return self._obj