"""ResourceConsumption module."""
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.resource_consumption import (
    ResourceConsumption,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.hardware_configuration import (
    HardwareConfiguration,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.software_context import (
    SoftwareContext,
)

__all__ = [
    "HardwareConfiguration",
    "ResourceConsumption",
    "SoftwareContext",
]
