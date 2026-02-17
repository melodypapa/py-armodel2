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
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

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
