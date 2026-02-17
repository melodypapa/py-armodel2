"""SoftwareCluster module."""
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster_resource import (
    CpSoftwareClusterResource,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.role_based_resource_dependency import (
    RoleBasedResourceDependency,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster import (
    CpSoftwareCluster,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster_to_ecu_instance_mapping import (
    CpSoftwareClusterToEcuInstanceMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster_resource_to_application_partition_mapping import (
    CpSoftwareClusterResourceToApplicationPartitionMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster_mapping_set import (
    CpSoftwareClusterMappingSet,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster_to_application_partition_mapping import (
    CpSoftwareClusterToApplicationPartitionMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.system_signal_to_communication_resource_mapping import (
    SystemSignalToCommunicationResourceMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.system_signal_group_to_communication_resource_mapping import (
    SystemSignalGroupToCommunicationResourceMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.sw_component_prototype_assignment import (
    SwComponentPrototypeAssignment,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster_resource_pool import (
    CpSoftwareClusterResourcePool,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster_communication_resource import (
    CpSoftwareClusterCommunicationResource,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster_communication_resource_props import (
    CpSoftwareClusterCommunicationResourceProps,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.data_com_props import (
    DataComProps,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.client_server_operation_com_props import (
    ClientServerOperationComProps,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster_service_resource import (
    CpSoftwareClusterServiceResource,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster_to_resource_mapping import (
    CpSoftwareClusterToResourceMapping,
)

__all__ = [
    "ClientServerOperationComProps",
    "CpSoftwareCluster",
    "CpSoftwareClusterCommunicationResource",
    "CpSoftwareClusterCommunicationResourceProps",
    "CpSoftwareClusterMappingSet",
    "CpSoftwareClusterResource",
    "CpSoftwareClusterResourcePool",
    "CpSoftwareClusterResourceToApplicationPartitionMapping",
    "CpSoftwareClusterServiceResource",
    "CpSoftwareClusterToApplicationPartitionMapping",
    "CpSoftwareClusterToEcuInstanceMapping",
    "CpSoftwareClusterToResourceMapping",
    "DataComProps",
    "RoleBasedResourceDependency",
    "SwComponentPrototypeAssignment",
    "SystemSignalGroupToCommunicationResourceMapping",
    "SystemSignalToCommunicationResourceMapping",
]
