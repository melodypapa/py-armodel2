"""SwcBswMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 110)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 656)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 217)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_SwcBswMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_internal_behavior import (
    BswInternalBehavior,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.SwcBswMapping.swc_bsw_runnable_mapping import (
    SwcBswRunnableMapping,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.SwcBswMapping.swc_bsw_synchronized_mode_group_prototype import (
    SwcBswSynchronizedModeGroupPrototype,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.SwcBswMapping.swc_bsw_synchronized_trigger import (
    SwcBswSynchronizedTrigger,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.swc_internal_behavior import (
    SwcInternalBehavior,
)


class SwcBswMapping(ARElement):
    """AUTOSAR SwcBswMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    bsw_behavior_ref: Optional[ARRef]
    runnable_mappings: list[SwcBswRunnableMapping]
    swc_behavior_ref: Optional[ARRef]
    synchronized_mode_groups: list[SwcBswSynchronizedModeGroupPrototype]
    synchronized_triggers: list[SwcBswSynchronizedTrigger]
    def __init__(self) -> None:
        """Initialize SwcBswMapping."""
        super().__init__()
        self.bsw_behavior_ref: Optional[ARRef] = None
        self.runnable_mappings: list[SwcBswRunnableMapping] = []
        self.swc_behavior_ref: Optional[ARRef] = None
        self.synchronized_mode_groups: list[SwcBswSynchronizedModeGroupPrototype] = []
        self.synchronized_triggers: list[SwcBswSynchronizedTrigger] = []

    def serialize(self) -> ET.Element:
        """Serialize SwcBswMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwcBswMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize bsw_behavior_ref
        if self.bsw_behavior_ref is not None:
            serialized = SerializationHelper.serialize_item(self.bsw_behavior_ref, "BswInternalBehavior")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BSW-BEHAVIOR-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize runnable_mappings (list to container "RUNNABLE-MAPPINGS")
        if self.runnable_mappings:
            wrapper = ET.Element("RUNNABLE-MAPPINGS")
            for item in self.runnable_mappings:
                serialized = SerializationHelper.serialize_item(item, "SwcBswRunnableMapping")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize swc_behavior_ref
        if self.swc_behavior_ref is not None:
            serialized = SerializationHelper.serialize_item(self.swc_behavior_ref, "SwcInternalBehavior")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SWC-BEHAVIOR-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize synchronized_mode_groups (list to container "SYNCHRONIZED-MODE-GROUPS")
        if self.synchronized_mode_groups:
            wrapper = ET.Element("SYNCHRONIZED-MODE-GROUPS")
            for item in self.synchronized_mode_groups:
                serialized = SerializationHelper.serialize_item(item, "SwcBswSynchronizedModeGroupPrototype")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize synchronized_triggers (list to container "SYNCHRONIZED-TRIGGERS")
        if self.synchronized_triggers:
            wrapper = ET.Element("SYNCHRONIZED-TRIGGERS")
            for item in self.synchronized_triggers:
                serialized = SerializationHelper.serialize_item(item, "SwcBswSynchronizedTrigger")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwcBswMapping":
        """Deserialize XML element to SwcBswMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwcBswMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwcBswMapping, cls).deserialize(element)

        # Parse bsw_behavior_ref
        child = SerializationHelper.find_child_element(element, "BSW-BEHAVIOR-REF")
        if child is not None:
            bsw_behavior_ref_value = ARRef.deserialize(child)
            obj.bsw_behavior_ref = bsw_behavior_ref_value

        # Parse runnable_mappings (list from container "RUNNABLE-MAPPINGS")
        obj.runnable_mappings = []
        container = SerializationHelper.find_child_element(element, "RUNNABLE-MAPPINGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.runnable_mappings.append(child_value)

        # Parse swc_behavior_ref
        child = SerializationHelper.find_child_element(element, "SWC-BEHAVIOR-REF")
        if child is not None:
            swc_behavior_ref_value = ARRef.deserialize(child)
            obj.swc_behavior_ref = swc_behavior_ref_value

        # Parse synchronized_mode_groups (list from container "SYNCHRONIZED-MODE-GROUPS")
        obj.synchronized_mode_groups = []
        container = SerializationHelper.find_child_element(element, "SYNCHRONIZED-MODE-GROUPS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.synchronized_mode_groups.append(child_value)

        # Parse synchronized_triggers (list from container "SYNCHRONIZED-TRIGGERS")
        obj.synchronized_triggers = []
        container = SerializationHelper.find_child_element(element, "SYNCHRONIZED-TRIGGERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.synchronized_triggers.append(child_value)

        return obj



class SwcBswMappingBuilder(ARElementBuilder):
    """Builder for SwcBswMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SwcBswMapping = SwcBswMapping()


    def with_bsw_behavior(self, value: Optional[BswInternalBehavior]) -> "SwcBswMappingBuilder":
        """Set bsw_behavior attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.bsw_behavior = value
        return self

    def with_runnable_mappings(self, items: list[SwcBswRunnableMapping]) -> "SwcBswMappingBuilder":
        """Set runnable_mappings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.runnable_mappings = list(items) if items else []
        return self

    def with_swc_behavior(self, value: Optional[SwcInternalBehavior]) -> "SwcBswMappingBuilder":
        """Set swc_behavior attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.swc_behavior = value
        return self

    def with_synchronized_mode_groups(self, items: list[SwcBswSynchronizedModeGroupPrototype]) -> "SwcBswMappingBuilder":
        """Set synchronized_mode_groups list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.synchronized_mode_groups = list(items) if items else []
        return self

    def with_synchronized_triggers(self, items: list[SwcBswSynchronizedTrigger]) -> "SwcBswMappingBuilder":
        """Set synchronized_triggers list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.synchronized_triggers = list(items) if items else []
        return self


    def add_runnable_mapping(self, item: SwcBswRunnableMapping) -> "SwcBswMappingBuilder":
        """Add a single item to runnable_mappings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.runnable_mappings.append(item)
        return self

    def clear_runnable_mappings(self) -> "SwcBswMappingBuilder":
        """Clear all items from runnable_mappings list.

        Returns:
            self for method chaining
        """
        self._obj.runnable_mappings = []
        return self

    def add_synchronized_mode_group(self, item: SwcBswSynchronizedModeGroupPrototype) -> "SwcBswMappingBuilder":
        """Add a single item to synchronized_mode_groups list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.synchronized_mode_groups.append(item)
        return self

    def clear_synchronized_mode_groups(self) -> "SwcBswMappingBuilder":
        """Clear all items from synchronized_mode_groups list.

        Returns:
            self for method chaining
        """
        self._obj.synchronized_mode_groups = []
        return self

    def add_synchronized_trigger(self, item: SwcBswSynchronizedTrigger) -> "SwcBswMappingBuilder":
        """Add a single item to synchronized_triggers list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.synchronized_triggers.append(item)
        return self

    def clear_synchronized_triggers(self) -> "SwcBswMappingBuilder":
        """Clear all items from synchronized_triggers list.

        Returns:
            self for method chaining
        """
        self._obj.synchronized_triggers = []
        return self



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


    def build(self) -> SwcBswMapping:
        """Build and return the SwcBswMapping instance with validation."""
        self._validate_instance()
        pass
        return self._obj