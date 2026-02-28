"""EOCExecutableEntityRefGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 119)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingConstraint_ExecutionOrderConstraint.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.ExecutionOrderConstraint.eoc_executable_entity_ref_abstract import (
    EOCExecutableEntityRefAbstract,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.ExecutionOrderConstraint.eoc_executable_entity_ref_abstract import EOCExecutableEntityRefAbstractBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.ExecutionOrderConstraint import (
    LetDataExchangeParadigmEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description_event import (
    TimingDescriptionEvent,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class EOCExecutableEntityRefGroup(EOCExecutableEntityRefAbstract):
    """AUTOSAR EOCExecutableEntityRefGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "E-O-C-EXECUTABLE-ENTITY-REF-GROUP"


    let_data_exchange: Optional[LetDataExchangeParadigmEnum]
    let_interval_refs: list[ARRef]
    max_cycle: Optional[PositiveInteger]
    max_cycles: Optional[Integer]
    max_slots: Optional[Integer]
    max_slots_per: Optional[PositiveInteger]
    nested_element_refs: list[Any]
    successor_refs: list[Any]
    triggering_event_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "LET-DATA-EXCHANGE": lambda obj, elem: setattr(obj, "let_data_exchange", LetDataExchangeParadigmEnum.deserialize(elem)),
        "LET-INTERVALS": lambda obj, elem: obj.let_interval_refs.append(ARRef.deserialize(elem)),
        "MAX-CYCLE": lambda obj, elem: setattr(obj, "max_cycle", elem.text),
        "MAX-CYCLES": lambda obj, elem: setattr(obj, "max_cycles", elem.text),
        "MAX-SLOTS": lambda obj, elem: setattr(obj, "max_slots", elem.text),
        "MAX-SLOTS-PER": lambda obj, elem: setattr(obj, "max_slots_per", elem.text),
        "NESTED-ELEMENTS": lambda obj, elem: obj.nested_element_refs.append(ARRef.deserialize(elem)),
        "SUCCESSORS": lambda obj, elem: obj.successor_refs.append(ARRef.deserialize(elem)),
        "TRIGGERING-EVENT-REF": lambda obj, elem: setattr(obj, "triggering_event_ref", ARRef.deserialize(elem)),
    }


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
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

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
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
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
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
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
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
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



class EOCExecutableEntityRefGroupBuilder(EOCExecutableEntityRefAbstractBuilder):
    """Builder for EOCExecutableEntityRefGroup with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EOCExecutableEntityRefGroup = EOCExecutableEntityRefGroup()


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


    def build(self) -> EOCExecutableEntityRefGroup:
        """Build and return the EOCExecutableEntityRefGroup instance with validation."""
        self._validate_instance()
        pass
        return self._obj