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
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BswInternalBehavior, cls).deserialize(element)

        # Parse ar_typed_per_instance_memorie_refs (list from container "AR-TYPED-PER-INSTANCE-MEMORIES")
        obj.ar_typed_per_instance_memorie_refs = []
        container = ARObject._find_child_element(element, "AR-TYPED-PER-INSTANCE-MEMORIES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.ar_typed_per_instance_memorie_refs.append(child_value)

        # Parse bsw_per_instance_memory_policies (list from container "BSW-PER-INSTANCE-MEMORY-POLICIES")
        obj.bsw_per_instance_memory_policies = []
        container = ARObject._find_child_element(element, "BSW-PER-INSTANCE-MEMORY-POLICIES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.bsw_per_instance_memory_policies.append(child_value)

        # Parse client_policies (list from container "CLIENT-POLICIES")
        obj.client_policies = []
        container = ARObject._find_child_element(element, "CLIENT-POLICIES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.client_policies.append(child_value)

        # Parse distinguisheds (list from container "DISTINGUISHEDS")
        obj.distinguisheds = []
        container = ARObject._find_child_element(element, "DISTINGUISHEDS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.distinguisheds.append(child_value)

        # Parse entities (list from container "ENTITIES")
        obj.entities = []
        container = ARObject._find_child_element(element, "ENTITIES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.entities.append(child_value)

        # Parse events (list from container "EVENTS")
        obj.events = []
        container = ARObject._find_child_element(element, "EVENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.events.append(child_value)

        # Parse exclusive_areas (list from container "EXCLUSIVE-AREAS")
        obj.exclusive_areas = []
        container = ARObject._find_child_element(element, "EXCLUSIVE-AREAS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.exclusive_areas.append(child_value)

        # Parse included_data_type_set_refs (list from container "INCLUDED-DATA-TYPE-SETS")
        obj.included_data_type_set_refs = []
        container = ARObject._find_child_element(element, "INCLUDED-DATA-TYPE-SETS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.included_data_type_set_refs.append(child_value)

        # Parse included_modes (list from container "INCLUDED-MODES")
        obj.included_modes = []
        container = ARObject._find_child_element(element, "INCLUDED-MODES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.included_modes.append(child_value)

        # Parse internal_refs (list from container "INTERNALS")
        obj.internal_refs = []
        container = ARObject._find_child_element(element, "INTERNALS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.internal_refs.append(child_value)

        # Parse mode_receivers (list from container "MODE-RECEIVERS")
        obj.mode_receivers = []
        container = ARObject._find_child_element(element, "MODE-RECEIVERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.mode_receivers.append(child_value)

        # Parse mode_senders (list from container "MODE-SENDERS")
        obj.mode_senders = []
        container = ARObject._find_child_element(element, "MODE-SENDERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.mode_senders.append(child_value)

        # Parse parameter_policies (list from container "PARAMETER-POLICIES")
        obj.parameter_policies = []
        container = ARObject._find_child_element(element, "PARAMETER-POLICIES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.parameter_policies.append(child_value)

        # Parse per_instances (list from container "PER-INSTANCES")
        obj.per_instances = []
        container = ARObject._find_child_element(element, "PER-INSTANCES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.per_instances.append(child_value)

        # Parse reception_policies (list from container "RECEPTION-POLICIES")
        obj.reception_policies = []
        container = ARObject._find_child_element(element, "RECEPTION-POLICIES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.reception_policies.append(child_value)

        # Parse released_trigger_refs (list from container "RELEASED-TRIGGERS")
        obj.released_trigger_refs = []
        container = ARObject._find_child_element(element, "RELEASED-TRIGGERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.released_trigger_refs.append(child_value)

        # Parse scheduler_names (list from container "SCHEDULER-NAMES")
        obj.scheduler_names = []
        container = ARObject._find_child_element(element, "SCHEDULER-NAMES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.scheduler_names.append(child_value)

        # Parse send_policies (list from container "SEND-POLICIES")
        obj.send_policies = []
        container = ARObject._find_child_element(element, "SEND-POLICIES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.send_policies.append(child_value)

        # Parse services (list from container "SERVICES")
        obj.services = []
        container = ARObject._find_child_element(element, "SERVICES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.services.append(child_value)

        # Parse trigger_direct_refs (list from container "TRIGGER-DIRECTS")
        obj.trigger_direct_refs = []
        container = ARObject._find_child_element(element, "TRIGGER-DIRECTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.trigger_direct_refs.append(child_value)

        # Parse variation_point_proxies (list from container "VARIATION-POINT-PROXIES")
        obj.variation_point_proxies = []
        container = ARObject._find_child_element(element, "VARIATION-POINT-PROXIES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.variation_point_proxies.append(child_value)

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
