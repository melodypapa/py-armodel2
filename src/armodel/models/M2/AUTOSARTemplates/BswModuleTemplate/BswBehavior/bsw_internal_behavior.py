"""BswInternalBehavior AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 65)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 649)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2003)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 208)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 165)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.internal_behavior import (
    InternalBehavior,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_data_reception_policy import (
    BswDataReceptionPolicy,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_distinguished_partition import (
    BswDistinguishedPartition,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_event import (
    BswEvent,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_exclusive_area_policy import (
    BswExclusiveAreaPolicy,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_internal_triggering_point import (
    BswInternalTriggeringPoint,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_mode_receiver_policy import (
    BswModeReceiverPolicy,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_mode_sender_policy import (
    BswModeSenderPolicy,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_module_entity import (
    BswModuleEntity,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_scheduler_name_prefix import (
    BswSchedulerNamePrefix,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_trigger_direct_implementation import (
    BswTriggerDirectImplementation,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.IncludedDataTypes.included_data_type_set import (
    IncludedDataTypeSet,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ModeDeclarationGroup.included_mode_declaration_group_set import (
    IncludedModeDeclarationGroupSet,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.parameter_data_prototype import (
    ParameterDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.VariantHandling.variation_point_proxy import (
    VariationPointProxy,
)


class BswInternalBehavior(InternalBehavior):
    """AUTOSAR BswInternalBehavior."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ar_typed_per_instance_memorie_refs: list[ARRef]
    bsw_per_instance_memory_policies: list[BswPerInstanceMemoryPolicy]
    client_policies: list[BswClientPolicy]
    distinguisheds: list[BswDistinguishedPartition]
    entities: list[BswModuleEntity]
    events: list[BswEvent]
    exclusive_areas: list[BswExclusiveAreaPolicy]
    included_data_type_set_refs: list[ARRef]
    included_modes: list[IncludedModeDeclarationGroupSet]
    internal_refs: list[ARRef]
    mode_receivers: list[BswModeReceiverPolicy]
    mode_senders: list[BswModeSenderPolicy]
    parameter_policies: list[Any]
    per_instances: list[ParameterDataPrototype]
    reception_policies: list[BswDataReceptionPolicy]
    released_trigger_refs: list[Any]
    scheduler_names: list[BswSchedulerNamePrefix]
    send_policies: list[Any]
    services: list[Any]
    trigger_direct_refs: list[ARRef]
    variation_point_proxies: list[VariationPointProxy]
    def __init__(self) -> None:
        """Initialize BswInternalBehavior."""
        super().__init__()
        self.ar_typed_per_instance_memorie_refs: list[ARRef] = []
        self.bsw_per_instance_memory_policies: list[BswPerInstanceMemoryPolicy] = []
        self.client_policies: list[BswClientPolicy] = []
        self.distinguisheds: list[BswDistinguishedPartition] = []
        self.entities: list[BswModuleEntity] = []
        self.events: list[BswEvent] = []
        self.exclusive_areas: list[BswExclusiveAreaPolicy] = []
        self.included_data_type_set_refs: list[ARRef] = []
        self.included_modes: list[IncludedModeDeclarationGroupSet] = []
        self.internal_refs: list[ARRef] = []
        self.mode_receivers: list[BswModeReceiverPolicy] = []
        self.mode_senders: list[BswModeSenderPolicy] = []
        self.parameter_policies: list[Any] = []
        self.per_instances: list[ParameterDataPrototype] = []
        self.reception_policies: list[BswDataReceptionPolicy] = []
        self.released_trigger_refs: list[Any] = []
        self.scheduler_names: list[BswSchedulerNamePrefix] = []
        self.send_policies: list[Any] = []
        self.services: list[Any] = []
        self.trigger_direct_refs: list[ARRef] = []
        self.variation_point_proxies: list[VariationPointProxy] = []

    def serialize(self) -> ET.Element:
        """Serialize BswInternalBehavior to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BswInternalBehavior, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize ar_typed_per_instance_memorie_refs (list to container "AR-TYPED-PER-INSTANCE-MEMORIE-REFS")
        if self.ar_typed_per_instance_memorie_refs:
            wrapper = ET.Element("AR-TYPED-PER-INSTANCE-MEMORIE-REFS")
            for item in self.ar_typed_per_instance_memorie_refs:
                serialized = SerializationHelper.serialize_item(item, "VariableDataPrototype")
                if serialized is not None:
                    child_elem = ET.Element("AR-TYPED-PER-INSTANCE-MEMORIE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize bsw_per_instance_memory_policies (list to container "BSW-PER-INSTANCE-MEMORY-POLICIES")
        if self.bsw_per_instance_memory_policies:
            wrapper = ET.Element("BSW-PER-INSTANCE-MEMORY-POLICIES")
            for item in self.bsw_per_instance_memory_policies:
                serialized = SerializationHelper.serialize_item(item, "BswPerInstanceMemoryPolicy")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize client_policies (list to container "CLIENT-POLICIES")
        if self.client_policies:
            wrapper = ET.Element("CLIENT-POLICIES")
            for item in self.client_policies:
                serialized = SerializationHelper.serialize_item(item, "BswClientPolicy")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize distinguisheds (list to container "DISTINGUISHEDS")
        if self.distinguisheds:
            wrapper = ET.Element("DISTINGUISHEDS")
            for item in self.distinguisheds:
                serialized = SerializationHelper.serialize_item(item, "BswDistinguishedPartition")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize entities (list to container "ENTITIES")
        if self.entities:
            wrapper = ET.Element("ENTITIES")
            for item in self.entities:
                serialized = SerializationHelper.serialize_item(item, "BswModuleEntity")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize events (list to container "EVENTS")
        if self.events:
            wrapper = ET.Element("EVENTS")
            for item in self.events:
                serialized = SerializationHelper.serialize_item(item, "BswEvent")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize exclusive_areas (list to container "EXCLUSIVE-AREAS")
        if self.exclusive_areas:
            wrapper = ET.Element("EXCLUSIVE-AREAS")
            for item in self.exclusive_areas:
                serialized = SerializationHelper.serialize_item(item, "BswExclusiveAreaPolicy")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize included_data_type_set_refs (list to container "INCLUDED-DATA-TYPE-SET-REFS")
        if self.included_data_type_set_refs:
            wrapper = ET.Element("INCLUDED-DATA-TYPE-SET-REFS")
            for item in self.included_data_type_set_refs:
                serialized = SerializationHelper.serialize_item(item, "IncludedDataTypeSet")
                if serialized is not None:
                    child_elem = ET.Element("INCLUDED-DATA-TYPE-SET-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize included_modes (list to container "INCLUDED-MODES")
        if self.included_modes:
            wrapper = ET.Element("INCLUDED-MODES")
            for item in self.included_modes:
                serialized = SerializationHelper.serialize_item(item, "IncludedModeDeclarationGroupSet")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize internal_refs (list to container "INTERNAL-REFS")
        if self.internal_refs:
            wrapper = ET.Element("INTERNAL-REFS")
            for item in self.internal_refs:
                serialized = SerializationHelper.serialize_item(item, "BswInternalTriggeringPoint")
                if serialized is not None:
                    child_elem = ET.Element("INTERNAL-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize mode_receivers (list to container "MODE-RECEIVERS")
        if self.mode_receivers:
            wrapper = ET.Element("MODE-RECEIVERS")
            for item in self.mode_receivers:
                serialized = SerializationHelper.serialize_item(item, "BswModeReceiverPolicy")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize mode_senders (list to container "MODE-SENDERS")
        if self.mode_senders:
            wrapper = ET.Element("MODE-SENDERS")
            for item in self.mode_senders:
                serialized = SerializationHelper.serialize_item(item, "BswModeSenderPolicy")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize parameter_policies (list to container "PARAMETER-POLICIES")
        if self.parameter_policies:
            wrapper = ET.Element("PARAMETER-POLICIES")
            for item in self.parameter_policies:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize per_instances (list to container "PER-INSTANCES")
        if self.per_instances:
            wrapper = ET.Element("PER-INSTANCES")
            for item in self.per_instances:
                serialized = SerializationHelper.serialize_item(item, "ParameterDataPrototype")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize reception_policies (list to container "RECEPTION-POLICIES")
        if self.reception_policies:
            wrapper = ET.Element("RECEPTION-POLICIES")
            for item in self.reception_policies:
                serialized = SerializationHelper.serialize_item(item, "BswDataReceptionPolicy")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize released_trigger_refs (list to container "RELEASED-TRIGGER-REFS")
        if self.released_trigger_refs:
            wrapper = ET.Element("RELEASED-TRIGGER-REFS")
            for item in self.released_trigger_refs:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    child_elem = ET.Element("RELEASED-TRIGGER-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize scheduler_names (list to container "SCHEDULER-NAMES")
        if self.scheduler_names:
            wrapper = ET.Element("SCHEDULER-NAMES")
            for item in self.scheduler_names:
                serialized = SerializationHelper.serialize_item(item, "BswSchedulerNamePrefix")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize send_policies (list to container "SEND-POLICIES")
        if self.send_policies:
            wrapper = ET.Element("SEND-POLICIES")
            for item in self.send_policies:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize services (list to container "SERVICES")
        if self.services:
            wrapper = ET.Element("SERVICES")
            for item in self.services:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize trigger_direct_refs (list to container "TRIGGER-DIRECT-REFS")
        if self.trigger_direct_refs:
            wrapper = ET.Element("TRIGGER-DIRECT-REFS")
            for item in self.trigger_direct_refs:
                serialized = SerializationHelper.serialize_item(item, "BswTriggerDirectImplementation")
                if serialized is not None:
                    child_elem = ET.Element("TRIGGER-DIRECT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize variation_point_proxies (list to container "VARIATION-POINT-PROXIES")
        if self.variation_point_proxies:
            wrapper = ET.Element("VARIATION-POINT-PROXIES")
            for item in self.variation_point_proxies:
                serialized = SerializationHelper.serialize_item(item, "VariationPointProxy")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswInternalBehavior":
        """Deserialize XML element to BswInternalBehavior object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswInternalBehavior object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BswInternalBehavior, cls).deserialize(element)

        # Parse ar_typed_per_instance_memorie_refs (list from container "AR-TYPED-PER-INSTANCE-MEMORIE-REFS")
        obj.ar_typed_per_instance_memorie_refs = []
        container = SerializationHelper.find_child_element(element, "AR-TYPED-PER-INSTANCE-MEMORIE-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.ar_typed_per_instance_memorie_refs.append(child_value)

        # Parse bsw_per_instance_memory_policies (list from container "BSW-PER-INSTANCE-MEMORY-POLICIES")
        obj.bsw_per_instance_memory_policies = []
        container = SerializationHelper.find_child_element(element, "BSW-PER-INSTANCE-MEMORY-POLICIES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.bsw_per_instance_memory_policies.append(child_value)

        # Parse client_policies (list from container "CLIENT-POLICIES")
        obj.client_policies = []
        container = SerializationHelper.find_child_element(element, "CLIENT-POLICIES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.client_policies.append(child_value)

        # Parse distinguisheds (list from container "DISTINGUISHEDS")
        obj.distinguisheds = []
        container = SerializationHelper.find_child_element(element, "DISTINGUISHEDS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.distinguisheds.append(child_value)

        # Parse entities (list from container "ENTITIES")
        obj.entities = []
        container = SerializationHelper.find_child_element(element, "ENTITIES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.entities.append(child_value)

        # Parse events (list from container "EVENTS")
        obj.events = []
        container = SerializationHelper.find_child_element(element, "EVENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.events.append(child_value)

        # Parse exclusive_areas (list from container "EXCLUSIVE-AREAS")
        obj.exclusive_areas = []
        container = SerializationHelper.find_child_element(element, "EXCLUSIVE-AREAS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.exclusive_areas.append(child_value)

        # Parse included_data_type_set_refs (list from container "INCLUDED-DATA-TYPE-SET-REFS")
        obj.included_data_type_set_refs = []
        container = SerializationHelper.find_child_element(element, "INCLUDED-DATA-TYPE-SET-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.included_data_type_set_refs.append(child_value)

        # Parse included_modes (list from container "INCLUDED-MODES")
        obj.included_modes = []
        container = SerializationHelper.find_child_element(element, "INCLUDED-MODES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.included_modes.append(child_value)

        # Parse internal_refs (list from container "INTERNAL-REFS")
        obj.internal_refs = []
        container = SerializationHelper.find_child_element(element, "INTERNAL-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.internal_refs.append(child_value)

        # Parse mode_receivers (list from container "MODE-RECEIVERS")
        obj.mode_receivers = []
        container = SerializationHelper.find_child_element(element, "MODE-RECEIVERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.mode_receivers.append(child_value)

        # Parse mode_senders (list from container "MODE-SENDERS")
        obj.mode_senders = []
        container = SerializationHelper.find_child_element(element, "MODE-SENDERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.mode_senders.append(child_value)

        # Parse parameter_policies (list from container "PARAMETER-POLICIES")
        obj.parameter_policies = []
        container = SerializationHelper.find_child_element(element, "PARAMETER-POLICIES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.parameter_policies.append(child_value)

        # Parse per_instances (list from container "PER-INSTANCES")
        obj.per_instances = []
        container = SerializationHelper.find_child_element(element, "PER-INSTANCES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.per_instances.append(child_value)

        # Parse reception_policies (list from container "RECEPTION-POLICIES")
        obj.reception_policies = []
        container = SerializationHelper.find_child_element(element, "RECEPTION-POLICIES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.reception_policies.append(child_value)

        # Parse released_trigger_refs (list from container "RELEASED-TRIGGER-REFS")
        obj.released_trigger_refs = []
        container = SerializationHelper.find_child_element(element, "RELEASED-TRIGGER-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.released_trigger_refs.append(child_value)

        # Parse scheduler_names (list from container "SCHEDULER-NAMES")
        obj.scheduler_names = []
        container = SerializationHelper.find_child_element(element, "SCHEDULER-NAMES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.scheduler_names.append(child_value)

        # Parse send_policies (list from container "SEND-POLICIES")
        obj.send_policies = []
        container = SerializationHelper.find_child_element(element, "SEND-POLICIES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.send_policies.append(child_value)

        # Parse services (list from container "SERVICES")
        obj.services = []
        container = SerializationHelper.find_child_element(element, "SERVICES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.services.append(child_value)

        # Parse trigger_direct_refs (list from container "TRIGGER-DIRECT-REFS")
        obj.trigger_direct_refs = []
        container = SerializationHelper.find_child_element(element, "TRIGGER-DIRECT-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.trigger_direct_refs.append(child_value)

        # Parse variation_point_proxies (list from container "VARIATION-POINT-PROXIES")
        obj.variation_point_proxies = []
        container = SerializationHelper.find_child_element(element, "VARIATION-POINT-PROXIES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.variation_point_proxies.append(child_value)

        return obj



class BswInternalBehaviorBuilder:
    """Builder for BswInternalBehavior with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: BswInternalBehavior = BswInternalBehavior()


    def with_short_name(self, value: Identifier) -> "BswInternalBehaviorBuilder":
        """Set short_name attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.short_name = value
        return self

    def with_short_name_fragments(self, items: list[ShortNameFragment]) -> "BswInternalBehaviorBuilder":
        """Set short_name_fragments list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = list(items) if items else []
        return self

    def with_long_name(self, value: Optional[MultilanguageLongName]) -> "BswInternalBehaviorBuilder":
        """Set long_name attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.long_name = value
        return self

    def with_admin_data(self, value: Optional[AdminData]) -> "BswInternalBehaviorBuilder":
        """Set admin_data attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.admin_data = value
        return self

    def with_annotations(self, items: list[Annotation]) -> "BswInternalBehaviorBuilder":
        """Set annotations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.annotations = list(items) if items else []
        return self

    def with_desc(self, value: Optional[MultiLanguageOverviewParagraph]) -> "BswInternalBehaviorBuilder":
        """Set desc attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.desc = value
        return self

    def with_category(self, value: Optional[CategoryString]) -> "BswInternalBehaviorBuilder":
        """Set category attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.category = value
        return self

    def with_introduction(self, value: Optional[DocumentationBlock]) -> "BswInternalBehaviorBuilder":
        """Set introduction attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.introduction = value
        return self

    def with_uuid(self, value: Optional[String]) -> "BswInternalBehaviorBuilder":
        """Set uuid attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.uuid = value
        return self

    def with_constants(self, items: list[ParameterDataPrototype]) -> "BswInternalBehaviorBuilder":
        """Set constants list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.constants = list(items) if items else []
        return self

    def with_constant_values(self, items: list[ConstantSpecification]) -> "BswInternalBehaviorBuilder":
        """Set constant_values list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.constant_values = list(items) if items else []
        return self

    def with_data_types(self, items: list[DataTypeMappingSet]) -> "BswInternalBehaviorBuilder":
        """Set data_types list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.data_types = list(items) if items else []
        return self

    def with_exclusive_areas(self, items: list[ExclusiveArea]) -> "BswInternalBehaviorBuilder":
        """Set exclusive_areas list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.exclusive_areas = list(items) if items else []
        return self

    def with_exclusive_area_nestings(self, items: list[ExclusiveAreaNestingOrder]) -> "BswInternalBehaviorBuilder":
        """Set exclusive_area_nestings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.exclusive_area_nestings = list(items) if items else []
        return self

    def with_static_memories(self, items: list[VariableDataPrototype]) -> "BswInternalBehaviorBuilder":
        """Set static_memories list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.static_memories = list(items) if items else []
        return self

    def with_ar_typed_per_instance_memories(self, items: list[VariableDataPrototype]) -> "BswInternalBehaviorBuilder":
        """Set ar_typed_per_instance_memories list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.ar_typed_per_instance_memories = list(items) if items else []
        return self

    def with_bsw_per_instance_memory_policies(self, items: list[BswPerInstanceMemoryPolicy]) -> "BswInternalBehaviorBuilder":
        """Set bsw_per_instance_memory_policies list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.bsw_per_instance_memory_policies = list(items) if items else []
        return self

    def with_client_policies(self, items: list[BswClientPolicy]) -> "BswInternalBehaviorBuilder":
        """Set client_policies list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.client_policies = list(items) if items else []
        return self

    def with_distinguisheds(self, items: list[BswDistinguishedPartition]) -> "BswInternalBehaviorBuilder":
        """Set distinguisheds list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.distinguisheds = list(items) if items else []
        return self

    def with_entities(self, items: list[BswModuleEntity]) -> "BswInternalBehaviorBuilder":
        """Set entities list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.entities = list(items) if items else []
        return self

    def with_events(self, items: list[BswEvent]) -> "BswInternalBehaviorBuilder":
        """Set events list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.events = list(items) if items else []
        return self

    def with_included_data_type_sets(self, items: list[IncludedDataTypeSet]) -> "BswInternalBehaviorBuilder":
        """Set included_data_type_sets list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.included_data_type_sets = list(items) if items else []
        return self

    def with_included_modes(self, items: list[IncludedModeDeclarationGroupSet]) -> "BswInternalBehaviorBuilder":
        """Set included_modes list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.included_modes = list(items) if items else []
        return self

    def with_internals(self, items: list[BswInternalTriggeringPoint]) -> "BswInternalBehaviorBuilder":
        """Set internals list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.internals = list(items) if items else []
        return self

    def with_mode_receivers(self, items: list[BswModeReceiverPolicy]) -> "BswInternalBehaviorBuilder":
        """Set mode_receivers list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.mode_receivers = list(items) if items else []
        return self

    def with_mode_senders(self, items: list[BswModeSenderPolicy]) -> "BswInternalBehaviorBuilder":
        """Set mode_senders list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.mode_senders = list(items) if items else []
        return self

    def with_parameter_policies(self, items: list[any (BswParameterPolicy)]) -> "BswInternalBehaviorBuilder":
        """Set parameter_policies list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.parameter_policies = list(items) if items else []
        return self

    def with_per_instances(self, items: list[ParameterDataPrototype]) -> "BswInternalBehaviorBuilder":
        """Set per_instances list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.per_instances = list(items) if items else []
        return self

    def with_reception_policies(self, items: list[BswDataReceptionPolicy]) -> "BswInternalBehaviorBuilder":
        """Set reception_policies list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.reception_policies = list(items) if items else []
        return self

    def with_released_triggers(self, items: list[any (BswReleasedTrigger)]) -> "BswInternalBehaviorBuilder":
        """Set released_triggers list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.released_triggers = list(items) if items else []
        return self

    def with_scheduler_names(self, items: list[BswSchedulerNamePrefix]) -> "BswInternalBehaviorBuilder":
        """Set scheduler_names list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.scheduler_names = list(items) if items else []
        return self

    def with_send_policies(self, items: list[any (BswDataSendPolicy)]) -> "BswInternalBehaviorBuilder":
        """Set send_policies list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.send_policies = list(items) if items else []
        return self

    def with_services(self, items: list[any (BswService)]) -> "BswInternalBehaviorBuilder":
        """Set services list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.services = list(items) if items else []
        return self

    def with_trigger_directs(self, items: list[BswTriggerDirectImplementation]) -> "BswInternalBehaviorBuilder":
        """Set trigger_directs list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.trigger_directs = list(items) if items else []
        return self

    def with_variation_point_proxies(self, items: list[VariationPointProxy]) -> "BswInternalBehaviorBuilder":
        """Set variation_point_proxies list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.variation_point_proxies = list(items) if items else []
        return self


    def add_short_name_fragment(self, item: ShortNameFragment) -> "BswInternalBehaviorBuilder":
        """Add a single item to short_name_fragments list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments.append(item)
        return self

    def clear_short_name_fragments(self) -> "BswInternalBehaviorBuilder":
        """Clear all items from short_name_fragments list.

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = []
        return self

    def add_annotation(self, item: Annotation) -> "BswInternalBehaviorBuilder":
        """Add a single item to annotations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.annotations.append(item)
        return self

    def clear_annotations(self) -> "BswInternalBehaviorBuilder":
        """Clear all items from annotations list.

        Returns:
            self for method chaining
        """
        self._obj.annotations = []
        return self

    def add_constant(self, item: ParameterDataPrototype) -> "BswInternalBehaviorBuilder":
        """Add a single item to constants list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.constants.append(item)
        return self

    def clear_constants(self) -> "BswInternalBehaviorBuilder":
        """Clear all items from constants list.

        Returns:
            self for method chaining
        """
        self._obj.constants = []
        return self

    def add_constant_value(self, item: ConstantSpecification) -> "BswInternalBehaviorBuilder":
        """Add a single item to constant_values list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.constant_values.append(item)
        return self

    def clear_constant_values(self) -> "BswInternalBehaviorBuilder":
        """Clear all items from constant_values list.

        Returns:
            self for method chaining
        """
        self._obj.constant_values = []
        return self

    def add_data_type(self, item: DataTypeMappingSet) -> "BswInternalBehaviorBuilder":
        """Add a single item to data_types list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.data_types.append(item)
        return self

    def clear_data_types(self) -> "BswInternalBehaviorBuilder":
        """Clear all items from data_types list.

        Returns:
            self for method chaining
        """
        self._obj.data_types = []
        return self

    def add_exclusive_area(self, item: ExclusiveArea) -> "BswInternalBehaviorBuilder":
        """Add a single item to exclusive_areas list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.exclusive_areas.append(item)
        return self

    def clear_exclusive_areas(self) -> "BswInternalBehaviorBuilder":
        """Clear all items from exclusive_areas list.

        Returns:
            self for method chaining
        """
        self._obj.exclusive_areas = []
        return self

    def add_exclusive_area_nesting(self, item: ExclusiveAreaNestingOrder) -> "BswInternalBehaviorBuilder":
        """Add a single item to exclusive_area_nestings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.exclusive_area_nestings.append(item)
        return self

    def clear_exclusive_area_nestings(self) -> "BswInternalBehaviorBuilder":
        """Clear all items from exclusive_area_nestings list.

        Returns:
            self for method chaining
        """
        self._obj.exclusive_area_nestings = []
        return self

    def add_static_memorie(self, item: VariableDataPrototype) -> "BswInternalBehaviorBuilder":
        """Add a single item to static_memories list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.static_memories.append(item)
        return self

    def clear_static_memories(self) -> "BswInternalBehaviorBuilder":
        """Clear all items from static_memories list.

        Returns:
            self for method chaining
        """
        self._obj.static_memories = []
        return self

    def add_ar_typed_per_instance_memorie(self, item: VariableDataPrototype) -> "BswInternalBehaviorBuilder":
        """Add a single item to ar_typed_per_instance_memories list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.ar_typed_per_instance_memories.append(item)
        return self

    def clear_ar_typed_per_instance_memories(self) -> "BswInternalBehaviorBuilder":
        """Clear all items from ar_typed_per_instance_memories list.

        Returns:
            self for method chaining
        """
        self._obj.ar_typed_per_instance_memories = []
        return self

    def add_bsw_per_instance_memory_policie(self, item: BswPerInstanceMemoryPolicy) -> "BswInternalBehaviorBuilder":
        """Add a single item to bsw_per_instance_memory_policies list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.bsw_per_instance_memory_policies.append(item)
        return self

    def clear_bsw_per_instance_memory_policies(self) -> "BswInternalBehaviorBuilder":
        """Clear all items from bsw_per_instance_memory_policies list.

        Returns:
            self for method chaining
        """
        self._obj.bsw_per_instance_memory_policies = []
        return self

    def add_client_policie(self, item: BswClientPolicy) -> "BswInternalBehaviorBuilder":
        """Add a single item to client_policies list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.client_policies.append(item)
        return self

    def clear_client_policies(self) -> "BswInternalBehaviorBuilder":
        """Clear all items from client_policies list.

        Returns:
            self for method chaining
        """
        self._obj.client_policies = []
        return self

    def add_distinguished(self, item: BswDistinguishedPartition) -> "BswInternalBehaviorBuilder":
        """Add a single item to distinguisheds list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.distinguisheds.append(item)
        return self

    def clear_distinguisheds(self) -> "BswInternalBehaviorBuilder":
        """Clear all items from distinguisheds list.

        Returns:
            self for method chaining
        """
        self._obj.distinguisheds = []
        return self

    def add_entitie(self, item: BswModuleEntity) -> "BswInternalBehaviorBuilder":
        """Add a single item to entities list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.entities.append(item)
        return self

    def clear_entities(self) -> "BswInternalBehaviorBuilder":
        """Clear all items from entities list.

        Returns:
            self for method chaining
        """
        self._obj.entities = []
        return self

    def add_event(self, item: BswEvent) -> "BswInternalBehaviorBuilder":
        """Add a single item to events list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.events.append(item)
        return self

    def clear_events(self) -> "BswInternalBehaviorBuilder":
        """Clear all items from events list.

        Returns:
            self for method chaining
        """
        self._obj.events = []
        return self

    def add_included_data_type_set(self, item: IncludedDataTypeSet) -> "BswInternalBehaviorBuilder":
        """Add a single item to included_data_type_sets list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.included_data_type_sets.append(item)
        return self

    def clear_included_data_type_sets(self) -> "BswInternalBehaviorBuilder":
        """Clear all items from included_data_type_sets list.

        Returns:
            self for method chaining
        """
        self._obj.included_data_type_sets = []
        return self

    def add_included_mode(self, item: IncludedModeDeclarationGroupSet) -> "BswInternalBehaviorBuilder":
        """Add a single item to included_modes list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.included_modes.append(item)
        return self

    def clear_included_modes(self) -> "BswInternalBehaviorBuilder":
        """Clear all items from included_modes list.

        Returns:
            self for method chaining
        """
        self._obj.included_modes = []
        return self

    def add_internal(self, item: BswInternalTriggeringPoint) -> "BswInternalBehaviorBuilder":
        """Add a single item to internals list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.internals.append(item)
        return self

    def clear_internals(self) -> "BswInternalBehaviorBuilder":
        """Clear all items from internals list.

        Returns:
            self for method chaining
        """
        self._obj.internals = []
        return self

    def add_mode_receiver(self, item: BswModeReceiverPolicy) -> "BswInternalBehaviorBuilder":
        """Add a single item to mode_receivers list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.mode_receivers.append(item)
        return self

    def clear_mode_receivers(self) -> "BswInternalBehaviorBuilder":
        """Clear all items from mode_receivers list.

        Returns:
            self for method chaining
        """
        self._obj.mode_receivers = []
        return self

    def add_mode_sender(self, item: BswModeSenderPolicy) -> "BswInternalBehaviorBuilder":
        """Add a single item to mode_senders list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.mode_senders.append(item)
        return self

    def clear_mode_senders(self) -> "BswInternalBehaviorBuilder":
        """Clear all items from mode_senders list.

        Returns:
            self for method chaining
        """
        self._obj.mode_senders = []
        return self

    def add_parameter_policie(self, item: any (BswParameterPolicy)) -> "BswInternalBehaviorBuilder":
        """Add a single item to parameter_policies list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.parameter_policies.append(item)
        return self

    def clear_parameter_policies(self) -> "BswInternalBehaviorBuilder":
        """Clear all items from parameter_policies list.

        Returns:
            self for method chaining
        """
        self._obj.parameter_policies = []
        return self

    def add_per_instance(self, item: ParameterDataPrototype) -> "BswInternalBehaviorBuilder":
        """Add a single item to per_instances list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.per_instances.append(item)
        return self

    def clear_per_instances(self) -> "BswInternalBehaviorBuilder":
        """Clear all items from per_instances list.

        Returns:
            self for method chaining
        """
        self._obj.per_instances = []
        return self

    def add_reception_policie(self, item: BswDataReceptionPolicy) -> "BswInternalBehaviorBuilder":
        """Add a single item to reception_policies list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.reception_policies.append(item)
        return self

    def clear_reception_policies(self) -> "BswInternalBehaviorBuilder":
        """Clear all items from reception_policies list.

        Returns:
            self for method chaining
        """
        self._obj.reception_policies = []
        return self

    def add_released_trigger(self, item: any (BswReleasedTrigger)) -> "BswInternalBehaviorBuilder":
        """Add a single item to released_triggers list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.released_triggers.append(item)
        return self

    def clear_released_triggers(self) -> "BswInternalBehaviorBuilder":
        """Clear all items from released_triggers list.

        Returns:
            self for method chaining
        """
        self._obj.released_triggers = []
        return self

    def add_scheduler_name(self, item: BswSchedulerNamePrefix) -> "BswInternalBehaviorBuilder":
        """Add a single item to scheduler_names list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.scheduler_names.append(item)
        return self

    def clear_scheduler_names(self) -> "BswInternalBehaviorBuilder":
        """Clear all items from scheduler_names list.

        Returns:
            self for method chaining
        """
        self._obj.scheduler_names = []
        return self

    def add_send_policie(self, item: any (BswDataSendPolicy)) -> "BswInternalBehaviorBuilder":
        """Add a single item to send_policies list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.send_policies.append(item)
        return self

    def clear_send_policies(self) -> "BswInternalBehaviorBuilder":
        """Clear all items from send_policies list.

        Returns:
            self for method chaining
        """
        self._obj.send_policies = []
        return self

    def add_service(self, item: any (BswService)) -> "BswInternalBehaviorBuilder":
        """Add a single item to services list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.services.append(item)
        return self

    def clear_services(self) -> "BswInternalBehaviorBuilder":
        """Clear all items from services list.

        Returns:
            self for method chaining
        """
        self._obj.services = []
        return self

    def add_trigger_direct(self, item: BswTriggerDirectImplementation) -> "BswInternalBehaviorBuilder":
        """Add a single item to trigger_directs list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.trigger_directs.append(item)
        return self

    def clear_trigger_directs(self) -> "BswInternalBehaviorBuilder":
        """Clear all items from trigger_directs list.

        Returns:
            self for method chaining
        """
        self._obj.trigger_directs = []
        return self

    def add_variation_point_proxie(self, item: VariationPointProxy) -> "BswInternalBehaviorBuilder":
        """Add a single item to variation_point_proxies list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.variation_point_proxies.append(item)
        return self

    def clear_variation_point_proxies(self) -> "BswInternalBehaviorBuilder":
        """Clear all items from variation_point_proxies list.

        Returns:
            self for method chaining
        """
        self._obj.variation_point_proxies = []
        return self


    @staticmethod
    def _coerce_to_int(value: Any) -> int:
        """Coerce value to int.

        Args:
            value: Value to coerce

        Returns:
            Integer value

        Raises:
            ValueError: If value cannot be coerced to int
        """
        if isinstance(value, int):
            return value
        if isinstance(value, str) and value.isdigit():
            return int(value)
        if isinstance(value, float):
            return int(value)
        if isinstance(value, bool):
            return int(value)
        raise ValueError(f"Cannot coerce {type(value).__name__} to int: {value}")

    @staticmethod
    def _coerce_to_float(value: Any) -> float:
        """Coerce value to float.

        Args:
            value: Value to coerce

        Returns:
            Float value

        Raises:
            ValueError: If value cannot be coerced to float
        """
        if isinstance(value, float):
            return value
        if isinstance(value, int):
            return float(value)
        if isinstance(value, str):
            try:
                return float(value)
            except ValueError:
                pass
        raise ValueError(f"Cannot coerce {type(value).__name__} to float: {value}")

    @staticmethod
    def _coerce_to_bool(value: Any) -> bool:
        """Coerce value to bool.

        Args:
            value: Value to coerce

        Returns:
            Boolean value

        Raises:
            ValueError: If value cannot be coerced to bool
        """
        if isinstance(value, bool):
            return value
        if isinstance(value, int):
            return bool(value)
        if isinstance(value, str):
            if value.lower() in ("true", "1", "yes"):
                return True
            if value.lower() in ("false", "0", "no"):
                return False
        raise ValueError(f"Cannot coerce {type(value).__name__} to bool: {value}")

    @staticmethod
    def _coerce_to_str(value: Any) -> str:
        """Coerce value to str.

        Args:
            value: Value to coerce

        Returns:
            String value
        """
        return str(value)


    @staticmethod
    def _coerce_to_list(value: Any, item_type: str) -> list:
        """Coerce value to list.

        Args:
            value: Value to coerce
            item_type: Expected item type (for error messages)

        Returns:
            List value

        Raises:
            ValueError: If value cannot be coerced to list
        """
        if isinstance(value, list):
            return value
        if isinstance(value, tuple):
            return list(value)
        raise ValueError(f"Cannot coerce {type(value).__name__} to list[{item_type}]: {value}")


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


    def build(self) -> BswInternalBehavior:
        """Build and return the BswInternalBehavior instance with validation."""
        self._validate_instance()
        pass
        return self._obj