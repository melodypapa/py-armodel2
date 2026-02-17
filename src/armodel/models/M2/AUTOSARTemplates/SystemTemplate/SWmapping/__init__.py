"""SWmapping module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping.swc_to_ecu_mapping import (
        SwcToEcuMapping,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping.swc_to_impl_mapping import (
        SwcToImplMapping,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping.swc_to_application_partition_mapping import (
        SwcToApplicationPartitionMapping,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping.application_partition import (
        ApplicationPartition,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping.application_partition_to_ecu_partition_mapping import (
        ApplicationPartitionToEcuPartitionMapping,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping.ecu_partition import (
        EcuPartition,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping.mapping_constraint import (
        MappingConstraint,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping.component_clustering import (
        ComponentClustering,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping.component_separation import (
        ComponentSeparation,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping.j1939_controller_application_to_j1939_nm_node_mapping import (
        J1939ControllerApplicationToJ1939NmNodeMapping,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping.j1939_controller_application import (
        J1939ControllerApplication,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping.ecu_resource_estimation import (
        EcuResourceEstimation,
    )

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping.mapping_scope_enum import (
    MappingScopeEnum,
)

__all__ = [
    "ApplicationPartition",
    "ApplicationPartitionToEcuPartitionMapping",
    "ComponentClustering",
    "ComponentSeparation",
    "EcuPartition",
    "EcuResourceEstimation",
    "J1939ControllerApplication",
    "J1939ControllerApplicationToJ1939NmNodeMapping",
    "MappingConstraint",
    "MappingScopeEnum",
    "SwcToApplicationPartitionMapping",
    "SwcToEcuMapping",
    "SwcToImplMapping",
]
