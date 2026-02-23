"""BswModuleEntity AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 70)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 215)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 429)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.executable_entity import (
    ExecutableEntity,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from abc import ABC, abstractmethod
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.executable_entity import ExecutableEntityBuilder
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_internal_triggering_point import (
    BswInternalTriggeringPoint,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_module_call_point import (
    BswModuleCallPoint,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_module_entry import (
    BswModuleEntry,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_scheduler_name_prefix import (
    BswSchedulerNamePrefix,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_variable_access import (
    BswVariableAccess,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group_prototype import (
    ModeDeclarationGroupPrototype,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger import (
    Trigger,
)
from abc import ABC, abstractmethod
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class BswModuleEntity(ExecutableEntity, ABC):
    """AUTOSAR BswModuleEntity."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    accessed_mode_group_refs: list[ARRef]
    activation_point_refs: list[ARRef]
    call_points: list[BswModuleCallPoint]
    data_receive_points: list[BswVariableAccess]
    data_send_points: list[BswVariableAccess]
    implemented_entry_ref: Optional[ARRef]
    issued_trigger_refs: list[ARRef]
    managed_mode_group_refs: list[ARRef]
    scheduler_name_prefix_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize BswModuleEntity."""
        super().__init__()
        self.accessed_mode_group_refs: list[ARRef] = []
        self.activation_point_refs: list[ARRef] = []
        self.call_points: list[BswModuleCallPoint] = []
        self.data_receive_points: list[BswVariableAccess] = []
        self.data_send_points: list[BswVariableAccess] = []
        self.implemented_entry_ref: Optional[ARRef] = None
        self.issued_trigger_refs: list[ARRef] = []
        self.managed_mode_group_refs: list[ARRef] = []
        self.scheduler_name_prefix_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize BswModuleEntity to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BswModuleEntity, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize accessed_mode_group_refs (list to container "ACCESSED-MODE-GROUP-REFS")
        if self.accessed_mode_group_refs:
            wrapper = ET.Element("ACCESSED-MODE-GROUP-REFS")
            for item in self.accessed_mode_group_refs:
                serialized = SerializationHelper.serialize_item(item, "ModeDeclarationGroup")
                if serialized is not None:
                    child_elem = ET.Element("ACCESSED-MODE-GROUP-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize activation_point_refs (list to container "ACTIVATION-POINT-REFS")
        if self.activation_point_refs:
            wrapper = ET.Element("ACTIVATION-POINT-REFS")
            for item in self.activation_point_refs:
                serialized = SerializationHelper.serialize_item(item, "BswInternalTriggeringPoint")
                if serialized is not None:
                    child_elem = ET.Element("ACTIVATION-POINT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize call_points (list to container "CALL-POINTS")
        if self.call_points:
            wrapper = ET.Element("CALL-POINTS")
            for item in self.call_points:
                serialized = SerializationHelper.serialize_item(item, "BswModuleCallPoint")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize data_receive_points (list to container "DATA-RECEIVE-POINTS")
        if self.data_receive_points:
            wrapper = ET.Element("DATA-RECEIVE-POINTS")
            for item in self.data_receive_points:
                serialized = SerializationHelper.serialize_item(item, "BswVariableAccess")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize data_send_points (list to container "DATA-SEND-POINTS")
        if self.data_send_points:
            wrapper = ET.Element("DATA-SEND-POINTS")
            for item in self.data_send_points:
                serialized = SerializationHelper.serialize_item(item, "BswVariableAccess")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize implemented_entry_ref
        if self.implemented_entry_ref is not None:
            serialized = SerializationHelper.serialize_item(self.implemented_entry_ref, "BswModuleEntry")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IMPLEMENTED-ENTRY-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize issued_trigger_refs (list to container "ISSUED-TRIGGER-REFS")
        if self.issued_trigger_refs:
            wrapper = ET.Element("ISSUED-TRIGGER-REFS")
            for item in self.issued_trigger_refs:
                serialized = SerializationHelper.serialize_item(item, "Trigger")
                if serialized is not None:
                    child_elem = ET.Element("ISSUED-TRIGGER-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize managed_mode_group_refs (list to container "MANAGED-MODE-GROUP-REFS")
        if self.managed_mode_group_refs:
            wrapper = ET.Element("MANAGED-MODE-GROUP-REFS")
            for item in self.managed_mode_group_refs:
                serialized = SerializationHelper.serialize_item(item, "ModeDeclarationGroupPrototype")
                if serialized is not None:
                    child_elem = ET.Element("MANAGED-MODE-GROUP-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize scheduler_name_prefix_ref
        if self.scheduler_name_prefix_ref is not None:
            serialized = SerializationHelper.serialize_item(self.scheduler_name_prefix_ref, "BswSchedulerNamePrefix")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SCHEDULER-NAME-PREFIX-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswModuleEntity":
        """Deserialize XML element to BswModuleEntity object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswModuleEntity object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BswModuleEntity, cls).deserialize(element)

        # Parse accessed_mode_group_refs (list from container "ACCESSED-MODE-GROUP-REFS")
        obj.accessed_mode_group_refs = []
        container = SerializationHelper.find_child_element(element, "ACCESSED-MODE-GROUP-REFS")
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
                    obj.accessed_mode_group_refs.append(child_value)

        # Parse activation_point_refs (list from container "ACTIVATION-POINT-REFS")
        obj.activation_point_refs = []
        container = SerializationHelper.find_child_element(element, "ACTIVATION-POINT-REFS")
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
                    obj.activation_point_refs.append(child_value)

        # Parse call_points (list from container "CALL-POINTS")
        obj.call_points = []
        container = SerializationHelper.find_child_element(element, "CALL-POINTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.call_points.append(child_value)

        # Parse data_receive_points (list from container "DATA-RECEIVE-POINTS")
        obj.data_receive_points = []
        container = SerializationHelper.find_child_element(element, "DATA-RECEIVE-POINTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.data_receive_points.append(child_value)

        # Parse data_send_points (list from container "DATA-SEND-POINTS")
        obj.data_send_points = []
        container = SerializationHelper.find_child_element(element, "DATA-SEND-POINTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.data_send_points.append(child_value)

        # Parse implemented_entry_ref
        child = SerializationHelper.find_child_element(element, "IMPLEMENTED-ENTRY-REF")
        if child is not None:
            implemented_entry_ref_value = ARRef.deserialize(child)
            obj.implemented_entry_ref = implemented_entry_ref_value

        # Parse issued_trigger_refs (list from container "ISSUED-TRIGGER-REFS")
        obj.issued_trigger_refs = []
        container = SerializationHelper.find_child_element(element, "ISSUED-TRIGGER-REFS")
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
                    obj.issued_trigger_refs.append(child_value)

        # Parse managed_mode_group_refs (list from container "MANAGED-MODE-GROUP-REFS")
        obj.managed_mode_group_refs = []
        container = SerializationHelper.find_child_element(element, "MANAGED-MODE-GROUP-REFS")
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
                    obj.managed_mode_group_refs.append(child_value)

        # Parse scheduler_name_prefix_ref
        child = SerializationHelper.find_child_element(element, "SCHEDULER-NAME-PREFIX-REF")
        if child is not None:
            scheduler_name_prefix_ref_value = ARRef.deserialize(child)
            obj.scheduler_name_prefix_ref = scheduler_name_prefix_ref_value

        return obj



class BswModuleEntityBuilder(ExecutableEntityBuilder):
    """Builder for BswModuleEntity with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: BswModuleEntity = BswModuleEntity()


    def with_accessed_mode_groups(self, items: list[ModeDeclarationGroup]) -> "BswModuleEntityBuilder":
        """Set accessed_mode_groups list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.accessed_mode_groups = list(items) if items else []
        return self

    def with_activation_points(self, items: list[BswInternalTriggeringPoint]) -> "BswModuleEntityBuilder":
        """Set activation_points list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.activation_points = list(items) if items else []
        return self

    def with_call_points(self, items: list[BswModuleCallPoint]) -> "BswModuleEntityBuilder":
        """Set call_points list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.call_points = list(items) if items else []
        return self

    def with_data_receive_points(self, items: list[BswVariableAccess]) -> "BswModuleEntityBuilder":
        """Set data_receive_points list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.data_receive_points = list(items) if items else []
        return self

    def with_data_send_points(self, items: list[BswVariableAccess]) -> "BswModuleEntityBuilder":
        """Set data_send_points list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.data_send_points = list(items) if items else []
        return self

    def with_implemented_entry(self, value: Optional[BswModuleEntry]) -> "BswModuleEntityBuilder":
        """Set implemented_entry attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.implemented_entry = value
        return self

    def with_issued_triggers(self, items: list[Trigger]) -> "BswModuleEntityBuilder":
        """Set issued_triggers list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.issued_triggers = list(items) if items else []
        return self

    def with_managed_mode_groups(self, items: list[ModeDeclarationGroupPrototype]) -> "BswModuleEntityBuilder":
        """Set managed_mode_groups list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.managed_mode_groups = list(items) if items else []
        return self

    def with_scheduler_name_prefix(self, value: Optional[BswSchedulerNamePrefix]) -> "BswModuleEntityBuilder":
        """Set scheduler_name_prefix attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.scheduler_name_prefix = value
        return self


    def add_accessed_mode_group(self, item: ModeDeclarationGroup) -> "BswModuleEntityBuilder":
        """Add a single item to accessed_mode_groups list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.accessed_mode_groups.append(item)
        return self

    def clear_accessed_mode_groups(self) -> "BswModuleEntityBuilder":
        """Clear all items from accessed_mode_groups list.

        Returns:
            self for method chaining
        """
        self._obj.accessed_mode_groups = []
        return self

    def add_activation_point(self, item: BswInternalTriggeringPoint) -> "BswModuleEntityBuilder":
        """Add a single item to activation_points list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.activation_points.append(item)
        return self

    def clear_activation_points(self) -> "BswModuleEntityBuilder":
        """Clear all items from activation_points list.

        Returns:
            self for method chaining
        """
        self._obj.activation_points = []
        return self

    def add_call_point(self, item: BswModuleCallPoint) -> "BswModuleEntityBuilder":
        """Add a single item to call_points list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.call_points.append(item)
        return self

    def clear_call_points(self) -> "BswModuleEntityBuilder":
        """Clear all items from call_points list.

        Returns:
            self for method chaining
        """
        self._obj.call_points = []
        return self

    def add_data_receive_point(self, item: BswVariableAccess) -> "BswModuleEntityBuilder":
        """Add a single item to data_receive_points list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.data_receive_points.append(item)
        return self

    def clear_data_receive_points(self) -> "BswModuleEntityBuilder":
        """Clear all items from data_receive_points list.

        Returns:
            self for method chaining
        """
        self._obj.data_receive_points = []
        return self

    def add_data_send_point(self, item: BswVariableAccess) -> "BswModuleEntityBuilder":
        """Add a single item to data_send_points list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.data_send_points.append(item)
        return self

    def clear_data_send_points(self) -> "BswModuleEntityBuilder":
        """Clear all items from data_send_points list.

        Returns:
            self for method chaining
        """
        self._obj.data_send_points = []
        return self

    def add_issued_trigger(self, item: Trigger) -> "BswModuleEntityBuilder":
        """Add a single item to issued_triggers list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.issued_triggers.append(item)
        return self

    def clear_issued_triggers(self) -> "BswModuleEntityBuilder":
        """Clear all items from issued_triggers list.

        Returns:
            self for method chaining
        """
        self._obj.issued_triggers = []
        return self

    def add_managed_mode_group(self, item: ModeDeclarationGroupPrototype) -> "BswModuleEntityBuilder":
        """Add a single item to managed_mode_groups list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.managed_mode_groups.append(item)
        return self

    def clear_managed_mode_groups(self) -> "BswModuleEntityBuilder":
        """Clear all items from managed_mode_groups list.

        Returns:
            self for method chaining
        """
        self._obj.managed_mode_groups = []
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


    @abstractmethod
    def build(self) -> BswModuleEntity:
        """Build and return the BswModuleEntity instance (abstract)."""
        raise NotImplementedError