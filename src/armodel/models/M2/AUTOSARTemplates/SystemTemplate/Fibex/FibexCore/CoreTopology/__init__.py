"""CoreTopology module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_cluster import (
        CommunicationCluster,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.ecu_instance import (
        EcuInstance,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.physical_channel import (
        PhysicalChannel,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.client_id_range import (
        ClientIdRange,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_controller import (
        CommunicationController,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_connector import (
        CommunicationConnector,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.comm_connector_port import (
        CommConnectorPort,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_cycle import (
        CommunicationCycle,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.cycle_counter import (
        CycleCounter,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.cycle_repetition import (
        CycleRepetition,
    )

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.pnc_gateway_type_enum import (
    PncGatewayTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.cycle_repetition_type import (
    CycleRepetitionType,
)

__all__ = [
    "ClientIdRange",
    "CommConnectorPort",
    "CommunicationCluster",
    "CommunicationConnector",
    "CommunicationController",
    "CommunicationCycle",
    "CycleCounter",
    "CycleRepetition",
    "CycleRepetitionType",
    "EcuInstance",
    "PhysicalChannel",
    "PncGatewayTypeEnum",
]
