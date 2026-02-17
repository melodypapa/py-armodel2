"""SwcInternalBehavior AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 345)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 518)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2070)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 246)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 472)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 217)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.internal_behavior import (
    InternalBehavior,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.IncludedDataTypes.included_data_type_set import (
    IncludedDataTypeSet,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ModeDeclarationGroup.included_mode_declaration_group_set import (
    IncludedModeDeclarationGroupSet,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.InstantiationDataDefProps.instantiation_data_def_props import (
    InstantiationDataDefProps,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.parameter_data_prototype import (
    ParameterDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PerInstanceMemory.per_instance_memory import (
    PerInstanceMemory,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PortAPIOptions.port_api_option import (
    PortAPIOption,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import (
    RTEEvent,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.runnable_entity import (
    RunnableEntity,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.swc_exclusive_area_policy import (
    SwcExclusiveAreaPolicy,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.VariantHandling.variation_point_proxy import (
    VariationPointProxy,
)


class SwcInternalBehavior(InternalBehavior):
    """AUTOSAR SwcInternalBehavior."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "ar_typed_pers": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=VariableDataPrototype,
        ),  # arTypedPers
        "events": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=RTEEvent,
        ),  # events
        "exclusive_areas": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=SwcExclusiveAreaPolicy,
        ),  # exclusiveAreas
        "explicit_inters": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=VariableDataPrototype,
        ),  # explicitInters
        "implicit_inters": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=VariableDataPrototype,
        ),  # implicitInters
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
        "instantiation_data_defs": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=InstantiationDataDefProps,
        ),  # instantiationDataDefs
        "per_instance_memories": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=PerInstanceMemory,
        ),  # perInstanceMemories
        "per_instances": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=ParameterDataPrototype,
        ),  # perInstances
        "port_api_options": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=PortAPIOption,
        ),  # portAPIOptions
        "runnables": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=RunnableEntity,
        ),  # runnables
        "services": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=any (SwcService),
        ),  # services
        "shareds": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=ParameterDataPrototype,
        ),  # shareds
        "supports": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # supports
        "variation_point_proxies": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=VariationPointProxy,
        ),  # variationPointProxies
    }

    def __init__(self) -> None:
        """Initialize SwcInternalBehavior."""
        super().__init__()
        self.ar_typed_pers: list[VariableDataPrototype] = []
        self.events: list[RTEEvent] = []
        self.exclusive_areas: list[SwcExclusiveAreaPolicy] = []
        self.explicit_inters: list[VariableDataPrototype] = []
        self.implicit_inters: list[VariableDataPrototype] = []
        self.included_data_type_sets: list[IncludedDataTypeSet] = []
        self.included_modes: list[IncludedModeDeclarationGroupSet] = []
        self.instantiation_data_defs: list[InstantiationDataDefProps] = []
        self.per_instance_memories: list[PerInstanceMemory] = []
        self.per_instances: list[ParameterDataPrototype] = []
        self.port_api_options: list[PortAPIOption] = []
        self.runnables: list[RunnableEntity] = []
        self.services: list[Any] = []
        self.shareds: list[ParameterDataPrototype] = []
        self.supports: Optional[Boolean] = None
        self.variation_point_proxies: list[VariationPointProxy] = []


class SwcInternalBehaviorBuilder:
    """Builder for SwcInternalBehavior."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwcInternalBehavior = SwcInternalBehavior()

    def build(self) -> SwcInternalBehavior:
        """Build and return SwcInternalBehavior object.

        Returns:
            SwcInternalBehavior instance
        """
        # TODO: Add validation
        return self._obj
