"""SystemMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 190)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "applications": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=ApplicationPartitionToEcuPartitionMapping,
        ),  # applications
        "app_os_tasks": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=AppOsTaskProxyToEcuTaskProxyMapping,
        ),  # appOsTasks
        "coms": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=ComManagementMapping,
        ),  # coms
        "crypto_services": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=CryptoServiceMapping,
        ),  # cryptoServices
        "data_mappings": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=DataMapping,
        ),  # dataMappings
        "dds_i_signal_tos": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=DdsCpISignalToDdsTopicMapping,
        ),  # ddsISignalTos
        "ecu_resources": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=ECUMapping,
        ),  # ecuResources
        "j1939_controllers": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=any (J1939Controller),
        ),  # j1939Controllers
        "mappings": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=MappingConstraint,
        ),  # mappings
        "pnc_mappings": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=PncMapping,
        ),  # pncMappings
        "port_element_tos": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=PortElementToCommunicationResourceMapping,
        ),  # portElementTos
        "resources": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=EcuResourceEstimation,
        ),  # resources
        "resource_tos": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=CpSoftwareCluster,
        ),  # resourceTos
        "rte_event_in_systems": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=any (RteEventInSystem),
        ),  # rteEventInSystems
        "rte_event_to_oses": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=RteEventInSystemToOsTaskProxyMapping,
        ),  # rteEventToOses
        "signal_paths": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=SignalPathConstraint,
        ),  # signalPaths
        "software_clusters": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=any (CpSoftwareClusterTo),
        ),  # softwareClusters
        "sw_clusters": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=any (CpSoftwareClusterTo),
        ),  # swClusters
        "swc_tos": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=SwcToApplicationPartitionMapping,
        ),  # swcTos
        "sw_impl_mappings": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=SwcToImplMapping,
        ),  # swImplMappings
        "sw_mappings": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=SwcToEcuMapping,
        ),  # swMappings
        "system_signal_group_tos": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=SystemSignalGroupToCommunicationResourceMapping,
        ),  # systemSignalGroupTos
        "system_signal_tos": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=SystemSignalToCommunicationResourceMapping,
        ),  # systemSignalTos
    }

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
