"""FlexrayTopology module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayTopology.flexray_cluster import (
        FlexrayCluster,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayTopology.flexray_communication_controller import (
        FlexrayCommunicationController,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayTopology.flexray_fifo_configuration import (
        FlexrayFifoConfiguration,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayTopology.flexray_fifo_range import (
        FlexrayFifoRange,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayTopology.flexray_communication_connector import (
        FlexrayCommunicationConnector,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayTopology.flexray_physical_channel import (
        FlexrayPhysicalChannel,
    )

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayTopology.flexray_channel_name import (
    FlexrayChannelName,
)

__all__ = [
    "FlexrayChannelName",
    "FlexrayCluster",
    "FlexrayCommunicationConnector",
    "FlexrayCommunicationController",
    "FlexrayFifoConfiguration",
    "FlexrayFifoRange",
    "FlexrayPhysicalChannel",
]
