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
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SystemMapping, cls).deserialize(element)

        # Parse applications (list from container "APPLICATIONS")
        obj.applications = []
        container = ARObject._find_child_element(element, "APPLICATIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.applications.append(child_value)

        # Parse app_os_tasks (list from container "APP-OS-TASKS")
        obj.app_os_tasks = []
        container = ARObject._find_child_element(element, "APP-OS-TASKS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.app_os_tasks.append(child_value)

        # Parse coms (list from container "COMS")
        obj.coms = []
        container = ARObject._find_child_element(element, "COMS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.coms.append(child_value)

        # Parse crypto_service_refs (list from container "CRYPTO-SERVICES")
        obj.crypto_service_refs = []
        container = ARObject._find_child_element(element, "CRYPTO-SERVICES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.crypto_service_refs.append(child_value)

        # Parse data_mapping_refs (list from container "DATA-MAPPINGS")
        obj.data_mapping_refs = []
        container = ARObject._find_child_element(element, "DATA-MAPPINGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.data_mapping_refs.append(child_value)

        # Parse dds_i_signal_tos (list from container "DDS-I-SIGNAL-TOS")
        obj.dds_i_signal_tos = []
        container = ARObject._find_child_element(element, "DDS-I-SIGNAL-TOS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.dds_i_signal_tos.append(child_value)

        # Parse ecu_resource_refs (list from container "ECU-RESOURCES")
        obj.ecu_resource_refs = []
        container = ARObject._find_child_element(element, "ECU-RESOURCES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.ecu_resource_refs.append(child_value)

        # Parse j1939_controllers (list from container "J1939-CONTROLLERS")
        obj.j1939_controllers = []
        container = ARObject._find_child_element(element, "J1939-CONTROLLERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.j1939_controllers.append(child_value)

        # Parse mapping_refs (list from container "MAPPINGS")
        obj.mapping_refs = []
        container = ARObject._find_child_element(element, "MAPPINGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.mapping_refs.append(child_value)

        # Parse pnc_mapping_refs (list from container "PNC-MAPPINGS")
        obj.pnc_mapping_refs = []
        container = ARObject._find_child_element(element, "PNC-MAPPINGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.pnc_mapping_refs.append(child_value)

        # Parse port_element_tos (list from container "PORT-ELEMENT-TOS")
        obj.port_element_tos = []
        container = ARObject._find_child_element(element, "PORT-ELEMENT-TOS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.port_element_tos.append(child_value)

        # Parse resources (list from container "RESOURCES")
        obj.resources = []
        container = ARObject._find_child_element(element, "RESOURCES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.resources.append(child_value)

        # Parse resource_tos (list from container "RESOURCE-TOS")
        obj.resource_tos = []
        container = ARObject._find_child_element(element, "RESOURCE-TOS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.resource_tos.append(child_value)

        # Parse rte_event_in_systems (list from container "RTE-EVENT-IN-SYSTEMS")
        obj.rte_event_in_systems = []
        container = ARObject._find_child_element(element, "RTE-EVENT-IN-SYSTEMS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.rte_event_in_systems.append(child_value)

        # Parse rte_event_to_oses (list from container "RTE-EVENT-TO-OSES")
        obj.rte_event_to_oses = []
        container = ARObject._find_child_element(element, "RTE-EVENT-TO-OSES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.rte_event_to_oses.append(child_value)

        # Parse signal_paths (list from container "SIGNAL-PATHS")
        obj.signal_paths = []
        container = ARObject._find_child_element(element, "SIGNAL-PATHS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.signal_paths.append(child_value)

        # Parse software_clusters (list from container "SOFTWARE-CLUSTERS")
        obj.software_clusters = []
        container = ARObject._find_child_element(element, "SOFTWARE-CLUSTERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.software_clusters.append(child_value)

        # Parse sw_clusters (list from container "SW-CLUSTERS")
        obj.sw_clusters = []
        container = ARObject._find_child_element(element, "SW-CLUSTERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.sw_clusters.append(child_value)

        # Parse swc_tos (list from container "SWC-TOS")
        obj.swc_tos = []
        container = ARObject._find_child_element(element, "SWC-TOS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.swc_tos.append(child_value)

        # Parse sw_impl_mapping_refs (list from container "SW-IMPL-MAPPINGS")
        obj.sw_impl_mapping_refs = []
        container = ARObject._find_child_element(element, "SW-IMPL-MAPPINGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.sw_impl_mapping_refs.append(child_value)

        # Parse sw_mapping_refs (list from container "SW-MAPPINGS")
        obj.sw_mapping_refs = []
        container = ARObject._find_child_element(element, "SW-MAPPINGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.sw_mapping_refs.append(child_value)

        # Parse system_signal_group_to_refs (list from container "SYSTEM-SIGNAL-GROUP-TOS")
        obj.system_signal_group_to_refs = []
        container = ARObject._find_child_element(element, "SYSTEM-SIGNAL-GROUP-TOS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.system_signal_group_to_refs.append(child_value)

        # Parse system_signal_tos (list from container "SYSTEM-SIGNAL-TOS")
        obj.system_signal_tos = []
        container = ARObject._find_child_element(element, "SYSTEM-SIGNAL-TOS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.system_signal_tos.append(child_value)

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
