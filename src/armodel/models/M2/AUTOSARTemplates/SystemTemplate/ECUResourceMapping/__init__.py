"""ECUResourceMapping module."""
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.ECUResourceMapping.ecu_mapping import (
    ECUMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.ECUResourceMapping.communication_controller_mapping import (
    CommunicationControllerMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.ECUResourceMapping.hw_port_mapping import (
    HwPortMapping,
)

__all__ = [
    "CommunicationControllerMapping",
    "ECUMapping",
    "HwPortMapping",
]
