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
    released_trigger_refs: list[ARRef]
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
        self.released_trigger_refs: list[ARRef] = []
        self.scheduler_names: list[BswSchedulerNamePrefix] = []
        self.send_policies: list[Any] = []
        self.services: list[Any] = []
        self.trigger_direct_refs: list[ARRef] = []
        self.variation_point_proxies: list[VariationPointProxy] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswInternalBehavior":
        """Deserialize XML element to BswInternalBehavior object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswInternalBehavior object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse ar_typed_per_instance_memorie_refs (list)
        obj.ar_typed_per_instance_memorie_refs = []
        for child in ARObject._find_all_child_elements(element, "AR-TYPED-PER-INSTANCE-MEMORIES"):
            ar_typed_per_instance_memorie_refs_value = ARObject._deserialize_by_tag(child, "VariableDataPrototype")
            obj.ar_typed_per_instance_memorie_refs.append(ar_typed_per_instance_memorie_refs_value)

        # Parse bsw_per_instance_memory_policies (list)
        obj.bsw_per_instance_memory_policies = []
        for child in ARObject._find_all_child_elements(element, "BSW-PER-INSTANCE-MEMORY-POLICIES"):
            bsw_per_instance_memory_policies_value = ARObject._deserialize_by_tag(child, "BswPerInstanceMemoryPolicy")
            obj.bsw_per_instance_memory_policies.append(bsw_per_instance_memory_policies_value)

        # Parse client_policies (list)
        obj.client_policies = []
        for child in ARObject._find_all_child_elements(element, "CLIENT-POLICIES"):
            client_policies_value = ARObject._deserialize_by_tag(child, "BswClientPolicy")
            obj.client_policies.append(client_policies_value)

        # Parse distinguisheds (list)
        obj.distinguisheds = []
        for child in ARObject._find_all_child_elements(element, "DISTINGUISHEDS"):
            distinguisheds_value = ARObject._deserialize_by_tag(child, "BswDistinguishedPartition")
            obj.distinguisheds.append(distinguisheds_value)

        # Parse entities (list)
        obj.entities = []
        for child in ARObject._find_all_child_elements(element, "ENTITIES"):
            entities_value = ARObject._deserialize_by_tag(child, "BswModuleEntity")
            obj.entities.append(entities_value)

        # Parse events (list)
        obj.events = []
        for child in ARObject._find_all_child_elements(element, "EVENTS"):
            events_value = ARObject._deserialize_by_tag(child, "BswEvent")
            obj.events.append(events_value)

        # Parse exclusive_areas (list)
        obj.exclusive_areas = []
        for child in ARObject._find_all_child_elements(element, "EXCLUSIVE-AREAS"):
            exclusive_areas_value = ARObject._deserialize_by_tag(child, "BswExclusiveAreaPolicy")
            obj.exclusive_areas.append(exclusive_areas_value)

        # Parse included_data_type_set_refs (list)
        obj.included_data_type_set_refs = []
        for child in ARObject._find_all_child_elements(element, "INCLUDED-DATA-TYPE-SETS"):
            included_data_type_set_refs_value = ARObject._deserialize_by_tag(child, "IncludedDataTypeSet")
            obj.included_data_type_set_refs.append(included_data_type_set_refs_value)

        # Parse included_modes (list)
        obj.included_modes = []
        for child in ARObject._find_all_child_elements(element, "INCLUDED-MODES"):
            included_modes_value = ARObject._deserialize_by_tag(child, "IncludedModeDeclarationGroupSet")
            obj.included_modes.append(included_modes_value)

        # Parse internal_refs (list)
        obj.internal_refs = []
        for child in ARObject._find_all_child_elements(element, "INTERNALS"):
            internal_refs_value = ARObject._deserialize_by_tag(child, "BswInternalTriggeringPoint")
            obj.internal_refs.append(internal_refs_value)

        # Parse mode_receivers (list)
        obj.mode_receivers = []
        for child in ARObject._find_all_child_elements(element, "MODE-RECEIVERS"):
            mode_receivers_value = ARObject._deserialize_by_tag(child, "BswModeReceiverPolicy")
            obj.mode_receivers.append(mode_receivers_value)

        # Parse mode_senders (list)
        obj.mode_senders = []
        for child in ARObject._find_all_child_elements(element, "MODE-SENDERS"):
            mode_senders_value = ARObject._deserialize_by_tag(child, "BswModeSenderPolicy")
            obj.mode_senders.append(mode_senders_value)

        # Parse parameter_policies (list)
        obj.parameter_policies = []
        for child in ARObject._find_all_child_elements(element, "PARAMETER-POLICIES"):
            parameter_policies_value = child.text
            obj.parameter_policies.append(parameter_policies_value)

        # Parse per_instances (list)
        obj.per_instances = []
        for child in ARObject._find_all_child_elements(element, "PER-INSTANCES"):
            per_instances_value = ARObject._deserialize_by_tag(child, "ParameterDataPrototype")
            obj.per_instances.append(per_instances_value)

        # Parse reception_policies (list)
        obj.reception_policies = []
        for child in ARObject._find_all_child_elements(element, "RECEPTION-POLICIES"):
            reception_policies_value = ARObject._deserialize_by_tag(child, "BswDataReceptionPolicy")
            obj.reception_policies.append(reception_policies_value)

        # Parse released_trigger_refs (list)
        obj.released_trigger_refs = []
        for child in ARObject._find_all_child_elements(element, "RELEASED-TRIGGERS"):
            released_trigger_refs_value = child.text
            obj.released_trigger_refs.append(released_trigger_refs_value)

        # Parse scheduler_names (list)
        obj.scheduler_names = []
        for child in ARObject._find_all_child_elements(element, "SCHEDULER-NAMES"):
            scheduler_names_value = ARObject._deserialize_by_tag(child, "BswSchedulerNamePrefix")
            obj.scheduler_names.append(scheduler_names_value)

        # Parse send_policies (list)
        obj.send_policies = []
        for child in ARObject._find_all_child_elements(element, "SEND-POLICIES"):
            send_policies_value = child.text
            obj.send_policies.append(send_policies_value)

        # Parse services (list)
        obj.services = []
        for child in ARObject._find_all_child_elements(element, "SERVICES"):
            services_value = child.text
            obj.services.append(services_value)

        # Parse trigger_direct_refs (list)
        obj.trigger_direct_refs = []
        for child in ARObject._find_all_child_elements(element, "TRIGGER-DIRECTS"):
            trigger_direct_refs_value = ARObject._deserialize_by_tag(child, "BswTriggerDirectImplementation")
            obj.trigger_direct_refs.append(trigger_direct_refs_value)

        # Parse variation_point_proxies (list)
        obj.variation_point_proxies = []
        for child in ARObject._find_all_child_elements(element, "VARIATION-POINT-PROXIES"):
            variation_point_proxies_value = ARObject._deserialize_by_tag(child, "VariationPointProxy")
            obj.variation_point_proxies.append(variation_point_proxies_value)

        return obj



class BswInternalBehaviorBuilder:
    """Builder for BswInternalBehavior."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswInternalBehavior = BswInternalBehavior()

    def build(self) -> BswInternalBehavior:
        """Build and return BswInternalBehavior object.

        Returns:
            BswInternalBehavior instance
        """
        # TODO: Add validation
        return self._obj
