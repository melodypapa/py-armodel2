"""Composition module."""
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.composition_sw_component_type import (
    CompositionSwComponentType,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.sw_component_prototype import (
    SwComponentPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.assembly_sw_connector import (
    AssemblySwConnector,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.sw_connector import (
    SwConnector,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.delegation_sw_connector import (
    DelegationSwConnector,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.pass_through_sw_connector import (
    PassThroughSwConnector,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.instantiation_timing_event_props import (
    InstantiationTimingEventProps,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.instantiation_rte_event_props import (
    InstantiationRTEEventProps,
)

__all__ = [
    "AssemblySwConnector",
    "CompositionSwComponentType",
    "DelegationSwConnector",
    "InstantiationRTEEventProps",
    "InstantiationTimingEventProps",
    "PassThroughSwConnector",
    "SwComponentPrototype",
    "SwConnector",
]
