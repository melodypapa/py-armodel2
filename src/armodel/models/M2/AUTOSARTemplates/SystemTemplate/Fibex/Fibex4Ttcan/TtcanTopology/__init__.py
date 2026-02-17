"""TtcanTopology module."""
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ttcan.TtcanTopology.ttcan_cluster import (
    TtcanCluster,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ttcan.TtcanTopology.ttcan_communication_controller import (
    TtcanCommunicationController,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ttcan.TtcanTopology.ttcan_physical_channel import (
    TtcanPhysicalChannel,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ttcan.TtcanTopology.ttcan_communication_connector import (
    TtcanCommunicationConnector,
)

__all__ = [
    "TtcanCluster",
    "TtcanCommunicationConnector",
    "TtcanCommunicationController",
    "TtcanPhysicalChannel",
]
