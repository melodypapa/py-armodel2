"""SystemMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.RteEventToOsTaskMapping.app_os_task_proxy_to_ecu_task_proxy_mapping import (
    AppOsTaskProxyToEcuTaskProxyMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping.application_partition_to_ecu_partition_mapping import (
    ApplicationPartitionToEcuPartitionMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.com_management_mapping import (
    ComManagementMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster import (
    CpSoftwareCluster,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.crypto_service_mapping import (
    CryptoServiceMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.data_mapping import (
    DataMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds.dds_cp_i_signal_to_dds_topic_mapping import (
    DdsCpISignalToDdsTopicMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.ECUResourceMapping.ecu_mapping import (
    ECUMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping.ecu_resource_estimation import (
    EcuResourceEstimation,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping.mapping_constraint import (
    MappingConstraint,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.PncMapping.pnc_mapping import (
    PncMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.port_element_to_communication_resource_mapping import (
    PortElementToCommunicationResourceMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.RteEventToOsTaskMapping.rte_event_in_system_to_os_task_proxy_mapping import (
    RteEventInSystemToOsTaskProxyMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths.signal_path_constraint import (
    SignalPathConstraint,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping.swc_to_application_partition_mapping import (
    SwcToApplicationPartitionMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping.swc_to_ecu_mapping import (
    SwcToEcuMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping.swc_to_impl_mapping import (
    SwcToImplMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.system_signal_group_to_communication_resource_mapping import (
    SystemSignalGroupToCommunicationResourceMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.system_signal_to_communication_resource_mapping import (
    SystemSignalToCommunicationResourceMapping,
)


class SystemMapping(Identifiable):
    """AUTOSAR SystemMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("applications", None, False, True, ApplicationPartitionToEcuPartitionMapping),  # applications
        ("app_os_tasks", None, False, True, AppOsTaskProxyToEcuTaskProxyMapping),  # appOsTasks
        ("coms", None, False, True, ComManagementMapping),  # coms
        ("crypto_services", None, False, True, CryptoServiceMapping),  # cryptoServices
        ("data_mappings", None, False, True, DataMapping),  # dataMappings
        ("dds_i_signal_tos", None, False, True, DdsCpISignalToDdsTopicMapping),  # ddsISignalTos
        ("ecu_resources", None, False, True, ECUMapping),  # ecuResources
        ("j1939_controllers", None, False, True, any (J1939Controller)),  # j1939Controllers
        ("mappings", None, False, True, MappingConstraint),  # mappings
        ("pnc_mappings", None, False, True, PncMapping),  # pncMappings
        ("port_element_tos", None, False, True, PortElementToCommunicationResourceMapping),  # portElementTos
        ("resources", None, False, True, EcuResourceEstimation),  # resources
        ("resource_tos", None, False, True, CpSoftwareCluster),  # resourceTos
        ("rte_event_in_systems", None, False, True, any (RteEventInSystem)),  # rteEventInSystems
        ("rte_event_to_oses", None, False, True, RteEventInSystemToOsTaskProxyMapping),  # rteEventToOses
        ("signal_paths", None, False, True, SignalPathConstraint),  # signalPaths
        ("software_clusters", None, False, True, any (CpSoftwareClusterTo)),  # softwareClusters
        ("sw_clusters", None, False, True, any (CpSoftwareClusterTo)),  # swClusters
        ("swc_tos", None, False, True, SwcToApplicationPartitionMapping),  # swcTos
        ("sw_impl_mappings", None, False, True, SwcToImplMapping),  # swImplMappings
        ("sw_mappings", None, False, True, SwcToEcuMapping),  # swMappings
        ("system_signal_group_tos", None, False, True, SystemSignalGroupToCommunicationResourceMapping),  # systemSignalGroupTos
        ("system_signal_tos", None, False, True, SystemSignalToCommunicationResourceMapping),  # systemSignalTos
    ]

    def __init__(self) -> None:
        """Initialize SystemMapping."""
        super().__init__()
        self.applications: list[ApplicationPartitionToEcuPartitionMapping] = []
        self.app_os_tasks: list[AppOsTaskProxyToEcuTaskProxyMapping] = []
        self.coms: list[ComManagementMapping] = []
        self.crypto_services: list[CryptoServiceMapping] = []
        self.data_mappings: list[DataMapping] = []
        self.dds_i_signal_tos: list[DdsCpISignalToDdsTopicMapping] = []
        self.ecu_resources: list[ECUMapping] = []
        self.j1939_controllers: list[Any] = []
        self.mappings: list[MappingConstraint] = []
        self.pnc_mappings: list[PncMapping] = []
        self.port_element_tos: list[PortElementToCommunicationResourceMapping] = []
        self.resources: list[EcuResourceEstimation] = []
        self.resource_tos: list[CpSoftwareCluster] = []
        self.rte_event_in_systems: list[Any] = []
        self.rte_event_to_oses: list[RteEventInSystemToOsTaskProxyMapping] = []
        self.signal_paths: list[SignalPathConstraint] = []
        self.software_clusters: list[Any] = []
        self.sw_clusters: list[Any] = []
        self.swc_tos: list[SwcToApplicationPartitionMapping] = []
        self.sw_impl_mappings: list[SwcToImplMapping] = []
        self.sw_mappings: list[SwcToEcuMapping] = []
        self.system_signal_group_tos: list[SystemSignalGroupToCommunicationResourceMapping] = []
        self.system_signal_tos: list[SystemSignalToCommunicationResourceMapping] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SystemMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SystemMapping":
        """Create SystemMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SystemMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SystemMapping since parent returns ARObject
        return cast("SystemMapping", obj)


class SystemMappingBuilder:
    """Builder for SystemMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SystemMapping = SystemMapping()

    def build(self) -> SystemMapping:
        """Build and return SystemMapping object.

        Returns:
            SystemMapping instance
        """
        # TODO: Add validation
        return self._obj
