"""InstanceRef module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior.InstanceRef.inner_data_prototype_group_in_composition_instance_ref import (
        InnerDataPrototypeGroupInCompositionInstanceRef,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior.InstanceRef.inner_runnable_entity_group_in_composition_instance_ref import (
        InnerRunnableEntityGroupInCompositionInstanceRef,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior.InstanceRef.runnable_entity_in_composition_instance_ref import (
        RunnableEntityInCompositionInstanceRef,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior.InstanceRef.variable_data_prototype_in_composition_instance_ref import (
        VariableDataPrototypeInCompositionInstanceRef,
    )

__all__ = [
    "InnerDataPrototypeGroupInCompositionInstanceRef",
    "InnerRunnableEntityGroupInCompositionInstanceRef",
    "RunnableEntityInCompositionInstanceRef",
    "VariableDataPrototypeInCompositionInstanceRef",
]
