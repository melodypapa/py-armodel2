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
from armodel.serialization.decorators import xml_element_name

from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.internal_behavior import (
    InternalBehavior,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
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
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_service_dependency import (
    BswServiceDependency,
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

    _ar_typed_per_instance_memories: list[VariableDataPrototype]
    _bsw_per_instance_memory_policies: list[BswPerInstanceMemoryPolicy]
    _client_policies: list[BswClientPolicy]
    distinguished_partitions: list[BswDistinguishedPartition]
    _entities: list[BswModuleEntity]
    events: list[BswEvent]
    _exclusive_area_policies: list[BswExclusiveAreaPolicy]
    included_data_type_sets: list[IncludedDataTypeSet]
    included_mode_declaration_group_sets: list[IncludedModeDeclarationGroupSet]
    internal_triggering_points: list[BswInternalTriggeringPoint]
    _internal_triggering_point_policies: list[BswInternalTriggeringPointPolicy]
    _mode_receiver_policies: list[BswModeReceiverPolicy]
    _mode_sender_policies: list[BswModeSenderPolicy]
    _parameter_policies: list[BswParameterPolicy]
    per_instance_parameters: list[ParameterDataPrototype]
    _reception_policies: list[BswDataReceptionPolicy]
    _released_trigger_policies: list[BswReleasedTriggerPolicy]
    scheduler_name_prefixs: list[BswSchedulerNamePrefix]
    _send_policies: list[BswDataSendPolicy]
    _service_dependencies: list[BswServiceDependency]
    trigger_direct_implementations: list[BswTriggerDirectImplementation]
    _variation_point_proxies: list[VariationPointProxy]
    def __init__(self) -> None:
        """Initialize BswInternalBehavior."""
        super().__init__()
        self._ar_typed_per_instance_memories: list[VariableDataPrototype] = []
        self._bsw_per_instance_memory_policies: list[BswPerInstanceMemoryPolicy] = []
        self._client_policies: list[BswClientPolicy] = []
        self.distinguished_partitions: list[BswDistinguishedPartition] = []
        self._entities: list[BswModuleEntity] = []
        self.events: list[BswEvent] = []
        self._exclusive_area_policies: list[BswExclusiveAreaPolicy] = []
        self.included_data_type_sets: list[IncludedDataTypeSet] = []
        self.included_mode_declaration_group_sets: list[IncludedModeDeclarationGroupSet] = []
        self.internal_triggering_points: list[BswInternalTriggeringPoint] = []
        self._internal_triggering_point_policies: list[BswInternalTriggeringPointPolicy] = []
        self._mode_receiver_policies: list[BswModeReceiverPolicy] = []
        self._mode_sender_policies: list[BswModeSenderPolicy] = []
        self._parameter_policies: list[BswParameterPolicy] = []
        self.per_instance_parameters: list[ParameterDataPrototype] = []
        self._reception_policies: list[BswDataReceptionPolicy] = []
        self._released_trigger_policies: list[BswReleasedTriggerPolicy] = []
        self.scheduler_name_prefixs: list[BswSchedulerNamePrefix] = []
        self._send_policies: list[BswDataSendPolicy] = []
        self._service_dependencies: list[BswServiceDependency] = []
        self.trigger_direct_implementations: list[BswTriggerDirectImplementation] = []
        self._variation_point_proxies: list[VariationPointProxy] = []
    @property
    @xml_element_name("AR-TYPED-PER-INSTANCE-MEMORYS")
    def ar_typed_per_instance_memories(self) -> list[VariableDataPrototype]:
        """Get ar_typed_per_instance_memories with custom XML element name."""
        return self._ar_typed_per_instance_memories

    @ar_typed_per_instance_memories.setter
    def ar_typed_per_instance_memories(self, value: list[VariableDataPrototype]) -> None:
        """Set ar_typed_per_instance_memories with custom XML element name."""
        self._ar_typed_per_instance_memories = value

    @property
    @xml_element_name("BSW-PER-INSTANCE-MEMORY-POLICYS")
    def bsw_per_instance_memory_policies(self) -> list[BswPerInstanceMemoryPolicy]:
        """Get bsw_per_instance_memory_policies with custom XML element name."""
        return self._bsw_per_instance_memory_policies

    @bsw_per_instance_memory_policies.setter
    def bsw_per_instance_memory_policies(self, value: list[BswPerInstanceMemoryPolicy]) -> None:
        """Set bsw_per_instance_memory_policies with custom XML element name."""
        self._bsw_per_instance_memory_policies = value

    @property
    @xml_element_name("CLIENT-POLICYS")
    def client_policies(self) -> list[BswClientPolicy]:
        """Get client_policies with custom XML element name."""
        return self._client_policies

    @client_policies.setter
    def client_policies(self, value: list[BswClientPolicy]) -> None:
        """Set client_policies with custom XML element name."""
        self._client_policies = value

    @property
    @xml_element_name("ENTITYS")
    def entities(self) -> list[BswModuleEntity]:
        """Get entities with custom XML element name."""
        return self._entities

    @entities.setter
    def entities(self, value: list[BswModuleEntity]) -> None:
        """Set entities with custom XML element name."""
        self._entities = value

    @property
    @xml_element_name("EXCLUSIVE-AREA-POLICYS")
    def exclusive_area_policies(self) -> list[BswExclusiveAreaPolicy]:
        """Get exclusive_area_policies with custom XML element name."""
        return self._exclusive_area_policies

    @exclusive_area_policies.setter
    def exclusive_area_policies(self, value: list[BswExclusiveAreaPolicy]) -> None:
        """Set exclusive_area_policies with custom XML element name."""
        self._exclusive_area_policies = value

    @property
    @xml_element_name("INTERNAL-TRIGGERING-POINT-POLICYS")
    def internal_triggering_point_policies(self) -> list[BswInternalTriggeringPointPolicy]:
        """Get internal_triggering_point_policies with custom XML element name."""
        return self._internal_triggering_point_policies

    @internal_triggering_point_policies.setter
    def internal_triggering_point_policies(self, value: list[BswInternalTriggeringPointPolicy]) -> None:
        """Set internal_triggering_point_policies with custom XML element name."""
        self._internal_triggering_point_policies = value

    @property
    @xml_element_name("MODE-RECEIVER-POLICYS")
    def mode_receiver_policies(self) -> list[BswModeReceiverPolicy]:
        """Get mode_receiver_policies with custom XML element name."""
        return self._mode_receiver_policies

    @mode_receiver_policies.setter
    def mode_receiver_policies(self, value: list[BswModeReceiverPolicy]) -> None:
        """Set mode_receiver_policies with custom XML element name."""
        self._mode_receiver_policies = value

    @property
    @xml_element_name("MODE-SENDER-POLICYS")
    def mode_sender_policies(self) -> list[BswModeSenderPolicy]:
        """Get mode_sender_policies with custom XML element name."""
        return self._mode_sender_policies

    @mode_sender_policies.setter
    def mode_sender_policies(self, value: list[BswModeSenderPolicy]) -> None:
        """Set mode_sender_policies with custom XML element name."""
        self._mode_sender_policies = value

    @property
    @xml_element_name("PARAMETER-POLICYS")
    def parameter_policies(self) -> list[BswParameterPolicy]:
        """Get parameter_policies with custom XML element name."""
        return self._parameter_policies

    @parameter_policies.setter
    def parameter_policies(self, value: list[BswParameterPolicy]) -> None:
        """Set parameter_policies with custom XML element name."""
        self._parameter_policies = value

    @property
    @xml_element_name("RECEPTION-POLICYS")
    def reception_policies(self) -> list[BswDataReceptionPolicy]:
        """Get reception_policies with custom XML element name."""
        return self._reception_policies

    @reception_policies.setter
    def reception_policies(self, value: list[BswDataReceptionPolicy]) -> None:
        """Set reception_policies with custom XML element name."""
        self._reception_policies = value

    @property
    @xml_element_name("RELEASED-TRIGGER-POLICYS")
    def released_trigger_policies(self) -> list[BswReleasedTriggerPolicy]:
        """Get released_trigger_policies with custom XML element name."""
        return self._released_trigger_policies

    @released_trigger_policies.setter
    def released_trigger_policies(self, value: list[BswReleasedTriggerPolicy]) -> None:
        """Set released_trigger_policies with custom XML element name."""
        self._released_trigger_policies = value

    @property
    @xml_element_name("SEND-POLICYS")
    def send_policies(self) -> list[BswDataSendPolicy]:
        """Get send_policies with custom XML element name."""
        return self._send_policies

    @send_policies.setter
    def send_policies(self, value: list[BswDataSendPolicy]) -> None:
        """Set send_policies with custom XML element name."""
        self._send_policies = value

    @property
    @xml_element_name("SERVICE-DEPENDENCYS")
    def service_dependencies(self) -> list[BswServiceDependency]:
        """Get service_dependencies with custom XML element name."""
        return self._service_dependencies

    @service_dependencies.setter
    def service_dependencies(self, value: list[BswServiceDependency]) -> None:
        """Set service_dependencies with custom XML element name."""
        self._service_dependencies = value

    @property
    @xml_element_name("VARIATION-POINT-PROXYS")
    def variation_point_proxies(self) -> list[VariationPointProxy]:
        """Get variation_point_proxies with custom XML element name."""
        return self._variation_point_proxies

    @variation_point_proxies.setter
    def variation_point_proxies(self, value: list[VariationPointProxy]) -> None:
        """Set variation_point_proxies with custom XML element name."""
        self._variation_point_proxies = value


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

        # Serialize ar_typed_per_instance_memories (list to container "AR-TYPED-PER-INSTANCE-MEMORYS")
        if self.ar_typed_per_instance_memories:
            wrapper = ET.Element("AR-TYPED-PER-INSTANCE-MEMORYS")
            for item in self.ar_typed_per_instance_memories:
                serialized = SerializationHelper.serialize_item(item, "VariableDataPrototype")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize bsw_per_instance_memory_policies (list to container "BSW-PER-INSTANCE-MEMORY-POLICYS")
        if self.bsw_per_instance_memory_policies:
            wrapper = ET.Element("BSW-PER-INSTANCE-MEMORY-POLICYS")
            for item in self.bsw_per_instance_memory_policies:
                serialized = SerializationHelper.serialize_item(item, "BswPerInstanceMemoryPolicy")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize client_policies (list to container "CLIENT-POLICYS")
        if self.client_policies:
            wrapper = ET.Element("CLIENT-POLICYS")
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

        # Serialize exclusive_area_policies (list to container "EXCLUSIVE-AREA-POLICYS")
        if self.exclusive_area_policies:
            wrapper = ET.Element("EXCLUSIVE-AREA-POLICYS")
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

        # Serialize internal_triggering_point_policies (list to container "INTERNAL-TRIGGERING-POINT-POLICYS")
        if self.internal_triggering_point_policies:
            wrapper = ET.Element("INTERNAL-TRIGGERING-POINT-POLICYS")
            for item in self.internal_triggering_point_policies:
                serialized = SerializationHelper.serialize_item(item, "BswInternalTriggeringPointPolicy")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize mode_receiver_policies (list to container "MODE-RECEIVER-POLICYS")
        if self.mode_receiver_policies:
            wrapper = ET.Element("MODE-RECEIVER-POLICYS")
            for item in self.mode_receiver_policies:
                serialized = SerializationHelper.serialize_item(item, "BswModeReceiverPolicy")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize mode_sender_policies (list to container "MODE-SENDER-POLICYS")
        if self.mode_sender_policies:
            wrapper = ET.Element("MODE-SENDER-POLICYS")
            for item in self.mode_sender_policies:
                serialized = SerializationHelper.serialize_item(item, "BswModeSenderPolicy")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize parameter_policies (list to container "PARAMETER-POLICYS")
        if self.parameter_policies:
            wrapper = ET.Element("PARAMETER-POLICYS")
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

        # Serialize reception_policies (list to container "RECEPTION-POLICYS")
        if self.reception_policies:
            wrapper = ET.Element("RECEPTION-POLICYS")
            for item in self.reception_policies:
                serialized = SerializationHelper.serialize_item(item, "BswDataReceptionPolicy")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize released_trigger_policies (list to container "RELEASED-TRIGGER-POLICYS")
        if self.released_trigger_policies:
            wrapper = ET.Element("RELEASED-TRIGGER-POLICYS")
            for item in self.released_trigger_policies:
                serialized = SerializationHelper.serialize_item(item, "BswReleasedTriggerPolicy")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize scheduler_name_prefixs (list to container "SCHEDULER-NAME-PREFIXS")
        if self.scheduler_name_prefixs:
            wrapper = ET.Element("SCHEDULER-NAME-PREFIXS")
            for item in self.scheduler_name_prefixs:
                serialized = SerializationHelper.serialize_item(item, "BswSchedulerNamePrefix")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize send_policies (list to container "SEND-POLICYS")
        if self.send_policies:
            wrapper = ET.Element("SEND-POLICYS")
            for item in self.send_policies:
                serialized = SerializationHelper.serialize_item(item, "BswDataSendPolicy")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize service_dependencies (list to container "SERVICE-DEPENDENCYS")
        if self.service_dependencies:
            wrapper = ET.Element("SERVICE-DEPENDENCYS")
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

        # Serialize variation_point_proxies (list to container "VARIATION-POINT-PROXYS")
        if self.variation_point_proxies:
            wrapper = ET.Element("VARIATION-POINT-PROXYS")
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

        # Parse ar_typed_per_instance_memories (list from container "AR-TYPED-PER-INSTANCE-MEMORYS")
        obj.ar_typed_per_instance_memories = []
        container = SerializationHelper.find_child_element(element, "AR-TYPED-PER-INSTANCE-MEMORYS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.ar_typed_per_instance_memories.append(child_value)

        # Parse bsw_per_instance_memory_policies (list from container "BSW-PER-INSTANCE-MEMORY-POLICYS")
        obj.bsw_per_instance_memory_policies = []
        container = SerializationHelper.find_child_element(element, "BSW-PER-INSTANCE-MEMORY-POLICYS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.bsw_per_instance_memory_policies.append(child_value)

        # Parse client_policies (list from container "CLIENT-POLICYS")
        obj.client_policies = []
        container = SerializationHelper.find_child_element(element, "CLIENT-POLICYS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.client_policies.append(child_value)

        # Parse distinguished_partitions (list from container "DISTINGUISHED-PARTITIONS")
        obj.distinguished_partitions = []
        container = SerializationHelper.find_child_element(element, "DISTINGUISHED-PARTITIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.distinguished_partitions.append(child_value)

        # Parse entities (list from container "ENTITYS")
        obj.entities = []
        container = SerializationHelper.find_child_element(element, "ENTITYS")
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

        # Parse exclusive_area_policies (list from container "EXCLUSIVE-AREA-POLICYS")
        obj.exclusive_area_policies = []
        container = SerializationHelper.find_child_element(element, "EXCLUSIVE-AREA-POLICYS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.exclusive_area_policies.append(child_value)

        # Parse included_data_type_sets (list from container "INCLUDED-DATA-TYPE-SETS")
        obj.included_data_type_sets = []
        container = SerializationHelper.find_child_element(element, "INCLUDED-DATA-TYPE-SETS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.included_data_type_sets.append(child_value)

        # Parse included_mode_declaration_group_sets (list from container "INCLUDED-MODE-DECLARATION-GROUP-SETS")
        obj.included_mode_declaration_group_sets = []
        container = SerializationHelper.find_child_element(element, "INCLUDED-MODE-DECLARATION-GROUP-SETS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.included_mode_declaration_group_sets.append(child_value)

        # Parse internal_triggering_points (list from container "INTERNAL-TRIGGERING-POINTS")
        obj.internal_triggering_points = []
        container = SerializationHelper.find_child_element(element, "INTERNAL-TRIGGERING-POINTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.internal_triggering_points.append(child_value)

        # Parse internal_triggering_point_policies (list from container "INTERNAL-TRIGGERING-POINT-POLICYS")
        obj.internal_triggering_point_policies = []
        container = SerializationHelper.find_child_element(element, "INTERNAL-TRIGGERING-POINT-POLICYS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.internal_triggering_point_policies.append(child_value)

        # Parse mode_receiver_policies (list from container "MODE-RECEIVER-POLICYS")
        obj.mode_receiver_policies = []
        container = SerializationHelper.find_child_element(element, "MODE-RECEIVER-POLICYS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.mode_receiver_policies.append(child_value)

        # Parse mode_sender_policies (list from container "MODE-SENDER-POLICYS")
        obj.mode_sender_policies = []
        container = SerializationHelper.find_child_element(element, "MODE-SENDER-POLICYS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.mode_sender_policies.append(child_value)

        # Parse parameter_policies (list from container "PARAMETER-POLICYS")
        obj.parameter_policies = []
        container = SerializationHelper.find_child_element(element, "PARAMETER-POLICYS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.parameter_policies.append(child_value)

        # Parse per_instance_parameters (list from container "PER-INSTANCE-PARAMETERS")
        obj.per_instance_parameters = []
        container = SerializationHelper.find_child_element(element, "PER-INSTANCE-PARAMETERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.per_instance_parameters.append(child_value)

        # Parse reception_policies (list from container "RECEPTION-POLICYS")
        obj.reception_policies = []
        container = SerializationHelper.find_child_element(element, "RECEPTION-POLICYS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.reception_policies.append(child_value)

        # Parse released_trigger_policies (list from container "RELEASED-TRIGGER-POLICYS")
        obj.released_trigger_policies = []
        container = SerializationHelper.find_child_element(element, "RELEASED-TRIGGER-POLICYS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.released_trigger_policies.append(child_value)

        # Parse scheduler_name_prefixs (list from container "SCHEDULER-NAME-PREFIXS")
        obj.scheduler_name_prefixs = []
        container = SerializationHelper.find_child_element(element, "SCHEDULER-NAME-PREFIXS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.scheduler_name_prefixs.append(child_value)

        # Parse send_policies (list from container "SEND-POLICYS")
        obj.send_policies = []
        container = SerializationHelper.find_child_element(element, "SEND-POLICYS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.send_policies.append(child_value)

        # Parse service_dependencies (list from container "SERVICE-DEPENDENCYS")
        obj.service_dependencies = []
        container = SerializationHelper.find_child_element(element, "SERVICE-DEPENDENCYS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.service_dependencies.append(child_value)

        # Parse trigger_direct_implementations (list from container "TRIGGER-DIRECT-IMPLEMENTATIONS")
        obj.trigger_direct_implementations = []
        container = SerializationHelper.find_child_element(element, "TRIGGER-DIRECT-IMPLEMENTATIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.trigger_direct_implementations.append(child_value)

        # Parse variation_point_proxies (list from container "VARIATION-POINT-PROXYS")
        obj.variation_point_proxies = []
        container = SerializationHelper.find_child_element(element, "VARIATION-POINT-PROXYS")
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

    def with_constant_memoris(self, items: list[ParameterDataPrototype]) -> "BswInternalBehaviorBuilder":
        """Set constant_memoris list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.constant_memoris = list(items) if items else []
        return self

    def with_constant_value_mappings(self, items: list[ConstantSpecificationMappingSet]) -> "BswInternalBehaviorBuilder":
        """Set constant_value_mappings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.constant_value_mappings = list(items) if items else []
        return self

    def with_data_type_mappings(self, items: list[DataTypeMappingSet]) -> "BswInternalBehaviorBuilder":
        """Set data_type_mappings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.data_type_mappings = list(items) if items else []
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

    def with_exclusive_area_nesting_orders(self, items: list[ExclusiveAreaNestingOrder]) -> "BswInternalBehaviorBuilder":
        """Set exclusive_area_nesting_orders list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.exclusive_area_nesting_orders = list(items) if items else []
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

    def with_scheduler_name_prefixs(self, items: list[BswSchedulerNamePrefix]) -> "BswInternalBehaviorBuilder":
        """Set scheduler_name_prefixs list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.scheduler_name_prefixs = list(items) if items else []
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

    def add_constant_memori(self, item: ParameterDataPrototype) -> "BswInternalBehaviorBuilder":
        """Add a single item to constant_memoris list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.constant_memoris.append(item)
        return self

    def clear_constant_memoris(self) -> "BswInternalBehaviorBuilder":
        """Clear all items from constant_memoris list.

        Returns:
            self for method chaining
        """
        self._obj.constant_memoris = []
        return self

    def add_constant_value_mapping(self, item: ConstantSpecificationMappingSet) -> "BswInternalBehaviorBuilder":
        """Add a single item to constant_value_mappings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.constant_value_mappings.append(item)
        return self

    def clear_constant_value_mappings(self) -> "BswInternalBehaviorBuilder":
        """Clear all items from constant_value_mappings list.

        Returns:
            self for method chaining
        """
        self._obj.constant_value_mappings = []
        return self

    def add_data_type_mapping(self, item: DataTypeMappingSet) -> "BswInternalBehaviorBuilder":
        """Add a single item to data_type_mappings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.data_type_mappings.append(item)
        return self

    def clear_data_type_mappings(self) -> "BswInternalBehaviorBuilder":
        """Clear all items from data_type_mappings list.

        Returns:
            self for method chaining
        """
        self._obj.data_type_mappings = []
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

    def add_exclusive_area_nesting_order(self, item: ExclusiveAreaNestingOrder) -> "BswInternalBehaviorBuilder":
        """Add a single item to exclusive_area_nesting_orders list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.exclusive_area_nesting_orders.append(item)
        return self

    def clear_exclusive_area_nesting_orders(self) -> "BswInternalBehaviorBuilder":
        """Clear all items from exclusive_area_nesting_orders list.

        Returns:
            self for method chaining
        """
        self._obj.exclusive_area_nesting_orders = []
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

    def add_exclusive_area_policie(self, item: BswExclusiveAreaPolicy) -> "BswInternalBehaviorBuilder":
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

    def add_internal_triggering_point_policie(self, item: BswInternalTriggeringPointPolicy) -> "BswInternalBehaviorBuilder":
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

    def add_mode_receiver_policie(self, item: BswModeReceiverPolicy) -> "BswInternalBehaviorBuilder":
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

    def add_mode_sender_policie(self, item: BswModeSenderPolicy) -> "BswInternalBehaviorBuilder":
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

    def add_parameter_policie(self, item: BswParameterPolicy) -> "BswInternalBehaviorBuilder":
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

    def add_released_trigger_policie(self, item: BswReleasedTriggerPolicy) -> "BswInternalBehaviorBuilder":
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
        """Add a single item to scheduler_name_prefixs list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.scheduler_name_prefixs.append(item)
        return self

    def clear_scheduler_name_prefixs(self) -> "BswInternalBehaviorBuilder":
        """Clear all items from scheduler_name_prefixs list.

        Returns:
            self for method chaining
        """
        self._obj.scheduler_name_prefixs = []
        return self

    def add_send_policie(self, item: BswDataSendPolicy) -> "BswInternalBehaviorBuilder":
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

    def add_service_dependencie(self, item: BswServiceDependency) -> "BswInternalBehaviorBuilder":
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