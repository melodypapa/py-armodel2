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

    _XML_TAG = "SUPERVISED-ENTITY-NEEDS"


    activate_at_start: Optional[Boolean]
    checkpoint_refs: list[Any]
    enable: Optional[Boolean]
    expected_alive: Optional[TimeValue]
    max_alive_cycle: Optional[TimeValue]
    min_alive_cycle: Optional[TimeValue]
    tolerated_failed: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "ACTIVATE-AT-START": lambda obj, elem: setattr(obj, "activate_at_start", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "CHECKPOINTSES": lambda obj, elem: obj.checkpoint_refs.append(ARRef.deserialize(elem)),
        "ENABLE": lambda obj, elem: setattr(obj, "enable", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "EXPECTED-ALIVE": lambda obj, elem: setattr(obj, "expected_alive", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "MAX-ALIVE-CYCLE": lambda obj, elem: setattr(obj, "max_alive_cycle", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "MIN-ALIVE-CYCLE": lambda obj, elem: setattr(obj, "min_alive_cycle", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "TOLERATED-FAILED": lambda obj, elem: setattr(obj, "tolerated_failed", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


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
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

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

        # Serialize checkpoint_refs (list to container "CHECKPOINTS-REFS")
        if self.checkpoint_refs:
            wrapper = ET.Element("CHECKPOINTS-REFS")
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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "ACTIVATE-AT-START":
                setattr(obj, "activate_at_start", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "CHECKPOINTSES":
                # Iterate through wrapper children
                for item_elem in child:
                    item_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    obj.checkpoint_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "any (SupervisedEntity)"))
            elif tag == "ENABLE":
                setattr(obj, "enable", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "EXPECTED-ALIVE":
                setattr(obj, "expected_alive", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "MAX-ALIVE-CYCLE":
                setattr(obj, "max_alive_cycle", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "MIN-ALIVE-CYCLE":
                setattr(obj, "min_alive_cycle", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "TOLERATED-FAILED":
                setattr(obj, "tolerated_failed", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

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