"""BswInternalBehavior AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 65)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 649)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2003)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 208)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 165)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel2.serialization.decorators import xml_element_name

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.internal_behavior import (
    InternalBehavior,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.internal_behavior import InternalBehaviorBuilder
from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_data_reception_policy import (
    BswDataReceptionPolicy,
)
from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_distinguished_partition import (
    BswDistinguishedPartition,
)
from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_event import (
    BswEvent,
)
from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_exclusive_area_policy import (
    BswExclusiveAreaPolicy,
)
from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_internal_triggering_point import (
    BswInternalTriggeringPoint,
)
from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_mode_receiver_policy import (
    BswModeReceiverPolicy,
)
from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_mode_sender_policy import (
    BswModeSenderPolicy,
)
from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_module_entity import (
    BswModuleEntity,
)
from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_scheduler_name_prefix import (
    BswSchedulerNamePrefix,
)
from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_service_dependency import (
    BswServiceDependency,
)
from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_trigger_direct_implementation import (
    BswTriggerDirectImplementation,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.IncludedDataTypes.included_data_type_set import (
    IncludedDataTypeSet,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ModeDeclarationGroup.included_mode_declaration_group_set import (
    IncludedModeDeclarationGroupSet,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.parameter_data_prototype import (
    ParameterDataPrototype,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.VariantHandling.variation_point_proxy import (
    VariationPointProxy,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class BswInternalBehavior(InternalBehavior):
    """AUTOSAR BswInternalBehavior."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "BSW-INTERNAL-BEHAVIOR"


    ar_typed_per_instance_memories: list[VariableDataPrototype]
    bsw_per_instance_memory_policies: list[BswPerInstanceMemoryPolicy]
    client_policies: list[BswClientPolicy]
    distinguished_partitions: list[BswDistinguishedPartition]
    _entities: list[BswModuleEntity]
    events: list[BswEvent]
    exclusive_area_policies: list[BswExclusiveAreaPolicy]
    included_data_type_sets: list[IncludedDataTypeSet]
    included_mode_declaration_group_sets: list[IncludedModeDeclarationGroupSet]
    internal_triggering_points: list[BswInternalTriggeringPoint]
    internal_triggering_point_policies: list[BswInternalTriggeringPointPolicy]
    mode_receiver_policies: list[BswModeReceiverPolicy]
    mode_sender_policies: list[BswModeSenderPolicy]
    parameter_policies: list[BswParameterPolicy]
    per_instance_parameters: list[ParameterDataPrototype]
    reception_policies: list[BswDataReceptionPolicy]
    released_trigger_policies: list[BswReleasedTriggerPolicy]
    scheduler_name_prefixes: list[BswSchedulerNamePrefix]
    send_policies: list[BswDataSendPolicy]
    service_dependencies: list[BswServiceDependency]
    trigger_direct_implementations: list[BswTriggerDirectImplementation]
    variation_point_proxies: list[VariationPointProxy]
    _DESERIALIZE_DISPATCH = {
        "AR-TYPED-PER-INSTANCE-MEMORIES": lambda obj, elem: obj.ar_typed_per_instance_memories.append(SerializationHelper.deserialize_by_tag(elem, "VariableDataPrototype")),
        "BSW-PER-INSTANCE-MEMORY-POLICIES": lambda obj, elem: obj.bsw_per_instance_memory_policies.append(SerializationHelper.deserialize_by_tag(elem, "BswPerInstanceMemoryPolicy")),
        "CLIENT-POLICIES": lambda obj, elem: obj.client_policies.append(SerializationHelper.deserialize_by_tag(elem, "BswClientPolicy")),
        "DISTINGUISHED-PARTITIONS": lambda obj, elem: obj.distinguished_partitions.append(SerializationHelper.deserialize_by_tag(elem, "BswDistinguishedPartition")),
        "ENTITYS": ("_POLYMORPHIC_LIST", "_entities", ["BswCalledEntity", "BswInterruptEntity", "BswSchedulableEntity"]),
        "EVENTS": ("_POLYMORPHIC_LIST", "events", ["BswInterruptEvent", "BswOperationInvokedEvent", "BswScheduleEvent"]),
        "EXCLUSIVE-AREA-POLICIES": lambda obj, elem: obj.exclusive_area_policies.append(SerializationHelper.deserialize_by_tag(elem, "BswExclusiveAreaPolicy")),
        "INCLUDED-DATA-TYPE-SETS": lambda obj, elem: obj.included_data_type_sets.append(SerializationHelper.deserialize_by_tag(elem, "IncludedDataTypeSet")),
        "INCLUDED-MODE-DECLARATION-GROUP-SETS": lambda obj, elem: obj.included_mode_declaration_group_sets.append(SerializationHelper.deserialize_by_tag(elem, "IncludedModeDeclarationGroupSet")),
        "INTERNAL-TRIGGERING-POINTS": lambda obj, elem: obj.internal_triggering_points.append(SerializationHelper.deserialize_by_tag(elem, "BswInternalTriggeringPoint")),
        "INTERNAL-TRIGGERING-POINT-POLICIES": lambda obj, elem: obj.internal_triggering_point_policies.append(SerializationHelper.deserialize_by_tag(elem, "BswInternalTriggeringPointPolicy")),
        "MODE-RECEIVER-POLICIES": lambda obj, elem: obj.mode_receiver_policies.append(SerializationHelper.deserialize_by_tag(elem, "BswModeReceiverPolicy")),
        "MODE-SENDER-POLICIES": lambda obj, elem: obj.mode_sender_policies.append(SerializationHelper.deserialize_by_tag(elem, "BswModeSenderPolicy")),
        "PARAMETER-POLICIES": lambda obj, elem: obj.parameter_policies.append(SerializationHelper.deserialize_by_tag(elem, "BswParameterPolicy")),
        "PER-INSTANCE-PARAMETERS": lambda obj, elem: obj.per_instance_parameters.append(SerializationHelper.deserialize_by_tag(elem, "ParameterDataPrototype")),
        "RECEPTION-POLICIES": ("_POLYMORPHIC_LIST", "reception_policies", ["BswQueuedDataReceptionPolicy"]),
        "RELEASED-TRIGGER-POLICIES": lambda obj, elem: obj.released_trigger_policies.append(SerializationHelper.deserialize_by_tag(elem, "BswReleasedTriggerPolicy")),
        "SCHEDULER-NAME-PREFIXES": lambda obj, elem: obj.scheduler_name_prefixes.append(SerializationHelper.deserialize_by_tag(elem, "BswSchedulerNamePrefix")),
        "SEND-POLICIES": lambda obj, elem: obj.send_policies.append(SerializationHelper.deserialize_by_tag(elem, "BswDataSendPolicy")),
        "SERVICE-DEPENDENCIES": lambda obj, elem: obj.service_dependencies.append(SerializationHelper.deserialize_by_tag(elem, "BswServiceDependency")),
        "TRIGGER-DIRECT-IMPLEMENTATIONS": lambda obj, elem: obj.trigger_direct_implementations.append(SerializationHelper.deserialize_by_tag(elem, "BswTriggerDirectImplementation")),
        "VARIATION-POINT-PROXIES": lambda obj, elem: obj.variation_point_proxies.append(SerializationHelper.deserialize_by_tag(elem, "VariationPointProxy")),
    }


    def __init__(self) -> None:
        """Initialize BswInternalBehavior."""
        super().__init__()
        self.ar_typed_per_instance_memories: list[VariableDataPrototype] = []
        self.bsw_per_instance_memory_policies: list[BswPerInstanceMemoryPolicy] = []
        self.client_policies: list[BswClientPolicy] = []
        self.distinguished_partitions: list[BswDistinguishedPartition] = []
        self._entities: list[BswModuleEntity] = []
        self.events: list[BswEvent] = []
        self.exclusive_area_policies: list[BswExclusiveAreaPolicy] = []
        self.included_data_type_sets: list[IncludedDataTypeSet] = []
        self.included_mode_declaration_group_sets: list[IncludedModeDeclarationGroupSet] = []
        self.internal_triggering_points: list[BswInternalTriggeringPoint] = []
        self.internal_triggering_point_policies: list[BswInternalTriggeringPointPolicy] = []
        self.mode_receiver_policies: list[BswModeReceiverPolicy] = []
        self.mode_sender_policies: list[BswModeSenderPolicy] = []
        self.parameter_policies: list[BswParameterPolicy] = []
        self.per_instance_parameters: list[ParameterDataPrototype] = []
        self.reception_policies: list[BswDataReceptionPolicy] = []
        self.released_trigger_policies: list[BswReleasedTriggerPolicy] = []
        self.scheduler_name_prefixes: list[BswSchedulerNamePrefix] = []
        self.send_policies: list[BswDataSendPolicy] = []
        self.service_dependencies: list[BswServiceDependency] = []
        self.trigger_direct_implementations: list[BswTriggerDirectImplementation] = []
        self.variation_point_proxies: list[VariationPointProxy] = []
    @property
    @xml_element_name("ENTITYS/BSW-SCHEDULABLE-ENTITY")
    def entities(self) -> list[BswModuleEntity]:
        """Get entities with custom XML element name."""
        return self._entities

    @entities.setter
    def entities(self, value: list[BswModuleEntity]) -> None:
        """Set entities with custom XML element name."""
        self._entities = value


    def serialize(self) -> ET.Element:
        """Serialize BswInternalBehavior to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

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

        # Serialize ar_typed_per_instance_memories (list to container "AR-TYPED-PER-INSTANCE-MEMORIES")
        if self.ar_typed_per_instance_memories:
            wrapper = ET.Element("AR-TYPED-PER-INSTANCE-MEMORIES")
            for item in self.ar_typed_per_instance_memories:
                serialized = SerializationHelper.serialize_item(item, "VariableDataPrototype")
                if serialized is not None:
                    wrapper.append(serialized)
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

        # Serialize distinguished_partitions (list to container "DISTINGUISHED-PARTITIONS")
        if self.distinguished_partitions:
            wrapper = ET.Element("DISTINGUISHED-PARTITIONS")
            for item in self.distinguished_partitions:
                serialized = SerializationHelper.serialize_item(item, "BswDistinguishedPartition")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize entities (list to container "ENTITYS")
        if self.entities:
            wrapper = ET.Element("ENTITYS")
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

        # Serialize exclusive_area_policies (list to container "EXCLUSIVE-AREA-POLICIES")
        if self.exclusive_area_policies:
            wrapper = ET.Element("EXCLUSIVE-AREA-POLICIES")
            for item in self.exclusive_area_policies:
                serialized = SerializationHelper.serialize_item(item, "BswExclusiveAreaPolicy")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize included_data_type_sets (list to container "INCLUDED-DATA-TYPE-SETS")
        if self.included_data_type_sets:
            wrapper = ET.Element("INCLUDED-DATA-TYPE-SETS")
            for item in self.included_data_type_sets:
                serialized = SerializationHelper.serialize_item(item, "IncludedDataTypeSet")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize included_mode_declaration_group_sets (list to container "INCLUDED-MODE-DECLARATION-GROUP-SETS")
        if self.included_mode_declaration_group_sets:
            wrapper = ET.Element("INCLUDED-MODE-DECLARATION-GROUP-SETS")
            for item in self.included_mode_declaration_group_sets:
                serialized = SerializationHelper.serialize_item(item, "IncludedModeDeclarationGroupSet")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize internal_triggering_points (list to container "INTERNAL-TRIGGERING-POINTS")
        if self.internal_triggering_points:
            wrapper = ET.Element("INTERNAL-TRIGGERING-POINTS")
            for item in self.internal_triggering_points:
                serialized = SerializationHelper.serialize_item(item, "BswInternalTriggeringPoint")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize internal_triggering_point_policies (list to container "INTERNAL-TRIGGERING-POINT-POLICIES")
        if self.internal_triggering_point_policies:
            wrapper = ET.Element("INTERNAL-TRIGGERING-POINT-POLICIES")
            for item in self.internal_triggering_point_policies:
                serialized = SerializationHelper.serialize_item(item, "BswInternalTriggeringPointPolicy")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize mode_receiver_policies (list to container "MODE-RECEIVER-POLICIES")
        if self.mode_receiver_policies:
            wrapper = ET.Element("MODE-RECEIVER-POLICIES")
            for item in self.mode_receiver_policies:
                serialized = SerializationHelper.serialize_item(item, "BswModeReceiverPolicy")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize mode_sender_policies (list to container "MODE-SENDER-POLICIES")
        if self.mode_sender_policies:
            wrapper = ET.Element("MODE-SENDER-POLICIES")
            for item in self.mode_sender_policies:
                serialized = SerializationHelper.serialize_item(item, "BswModeSenderPolicy")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize parameter_policies (list to container "PARAMETER-POLICIES")
        if self.parameter_policies:
            wrapper = ET.Element("PARAMETER-POLICIES")
            for item in self.parameter_policies:
                serialized = SerializationHelper.serialize_item(item, "BswParameterPolicy")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize per_instance_parameters (list to container "PER-INSTANCE-PARAMETERS")
        if self.per_instance_parameters:
            wrapper = ET.Element("PER-INSTANCE-PARAMETERS")
            for item in self.per_instance_parameters:
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

        # Serialize released_trigger_policies (list to container "RELEASED-TRIGGER-POLICIES")
        if self.released_trigger_policies:
            wrapper = ET.Element("RELEASED-TRIGGER-POLICIES")
            for item in self.released_trigger_policies:
                serialized = SerializationHelper.serialize_item(item, "BswReleasedTriggerPolicy")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize scheduler_name_prefixes (list to container "SCHEDULER-NAME-PREFIXES")
        if self.scheduler_name_prefixes:
            wrapper = ET.Element("SCHEDULER-NAME-PREFIXES")
            for item in self.scheduler_name_prefixes:
                serialized = SerializationHelper.serialize_item(item, "BswSchedulerNamePrefix")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize send_policies (list to container "SEND-POLICIES")
        if self.send_policies:
            wrapper = ET.Element("SEND-POLICIES")
            for item in self.send_policies:
                serialized = SerializationHelper.serialize_item(item, "BswDataSendPolicy")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize service_dependencies (list to container "SERVICE-DEPENDENCIES")
        if self.service_dependencies:
            wrapper = ET.Element("SERVICE-DEPENDENCIES")
            for item in self.service_dependencies:
                serialized = SerializationHelper.serialize_item(item, "BswServiceDependency")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize trigger_direct_implementations (list to container "TRIGGER-DIRECT-IMPLEMENTATIONS")
        if self.trigger_direct_implementations:
            wrapper = ET.Element("TRIGGER-DIRECT-IMPLEMENTATIONS")
            for item in self.trigger_direct_implementations:
                serialized = SerializationHelper.serialize_item(item, "BswTriggerDirectImplementation")
                if serialized is not None:
                    wrapper.append(serialized)
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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "AR-TYPED-PER-INSTANCE-MEMORIES":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.ar_typed_per_instance_memories.append(SerializationHelper.deserialize_by_tag(item_elem, "VariableDataPrototype"))
            elif tag == "BSW-PER-INSTANCE-MEMORY-POLICIES":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.bsw_per_instance_memory_policies.append(SerializationHelper.deserialize_by_tag(item_elem, "BswPerInstanceMemoryPolicy"))
            elif tag == "CLIENT-POLICIES":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.client_policies.append(SerializationHelper.deserialize_by_tag(item_elem, "BswClientPolicy"))
            elif tag == "DISTINGUISHED-PARTITIONS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.distinguished_partitions.append(SerializationHelper.deserialize_by_tag(item_elem, "BswDistinguishedPartition"))
            elif tag == "ENTITYS":
                # Iterate through all child elements and deserialize each based on its concrete type
                for item_elem in child:
                    concrete_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    if concrete_tag == "BSW-CALLED-ENTITY":
                        obj._entities.append(SerializationHelper.deserialize_by_tag(item_elem, "BswCalledEntity"))
                    elif concrete_tag == "BSW-INTERRUPT-ENTITY":
                        obj._entities.append(SerializationHelper.deserialize_by_tag(item_elem, "BswInterruptEntity"))
                    elif concrete_tag == "BSW-SCHEDULABLE-ENTITY":
                        obj._entities.append(SerializationHelper.deserialize_by_tag(item_elem, "BswSchedulableEntity"))
            elif tag == "EVENTS":
                # Iterate through all child elements and deserialize each based on its concrete type
                for item_elem in child:
                    concrete_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    if concrete_tag == "BSW-INTERRUPT-EVENT":
                        obj.events.append(SerializationHelper.deserialize_by_tag(item_elem, "BswInterruptEvent"))
                    elif concrete_tag == "BSW-OPERATION-INVOKED-EVENT":
                        obj.events.append(SerializationHelper.deserialize_by_tag(item_elem, "BswOperationInvokedEvent"))
                    elif concrete_tag == "BSW-SCHEDULE-EVENT":
                        obj.events.append(SerializationHelper.deserialize_by_tag(item_elem, "BswScheduleEvent"))
            elif tag == "EXCLUSIVE-AREA-POLICIES":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.exclusive_area_policies.append(SerializationHelper.deserialize_by_tag(item_elem, "BswExclusiveAreaPolicy"))
            elif tag == "INCLUDED-DATA-TYPE-SETS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.included_data_type_sets.append(SerializationHelper.deserialize_by_tag(item_elem, "IncludedDataTypeSet"))
            elif tag == "INCLUDED-MODE-DECLARATION-GROUP-SETS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.included_mode_declaration_group_sets.append(SerializationHelper.deserialize_by_tag(item_elem, "IncludedModeDeclarationGroupSet"))
            elif tag == "INTERNAL-TRIGGERING-POINTS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.internal_triggering_points.append(SerializationHelper.deserialize_by_tag(item_elem, "BswInternalTriggeringPoint"))
            elif tag == "INTERNAL-TRIGGERING-POINT-POLICIES":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.internal_triggering_point_policies.append(SerializationHelper.deserialize_by_tag(item_elem, "BswInternalTriggeringPointPolicy"))
            elif tag == "MODE-RECEIVER-POLICIES":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.mode_receiver_policies.append(SerializationHelper.deserialize_by_tag(item_elem, "BswModeReceiverPolicy"))
            elif tag == "MODE-SENDER-POLICIES":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.mode_sender_policies.append(SerializationHelper.deserialize_by_tag(item_elem, "BswModeSenderPolicy"))
            elif tag == "PARAMETER-POLICIES":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.parameter_policies.append(SerializationHelper.deserialize_by_tag(item_elem, "BswParameterPolicy"))
            elif tag == "PER-INSTANCE-PARAMETERS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.per_instance_parameters.append(SerializationHelper.deserialize_by_tag(item_elem, "ParameterDataPrototype"))
            elif tag == "RECEPTION-POLICIES":
                # Iterate through all child elements and deserialize each based on its concrete type
                for item_elem in child:
                    concrete_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    if concrete_tag == "BSW-QUEUED-DATA-RECEPTION-POLICY":
                        obj.reception_policies.append(SerializationHelper.deserialize_by_tag(item_elem, "BswQueuedDataReceptionPolicy"))
            elif tag == "RELEASED-TRIGGER-POLICIES":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.released_trigger_policies.append(SerializationHelper.deserialize_by_tag(item_elem, "BswReleasedTriggerPolicy"))
            elif tag == "SCHEDULER-NAME-PREFIXES":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.scheduler_name_prefixes.append(SerializationHelper.deserialize_by_tag(item_elem, "BswSchedulerNamePrefix"))
            elif tag == "SEND-POLICIES":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.send_policies.append(SerializationHelper.deserialize_by_tag(item_elem, "BswDataSendPolicy"))
            elif tag == "SERVICE-DEPENDENCIES":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.service_dependencies.append(SerializationHelper.deserialize_by_tag(item_elem, "BswServiceDependency"))
            elif tag == "TRIGGER-DIRECT-IMPLEMENTATIONS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.trigger_direct_implementations.append(SerializationHelper.deserialize_by_tag(item_elem, "BswTriggerDirectImplementation"))
            elif tag == "VARIATION-POINT-PROXIES":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.variation_point_proxies.append(SerializationHelper.deserialize_by_tag(item_elem, "VariationPointProxy"))

        return obj



class BswInternalBehaviorBuilder(InternalBehaviorBuilder):
    """Builder for BswInternalBehavior with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: BswInternalBehavior = BswInternalBehavior()


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

    def with_distinguished_partitions(self, items: list[BswDistinguishedPartition]) -> "BswInternalBehaviorBuilder":
        """Set distinguished_partitions list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.distinguished_partitions = list(items) if items else []
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

    def with_exclusive_area_policies(self, items: list[BswExclusiveAreaPolicy]) -> "BswInternalBehaviorBuilder":
        """Set exclusive_area_policies list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.exclusive_area_policies = list(items) if items else []
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

    def with_included_mode_declaration_group_sets(self, items: list[IncludedModeDeclarationGroupSet]) -> "BswInternalBehaviorBuilder":
        """Set included_mode_declaration_group_sets list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.included_mode_declaration_group_sets = list(items) if items else []
        return self

    def with_internal_triggering_points(self, items: list[BswInternalTriggeringPoint]) -> "BswInternalBehaviorBuilder":
        """Set internal_triggering_points list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.internal_triggering_points = list(items) if items else []
        return self

    def with_internal_triggering_point_policies(self, items: list[BswInternalTriggeringPointPolicy]) -> "BswInternalBehaviorBuilder":
        """Set internal_triggering_point_policies list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.internal_triggering_point_policies = list(items) if items else []
        return self

    def with_mode_receiver_policies(self, items: list[BswModeReceiverPolicy]) -> "BswInternalBehaviorBuilder":
        """Set mode_receiver_policies list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.mode_receiver_policies = list(items) if items else []
        return self

    def with_mode_sender_policies(self, items: list[BswModeSenderPolicy]) -> "BswInternalBehaviorBuilder":
        """Set mode_sender_policies list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.mode_sender_policies = list(items) if items else []
        return self

    def with_parameter_policies(self, items: list[BswParameterPolicy]) -> "BswInternalBehaviorBuilder":
        """Set parameter_policies list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.parameter_policies = list(items) if items else []
        return self

    def with_per_instance_parameters(self, items: list[ParameterDataPrototype]) -> "BswInternalBehaviorBuilder":
        """Set per_instance_parameters list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.per_instance_parameters = list(items) if items else []
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

    def with_released_trigger_policies(self, items: list[BswReleasedTriggerPolicy]) -> "BswInternalBehaviorBuilder":
        """Set released_trigger_policies list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.released_trigger_policies = list(items) if items else []
        return self

    def with_scheduler_name_prefixes(self, items: list[BswSchedulerNamePrefix]) -> "BswInternalBehaviorBuilder":
        """Set scheduler_name_prefixes list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.scheduler_name_prefixes = list(items) if items else []
        return self

    def with_send_policies(self, items: list[BswDataSendPolicy]) -> "BswInternalBehaviorBuilder":
        """Set send_policies list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.send_policies = list(items) if items else []
        return self

    def with_service_dependencies(self, items: list[BswServiceDependency]) -> "BswInternalBehaviorBuilder":
        """Set service_dependencies list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.service_dependencies = list(items) if items else []
        return self

    def with_trigger_direct_implementations(self, items: list[BswTriggerDirectImplementation]) -> "BswInternalBehaviorBuilder":
        """Set trigger_direct_implementations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.trigger_direct_implementations = list(items) if items else []
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


    def add_ar_typed_per_instance_memory(self, item: VariableDataPrototype) -> "BswInternalBehaviorBuilder":
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

    def add_bsw_per_instance_memory_policy(self, item: BswPerInstanceMemoryPolicy) -> "BswInternalBehaviorBuilder":
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

    def add_client_policy(self, item: BswClientPolicy) -> "BswInternalBehaviorBuilder":
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

    def add_distinguished_partition(self, item: BswDistinguishedPartition) -> "BswInternalBehaviorBuilder":
        """Add a single item to distinguished_partitions list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.distinguished_partitions.append(item)
        return self

    def clear_distinguished_partitions(self) -> "BswInternalBehaviorBuilder":
        """Clear all items from distinguished_partitions list.

        Returns:
            self for method chaining
        """
        self._obj.distinguished_partitions = []
        return self

    def add_entity(self, item: BswModuleEntity) -> "BswInternalBehaviorBuilder":
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

    def add_exclusive_area_policy(self, item: BswExclusiveAreaPolicy) -> "BswInternalBehaviorBuilder":
        """Add a single item to exclusive_area_policies list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.exclusive_area_policies.append(item)
        return self

    def clear_exclusive_area_policies(self) -> "BswInternalBehaviorBuilder":
        """Clear all items from exclusive_area_policies list.

        Returns:
            self for method chaining
        """
        self._obj.exclusive_area_policies = []
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

    def add_included_mode_declaration_group_set(self, item: IncludedModeDeclarationGroupSet) -> "BswInternalBehaviorBuilder":
        """Add a single item to included_mode_declaration_group_sets list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.included_mode_declaration_group_sets.append(item)
        return self

    def clear_included_mode_declaration_group_sets(self) -> "BswInternalBehaviorBuilder":
        """Clear all items from included_mode_declaration_group_sets list.

        Returns:
            self for method chaining
        """
        self._obj.included_mode_declaration_group_sets = []
        return self

    def add_internal_triggering_point(self, item: BswInternalTriggeringPoint) -> "BswInternalBehaviorBuilder":
        """Add a single item to internal_triggering_points list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.internal_triggering_points.append(item)
        return self

    def clear_internal_triggering_points(self) -> "BswInternalBehaviorBuilder":
        """Clear all items from internal_triggering_points list.

        Returns:
            self for method chaining
        """
        self._obj.internal_triggering_points = []
        return self

    def add_internal_triggering_point_policy(self, item: BswInternalTriggeringPointPolicy) -> "BswInternalBehaviorBuilder":
        """Add a single item to internal_triggering_point_policies list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.internal_triggering_point_policies.append(item)
        return self

    def clear_internal_triggering_point_policies(self) -> "BswInternalBehaviorBuilder":
        """Clear all items from internal_triggering_point_policies list.

        Returns:
            self for method chaining
        """
        self._obj.internal_triggering_point_policies = []
        return self

    def add_mode_receiver_policy(self, item: BswModeReceiverPolicy) -> "BswInternalBehaviorBuilder":
        """Add a single item to mode_receiver_policies list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.mode_receiver_policies.append(item)
        return self

    def clear_mode_receiver_policies(self) -> "BswInternalBehaviorBuilder":
        """Clear all items from mode_receiver_policies list.

        Returns:
            self for method chaining
        """
        self._obj.mode_receiver_policies = []
        return self

    def add_mode_sender_policy(self, item: BswModeSenderPolicy) -> "BswInternalBehaviorBuilder":
        """Add a single item to mode_sender_policies list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.mode_sender_policies.append(item)
        return self

    def clear_mode_sender_policies(self) -> "BswInternalBehaviorBuilder":
        """Clear all items from mode_sender_policies list.

        Returns:
            self for method chaining
        """
        self._obj.mode_sender_policies = []
        return self

    def add_parameter_policy(self, item: BswParameterPolicy) -> "BswInternalBehaviorBuilder":
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

    def add_per_instance_parameter(self, item: ParameterDataPrototype) -> "BswInternalBehaviorBuilder":
        """Add a single item to per_instance_parameters list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.per_instance_parameters.append(item)
        return self

    def clear_per_instance_parameters(self) -> "BswInternalBehaviorBuilder":
        """Clear all items from per_instance_parameters list.

        Returns:
            self for method chaining
        """
        self._obj.per_instance_parameters = []
        return self

    def add_reception_policy(self, item: BswDataReceptionPolicy) -> "BswInternalBehaviorBuilder":
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

    def add_released_trigger_policy(self, item: BswReleasedTriggerPolicy) -> "BswInternalBehaviorBuilder":
        """Add a single item to released_trigger_policies list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.released_trigger_policies.append(item)
        return self

    def clear_released_trigger_policies(self) -> "BswInternalBehaviorBuilder":
        """Clear all items from released_trigger_policies list.

        Returns:
            self for method chaining
        """
        self._obj.released_trigger_policies = []
        return self

    def add_scheduler_name_prefix(self, item: BswSchedulerNamePrefix) -> "BswInternalBehaviorBuilder":
        """Add a single item to scheduler_name_prefixes list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.scheduler_name_prefixes.append(item)
        return self

    def clear_scheduler_name_prefixes(self) -> "BswInternalBehaviorBuilder":
        """Clear all items from scheduler_name_prefixes list.

        Returns:
            self for method chaining
        """
        self._obj.scheduler_name_prefixes = []
        return self

    def add_send_policy(self, item: BswDataSendPolicy) -> "BswInternalBehaviorBuilder":
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

    def add_service_dependency(self, item: BswServiceDependency) -> "BswInternalBehaviorBuilder":
        """Add a single item to service_dependencies list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.service_dependencies.append(item)
        return self

    def clear_service_dependencies(self) -> "BswInternalBehaviorBuilder":
        """Clear all items from service_dependencies list.

        Returns:
            self for method chaining
        """
        self._obj.service_dependencies = []
        return self

    def add_trigger_direct_implementation(self, item: BswTriggerDirectImplementation) -> "BswInternalBehaviorBuilder":
        """Add a single item to trigger_direct_implementations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.trigger_direct_implementations.append(item)
        return self

    def clear_trigger_direct_implementations(self) -> "BswInternalBehaviorBuilder":
        """Clear all items from trigger_direct_implementations list.

        Returns:
            self for method chaining
        """
        self._obj.trigger_direct_implementations = []
        return self

    def add_variation_point_proxy(self, item: VariationPointProxy) -> "BswInternalBehaviorBuilder":
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


    def build(self) -> BswInternalBehavior:
        """Build and return the BswInternalBehavior instance with validation."""
        self._validate_instance()
        pass
        return self._obj