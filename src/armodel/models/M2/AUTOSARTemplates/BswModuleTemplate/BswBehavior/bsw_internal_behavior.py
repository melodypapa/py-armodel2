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
from armodel.serialization import XMLMember

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
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "ar_typed_pers": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=VariableDataPrototype,
        ),  # arTypedPers
        "bsw_per_instances": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=Any,
        ),  # bswPerInstances
        "client_policies": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=Any,
        ),  # clientPolicies
        "distinguisheds": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=BswDistinguishedPartition,
        ),  # distinguisheds
        "entities": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=BswModuleEntity,
        ),  # entities
        "events": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=BswEvent,
        ),  # events
        "exclusive_areas": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=BswExclusiveAreaPolicy,
        ),  # exclusiveAreas
        "included_data_type_sets": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=IncludedDataTypeSet,
        ),  # includedDataTypeSets
        "included_modes": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=IncludedModeDeclarationGroupSet,
        ),  # includedModes
        "internals": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=BswInternalTriggeringPoint,
        ),  # internals
        "mode_receivers": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=BswModeReceiverPolicy,
        ),  # modeReceivers
        "mode_senders": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=BswModeSenderPolicy,
        ),  # modeSenders
        "parameter_policies": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=Any,
        ),  # parameterPolicies
        "per_instances": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=ParameterDataPrototype,
        ),  # perInstances
        "reception_policies": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=BswDataReceptionPolicy,
        ),  # receptionPolicies
        "released_triggers": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=Any,
        ),  # releasedTriggers
        "scheduler_names": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=BswSchedulerNamePrefix,
        ),  # schedulerNames
        "send_policies": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=Any,
        ),  # sendPolicies
        "services": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=Any,
        ),  # services
        "trigger_directs": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=BswTriggerDirectImplementation,
        ),  # triggerDirects
        "variation_point_proxies": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=VariationPointProxy,
        ),  # variationPointProxies
    }

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
