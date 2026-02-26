"""SupervisedEntityNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 234)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 707)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_needs import (
    ServiceNeeds,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_needs import ServiceNeedsBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    TimeValue,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SupervisedEntityNeeds(ServiceNeeds):
    """AUTOSAR SupervisedEntityNeeds."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    activate_at_start: Optional[Boolean]
    checkpoint_refs: list[Any]
    enable: Optional[Boolean]
    expected_alive: Optional[TimeValue]
    max_alive_cycle: Optional[TimeValue]
    min_alive_cycle: Optional[TimeValue]
    tolerated_failed: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize SupervisedEntityNeeds."""
        super().__init__()
        self.activate_at_start: Optional[Boolean] = None
        self.checkpoint_refs: list[Any] = []
        self.enable: Optional[Boolean] = None
        self.expected_alive: Optional[TimeValue] = None
        self.max_alive_cycle: Optional[TimeValue] = None
        self.min_alive_cycle: Optional[TimeValue] = None
        self.tolerated_failed: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize SupervisedEntityNeeds to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SupervisedEntityNeeds, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize activate_at_start
        if self.activate_at_start is not None:
            serialized = SerializationHelper.serialize_item(self.activate_at_start, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ACTIVATE-AT-START")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize checkpoint_refs (list to container "CHECKPOINT-REFS")
        if self.checkpoint_refs:
            wrapper = ET.Element("CHECKPOINT-REFS")
            for item in self.checkpoint_refs:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    child_elem = ET.Element("CHECKPOINT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize enable
        if self.enable is not None:
            serialized = SerializationHelper.serialize_item(self.enable, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ENABLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize expected_alive
        if self.expected_alive is not None:
            serialized = SerializationHelper.serialize_item(self.expected_alive, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EXPECTED-ALIVE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_alive_cycle
        if self.max_alive_cycle is not None:
            serialized = SerializationHelper.serialize_item(self.max_alive_cycle, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-ALIVE-CYCLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize min_alive_cycle
        if self.min_alive_cycle is not None:
            serialized = SerializationHelper.serialize_item(self.min_alive_cycle, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MIN-ALIVE-CYCLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tolerated_failed
        if self.tolerated_failed is not None:
            serialized = SerializationHelper.serialize_item(self.tolerated_failed, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TOLERATED-FAILED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SupervisedEntityNeeds":
        """Deserialize XML element to SupervisedEntityNeeds object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SupervisedEntityNeeds object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SupervisedEntityNeeds, cls).deserialize(element)

        # Parse activate_at_start
        child = SerializationHelper.find_child_element(element, "ACTIVATE-AT-START")
        if child is not None:
            activate_at_start_value = child.text
            obj.activate_at_start = activate_at_start_value

        # Parse checkpoint_refs (list from container "CHECKPOINT-REFS")
        obj.checkpoint_refs = []
        container = SerializationHelper.find_child_element(element, "CHECKPOINT-REFS")
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
                    obj.checkpoint_refs.append(child_value)

        # Parse enable
        child = SerializationHelper.find_child_element(element, "ENABLE")
        if child is not None:
            enable_value = child.text
            obj.enable = enable_value

        # Parse expected_alive
        child = SerializationHelper.find_child_element(element, "EXPECTED-ALIVE")
        if child is not None:
            expected_alive_value = child.text
            obj.expected_alive = expected_alive_value

        # Parse max_alive_cycle
        child = SerializationHelper.find_child_element(element, "MAX-ALIVE-CYCLE")
        if child is not None:
            max_alive_cycle_value = child.text
            obj.max_alive_cycle = max_alive_cycle_value

        # Parse min_alive_cycle
        child = SerializationHelper.find_child_element(element, "MIN-ALIVE-CYCLE")
        if child is not None:
            min_alive_cycle_value = child.text
            obj.min_alive_cycle = min_alive_cycle_value

        # Parse tolerated_failed
        child = SerializationHelper.find_child_element(element, "TOLERATED-FAILED")
        if child is not None:
            tolerated_failed_value = child.text
            obj.tolerated_failed = tolerated_failed_value

        return obj



class SupervisedEntityNeedsBuilder(ServiceNeedsBuilder):
    """Builder for SupervisedEntityNeeds with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SupervisedEntityNeeds = SupervisedEntityNeeds()


    def with_activate_at_start(self, value: Optional[Boolean]) -> "SupervisedEntityNeedsBuilder":
        """Set activate_at_start attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.activate_at_start = value
        return self

    def with_checkpointses(self, items: list[any (SupervisedEntity)]) -> "SupervisedEntityNeedsBuilder":
        """Set checkpointses list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.checkpointses = list(items) if items else []
        return self

    def with_enable(self, value: Optional[Boolean]) -> "SupervisedEntityNeedsBuilder":
        """Set enable attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.enable = value
        return self

    def with_expected_alive(self, value: Optional[TimeValue]) -> "SupervisedEntityNeedsBuilder":
        """Set expected_alive attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.expected_alive = value
        return self

    def with_max_alive_cycle(self, value: Optional[TimeValue]) -> "SupervisedEntityNeedsBuilder":
        """Set max_alive_cycle attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.max_alive_cycle = value
        return self

    def with_min_alive_cycle(self, value: Optional[TimeValue]) -> "SupervisedEntityNeedsBuilder":
        """Set min_alive_cycle attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.min_alive_cycle = value
        return self

    def with_tolerated_failed(self, value: Optional[PositiveInteger]) -> "SupervisedEntityNeedsBuilder":
        """Set tolerated_failed attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tolerated_failed = value
        return self


    def add_checkpoints(self, item: any (SupervisedEntity)) -> "SupervisedEntityNeedsBuilder":
        """Add a single item to checkpointses list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.checkpointses.append(item)
        return self

    def clear_checkpointses(self) -> "SupervisedEntityNeedsBuilder":
        """Clear all items from checkpointses list.

        Returns:
            self for method chaining
        """
        self._obj.checkpointses = []
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


    def build(self) -> SupervisedEntityNeeds:
        """Build and return the SupervisedEntityNeeds instance with validation."""
        self._validate_instance()
        pass
        return self._obj