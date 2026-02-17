"""InstanceRefs module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs.variable_in_atomic_swc_instance_ref import (
        VariableInAtomicSwcInstanceRef,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs.r_variable_in_atomic_swc_instance_ref import (
        RVariableInAtomicSwcInstanceRef,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs.r_mode_in_atomic_swc_instance_ref import (
        RModeInAtomicSwcInstanceRef,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs.inner_port_group_in_composition_instance_ref import (
        InnerPortGroupInCompositionInstanceRef,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs.trigger_in_atomic_swc_instance_ref import (
        TriggerInAtomicSwcInstanceRef,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs.r_trigger_in_atomic_swc_instance_ref import (
        RTriggerInAtomicSwcInstanceRef,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs.p_trigger_in_atomic_swc_type_instance_ref import (
        PTriggerInAtomicSwcTypeInstanceRef,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs.operation_in_atomic_swc_instance_ref import (
        OperationInAtomicSwcInstanceRef,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs.r_operation_in_atomic_swc_instance_ref import (
        ROperationInAtomicSwcInstanceRef,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs.p_operation_in_atomic_swc_instance_ref import (
        POperationInAtomicSwcInstanceRef,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs.r_mode_group_in_atomic_swc_instance_ref import (
        RModeGroupInAtomicSWCInstanceRef,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs.p_mode_group_in_atomic_swc_instance_ref import (
        PModeGroupInAtomicSwcInstanceRef,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs.mode_group_in_atomic_swc_instance_ref import (
        ModeGroupInAtomicSwcInstanceRef,
    )

__all__ = [
    "InnerPortGroupInCompositionInstanceRef",
    "ModeGroupInAtomicSwcInstanceRef",
    "OperationInAtomicSwcInstanceRef",
    "PModeGroupInAtomicSwcInstanceRef",
    "POperationInAtomicSwcInstanceRef",
    "PTriggerInAtomicSwcTypeInstanceRef",
    "RModeGroupInAtomicSWCInstanceRef",
    "RModeInAtomicSwcInstanceRef",
    "ROperationInAtomicSwcInstanceRef",
    "RTriggerInAtomicSwcInstanceRef",
    "RVariableInAtomicSwcInstanceRef",
    "TriggerInAtomicSwcInstanceRef",
    "VariableInAtomicSwcInstanceRef",
]
