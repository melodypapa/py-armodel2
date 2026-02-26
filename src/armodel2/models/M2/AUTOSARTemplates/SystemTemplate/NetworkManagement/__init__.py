"""NetworkManagement module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.j1939_nm_node import (
        J1939NmNode,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_config import (
        NmConfig,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_cluster import (
        NmCluster,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_ecu import (
        NmEcu,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.busspecific_nm_ecu import (
        BusspecificNmEcu,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_coordinator import (
        NmCoordinator,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_node import (
        NmNode,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_cluster_coupling import (
        NmClusterCoupling,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.flexray_nm_cluster import (
        FlexrayNmCluster,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.flexray_nm_ecu import (
        FlexrayNmEcu,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.flexray_nm_cluster_coupling import (
        FlexrayNmClusterCoupling,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.flexray_nm_node import (
        FlexrayNmNode,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.can_nm_cluster import (
        CanNmCluster,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.can_nm_ecu import (
        CanNmEcu,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.can_nm_cluster_coupling import (
        CanNmClusterCoupling,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.can_nm_node import (
        CanNmNode,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.udp_nm_cluster import (
        UdpNmCluster,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.udp_nm_ecu import (
        UdpNmEcu,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.udp_nm_cluster_coupling import (
        UdpNmClusterCoupling,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.udp_nm_node import (
        UdpNmNode,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.j1939_nm_cluster import (
        J1939NmCluster,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.j1939_node_name import (
        J1939NodeName,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.j1939_nm_ecu import (
        J1939NmEcu,
    )

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_coordinator_role_enum import (
    NmCoordinatorRoleEnum,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.flexray_nm_schedule_variant import (
    FlexrayNmScheduleVariant,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.j1939_nm_address_configuration_capability_enum import (
    J1939NmAddressConfigurationCapabilityEnum,
)

__all__ = [
    "BusspecificNmEcu",
    "CanNmCluster",
    "CanNmClusterCoupling",
    "CanNmEcu",
    "CanNmNode",
    "FlexrayNmCluster",
    "FlexrayNmClusterCoupling",
    "FlexrayNmEcu",
    "FlexrayNmNode",
    "FlexrayNmScheduleVariant",
    "J1939NmAddressConfigurationCapabilityEnum",
    "J1939NmCluster",
    "J1939NmEcu",
    "J1939NmNode",
    "J1939NodeName",
    "NmCluster",
    "NmClusterCoupling",
    "NmConfig",
    "NmCoordinator",
    "NmCoordinatorRoleEnum",
    "NmEcu",
    "NmNode",
    "UdpNmCluster",
    "UdpNmClusterCoupling",
    "UdpNmEcu",
    "UdpNmNode",
]
