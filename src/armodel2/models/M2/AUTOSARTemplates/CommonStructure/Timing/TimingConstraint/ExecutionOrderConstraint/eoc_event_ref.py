"""EOCEventRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 120)

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
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.abstract_event import (
    AbstractEvent,
)
from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswImplementation.bsw_implementation import (
    BswImplementation,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class EOCEventRef(EOCExecutableEntityRefAbstract):
    """AUTOSAR EOCEventRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    bsw_module_ref: Optional[ARRef]
    component: Optional[Any]
    event_ref: Optional[ARRef]
    successor_refs: list[Any]
    def __init__(self) -> None:
        """Initialize EOCEventRef."""
        super().__init__()
        self.bsw_module_ref: Optional[ARRef] = None
        self.component: Optional[Any] = None
        self.event_ref: Optional[ARRef] = None
        self.successor_refs: list[Any] = []

    def serialize(self) -> ET.Element:
        """Serialize EOCEventRef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EOCEventRef, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize bsw_module_ref
        if self.bsw_module_ref is not None:
            serialized = SerializationHelper.serialize_item(self.bsw_module_ref, "BswImplementation")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BSW-MODULE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize component
        if self.component is not None:
            serialized = SerializationHelper.serialize_item(self.component, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COMPONENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize event_ref
        if self.event_ref is not None:
            serialized = SerializationHelper.serialize_item(self.event_ref, "AbstractEvent")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EVENT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

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

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EOCEventRef":
        """Deserialize XML element to EOCEventRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EOCEventRef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EOCEventRef, cls).deserialize(element)

        # Parse bsw_module_ref
        child = SerializationHelper.find_child_element(element, "BSW-MODULE-REF")
        if child is not None:
            bsw_module_ref_value = ARRef.deserialize(child)
            obj.bsw_module_ref = bsw_module_ref_value

        # Parse component
        child = SerializationHelper.find_child_element(element, "COMPONENT")
        if child is not None:
            component_value = child.text
            obj.component = component_value

        # Parse event_ref
        child = SerializationHelper.find_child_element(element, "EVENT-REF")
        if child is not None:
            event_ref_value = ARRef.deserialize(child)
            obj.event_ref = event_ref_value

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

        return obj



class EOCEventRefBuilder(EOCExecutableEntityRefAbstractBuilder):
    """Builder for EOCEventRef with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EOCEventRef = EOCEventRef()


    def with_bsw_module(self, value: Optional[BswImplementation]) -> "EOCEventRefBuilder":
        """Set bsw_module attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.bsw_module = value
        return self

    def with_component(self, value: Optional[any (SwComponent)]) -> "EOCEventRefBuilder":
        """Set component attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.component = value
        return self

    def with_event(self, value: Optional[AbstractEvent]) -> "EOCEventRefBuilder":
        """Set event attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.event = value
        return self

    def with_successors(self, items: list[any (EOCExecutableEntity)]) -> "EOCEventRefBuilder":
        """Set successors list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.successors = list(items) if items else []
        return self


    def add_successor(self, item: any (EOCExecutableEntity)) -> "EOCEventRefBuilder":
        """Add a single item to successors list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.successors.append(item)
        return self

    def clear_successors(self) -> "EOCEventRefBuilder":
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


    def build(self) -> EOCEventRef:
        """Build and return the EOCEventRef instance with validation."""
        self._validate_instance()
        pass
        return self._obj