"""LinTopology module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology.lin_cluster import (
        LinCluster,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology.lin_communication_controller import (
        LinCommunicationController,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology.lin_master import (
        LinMaster,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology.lin_slave_config import (
        LinSlaveConfig,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology.lin_slave_config_ident import (
        LinSlaveConfigIdent,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology.lin_slave import (
        LinSlave,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology.lin_communication_connector import (
        LinCommunicationConnector,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology.lin_configurable_frame import (
        LinConfigurableFrame,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology.lin_ordered_configurable_frame import (
        LinOrderedConfigurableFrame,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology.lin_physical_channel import (
        LinPhysicalChannel,
    )

__all__ = [
    "LinCluster",
    "LinCommunicationConnector",
    "LinCommunicationController",
    "LinConfigurableFrame",
    "LinMaster",
    "LinOrderedConfigurableFrame",
    "LinPhysicalChannel",
    "LinSlave",
    "LinSlaveConfig",
    "LinSlaveConfigIdent",
]
