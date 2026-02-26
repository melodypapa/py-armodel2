"""ResourceConsumption module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.resource_consumption import (
        ResourceConsumption,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.hardware_configuration import (
        HardwareConfiguration,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.software_context import (
        SoftwareContext,
    )

__all__ = [
    "HardwareConfiguration",
    "ResourceConsumption",
    "SoftwareContext",
]
