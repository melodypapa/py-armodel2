"""BswInternalBehavior AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.internal_behavior import (
    InternalBehavior,
)
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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("ar_typed_pers", None, False, True, VariableDataPrototype),  # arTypedPers
        ("bsw_per_instances", None, False, True, any (BswPerInstance)),  # bswPerInstances
        ("client_policies", None, False, True, any (BswClientPolicy)),  # clientPolicies
        ("distinguisheds", None, False, True, BswDistinguishedPartition),  # distinguisheds
        ("entities", None, False, True, BswModuleEntity),  # entities
        ("events", None, False, True, BswEvent),  # events
        ("exclusive_areas", None, False, True, BswExclusiveAreaPolicy),  # exclusiveAreas
        ("included_data_type_sets", None, False, True, IncludedDataTypeSet),  # includedDataTypeSets
        ("included_modes", None, False, True, IncludedModeDeclarationGroupSet),  # includedModes
        ("internals", None, False, True, BswInternalTriggeringPoint),  # internals
        ("mode_receivers", None, False, True, BswModeReceiverPolicy),  # modeReceivers
        ("mode_senders", None, False, True, BswModeSenderPolicy),  # modeSenders
        ("parameter_policies", None, False, True, any (BswParameterPolicy)),  # parameterPolicies
        ("per_instances", None, False, True, ParameterDataPrototype),  # perInstances
        ("reception_policies", None, False, True, BswDataReceptionPolicy),  # receptionPolicies
        ("released_triggers", None, False, True, any (BswReleasedTrigger)),  # releasedTriggers
        ("scheduler_names", None, False, True, BswSchedulerNamePrefix),  # schedulerNames
        ("send_policies", None, False, True, any (BswDataSendPolicy)),  # sendPolicies
        ("services", None, False, True, any (BswService)),  # services
        ("trigger_directs", None, False, True, BswTriggerDirectImplementation),  # triggerDirects
        ("variation_point_proxies", None, False, True, VariationPointProxy),  # variationPointProxies
    ]

    def __init__(self) -> None:
        """Initialize BswInternalBehavior."""
        super().__init__()
        self.ar_typed_pers: list[VariableDataPrototype] = []
        self.bsw_per_instances: list[Any] = []
        self.client_policies: list[Any] = []
        self.distinguisheds: list[BswDistinguishedPartition] = []
        self.entities: list[BswModuleEntity] = []
        self.events: list[BswEvent] = []
        self.exclusive_areas: list[BswExclusiveAreaPolicy] = []
        self.included_data_type_sets: list[IncludedDataTypeSet] = []
        self.included_modes: list[IncludedModeDeclarationGroupSet] = []
        self.internals: list[BswInternalTriggeringPoint] = []
        self.mode_receivers: list[BswModeReceiverPolicy] = []
        self.mode_senders: list[BswModeSenderPolicy] = []
        self.parameter_policies: list[Any] = []
        self.per_instances: list[ParameterDataPrototype] = []
        self.reception_policies: list[BswDataReceptionPolicy] = []
        self.released_triggers: list[Any] = []
        self.scheduler_names: list[BswSchedulerNamePrefix] = []
        self.send_policies: list[Any] = []
        self.services: list[Any] = []
        self.trigger_directs: list[BswTriggerDirectImplementation] = []
        self.variation_point_proxies: list[VariationPointProxy] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BswInternalBehavior to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswInternalBehavior":
        """Create BswInternalBehavior from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BswInternalBehavior instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BswInternalBehavior since parent returns ARObject
        return cast("BswInternalBehavior", obj)


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
