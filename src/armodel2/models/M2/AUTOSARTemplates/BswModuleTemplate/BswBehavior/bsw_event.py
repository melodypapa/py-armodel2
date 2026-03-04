"""BswEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 87)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 206)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.abstract_event import (
    AbstractEvent,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.abstract_event import AbstractEventBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_distinguished_partition import (
    BswDistinguishedPartition,
)
from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_module_entity import (
    BswModuleEntity,
)

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswOverview.InstanceRefs.mode_in_bsw_module_description_instance_ref import (
        ModeInBswModuleDescriptionInstanceRef,
    )



from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class BswEvent(AbstractEvent, ABC):
    """AUTOSAR BswEvent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    context_limitation_refs: list[ARRef]
    disabled_in_irefs: list[ModeInBswModuleDescriptionInstanceRef]
    starts_on_event_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "CONTEXT-LIMITATION-REFS": lambda obj, elem: [obj.context_limitation_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
        "DISABLED-INS-IREF": lambda obj, elem: obj.disabled_in_irefs.append(SerializationHelper.deserialize_by_tag(elem, "ModeInBswModuleDescriptionInstanceRef")),
        "STARTS-ON-EVENT-REF": ("_POLYMORPHIC", "starts_on_event_ref", ["BswCalledEntity", "BswInterruptEntity", "BswSchedulableEntity"]),
    }


    def __init__(self) -> None:
        """Initialize BswEvent."""
        super().__init__()
        self.context_limitation_refs: list[ARRef] = []
        self.disabled_in_irefs: list[ModeInBswModuleDescriptionInstanceRef] = []
        self.starts_on_event_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize BswEvent to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BswEvent, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize context_limitation_refs (list to container "CONTEXT-LIMITATION-REFS")
        if self.context_limitation_refs:
            wrapper = ET.Element("CONTEXT-LIMITATION-REFS")
            for item in self.context_limitation_refs:
                serialized = SerializationHelper.serialize_item(item, "BswDistinguishedPartition")
                if serialized is not None:
                    child_elem = ET.Element("CONTEXT-LIMITATION-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize disabled_in_irefs (list of instance references with wrapper "DISABLED-INS-IREF")
        if self.disabled_in_irefs:
            serialized = SerializationHelper.serialize_item(self.disabled_in_irefs, "ModeInBswModuleDescriptionInstanceRef")
            if serialized is not None:
                # Wrap in IREF wrapper element
                iref_wrapper = ET.Element("DISABLED-INS-IREF")
                # Flatten: append children of serialized element directly to iref wrapper
                for child in serialized:
                    iref_wrapper.append(child)
                elem.append(iref_wrapper)

        # Serialize starts_on_event_ref
        if self.starts_on_event_ref is not None:
            serialized = SerializationHelper.serialize_item(self.starts_on_event_ref, "BswModuleEntity")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("STARTS-ON-EVENT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswEvent":
        """Deserialize XML element to BswEvent object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswEvent object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BswEvent, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CONTEXT-LIMITATION-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.context_limitation_refs.append(ARRef.deserialize(item_elem))
            elif tag == "DISABLED-IN-IREFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.disabled_in_irefs.append(SerializationHelper.deserialize_by_tag(item_elem, "ModeInBswModuleDescriptionInstanceRef"))
            elif tag == "STARTS-ON-EVENT-REF":
                setattr(obj, "starts_on_event_ref", ARRef.deserialize(child))

        return obj



class BswEventBuilder(AbstractEventBuilder):
    """Builder for BswEvent with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: BswEvent = BswEvent()


    def with_context_limitations(self, items: list[BswDistinguishedPartition]) -> "BswEventBuilder":
        """Set context_limitations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.context_limitations = list(items) if items else []
        return self

    def with_disabled_ins(self, items: list[ModeInBswModuleDescriptionInstanceRef]) -> "BswEventBuilder":
        """Set disabled_ins list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.disabled_ins = list(items) if items else []
        return self

    def with_starts_on_event(self, value: Optional[BswModuleEntity]) -> "BswEventBuilder":
        """Set starts_on_event attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.starts_on_event = value
        return self


    def add_context_limitation(self, item: BswDistinguishedPartition) -> "BswEventBuilder":
        """Add a single item to context_limitations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.context_limitations.append(item)
        return self

    def clear_context_limitations(self) -> "BswEventBuilder":
        """Clear all items from context_limitations list.

        Returns:
            self for method chaining
        """
        self._obj.context_limitations = []
        return self

    def add_disabled_in(self, item: ModeInBswModuleDescriptionInstanceRef) -> "BswEventBuilder":
        """Add a single item to disabled_ins list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.disabled_ins.append(item)
        return self

    def clear_disabled_ins(self) -> "BswEventBuilder":
        """Clear all items from disabled_ins list.

        Returns:
            self for method chaining
        """
        self._obj.disabled_ins = []
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
    def build(self) -> BswEvent:
        """Build and return the BswEvent instance (abstract)."""
        raise NotImplementedError