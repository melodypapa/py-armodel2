"""TtcanTopology module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ttcan.TtcanTopology.ttcan_cluster import (
        TtcanCluster,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ttcan.TtcanTopology.ttcan_communication_controller import (
        TtcanCommunicationController,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ttcan.TtcanTopology.ttcan_physical_channel import (
        TtcanPhysicalChannel,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ttcan.TtcanTopology.ttcan_communication_connector import (
        TtcanCommunicationConnector,
    )

__all__ = [
    "TtcanCluster",
    "TtcanCommunicationConnector",
    "TtcanCommunicationController",
    "TtcanPhysicalChannel",
]
