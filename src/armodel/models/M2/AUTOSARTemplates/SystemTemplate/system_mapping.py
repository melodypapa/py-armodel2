"""SystemMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 190)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.RteEventToOsTaskMapping.app_os_task_proxy_to_ecu_task_proxy_mapping import (
    AppOsTaskProxyToEcuTaskProxyMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping.application_partition_to_ecu_partition_mapping import (
    ApplicationPartitionToEcuPartitionMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.com_management_mapping import (
    ComManagementMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster_resource_to_application_partition_mapping import (
    CpSoftwareClusterResourceToApplicationPartitionMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster_to_application_partition_mapping import (
    CpSoftwareClusterToApplicationPartitionMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster_to_ecu_instance_mapping import (
    CpSoftwareClusterToEcuInstanceMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster_to_resource_mapping import (
    CpSoftwareClusterToResourceMapping,
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
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping.j1939_controller_application_to_j1939_nm_node_mapping import (
    J1939ControllerApplicationToJ1939NmNodeMapping,
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
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.RteEventToOsTaskMapping.rte_event_in_system_separation import (
    RteEventInSystemSeparation,
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
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping.swc_to_impl_mapping import (
    SwcToImplMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.system_signal_group_to_communication_resource_mapping import (
    SystemSignalGroupToCommunicationResourceMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.system_signal_to_communication_resource_mapping import (
    SystemSignalToCommunicationResourceMapping,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping.ecu_resource_estimation import (
        EcuResourceEstimation,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping.swc_to_ecu_mapping import (
        SwcToEcuMapping,
    )



from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
class SystemMapping(Identifiable):
    """AUTOSAR SystemMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    application_partition_to_ecu_partition_mappings: list[ApplicationPartitionToEcuPartitionMapping]
    app_os_task_proxy_to_ecu_task_proxy_mappings: list[AppOsTaskProxyToEcuTaskProxyMapping]
    com_management_mappings: list[ComManagementMapping]
    crypto_service_mappings: list[CryptoServiceMapping]
    data_mappings: list[DataMapping]
    dds_i_signal_to_topic_mappings: list[DdsCpISignalToDdsTopicMapping]
    ecu_resources_mappings: list[ECUMapping]
    j1939_controller_application_to_j1939_nm_node_mappings: list[J1939ControllerApplicationToJ1939NmNodeMapping]
    mapping_constraints: list[MappingConstraint]
    pnc_mappings: list[PncMapping]
    port_element_to_com_resource_mappings: list[PortElementToCommunicationResourceMapping]
    resource_estimations: list[EcuResourceEstimation]
    resource_to_application_partition_mappings: list[CpSoftwareClusterResourceToApplicationPartitionMapping]
    rte_event_separations: list[RteEventInSystemSeparation]
    rte_event_to_os_task_proxy_mappings: list[RteEventInSystemToOsTaskProxyMapping]
    signal_path_constraints: list[SignalPathConstraint]
    software_cluster_to_application_partition_mappings: list[CpSoftwareClusterToApplicationPartitionMapping]
    sw_cluster_to_resource_mappings: list[CpSoftwareClusterToResourceMapping]
    sw_cluster_mappings: list[CpSoftwareClusterToEcuInstanceMapping]
    swc_to_application_partition_mappings: list[SwcToApplicationPartitionMapping]
    sw_impl_mappings: list[SwcToImplMapping]
    sw_mappings: list[SwcToEcuMapping]
    system_signal_group_to_com_resource_mappings: list[SystemSignalGroupToCommunicationResourceMapping]
    system_signal_to_com_resource_mappings: list[SystemSignalToCommunicationResourceMapping]
    def __init__(self) -> None:
        """Initialize SystemMapping."""
        super().__init__()
        self.application_partition_to_ecu_partition_mappings: list[ApplicationPartitionToEcuPartitionMapping] = []
        self.app_os_task_proxy_to_ecu_task_proxy_mappings: list[AppOsTaskProxyToEcuTaskProxyMapping] = []
        self.com_management_mappings: list[ComManagementMapping] = []
        self.crypto_service_mappings: list[CryptoServiceMapping] = []
        self.data_mappings: list[DataMapping] = []
        self.dds_i_signal_to_topic_mappings: list[DdsCpISignalToDdsTopicMapping] = []
        self.ecu_resources_mappings: list[ECUMapping] = []
        self.j1939_controller_application_to_j1939_nm_node_mappings: list[J1939ControllerApplicationToJ1939NmNodeMapping] = []
        self.mapping_constraints: list[MappingConstraint] = []
        self.pnc_mappings: list[PncMapping] = []
        self.port_element_to_com_resource_mappings: list[PortElementToCommunicationResourceMapping] = []
        self.resource_estimations: list[EcuResourceEstimation] = []
        self.resource_to_application_partition_mappings: list[CpSoftwareClusterResourceToApplicationPartitionMapping] = []
        self.rte_event_separations: list[RteEventInSystemSeparation] = []
        self.rte_event_to_os_task_proxy_mappings: list[RteEventInSystemToOsTaskProxyMapping] = []
        self.signal_path_constraints: list[SignalPathConstraint] = []
        self.software_cluster_to_application_partition_mappings: list[CpSoftwareClusterToApplicationPartitionMapping] = []
        self.sw_cluster_to_resource_mappings: list[CpSoftwareClusterToResourceMapping] = []
        self.sw_cluster_mappings: list[CpSoftwareClusterToEcuInstanceMapping] = []
        self.swc_to_application_partition_mappings: list[SwcToApplicationPartitionMapping] = []
        self.sw_impl_mappings: list[SwcToImplMapping] = []
        self.sw_mappings: list[SwcToEcuMapping] = []
        self.system_signal_group_to_com_resource_mappings: list[SystemSignalGroupToCommunicationResourceMapping] = []
        self.system_signal_to_com_resource_mappings: list[SystemSignalToCommunicationResourceMapping] = []

    def serialize(self) -> ET.Element:
        """Serialize SystemMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SystemMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize application_partition_to_ecu_partition_mappings (list to container "APPLICATION-PARTITION-TO-ECU-PARTITION-MAPPINGS")
        if self.application_partition_to_ecu_partition_mappings:
            wrapper = ET.Element("APPLICATION-PARTITION-TO-ECU-PARTITION-MAPPINGS")
            for item in self.application_partition_to_ecu_partition_mappings:
                serialized = SerializationHelper.serialize_item(item, "ApplicationPartitionToEcuPartitionMapping")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize app_os_task_proxy_to_ecu_task_proxy_mappings (list to container "APP-OS-TASK-PROXY-TO-ECU-TASK-PROXY-MAPPINGS")
        if self.app_os_task_proxy_to_ecu_task_proxy_mappings:
            wrapper = ET.Element("APP-OS-TASK-PROXY-TO-ECU-TASK-PROXY-MAPPINGS")
            for item in self.app_os_task_proxy_to_ecu_task_proxy_mappings:
                serialized = SerializationHelper.serialize_item(item, "AppOsTaskProxyToEcuTaskProxyMapping")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize com_management_mappings (list to container "COM-MANAGEMENT-MAPPINGS")
        if self.com_management_mappings:
            wrapper = ET.Element("COM-MANAGEMENT-MAPPINGS")
            for item in self.com_management_mappings:
                serialized = SerializationHelper.serialize_item(item, "ComManagementMapping")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize crypto_service_mappings (list to container "CRYPTO-SERVICE-MAPPINGS")
        if self.crypto_service_mappings:
            wrapper = ET.Element("CRYPTO-SERVICE-MAPPINGS")
            for item in self.crypto_service_mappings:
                serialized = SerializationHelper.serialize_item(item, "CryptoServiceMapping")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize data_mappings (list to container "DATA-MAPPINGS")
        if self.data_mappings:
            wrapper = ET.Element("DATA-MAPPINGS")
            for item in self.data_mappings:
                serialized = SerializationHelper.serialize_item(item, "DataMapping")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize dds_i_signal_to_topic_mappings (list to container "DDS-I-SIGNAL-TO-TOPIC-MAPPINGS")
        if self.dds_i_signal_to_topic_mappings:
            wrapper = ET.Element("DDS-I-SIGNAL-TO-TOPIC-MAPPINGS")
            for item in self.dds_i_signal_to_topic_mappings:
                serialized = SerializationHelper.serialize_item(item, "DdsCpISignalToDdsTopicMapping")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize ecu_resources_mappings (list to container "ECU-RESOURCES-MAPPINGS")
        if self.ecu_resources_mappings:
            wrapper = ET.Element("ECU-RESOURCES-MAPPINGS")
            for item in self.ecu_resources_mappings:
                serialized = SerializationHelper.serialize_item(item, "ECUMapping")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize j1939_controller_application_to_j1939_nm_node_mappings (list to container "J1939-CONTROLLER-APPLICATION-TO-J1939-NM-NODE-MAPPINGS")
        if self.j1939_controller_application_to_j1939_nm_node_mappings:
            wrapper = ET.Element("J1939-CONTROLLER-APPLICATION-TO-J1939-NM-NODE-MAPPINGS")
            for item in self.j1939_controller_application_to_j1939_nm_node_mappings:
                serialized = SerializationHelper.serialize_item(item, "J1939ControllerApplicationToJ1939NmNodeMapping")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize mapping_constraints (list to container "MAPPING-CONSTRAINTS")
        if self.mapping_constraints:
            wrapper = ET.Element("MAPPING-CONSTRAINTS")
            for item in self.mapping_constraints:
                serialized = SerializationHelper.serialize_item(item, "MappingConstraint")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize pnc_mappings (list to container "PNC-MAPPINGS")
        if self.pnc_mappings:
            wrapper = ET.Element("PNC-MAPPINGS")
            for item in self.pnc_mappings:
                serialized = SerializationHelper.serialize_item(item, "PncMapping")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize port_element_to_com_resource_mappings (list to container "PORT-ELEMENT-TO-COM-RESOURCE-MAPPINGS")
        if self.port_element_to_com_resource_mappings:
            wrapper = ET.Element("PORT-ELEMENT-TO-COM-RESOURCE-MAPPINGS")
            for item in self.port_element_to_com_resource_mappings:
                serialized = SerializationHelper.serialize_item(item, "PortElementToCommunicationResourceMapping")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize resource_estimations (list to container "RESOURCE-ESTIMATIONS")
        if self.resource_estimations:
            wrapper = ET.Element("RESOURCE-ESTIMATIONS")
            for item in self.resource_estimations:
                serialized = SerializationHelper.serialize_item(item, "EcuResourceEstimation")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize resource_to_application_partition_mappings (list to container "RESOURCE-TO-APPLICATION-PARTITION-MAPPINGS")
        if self.resource_to_application_partition_mappings:
            wrapper = ET.Element("RESOURCE-TO-APPLICATION-PARTITION-MAPPINGS")
            for item in self.resource_to_application_partition_mappings:
                serialized = SerializationHelper.serialize_item(item, "CpSoftwareClusterResourceToApplicationPartitionMapping")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize rte_event_separations (list to container "RTE-EVENT-SEPARATIONS")
        if self.rte_event_separations:
            wrapper = ET.Element("RTE-EVENT-SEPARATIONS")
            for item in self.rte_event_separations:
                serialized = SerializationHelper.serialize_item(item, "RteEventInSystemSeparation")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize rte_event_to_os_task_proxy_mappings (list to container "RTE-EVENT-TO-OS-TASK-PROXY-MAPPINGS")
        if self.rte_event_to_os_task_proxy_mappings:
            wrapper = ET.Element("RTE-EVENT-TO-OS-TASK-PROXY-MAPPINGS")
            for item in self.rte_event_to_os_task_proxy_mappings:
                serialized = SerializationHelper.serialize_item(item, "RteEventInSystemToOsTaskProxyMapping")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize signal_path_constraints (list to container "SIGNAL-PATH-CONSTRAINTS")
        if self.signal_path_constraints:
            wrapper = ET.Element("SIGNAL-PATH-CONSTRAINTS")
            for item in self.signal_path_constraints:
                serialized = SerializationHelper.serialize_item(item, "SignalPathConstraint")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize software_cluster_to_application_partition_mappings (list to container "SOFTWARE-CLUSTER-TO-APPLICATION-PARTITION-MAPPINGS")
        if self.software_cluster_to_application_partition_mappings:
            wrapper = ET.Element("SOFTWARE-CLUSTER-TO-APPLICATION-PARTITION-MAPPINGS")
            for item in self.software_cluster_to_application_partition_mappings:
                serialized = SerializationHelper.serialize_item(item, "CpSoftwareClusterToApplicationPartitionMapping")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize sw_cluster_to_resource_mappings (list to container "SW-CLUSTER-TO-RESOURCE-MAPPINGS")
        if self.sw_cluster_to_resource_mappings:
            wrapper = ET.Element("SW-CLUSTER-TO-RESOURCE-MAPPINGS")
            for item in self.sw_cluster_to_resource_mappings:
                serialized = SerializationHelper.serialize_item(item, "CpSoftwareClusterToResourceMapping")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize sw_cluster_mappings (list to container "SW-CLUSTER-MAPPINGS")
        if self.sw_cluster_mappings:
            wrapper = ET.Element("SW-CLUSTER-MAPPINGS")
            for item in self.sw_cluster_mappings:
                serialized = SerializationHelper.serialize_item(item, "CpSoftwareClusterToEcuInstanceMapping")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize swc_to_application_partition_mappings (list to container "SWC-TO-APPLICATION-PARTITION-MAPPINGS")
        if self.swc_to_application_partition_mappings:
            wrapper = ET.Element("SWC-TO-APPLICATION-PARTITION-MAPPINGS")
            for item in self.swc_to_application_partition_mappings:
                serialized = SerializationHelper.serialize_item(item, "SwcToApplicationPartitionMapping")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize sw_impl_mappings (list to container "SW-IMPL-MAPPINGS")
        if self.sw_impl_mappings:
            wrapper = ET.Element("SW-IMPL-MAPPINGS")
            for item in self.sw_impl_mappings:
                serialized = SerializationHelper.serialize_item(item, "SwcToImplMapping")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize sw_mappings (list to container "SW-MAPPINGS")
        if self.sw_mappings:
            wrapper = ET.Element("SW-MAPPINGS")
            for item in self.sw_mappings:
                serialized = SerializationHelper.serialize_item(item, "SwcToEcuMapping")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize system_signal_group_to_com_resource_mappings (list to container "SYSTEM-SIGNAL-GROUP-TO-COM-RESOURCE-MAPPINGS")
        if self.system_signal_group_to_com_resource_mappings:
            wrapper = ET.Element("SYSTEM-SIGNAL-GROUP-TO-COM-RESOURCE-MAPPINGS")
            for item in self.system_signal_group_to_com_resource_mappings:
                serialized = SerializationHelper.serialize_item(item, "SystemSignalGroupToCommunicationResourceMapping")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize system_signal_to_com_resource_mappings (list to container "SYSTEM-SIGNAL-TO-COM-RESOURCE-MAPPINGS")
        if self.system_signal_to_com_resource_mappings:
            wrapper = ET.Element("SYSTEM-SIGNAL-TO-COM-RESOURCE-MAPPINGS")
            for item in self.system_signal_to_com_resource_mappings:
                serialized = SerializationHelper.serialize_item(item, "SystemSignalToCommunicationResourceMapping")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

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

        # Parse application_partition_to_ecu_partition_mappings (list from container "APPLICATION-PARTITION-TO-ECU-PARTITION-MAPPINGS")
        obj.application_partition_to_ecu_partition_mappings = []
        container = SerializationHelper.find_child_element(element, "APPLICATION-PARTITION-TO-ECU-PARTITION-MAPPINGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.application_partition_to_ecu_partition_mappings.append(child_value)

        # Parse app_os_task_proxy_to_ecu_task_proxy_mappings (list from container "APP-OS-TASK-PROXY-TO-ECU-TASK-PROXY-MAPPINGS")
        obj.app_os_task_proxy_to_ecu_task_proxy_mappings = []
        container = SerializationHelper.find_child_element(element, "APP-OS-TASK-PROXY-TO-ECU-TASK-PROXY-MAPPINGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.app_os_task_proxy_to_ecu_task_proxy_mappings.append(child_value)

        # Parse com_management_mappings (list from container "COM-MANAGEMENT-MAPPINGS")
        obj.com_management_mappings = []
        container = SerializationHelper.find_child_element(element, "COM-MANAGEMENT-MAPPINGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.com_management_mappings.append(child_value)

        # Parse crypto_service_mappings (list from container "CRYPTO-SERVICE-MAPPINGS")
        obj.crypto_service_mappings = []
        container = SerializationHelper.find_child_element(element, "CRYPTO-SERVICE-MAPPINGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.crypto_service_mappings.append(child_value)

        # Parse data_mappings (list from container "DATA-MAPPINGS")
        obj.data_mappings = []
        container = SerializationHelper.find_child_element(element, "DATA-MAPPINGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.data_mappings.append(child_value)

        # Parse dds_i_signal_to_topic_mappings (list from container "DDS-I-SIGNAL-TO-TOPIC-MAPPINGS")
        obj.dds_i_signal_to_topic_mappings = []
        container = SerializationHelper.find_child_element(element, "DDS-I-SIGNAL-TO-TOPIC-MAPPINGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.dds_i_signal_to_topic_mappings.append(child_value)

        # Parse ecu_resources_mappings (list from container "ECU-RESOURCES-MAPPINGS")
        obj.ecu_resources_mappings = []
        container = SerializationHelper.find_child_element(element, "ECU-RESOURCES-MAPPINGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.ecu_resources_mappings.append(child_value)

        # Parse j1939_controller_application_to_j1939_nm_node_mappings (list from container "J1939-CONTROLLER-APPLICATION-TO-J1939-NM-NODE-MAPPINGS")
        obj.j1939_controller_application_to_j1939_nm_node_mappings = []
        container = SerializationHelper.find_child_element(element, "J1939-CONTROLLER-APPLICATION-TO-J1939-NM-NODE-MAPPINGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.j1939_controller_application_to_j1939_nm_node_mappings.append(child_value)

        # Parse mapping_constraints (list from container "MAPPING-CONSTRAINTS")
        obj.mapping_constraints = []
        container = SerializationHelper.find_child_element(element, "MAPPING-CONSTRAINTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.mapping_constraints.append(child_value)

        # Parse pnc_mappings (list from container "PNC-MAPPINGS")
        obj.pnc_mappings = []
        container = SerializationHelper.find_child_element(element, "PNC-MAPPINGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.pnc_mappings.append(child_value)

        # Parse port_element_to_com_resource_mappings (list from container "PORT-ELEMENT-TO-COM-RESOURCE-MAPPINGS")
        obj.port_element_to_com_resource_mappings = []
        container = SerializationHelper.find_child_element(element, "PORT-ELEMENT-TO-COM-RESOURCE-MAPPINGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.port_element_to_com_resource_mappings.append(child_value)

        # Parse resource_estimations (list from container "RESOURCE-ESTIMATIONS")
        obj.resource_estimations = []
        container = SerializationHelper.find_child_element(element, "RESOURCE-ESTIMATIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.resource_estimations.append(child_value)

        # Parse resource_to_application_partition_mappings (list from container "RESOURCE-TO-APPLICATION-PARTITION-MAPPINGS")
        obj.resource_to_application_partition_mappings = []
        container = SerializationHelper.find_child_element(element, "RESOURCE-TO-APPLICATION-PARTITION-MAPPINGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.resource_to_application_partition_mappings.append(child_value)

        # Parse rte_event_separations (list from container "RTE-EVENT-SEPARATIONS")
        obj.rte_event_separations = []
        container = SerializationHelper.find_child_element(element, "RTE-EVENT-SEPARATIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.rte_event_separations.append(child_value)

        # Parse rte_event_to_os_task_proxy_mappings (list from container "RTE-EVENT-TO-OS-TASK-PROXY-MAPPINGS")
        obj.rte_event_to_os_task_proxy_mappings = []
        container = SerializationHelper.find_child_element(element, "RTE-EVENT-TO-OS-TASK-PROXY-MAPPINGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.rte_event_to_os_task_proxy_mappings.append(child_value)

        # Parse signal_path_constraints (list from container "SIGNAL-PATH-CONSTRAINTS")
        obj.signal_path_constraints = []
        container = SerializationHelper.find_child_element(element, "SIGNAL-PATH-CONSTRAINTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.signal_path_constraints.append(child_value)

        # Parse software_cluster_to_application_partition_mappings (list from container "SOFTWARE-CLUSTER-TO-APPLICATION-PARTITION-MAPPINGS")
        obj.software_cluster_to_application_partition_mappings = []
        container = SerializationHelper.find_child_element(element, "SOFTWARE-CLUSTER-TO-APPLICATION-PARTITION-MAPPINGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.software_cluster_to_application_partition_mappings.append(child_value)

        # Parse sw_cluster_to_resource_mappings (list from container "SW-CLUSTER-TO-RESOURCE-MAPPINGS")
        obj.sw_cluster_to_resource_mappings = []
        container = SerializationHelper.find_child_element(element, "SW-CLUSTER-TO-RESOURCE-MAPPINGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.sw_cluster_to_resource_mappings.append(child_value)

        # Parse sw_cluster_mappings (list from container "SW-CLUSTER-MAPPINGS")
        obj.sw_cluster_mappings = []
        container = SerializationHelper.find_child_element(element, "SW-CLUSTER-MAPPINGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.sw_cluster_mappings.append(child_value)

        # Parse swc_to_application_partition_mappings (list from container "SWC-TO-APPLICATION-PARTITION-MAPPINGS")
        obj.swc_to_application_partition_mappings = []
        container = SerializationHelper.find_child_element(element, "SWC-TO-APPLICATION-PARTITION-MAPPINGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.swc_to_application_partition_mappings.append(child_value)

        # Parse sw_impl_mappings (list from container "SW-IMPL-MAPPINGS")
        obj.sw_impl_mappings = []
        container = SerializationHelper.find_child_element(element, "SW-IMPL-MAPPINGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.sw_impl_mappings.append(child_value)

        # Parse sw_mappings (list from container "SW-MAPPINGS")
        obj.sw_mappings = []
        container = SerializationHelper.find_child_element(element, "SW-MAPPINGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.sw_mappings.append(child_value)

        # Parse system_signal_group_to_com_resource_mappings (list from container "SYSTEM-SIGNAL-GROUP-TO-COM-RESOURCE-MAPPINGS")
        obj.system_signal_group_to_com_resource_mappings = []
        container = SerializationHelper.find_child_element(element, "SYSTEM-SIGNAL-GROUP-TO-COM-RESOURCE-MAPPINGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.system_signal_group_to_com_resource_mappings.append(child_value)

        # Parse system_signal_to_com_resource_mappings (list from container "SYSTEM-SIGNAL-TO-COM-RESOURCE-MAPPINGS")
        obj.system_signal_to_com_resource_mappings = []
        container = SerializationHelper.find_child_element(element, "SYSTEM-SIGNAL-TO-COM-RESOURCE-MAPPINGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.system_signal_to_com_resource_mappings.append(child_value)

        return obj



class SystemMappingBuilder(IdentifiableBuilder):
    """Builder for SystemMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SystemMapping = SystemMapping()


    def with_application_partition_to_ecu_partition_mappings(self, items: list[ApplicationPartitionToEcuPartitionMapping]) -> "SystemMappingBuilder":
        """Set application_partition_to_ecu_partition_mappings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.application_partition_to_ecu_partition_mappings = list(items) if items else []
        return self

    def with_app_os_task_proxy_to_ecu_task_proxy_mappings(self, items: list[AppOsTaskProxyToEcuTaskProxyMapping]) -> "SystemMappingBuilder":
        """Set app_os_task_proxy_to_ecu_task_proxy_mappings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.app_os_task_proxy_to_ecu_task_proxy_mappings = list(items) if items else []
        return self

    def with_com_management_mappings(self, items: list[ComManagementMapping]) -> "SystemMappingBuilder":
        """Set com_management_mappings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.com_management_mappings = list(items) if items else []
        return self

    def with_crypto_service_mappings(self, items: list[CryptoServiceMapping]) -> "SystemMappingBuilder":
        """Set crypto_service_mappings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.crypto_service_mappings = list(items) if items else []
        return self

    def with_data_mappings(self, items: list[DataMapping]) -> "SystemMappingBuilder":
        """Set data_mappings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.data_mappings = list(items) if items else []
        return self

    def with_dds_i_signal_to_topic_mappings(self, items: list[DdsCpISignalToDdsTopicMapping]) -> "SystemMappingBuilder":
        """Set dds_i_signal_to_topic_mappings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.dds_i_signal_to_topic_mappings = list(items) if items else []
        return self

    def with_ecu_resources_mappings(self, items: list[ECUMapping]) -> "SystemMappingBuilder":
        """Set ecu_resources_mappings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.ecu_resources_mappings = list(items) if items else []
        return self

    def with_j1939_controller_application_to_j1939_nm_node_mappings(self, items: list[J1939ControllerApplicationToJ1939NmNodeMapping]) -> "SystemMappingBuilder":
        """Set j1939_controller_application_to_j1939_nm_node_mappings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.j1939_controller_application_to_j1939_nm_node_mappings = list(items) if items else []
        return self

    def with_mapping_constraints(self, items: list[MappingConstraint]) -> "SystemMappingBuilder":
        """Set mapping_constraints list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.mapping_constraints = list(items) if items else []
        return self

    def with_pnc_mappings(self, items: list[PncMapping]) -> "SystemMappingBuilder":
        """Set pnc_mappings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.pnc_mappings = list(items) if items else []
        return self

    def with_port_element_to_com_resource_mappings(self, items: list[PortElementToCommunicationResourceMapping]) -> "SystemMappingBuilder":
        """Set port_element_to_com_resource_mappings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.port_element_to_com_resource_mappings = list(items) if items else []
        return self

    def with_resource_estimations(self, items: list[EcuResourceEstimation]) -> "SystemMappingBuilder":
        """Set resource_estimations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.resource_estimations = list(items) if items else []
        return self

    def with_resource_to_application_partition_mappings(self, items: list[CpSoftwareClusterResourceToApplicationPartitionMapping]) -> "SystemMappingBuilder":
        """Set resource_to_application_partition_mappings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.resource_to_application_partition_mappings = list(items) if items else []
        return self

    def with_rte_event_separations(self, items: list[RteEventInSystemSeparation]) -> "SystemMappingBuilder":
        """Set rte_event_separations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.rte_event_separations = list(items) if items else []
        return self

    def with_rte_event_to_os_task_proxy_mappings(self, items: list[RteEventInSystemToOsTaskProxyMapping]) -> "SystemMappingBuilder":
        """Set rte_event_to_os_task_proxy_mappings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.rte_event_to_os_task_proxy_mappings = list(items) if items else []
        return self

    def with_signal_path_constraints(self, items: list[SignalPathConstraint]) -> "SystemMappingBuilder":
        """Set signal_path_constraints list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.signal_path_constraints = list(items) if items else []
        return self

    def with_software_cluster_to_application_partition_mappings(self, items: list[CpSoftwareClusterToApplicationPartitionMapping]) -> "SystemMappingBuilder":
        """Set software_cluster_to_application_partition_mappings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.software_cluster_to_application_partition_mappings = list(items) if items else []
        return self

    def with_sw_cluster_to_resource_mappings(self, items: list[CpSoftwareClusterToResourceMapping]) -> "SystemMappingBuilder":
        """Set sw_cluster_to_resource_mappings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.sw_cluster_to_resource_mappings = list(items) if items else []
        return self

    def with_sw_cluster_mappings(self, items: list[CpSoftwareClusterToEcuInstanceMapping]) -> "SystemMappingBuilder":
        """Set sw_cluster_mappings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.sw_cluster_mappings = list(items) if items else []
        return self

    def with_swc_to_application_partition_mappings(self, items: list[SwcToApplicationPartitionMapping]) -> "SystemMappingBuilder":
        """Set swc_to_application_partition_mappings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.swc_to_application_partition_mappings = list(items) if items else []
        return self

    def with_sw_impl_mappings(self, items: list[SwcToImplMapping]) -> "SystemMappingBuilder":
        """Set sw_impl_mappings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.sw_impl_mappings = list(items) if items else []
        return self

    def with_sw_mappings(self, items: list[SwcToEcuMapping]) -> "SystemMappingBuilder":
        """Set sw_mappings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.sw_mappings = list(items) if items else []
        return self

    def with_system_signal_group_to_com_resource_mappings(self, items: list[SystemSignalGroupToCommunicationResourceMapping]) -> "SystemMappingBuilder":
        """Set system_signal_group_to_com_resource_mappings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.system_signal_group_to_com_resource_mappings = list(items) if items else []
        return self

    def with_system_signal_to_com_resource_mappings(self, items: list[SystemSignalToCommunicationResourceMapping]) -> "SystemMappingBuilder":
        """Set system_signal_to_com_resource_mappings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.system_signal_to_com_resource_mappings = list(items) if items else []
        return self


    def add_application_partition_to_ecu_partition_mapping(self, item: ApplicationPartitionToEcuPartitionMapping) -> "SystemMappingBuilder":
        """Add a single item to application_partition_to_ecu_partition_mappings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.application_partition_to_ecu_partition_mappings.append(item)
        return self

    def clear_application_partition_to_ecu_partition_mappings(self) -> "SystemMappingBuilder":
        """Clear all items from application_partition_to_ecu_partition_mappings list.

        Returns:
            self for method chaining
        """
        self._obj.application_partition_to_ecu_partition_mappings = []
        return self

    def add_app_os_task_proxy_to_ecu_task_proxy_mapping(self, item: AppOsTaskProxyToEcuTaskProxyMapping) -> "SystemMappingBuilder":
        """Add a single item to app_os_task_proxy_to_ecu_task_proxy_mappings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.app_os_task_proxy_to_ecu_task_proxy_mappings.append(item)
        return self

    def clear_app_os_task_proxy_to_ecu_task_proxy_mappings(self) -> "SystemMappingBuilder":
        """Clear all items from app_os_task_proxy_to_ecu_task_proxy_mappings list.

        Returns:
            self for method chaining
        """
        self._obj.app_os_task_proxy_to_ecu_task_proxy_mappings = []
        return self

    def add_com_management_mapping(self, item: ComManagementMapping) -> "SystemMappingBuilder":
        """Add a single item to com_management_mappings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.com_management_mappings.append(item)
        return self

    def clear_com_management_mappings(self) -> "SystemMappingBuilder":
        """Clear all items from com_management_mappings list.

        Returns:
            self for method chaining
        """
        self._obj.com_management_mappings = []
        return self

    def add_crypto_service_mapping(self, item: CryptoServiceMapping) -> "SystemMappingBuilder":
        """Add a single item to crypto_service_mappings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.crypto_service_mappings.append(item)
        return self

    def clear_crypto_service_mappings(self) -> "SystemMappingBuilder":
        """Clear all items from crypto_service_mappings list.

        Returns:
            self for method chaining
        """
        self._obj.crypto_service_mappings = []
        return self

    def add_data_mapping(self, item: DataMapping) -> "SystemMappingBuilder":
        """Add a single item to data_mappings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.data_mappings.append(item)
        return self

    def clear_data_mappings(self) -> "SystemMappingBuilder":
        """Clear all items from data_mappings list.

        Returns:
            self for method chaining
        """
        self._obj.data_mappings = []
        return self

    def add_dds_i_signal_to_topic_mapping(self, item: DdsCpISignalToDdsTopicMapping) -> "SystemMappingBuilder":
        """Add a single item to dds_i_signal_to_topic_mappings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.dds_i_signal_to_topic_mappings.append(item)
        return self

    def clear_dds_i_signal_to_topic_mappings(self) -> "SystemMappingBuilder":
        """Clear all items from dds_i_signal_to_topic_mappings list.

        Returns:
            self for method chaining
        """
        self._obj.dds_i_signal_to_topic_mappings = []
        return self

    def add_ecu_resources_mapping(self, item: ECUMapping) -> "SystemMappingBuilder":
        """Add a single item to ecu_resources_mappings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.ecu_resources_mappings.append(item)
        return self

    def clear_ecu_resources_mappings(self) -> "SystemMappingBuilder":
        """Clear all items from ecu_resources_mappings list.

        Returns:
            self for method chaining
        """
        self._obj.ecu_resources_mappings = []
        return self

    def add_j1939_controller_application_to_j1939_nm_node_mapping(self, item: J1939ControllerApplicationToJ1939NmNodeMapping) -> "SystemMappingBuilder":
        """Add a single item to j1939_controller_application_to_j1939_nm_node_mappings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.j1939_controller_application_to_j1939_nm_node_mappings.append(item)
        return self

    def clear_j1939_controller_application_to_j1939_nm_node_mappings(self) -> "SystemMappingBuilder":
        """Clear all items from j1939_controller_application_to_j1939_nm_node_mappings list.

        Returns:
            self for method chaining
        """
        self._obj.j1939_controller_application_to_j1939_nm_node_mappings = []
        return self

    def add_mapping_constraint(self, item: MappingConstraint) -> "SystemMappingBuilder":
        """Add a single item to mapping_constraints list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.mapping_constraints.append(item)
        return self

    def clear_mapping_constraints(self) -> "SystemMappingBuilder":
        """Clear all items from mapping_constraints list.

        Returns:
            self for method chaining
        """
        self._obj.mapping_constraints = []
        return self

    def add_pnc_mapping(self, item: PncMapping) -> "SystemMappingBuilder":
        """Add a single item to pnc_mappings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.pnc_mappings.append(item)
        return self

    def clear_pnc_mappings(self) -> "SystemMappingBuilder":
        """Clear all items from pnc_mappings list.

        Returns:
            self for method chaining
        """
        self._obj.pnc_mappings = []
        return self

    def add_port_element_to_com_resource_mapping(self, item: PortElementToCommunicationResourceMapping) -> "SystemMappingBuilder":
        """Add a single item to port_element_to_com_resource_mappings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.port_element_to_com_resource_mappings.append(item)
        return self

    def clear_port_element_to_com_resource_mappings(self) -> "SystemMappingBuilder":
        """Clear all items from port_element_to_com_resource_mappings list.

        Returns:
            self for method chaining
        """
        self._obj.port_element_to_com_resource_mappings = []
        return self

    def add_resource_estimation(self, item: EcuResourceEstimation) -> "SystemMappingBuilder":
        """Add a single item to resource_estimations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.resource_estimations.append(item)
        return self

    def clear_resource_estimations(self) -> "SystemMappingBuilder":
        """Clear all items from resource_estimations list.

        Returns:
            self for method chaining
        """
        self._obj.resource_estimations = []
        return self

    def add_resource_to_application_partition_mapping(self, item: CpSoftwareClusterResourceToApplicationPartitionMapping) -> "SystemMappingBuilder":
        """Add a single item to resource_to_application_partition_mappings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.resource_to_application_partition_mappings.append(item)
        return self

    def clear_resource_to_application_partition_mappings(self) -> "SystemMappingBuilder":
        """Clear all items from resource_to_application_partition_mappings list.

        Returns:
            self for method chaining
        """
        self._obj.resource_to_application_partition_mappings = []
        return self

    def add_rte_event_separation(self, item: RteEventInSystemSeparation) -> "SystemMappingBuilder":
        """Add a single item to rte_event_separations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.rte_event_separations.append(item)
        return self

    def clear_rte_event_separations(self) -> "SystemMappingBuilder":
        """Clear all items from rte_event_separations list.

        Returns:
            self for method chaining
        """
        self._obj.rte_event_separations = []
        return self

    def add_rte_event_to_os_task_proxy_mapping(self, item: RteEventInSystemToOsTaskProxyMapping) -> "SystemMappingBuilder":
        """Add a single item to rte_event_to_os_task_proxy_mappings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.rte_event_to_os_task_proxy_mappings.append(item)
        return self

    def clear_rte_event_to_os_task_proxy_mappings(self) -> "SystemMappingBuilder":
        """Clear all items from rte_event_to_os_task_proxy_mappings list.

        Returns:
            self for method chaining
        """
        self._obj.rte_event_to_os_task_proxy_mappings = []
        return self

    def add_signal_path_constraint(self, item: SignalPathConstraint) -> "SystemMappingBuilder":
        """Add a single item to signal_path_constraints list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.signal_path_constraints.append(item)
        return self

    def clear_signal_path_constraints(self) -> "SystemMappingBuilder":
        """Clear all items from signal_path_constraints list.

        Returns:
            self for method chaining
        """
        self._obj.signal_path_constraints = []
        return self

    def add_software_cluster_to_application_partition_mapping(self, item: CpSoftwareClusterToApplicationPartitionMapping) -> "SystemMappingBuilder":
        """Add a single item to software_cluster_to_application_partition_mappings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.software_cluster_to_application_partition_mappings.append(item)
        return self

    def clear_software_cluster_to_application_partition_mappings(self) -> "SystemMappingBuilder":
        """Clear all items from software_cluster_to_application_partition_mappings list.

        Returns:
            self for method chaining
        """
        self._obj.software_cluster_to_application_partition_mappings = []
        return self

    def add_sw_cluster_to_resource_mapping(self, item: CpSoftwareClusterToResourceMapping) -> "SystemMappingBuilder":
        """Add a single item to sw_cluster_to_resource_mappings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.sw_cluster_to_resource_mappings.append(item)
        return self

    def clear_sw_cluster_to_resource_mappings(self) -> "SystemMappingBuilder":
        """Clear all items from sw_cluster_to_resource_mappings list.

        Returns:
            self for method chaining
        """
        self._obj.sw_cluster_to_resource_mappings = []
        return self

    def add_sw_cluster_mapping(self, item: CpSoftwareClusterToEcuInstanceMapping) -> "SystemMappingBuilder":
        """Add a single item to sw_cluster_mappings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.sw_cluster_mappings.append(item)
        return self

    def clear_sw_cluster_mappings(self) -> "SystemMappingBuilder":
        """Clear all items from sw_cluster_mappings list.

        Returns:
            self for method chaining
        """
        self._obj.sw_cluster_mappings = []
        return self

    def add_swc_to_application_partition_mapping(self, item: SwcToApplicationPartitionMapping) -> "SystemMappingBuilder":
        """Add a single item to swc_to_application_partition_mappings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.swc_to_application_partition_mappings.append(item)
        return self

    def clear_swc_to_application_partition_mappings(self) -> "SystemMappingBuilder":
        """Clear all items from swc_to_application_partition_mappings list.

        Returns:
            self for method chaining
        """
        self._obj.swc_to_application_partition_mappings = []
        return self

    def add_sw_impl_mapping(self, item: SwcToImplMapping) -> "SystemMappingBuilder":
        """Add a single item to sw_impl_mappings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.sw_impl_mappings.append(item)
        return self

    def clear_sw_impl_mappings(self) -> "SystemMappingBuilder":
        """Clear all items from sw_impl_mappings list.

        Returns:
            self for method chaining
        """
        self._obj.sw_impl_mappings = []
        return self

    def add_sw_mapping(self, item: SwcToEcuMapping) -> "SystemMappingBuilder":
        """Add a single item to sw_mappings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.sw_mappings.append(item)
        return self

    def clear_sw_mappings(self) -> "SystemMappingBuilder":
        """Clear all items from sw_mappings list.

        Returns:
            self for method chaining
        """
        self._obj.sw_mappings = []
        return self

    def add_system_signal_group_to_com_resource_mapping(self, item: SystemSignalGroupToCommunicationResourceMapping) -> "SystemMappingBuilder":
        """Add a single item to system_signal_group_to_com_resource_mappings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.system_signal_group_to_com_resource_mappings.append(item)
        return self

    def clear_system_signal_group_to_com_resource_mappings(self) -> "SystemMappingBuilder":
        """Clear all items from system_signal_group_to_com_resource_mappings list.

        Returns:
            self for method chaining
        """
        self._obj.system_signal_group_to_com_resource_mappings = []
        return self

    def add_system_signal_to_com_resource_mapping(self, item: SystemSignalToCommunicationResourceMapping) -> "SystemMappingBuilder":
        """Add a single item to system_signal_to_com_resource_mappings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.system_signal_to_com_resource_mappings.append(item)
        return self

    def clear_system_signal_to_com_resource_mappings(self) -> "SystemMappingBuilder":
        """Clear all items from system_signal_to_com_resource_mappings list.

        Returns:
            self for method chaining
        """
        self._obj.system_signal_to_com_resource_mappings = []
        return self



    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Get type hints for the class
        try:
            type_hints_dict = get_type_hints(type(self._obj))
        except Exception:
            # Cannot resolve type hints (e.g., forward references), skip validation
            return

        for attr_name, attr_type in type_hints_dict.items():
            if attr_name.startswith("_"):
                continue

            value = getattr(self._obj, attr_name)

            # Check required fields (not Optional)
            if value is None and not self._is_optional_type(attr_type):
                if mode == BuilderValidationMode.STRICT:
                    raise ValueError(
                        f"Required attribute '{attr_name}' is None"
                    )
                elif mode == BuilderValidationMode.LENIENT:
                    import warnings
                    warnings.warn(
                        f"Required attribute '{attr_name}' is None",
                        UserWarning
                    )

    @staticmethod
    def _is_optional_type(type_hint: Any) -> bool:
        """Check if a type hint is Optional.

        Args:
            type_hint: Type hint to check

        Returns:
            True if type is Optional, False otherwise
        """
        origin = getattr(type_hint, "__origin__", None)
        return origin is Union

    @staticmethod
    def _get_expected_type(type_hint: Any) -> type:
        """Extract expected type from type hint.

        Args:
            type_hint: Type hint to extract from

        Returns:
            Expected type
        """
        if isinstance(type_hint, str):
            return object
        origin = getattr(type_hint, "__origin__", None)
        if origin is Union:
            args = getattr(type_hint, "__args__", [])
            for arg in args:
                if arg is not type(None):
                    return arg
        elif origin is list:
            args = getattr(type_hint, "__args__", [object])
            return args[0] if args else object
        return type_hint if isinstance(type_hint, type) else object


    def build(self) -> SystemMapping:
        """Build and return the SystemMapping instance with validation."""
        self._validate_instance()
        pass
        return self._obj