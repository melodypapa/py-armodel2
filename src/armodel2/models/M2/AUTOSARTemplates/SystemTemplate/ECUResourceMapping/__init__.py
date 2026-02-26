"""ECUResourceMapping module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.ECUResourceMapping.ecu_mapping import (
        ECUMapping,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.ECUResourceMapping.communication_controller_mapping import (
        CommunicationControllerMapping,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.ECUResourceMapping.hw_port_mapping import (
        HwPortMapping,
    )

__all__ = [
    "CommunicationControllerMapping",
    "ECUMapping",
    "HwPortMapping",
]
