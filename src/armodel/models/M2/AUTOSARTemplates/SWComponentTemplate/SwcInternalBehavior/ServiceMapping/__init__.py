"""ServiceMapping module."""
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServiceMapping.role_based_data_type_assignment import (
    RoleBasedDataTypeAssignment,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServiceMapping.role_based_port_assignment import (
    RoleBasedPortAssignment,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServiceMapping.swc_service_dependency import (
    SwcServiceDependency,
)

__all__ = [
    "RoleBasedDataTypeAssignment",
    "RoleBasedPortAssignment",
    "SwcServiceDependency",
]
