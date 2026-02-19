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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ar_typed_per_refs: list[ARRef]
    events: list[RTEEvent]
    exclusive_areas: list[SwcExclusiveAreaPolicy]
    explicit_inter_refs: list[ARRef]
    implicit_inter_refs: list[ARRef]
    included_data_type_set_refs: list[ARRef]
    included_modes: list[IncludedModeDeclarationGroupSet]
    instantiation_data_defs: list[InstantiationDataDefProps]
    per_instance_memories: list[PerInstanceMemory]
    per_instances: list[ParameterDataPrototype]
    port_api_options: list[PortAPIOption]
    runnables: list[RunnableEntity]
    services: list[Any]
    shareds: list[ParameterDataPrototype]
    supports: Optional[Boolean]
    variation_point_proxies: list[VariationPointProxy]
    def __init__(self) -> None:
        """Initialize SwcInternalBehavior."""
        super().__init__()
        self.ar_typed_per_refs: list[ARRef] = []
        self.events: list[RTEEvent] = []
        self.exclusive_areas: list[SwcExclusiveAreaPolicy] = []
        self.explicit_inter_refs: list[ARRef] = []
        self.implicit_inter_refs: list[ARRef] = []
        self.included_data_type_set_refs: list[ARRef] = []
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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwcInternalBehavior":
        """Deserialize XML element to SwcInternalBehavior object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwcInternalBehavior object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse ar_typed_per_refs (list)
        obj.ar_typed_per_refs = []
        for child in ARObject._find_all_child_elements(element, "AR-TYPED-PERS"):
            ar_typed_per_refs_value = ARObject._deserialize_by_tag(child, "VariableDataPrototype")
            obj.ar_typed_per_refs.append(ar_typed_per_refs_value)

        # Parse events (list)
        obj.events = []
        for child in ARObject._find_all_child_elements(element, "EVENTS"):
            events_value = ARObject._deserialize_by_tag(child, "RTEEvent")
            obj.events.append(events_value)

        # Parse exclusive_areas (list)
        obj.exclusive_areas = []
        for child in ARObject._find_all_child_elements(element, "EXCLUSIVE-AREAS"):
            exclusive_areas_value = ARObject._deserialize_by_tag(child, "SwcExclusiveAreaPolicy")
            obj.exclusive_areas.append(exclusive_areas_value)

        # Parse explicit_inter_refs (list)
        obj.explicit_inter_refs = []
        for child in ARObject._find_all_child_elements(element, "EXPLICIT-INTERS"):
            explicit_inter_refs_value = ARObject._deserialize_by_tag(child, "VariableDataPrototype")
            obj.explicit_inter_refs.append(explicit_inter_refs_value)

        # Parse implicit_inter_refs (list)
        obj.implicit_inter_refs = []
        for child in ARObject._find_all_child_elements(element, "IMPLICIT-INTERS"):
            implicit_inter_refs_value = ARObject._deserialize_by_tag(child, "VariableDataPrototype")
            obj.implicit_inter_refs.append(implicit_inter_refs_value)

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

        # Parse instantiation_data_defs (list)
        obj.instantiation_data_defs = []
        for child in ARObject._find_all_child_elements(element, "INSTANTIATION-DATA-DEFS"):
            instantiation_data_defs_value = ARObject._deserialize_by_tag(child, "InstantiationDataDefProps")
            obj.instantiation_data_defs.append(instantiation_data_defs_value)

        # Parse per_instance_memories (list)
        obj.per_instance_memories = []
        for child in ARObject._find_all_child_elements(element, "PER-INSTANCE-MEMORIES"):
            per_instance_memories_value = ARObject._deserialize_by_tag(child, "PerInstanceMemory")
            obj.per_instance_memories.append(per_instance_memories_value)

        # Parse per_instances (list)
        obj.per_instances = []
        for child in ARObject._find_all_child_elements(element, "PER-INSTANCES"):
            per_instances_value = ARObject._deserialize_by_tag(child, "ParameterDataPrototype")
            obj.per_instances.append(per_instances_value)

        # Parse port_api_options (list)
        obj.port_api_options = []
        for child in ARObject._find_all_child_elements(element, "PORT-API-OPTIONS"):
            port_api_options_value = ARObject._deserialize_by_tag(child, "PortAPIOption")
            obj.port_api_options.append(port_api_options_value)

        # Parse runnables (list)
        obj.runnables = []
        for child in ARObject._find_all_child_elements(element, "RUNNABLES"):
            runnables_value = ARObject._deserialize_by_tag(child, "RunnableEntity")
            obj.runnables.append(runnables_value)

        # Parse services (list)
        obj.services = []
        for child in ARObject._find_all_child_elements(element, "SERVICES"):
            services_value = child.text
            obj.services.append(services_value)

        # Parse shareds (list)
        obj.shareds = []
        for child in ARObject._find_all_child_elements(element, "SHAREDS"):
            shareds_value = ARObject._deserialize_by_tag(child, "ParameterDataPrototype")
            obj.shareds.append(shareds_value)

        # Parse supports
        child = ARObject._find_child_element(element, "SUPPORTS")
        if child is not None:
            supports_value = child.text
            obj.supports = supports_value

        # Parse variation_point_proxies (list)
        obj.variation_point_proxies = []
        for child in ARObject._find_all_child_elements(element, "VARIATION-POINT-PROXIES"):
            variation_point_proxies_value = ARObject._deserialize_by_tag(child, "VariationPointProxy")
            obj.variation_point_proxies.append(variation_point_proxies_value)

        return obj



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
