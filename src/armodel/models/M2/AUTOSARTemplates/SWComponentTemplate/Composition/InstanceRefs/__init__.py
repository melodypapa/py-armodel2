"""InstanceRefs module."""
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs.component_in_composition_instance_ref import (
    ComponentInCompositionInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs.port_in_composition_type_instance_ref import (
    PortInCompositionTypeInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs.p_port_in_composition_instance_ref import (
    PPortInCompositionInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs.r_port_in_composition_instance_ref import (
    RPortInCompositionInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs.instance_event_in_composition_instance_ref import (
    InstanceEventInCompositionInstanceRef,
)

__all__ = [
    "ComponentInCompositionInstanceRef",
    "InstanceEventInCompositionInstanceRef",
    "PPortInCompositionInstanceRef",
    "PortInCompositionTypeInstanceRef",
    "RPortInCompositionInstanceRef",
]
