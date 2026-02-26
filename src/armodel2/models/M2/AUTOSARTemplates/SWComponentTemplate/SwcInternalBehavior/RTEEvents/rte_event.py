"""RTEEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 327)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 541)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 208)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 238)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_RTEEvents.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.abstract_event import (
    AbstractEvent,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.abstract_event import AbstractEventBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.runnable_entity import (
        RunnableEntity,
    )



from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class RTEEvent(AbstractEvent, ABC):
    """AUTOSAR RTEEvent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    disabled_mode_instance_refs: list[ModeDeclaration]
    start_on_event_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize RTEEvent."""
        super().__init__()
        self.disabled_mode_instance_refs: list[ModeDeclaration] = []
        self.start_on_event_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize RTEEvent to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(RTEEvent, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize disabled_mode_instance_refs (list to container "DISABLED-MODE-INSTANCE-REFS")
        if self.disabled_mode_instance_refs:
            wrapper = ET.Element("DISABLED-MODE-INSTANCE-REFS")
            for item in self.disabled_mode_instance_refs:
                serialized = SerializationHelper.serialize_item(item, "ModeDeclaration")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize start_on_event_ref
        if self.start_on_event_ref is not None:
            serialized = SerializationHelper.serialize_item(self.start_on_event_ref, "RunnableEntity")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("START-ON-EVENT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RTEEvent":
        """Deserialize XML element to RTEEvent object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RTEEvent object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(RTEEvent, cls).deserialize(element)

        # Parse disabled_mode_instance_refs (list from container "DISABLED-MODE-INSTANCE-REFS")
        obj.disabled_mode_instance_refs = []
        container = SerializationHelper.find_child_element(element, "DISABLED-MODE-INSTANCE-REFS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.disabled_mode_instance_refs.append(child_value)

        # Parse start_on_event_ref
        child = SerializationHelper.find_child_element(element, "START-ON-EVENT-REF")
        if child is not None:
            start_on_event_ref_value = ARRef.deserialize(child)
            obj.start_on_event_ref = start_on_event_ref_value

        return obj



class RTEEventBuilder(AbstractEventBuilder):
    """Builder for RTEEvent with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: RTEEvent = RTEEvent()


    def with_disabled_mode_instance_refs(self, items: list[ModeDeclaration]) -> "RTEEventBuilder":
        """Set disabled_mode_instance_refs list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.disabled_mode_instance_refs = list(items) if items else []
        return self

    def with_start_on_event(self, value: Optional[RunnableEntity]) -> "RTEEventBuilder":
        """Set start_on_event attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.start_on_event = value
        return self


    def add_disabled_mode_instance_ref(self, item: ModeDeclaration) -> "RTEEventBuilder":
        """Add a single item to disabled_mode_instance_refs list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.disabled_mode_instance_refs.append(item)
        return self

    def clear_disabled_mode_instance_refs(self) -> "RTEEventBuilder":
        """Clear all items from disabled_mode_instance_refs list.

        Returns:
            self for method chaining
        """
        self._obj.disabled_mode_instance_refs = []
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
    def build(self) -> RTEEvent:
        """Build and return the RTEEvent instance (abstract)."""
        raise NotImplementedError