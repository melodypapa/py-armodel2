"""SwcInternalBehavior AUTOSAR element."""

from typing import Optional, cast
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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("ar_typed_pers", None, False, True, VariableDataPrototype),  # arTypedPers
        ("events", None, False, True, RTEEvent),  # events
        ("exclusive_areas", None, False, True, SwcExclusiveAreaPolicy),  # exclusiveAreas
        ("explicit_inters", None, False, True, VariableDataPrototype),  # explicitInters
        ("implicit_inters", None, False, True, VariableDataPrototype),  # implicitInters
        ("included_data_type_sets", None, False, True, IncludedDataTypeSet),  # includedDataTypeSets
        ("included_modes", None, False, True, IncludedModeDeclarationGroupSet),  # includedModes
        ("instantiation_data_defs", None, False, True, InstantiationDataDefProps),  # instantiationDataDefs
        ("per_instance_memories", None, False, True, PerInstanceMemory),  # perInstanceMemories
        ("per_instances", None, False, True, ParameterDataPrototype),  # perInstances
        ("port_api_options", None, False, True, PortAPIOption),  # portAPIOptions
        ("runnables", None, False, True, RunnableEntity),  # runnables
        ("services", None, False, True, any (SwcService)),  # services
        ("shareds", None, False, True, ParameterDataPrototype),  # shareds
        ("supports", None, True, False, None),  # supports
        ("variation_point_proxies", None, False, True, VariationPointProxy),  # variationPointProxies
    ]

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

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SwcInternalBehavior to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwcInternalBehavior":
        """Create SwcInternalBehavior from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SwcInternalBehavior instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SwcInternalBehavior since parent returns ARObject
        return cast("SwcInternalBehavior", obj)


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
