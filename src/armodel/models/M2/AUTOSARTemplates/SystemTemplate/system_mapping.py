"""SystemMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 190)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    applications: list[ApplicationPartitionToEcuPartitionMapping]
    app_os_tasks: list[AppOsTaskProxyToEcuTaskProxyMapping]
    coms: list[ComManagementMapping]
    crypto_service_refs: list[ARRef]
    data_mapping_refs: list[ARRef]
    dds_i_signal_tos: list[DdsCpISignalToDdsTopicMapping]
    ecu_resource_refs: list[ARRef]
    j1939_controllers: list[Any]
    mapping_refs: list[ARRef]
    pnc_mapping_refs: list[ARRef]
    port_element_tos: list[PortElementToCommunicationResourceMapping]
    resources: list[EcuResourceEstimation]
    resource_tos: list[CpSoftwareCluster]
    rte_event_in_systems: list[Any]
    rte_event_to_oses: list[RteEventInSystemToOsTaskProxyMapping]
    signal_paths: list[SignalPathConstraint]
    software_clusters: list[Any]
    sw_clusters: list[Any]
    swc_tos: list[SwcToApplicationPartitionMapping]
    sw_impl_mapping_refs: list[ARRef]
    sw_mapping_refs: list[ARRef]
    system_signal_group_to_refs: list[ARRef]
    system_signal_tos: list[SystemSignalToCommunicationResourceMapping]
    def __init__(self) -> None:
        """Initialize SystemMapping."""
        super().__init__()
        self.applications: list[ApplicationPartitionToEcuPartitionMapping] = []
        self.app_os_tasks: list[AppOsTaskProxyToEcuTaskProxyMapping] = []
        self.coms: list[ComManagementMapping] = []
        self.crypto_service_refs: list[ARRef] = []
        self.data_mapping_refs: list[ARRef] = []
        self.dds_i_signal_tos: list[DdsCpISignalToDdsTopicMapping] = []
        self.ecu_resource_refs: list[ARRef] = []
        self.j1939_controllers: list[Any] = []
        self.mapping_refs: list[ARRef] = []
        self.pnc_mapping_refs: list[ARRef] = []
        self.port_element_tos: list[PortElementToCommunicationResourceMapping] = []
        self.resources: list[EcuResourceEstimation] = []
        self.resource_tos: list[CpSoftwareCluster] = []
        self.rte_event_in_systems: list[Any] = []
        self.rte_event_to_oses: list[RteEventInSystemToOsTaskProxyMapping] = []
        self.signal_paths: list[SignalPathConstraint] = []
        self.software_clusters: list[Any] = []
        self.sw_clusters: list[Any] = []
        self.swc_tos: list[SwcToApplicationPartitionMapping] = []
        self.sw_impl_mapping_refs: list[ARRef] = []
        self.sw_mapping_refs: list[ARRef] = []
        self.system_signal_group_to_refs: list[ARRef] = []
        self.system_signal_tos: list[SystemSignalToCommunicationResourceMapping] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SystemMapping":
        """Deserialize XML element to SystemMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SystemMapping object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse applications (list)
        obj.applications = []
        for child in ARObject._find_all_child_elements(element, "APPLICATIONS"):
            applications_value = ARObject._deserialize_by_tag(child, "ApplicationPartitionToEcuPartitionMapping")
            obj.applications.append(applications_value)

        # Parse app_os_tasks (list)
        obj.app_os_tasks = []
        for child in ARObject._find_all_child_elements(element, "APP-OS-TASKS"):
            app_os_tasks_value = ARObject._deserialize_by_tag(child, "AppOsTaskProxyToEcuTaskProxyMapping")
            obj.app_os_tasks.append(app_os_tasks_value)

        # Parse coms (list)
        obj.coms = []
        for child in ARObject._find_all_child_elements(element, "COMS"):
            coms_value = ARObject._deserialize_by_tag(child, "ComManagementMapping")
            obj.coms.append(coms_value)

        # Parse crypto_service_refs (list)
        obj.crypto_service_refs = []
        for child in ARObject._find_all_child_elements(element, "CRYPTO-SERVICES"):
            crypto_service_refs_value = ARObject._deserialize_by_tag(child, "CryptoServiceMapping")
            obj.crypto_service_refs.append(crypto_service_refs_value)

        # Parse data_mapping_refs (list)
        obj.data_mapping_refs = []
        for child in ARObject._find_all_child_elements(element, "DATA-MAPPINGS"):
            data_mapping_refs_value = ARObject._deserialize_by_tag(child, "DataMapping")
            obj.data_mapping_refs.append(data_mapping_refs_value)

        # Parse dds_i_signal_tos (list)
        obj.dds_i_signal_tos = []
        for child in ARObject._find_all_child_elements(element, "DDS-I-SIGNAL-TOS"):
            dds_i_signal_tos_value = ARObject._deserialize_by_tag(child, "DdsCpISignalToDdsTopicMapping")
            obj.dds_i_signal_tos.append(dds_i_signal_tos_value)

        # Parse ecu_resource_refs (list)
        obj.ecu_resource_refs = []
        for child in ARObject._find_all_child_elements(element, "ECU-RESOURCES"):
            ecu_resource_refs_value = ARObject._deserialize_by_tag(child, "ECUMapping")
            obj.ecu_resource_refs.append(ecu_resource_refs_value)

        # Parse j1939_controllers (list)
        obj.j1939_controllers = []
        for child in ARObject._find_all_child_elements(element, "J1939-CONTROLLERS"):
            j1939_controllers_value = child.text
            obj.j1939_controllers.append(j1939_controllers_value)

        # Parse mapping_refs (list)
        obj.mapping_refs = []
        for child in ARObject._find_all_child_elements(element, "MAPPINGS"):
            mapping_refs_value = ARObject._deserialize_by_tag(child, "MappingConstraint")
            obj.mapping_refs.append(mapping_refs_value)

        # Parse pnc_mapping_refs (list)
        obj.pnc_mapping_refs = []
        for child in ARObject._find_all_child_elements(element, "PNC-MAPPINGS"):
            pnc_mapping_refs_value = ARObject._deserialize_by_tag(child, "PncMapping")
            obj.pnc_mapping_refs.append(pnc_mapping_refs_value)

        # Parse port_element_tos (list)
        obj.port_element_tos = []
        for child in ARObject._find_all_child_elements(element, "PORT-ELEMENT-TOS"):
            port_element_tos_value = ARObject._deserialize_by_tag(child, "PortElementToCommunicationResourceMapping")
            obj.port_element_tos.append(port_element_tos_value)

        # Parse resources (list)
        obj.resources = []
        for child in ARObject._find_all_child_elements(element, "RESOURCES"):
            resources_value = ARObject._deserialize_by_tag(child, "EcuResourceEstimation")
            obj.resources.append(resources_value)

        # Parse resource_tos (list)
        obj.resource_tos = []
        for child in ARObject._find_all_child_elements(element, "RESOURCE-TOS"):
            resource_tos_value = ARObject._deserialize_by_tag(child, "CpSoftwareCluster")
            obj.resource_tos.append(resource_tos_value)

        # Parse rte_event_in_systems (list)
        obj.rte_event_in_systems = []
        for child in ARObject._find_all_child_elements(element, "RTE-EVENT-IN-SYSTEMS"):
            rte_event_in_systems_value = child.text
            obj.rte_event_in_systems.append(rte_event_in_systems_value)

        # Parse rte_event_to_oses (list)
        obj.rte_event_to_oses = []
        for child in ARObject._find_all_child_elements(element, "RTE-EVENT-TO-OSES"):
            rte_event_to_oses_value = ARObject._deserialize_by_tag(child, "RteEventInSystemToOsTaskProxyMapping")
            obj.rte_event_to_oses.append(rte_event_to_oses_value)

        # Parse signal_paths (list)
        obj.signal_paths = []
        for child in ARObject._find_all_child_elements(element, "SIGNAL-PATHS"):
            signal_paths_value = ARObject._deserialize_by_tag(child, "SignalPathConstraint")
            obj.signal_paths.append(signal_paths_value)

        # Parse software_clusters (list)
        obj.software_clusters = []
        for child in ARObject._find_all_child_elements(element, "SOFTWARE-CLUSTERS"):
            software_clusters_value = child.text
            obj.software_clusters.append(software_clusters_value)

        # Parse sw_clusters (list)
        obj.sw_clusters = []
        for child in ARObject._find_all_child_elements(element, "SW-CLUSTERS"):
            sw_clusters_value = child.text
            obj.sw_clusters.append(sw_clusters_value)

        # Parse swc_tos (list)
        obj.swc_tos = []
        for child in ARObject._find_all_child_elements(element, "SWC-TOS"):
            swc_tos_value = ARObject._deserialize_by_tag(child, "SwcToApplicationPartitionMapping")
            obj.swc_tos.append(swc_tos_value)

        # Parse sw_impl_mapping_refs (list)
        obj.sw_impl_mapping_refs = []
        for child in ARObject._find_all_child_elements(element, "SW-IMPL-MAPPINGS"):
            sw_impl_mapping_refs_value = ARObject._deserialize_by_tag(child, "SwcToImplMapping")
            obj.sw_impl_mapping_refs.append(sw_impl_mapping_refs_value)

        # Parse sw_mapping_refs (list)
        obj.sw_mapping_refs = []
        for child in ARObject._find_all_child_elements(element, "SW-MAPPINGS"):
            sw_mapping_refs_value = ARObject._deserialize_by_tag(child, "SwcToEcuMapping")
            obj.sw_mapping_refs.append(sw_mapping_refs_value)

        # Parse system_signal_group_to_refs (list)
        obj.system_signal_group_to_refs = []
        for child in ARObject._find_all_child_elements(element, "SYSTEM-SIGNAL-GROUP-TOS"):
            system_signal_group_to_refs_value = ARObject._deserialize_by_tag(child, "SystemSignalGroupToCommunicationResourceMapping")
            obj.system_signal_group_to_refs.append(system_signal_group_to_refs_value)

        # Parse system_signal_tos (list)
        obj.system_signal_tos = []
        for child in ARObject._find_all_child_elements(element, "SYSTEM-SIGNAL-TOS"):
            system_signal_tos_value = ARObject._deserialize_by_tag(child, "SystemSignalToCommunicationResourceMapping")
            obj.system_signal_tos.append(system_signal_tos_value)

        return obj



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
