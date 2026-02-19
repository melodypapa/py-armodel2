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
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger import (
    Trigger,
)
from abc import ABC, abstractmethod


class BswModuleEntity(ExecutableEntity, ABC):
    """AUTOSAR BswModuleEntity."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    accessed_mode_refs: list[ARRef]
    activation_point_refs: list[ARRef]
    call_points: list[BswModuleCallPoint]
    data_receives: list[BswVariableAccess]
    data_send_points: list[BswVariableAccess]
    implemented: Optional[BswModuleEntry]
    issued_trigger_refs: list[ARRef]
    managed_mode_refs: list[ARRef]
    scheduler_name: Optional[BswSchedulerNamePrefix]
    def __init__(self) -> None:
        """Initialize BswModuleEntity."""
        super().__init__()
        self.accessed_mode_refs: list[ARRef] = []
        self.activation_point_refs: list[ARRef] = []
        self.call_points: list[BswModuleCallPoint] = []
        self.data_receives: list[BswVariableAccess] = []
        self.data_send_points: list[BswVariableAccess] = []
        self.implemented: Optional[BswModuleEntry] = None
        self.issued_trigger_refs: list[ARRef] = []
        self.managed_mode_refs: list[ARRef] = []
        self.scheduler_name: Optional[BswSchedulerNamePrefix] = None

    def serialize(self) -> ET.Element:
        """Serialize BswModuleEntity to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BswModuleEntity, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize accessed_mode_refs (list to container "ACCESSED-MODES")
        if self.accessed_mode_refs:
            wrapper = ET.Element("ACCESSED-MODES")
            for item in self.accessed_mode_refs:
                serialized = ARObject._serialize_item(item, "ModeDeclarationGroup")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize activation_point_refs (list to container "ACTIVATION-POINTS")
        if self.activation_point_refs:
            wrapper = ET.Element("ACTIVATION-POINTS")
            for item in self.activation_point_refs:
                serialized = ARObject._serialize_item(item, "BswInternalTriggeringPoint")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize call_points (list to container "CALL-POINTS")
        if self.call_points:
            wrapper = ET.Element("CALL-POINTS")
            for item in self.call_points:
                serialized = ARObject._serialize_item(item, "BswModuleCallPoint")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize data_receives (list to container "DATA-RECEIVES")
        if self.data_receives:
            wrapper = ET.Element("DATA-RECEIVES")
            for item in self.data_receives:
                serialized = ARObject._serialize_item(item, "BswVariableAccess")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize data_send_points (list to container "DATA-SEND-POINTS")
        if self.data_send_points:
            wrapper = ET.Element("DATA-SEND-POINTS")
            for item in self.data_send_points:
                serialized = ARObject._serialize_item(item, "BswVariableAccess")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize implemented
        if self.implemented is not None:
            serialized = ARObject._serialize_item(self.implemented, "BswModuleEntry")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IMPLEMENTED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize issued_trigger_refs (list to container "ISSUED-TRIGGERS")
        if self.issued_trigger_refs:
            wrapper = ET.Element("ISSUED-TRIGGERS")
            for item in self.issued_trigger_refs:
                serialized = ARObject._serialize_item(item, "Trigger")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize managed_mode_refs (list to container "MANAGED-MODES")
        if self.managed_mode_refs:
            wrapper = ET.Element("MANAGED-MODES")
            for item in self.managed_mode_refs:
                serialized = ARObject._serialize_item(item, "ModeDeclarationGroup")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize scheduler_name
        if self.scheduler_name is not None:
            serialized = ARObject._serialize_item(self.scheduler_name, "BswSchedulerNamePrefix")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SCHEDULER-NAME")
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

        # Parse accessed_mode_refs (list from container "ACCESSED-MODES")
        obj.accessed_mode_refs = []
        container = ARObject._find_child_element(element, "ACCESSED-MODES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.accessed_mode_refs.append(child_value)

        # Parse activation_point_refs (list from container "ACTIVATION-POINTS")
        obj.activation_point_refs = []
        container = ARObject._find_child_element(element, "ACTIVATION-POINTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.activation_point_refs.append(child_value)

        # Parse call_points (list from container "CALL-POINTS")
        obj.call_points = []
        container = ARObject._find_child_element(element, "CALL-POINTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.call_points.append(child_value)

        # Parse data_receives (list from container "DATA-RECEIVES")
        obj.data_receives = []
        container = ARObject._find_child_element(element, "DATA-RECEIVES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.data_receives.append(child_value)

        # Parse data_send_points (list from container "DATA-SEND-POINTS")
        obj.data_send_points = []
        container = ARObject._find_child_element(element, "DATA-SEND-POINTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.data_send_points.append(child_value)

        # Parse implemented
        child = ARObject._find_child_element(element, "IMPLEMENTED")
        if child is not None:
            implemented_value = ARObject._deserialize_by_tag(child, "BswModuleEntry")
            obj.implemented = implemented_value

        # Parse issued_trigger_refs (list from container "ISSUED-TRIGGERS")
        obj.issued_trigger_refs = []
        container = ARObject._find_child_element(element, "ISSUED-TRIGGERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.issued_trigger_refs.append(child_value)

        # Parse managed_mode_refs (list from container "MANAGED-MODES")
        obj.managed_mode_refs = []
        container = ARObject._find_child_element(element, "MANAGED-MODES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.managed_mode_refs.append(child_value)

        # Parse scheduler_name
        child = ARObject._find_child_element(element, "SCHEDULER-NAME")
        if child is not None:
            scheduler_name_value = ARObject._deserialize_by_tag(child, "BswSchedulerNamePrefix")
            obj.scheduler_name = scheduler_name_value

        return obj



class BswModuleEntityBuilder:
    """Builder for BswModuleEntity."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswModuleEntity = BswModuleEntity()

    def build(self) -> BswModuleEntity:
        """Build and return BswModuleEntity object.

        Returns:
            BswModuleEntity instance
        """
        # TODO: Add validation
        return self._obj
