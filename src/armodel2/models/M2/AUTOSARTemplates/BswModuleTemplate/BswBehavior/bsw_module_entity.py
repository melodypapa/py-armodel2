"""BswModuleEntity AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 70)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 215)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 429)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel2.serialization.decorators import ref_conditional

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.executable_entity import (
    ExecutableEntity,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.executable_entity import ExecutableEntityBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_internal_triggering_point import (
    BswInternalTriggeringPoint,
)
from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_module_call_point import (
    BswModuleCallPoint,
)
from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_module_entry import (
    BswModuleEntry,
)
from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_scheduler_name_prefix import (
    BswSchedulerNamePrefix,
)
from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_variable_access import (
    BswVariableAccess,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group_prototype import (
    ModeDeclarationGroupPrototype,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger import (
    Trigger,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class BswModuleEntity(ExecutableEntity, ABC):
    """AUTOSAR BswModuleEntity."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    _accessed_mode_group_refs: list[ARRef]
    activation_point_refs: list[ARRef]
    call_points: list[BswModuleCallPoint]
    data_receive_points: list[BswVariableAccess]
    data_send_points: list[BswVariableAccess]
    implemented_entry_ref: Optional[ARRef]
    issued_trigger_refs: list[ARRef]
    _managed_mode_group_refs: list[ARRef]
    scheduler_name_prefix_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "ACCESSED-MODE-GROUP-REFS": lambda obj, elem: [obj._accessed_mode_group_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
        "ACTIVATION-POINT-REFS": lambda obj, elem: [obj.activation_point_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
        "CALL-POINTS": ("_POLYMORPHIC_LIST", "call_points", ["Bsw", "BswAsynchronousServerCallPoint", "BswAsynchronousServerCallResultPoint", "BswDirectCallPoint"]),
        "DATA-RECEIVE-POINTS": lambda obj, elem: obj.data_receive_points.append(SerializationHelper.deserialize_by_tag(elem, "BswVariableAccess")),
        "DATA-SEND-POINTS": lambda obj, elem: obj.data_send_points.append(SerializationHelper.deserialize_by_tag(elem, "BswVariableAccess")),
        "IMPLEMENTED-ENTRY-REF": lambda obj, elem: setattr(obj, "implemented_entry_ref", ARRef.deserialize(elem)),
        "ISSUED-TRIGGER-REFS": lambda obj, elem: [obj.issued_trigger_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
        "MANAGED-MODE-GROUP-REFS": lambda obj, elem: [obj._managed_mode_group_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
        "SCHEDULER-NAME-PREFIX-REF": lambda obj, elem: setattr(obj, "scheduler_name_prefix_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize BswModuleEntity."""
        super().__init__()
        self._accessed_mode_group_refs: list[ARRef] = []
        self.activation_point_refs: list[ARRef] = []
        self.call_points: list[BswModuleCallPoint] = []
        self.data_receive_points: list[BswVariableAccess] = []
        self.data_send_points: list[BswVariableAccess] = []
        self.implemented_entry_ref: Optional[ARRef] = None
        self.issued_trigger_refs: list[ARRef] = []
        self._managed_mode_group_refs: list[ARRef] = []
        self.scheduler_name_prefix_ref: Optional[ARRef] = None
    @property
    @ref_conditional("ACCESSED-MODE-GROUPS")
    def accessed_mode_group_refs(self) -> list[ARRef]:
        """Get accessed_mode_group_refs with ref_conditional wrapper."""
        return self._accessed_mode_group_refs

    @accessed_mode_group_refs.setter
    def accessed_mode_group_refs(self, value: list[ARRef]) -> None:
        """Set accessed_mode_group_refs with ref_conditional wrapper."""
        self._accessed_mode_group_refs = value

    @property
    @ref_conditional("MANAGED-MODE-GROUPS")
    def managed_mode_group_refs(self) -> list[ARRef]:
        """Get managed_mode_group_refs with ref_conditional wrapper."""
        return self._managed_mode_group_refs

    @managed_mode_group_refs.setter
    def managed_mode_group_refs(self, value: list[ARRef]) -> None:
        """Set managed_mode_group_refs with ref_conditional wrapper."""
        self._managed_mode_group_refs = value


    def serialize(self) -> ET.Element:
        """Serialize BswModuleEntity to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

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

        # Serialize accessed_mode_group_refs (list to container "ACCESSED-MODE-GROUPS")
        if self.accessed_mode_group_refs:
            wrapper = ET.Element("ACCESSED-MODE-GROUPS")
            for item in self.accessed_mode_group_refs:
                serialized = SerializationHelper.serialize_item(item, "ModeDeclarationGroupPrototype")
                if serialized is not None:
                    # Wrap in MODE-DECLARATION-GROUP-PROTOTYPE-REF-CONDITIONAL
                    conditional = ET.Element("MODE-DECLARATION-GROUP-PROTOTYPE-REF-CONDITIONAL")
                    ref_elem = ET.Element("MODE-DECLARATION-GROUP-PROTOTYPE-REF")
                    if hasattr(serialized, 'attrib'):
                        ref_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        ref_elem.text = serialized.text
                    for child in serialized:
                        ref_elem.append(child)
                    conditional.append(ref_elem)
                    wrapper.append(conditional)
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

        # Serialize managed_mode_group_refs (list to container "MANAGED-MODE-GROUPS")
        if self.managed_mode_group_refs:
            wrapper = ET.Element("MANAGED-MODE-GROUPS")
            for item in self.managed_mode_group_refs:
                serialized = SerializationHelper.serialize_item(item, "ModeDeclarationGroupPrototype")
                if serialized is not None:
                    # Wrap in MODE-DECLARATION-GROUP-PROTOTYPE-REF-CONDITIONAL
                    conditional = ET.Element("MODE-DECLARATION-GROUP-PROTOTYPE-REF-CONDITIONAL")
                    ref_elem = ET.Element("MODE-DECLARATION-GROUP-PROTOTYPE-REF")
                    if hasattr(serialized, 'attrib'):
                        ref_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        ref_elem.text = serialized.text
                    for child in serialized:
                        ref_elem.append(child)
                    conditional.append(ref_elem)
                    wrapper.append(conditional)
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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ACCESSED-MODE-GROUPS":
                # Unwrap ref_conditional pattern
                for item_elem in child:
                    # item_elem is XXX-REF-CONDITIONAL, unwrap to get XXX-REF
                    if len(item_elem) > 0:
                        ref_elem = item_elem[0]
                        obj._accessed_mode_group_refs.append(ARRef.deserialize(ref_elem))
            elif tag == "ACTIVATION-POINT-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.activation_point_refs.append(ARRef.deserialize(item_elem))
            elif tag == "CALL-POINTS":
                # Iterate through all child elements and deserialize each based on its concrete type
                for item_elem in child:
                    concrete_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    if concrete_tag == "BSW":
                        obj.call_points.append(SerializationHelper.deserialize_by_tag(item_elem, "Bsw"))
                    elif concrete_tag == "BSW-ASYNCHRONOUS-SERVER-CALL-POINT":
                        obj.call_points.append(SerializationHelper.deserialize_by_tag(item_elem, "BswAsynchronousServerCallPoint"))
                    elif concrete_tag == "BSW-ASYNCHRONOUS-SERVER-CALL-RESULT-POINT":
                        obj.call_points.append(SerializationHelper.deserialize_by_tag(item_elem, "BswAsynchronousServerCallResultPoint"))
                    elif concrete_tag == "BSW-DIRECT-CALL-POINT":
                        obj.call_points.append(SerializationHelper.deserialize_by_tag(item_elem, "BswDirectCallPoint"))
            elif tag == "DATA-RECEIVE-POINTS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.data_receive_points.append(SerializationHelper.deserialize_by_tag(item_elem, "BswVariableAccess"))
            elif tag == "DATA-SEND-POINTS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.data_send_points.append(SerializationHelper.deserialize_by_tag(item_elem, "BswVariableAccess"))
            elif tag == "IMPLEMENTED-ENTRY-REF":
                setattr(obj, "implemented_entry_ref", ARRef.deserialize(child))
            elif tag == "ISSUED-TRIGGER-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.issued_trigger_refs.append(ARRef.deserialize(item_elem))
            elif tag == "MANAGED-MODE-GROUPS":
                # Unwrap ref_conditional pattern
                for item_elem in child:
                    # item_elem is XXX-REF-CONDITIONAL, unwrap to get XXX-REF
                    if len(item_elem) > 0:
                        ref_elem = item_elem[0]
                        obj._managed_mode_group_refs.append(ARRef.deserialize(ref_elem))
            elif tag == "SCHEDULER-NAME-PREFIX-REF":
                setattr(obj, "scheduler_name_prefix_ref", ARRef.deserialize(child))

        return obj



class BswModuleEntityBuilder(ExecutableEntityBuilder):
    """Builder for BswModuleEntity with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: BswModuleEntity = BswModuleEntity()


    def with_accessed_mode_groups(self, items: list[ModeDeclarationGroupPrototype]) -> "BswModuleEntityBuilder":
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
            raise ValueError("Attribute 'implemented_entry' is required and cannot be None")
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
            raise ValueError("Attribute 'scheduler_name_prefix' is required and cannot be None")
        self._obj.scheduler_name_prefix = value
        return self


    def add_accessed_mode_group(self, item: ModeDeclarationGroupPrototype) -> "BswModuleEntityBuilder":
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


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "accessedModeGroup",
        "activationPoint",
        "callPoint",
        "dataReceivePoint",
        "dataSendPoint",
        "implementedEntry",
        "issuedTrigger",
        "managedModeGroup",
        "schedulerNamePrefix",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    @abstractmethod
    def build(self) -> BswModuleEntity:
        """Build and return the BswModuleEntity instance (abstract)."""
        raise NotImplementedError