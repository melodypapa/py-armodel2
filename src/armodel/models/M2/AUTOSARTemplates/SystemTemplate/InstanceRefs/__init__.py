"""InstanceRefs module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs.component_in_system_instance_ref import (
        ComponentInSystemInstanceRef,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs.operation_in_system_instance_ref import (
        OperationInSystemInstanceRef,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs.variable_data_prototype_in_system_instance_ref import (
        VariableDataPrototypeInSystemInstanceRef,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs.trigger_in_system_instance_ref import (
        TriggerInSystemInstanceRef,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs.port_group_in_system_instance_ref import (
        PortGroupInSystemInstanceRef,
    )

__all__ = [
    "ComponentInSystemInstanceRef",
    "OperationInSystemInstanceRef",
    "PortGroupInSystemInstanceRef",
    "TriggerInSystemInstanceRef",
    "VariableDataPrototypeInSystemInstanceRef",
]
