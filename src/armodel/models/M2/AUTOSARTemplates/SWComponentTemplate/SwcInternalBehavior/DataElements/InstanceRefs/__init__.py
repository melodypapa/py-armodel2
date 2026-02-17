"""InstanceRefs module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.InstanceRefs.parameter_in_atomic_swc_type_instance_ref import (
        ParameterInAtomicSWCTypeInstanceRef,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.InstanceRefs.variable_in_atomic_swc_type_instance_ref import (
        VariableInAtomicSWCTypeInstanceRef,
    )

__all__ = [
    "ParameterInAtomicSWCTypeInstanceRef",
    "VariableInAtomicSWCTypeInstanceRef",
]
