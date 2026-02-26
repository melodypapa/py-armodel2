"""ServiceMapping module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServiceMapping.role_based_data_type_assignment import (
        RoleBasedDataTypeAssignment,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServiceMapping.role_based_port_assignment import (
        RoleBasedPortAssignment,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServiceMapping.swc_service_dependency import (
        SwcServiceDependency,
    )

__all__ = [
    "RoleBasedDataTypeAssignment",
    "RoleBasedPortAssignment",
    "SwcServiceDependency",
]
