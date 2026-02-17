"""CddSupport module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.CddSupport.user_defined_cluster import (
        UserDefinedCluster,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.CddSupport.user_defined_physical_channel import (
        UserDefinedPhysicalChannel,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.CddSupport.user_defined_communication_connector import (
        UserDefinedCommunicationConnector,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.CddSupport.user_defined_communication_controller import (
        UserDefinedCommunicationController,
    )

__all__ = [
    "UserDefinedCluster",
    "UserDefinedCommunicationConnector",
    "UserDefinedCommunicationController",
    "UserDefinedPhysicalChannel",
]
