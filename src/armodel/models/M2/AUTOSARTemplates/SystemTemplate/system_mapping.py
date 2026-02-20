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

    def serialize(self) -> ET.Element:
        """Serialize SystemMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SystemMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize applications (list to container "APPLICATIONS")
        if self.applications:
            wrapper = ET.Element("APPLICATIONS")
            for item in self.applications:
                serialized = ARObject._serialize_item(item, "ApplicationPartitionToEcuPartitionMapping")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize app_os_tasks (list to container "APP-OS-TASKS")
        if self.app_os_tasks:
            wrapper = ET.Element("APP-OS-TASKS")
            for item in self.app_os_tasks:
                serialized = ARObject._serialize_item(item, "AppOsTaskProxyToEcuTaskProxyMapping")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize coms (list to container "COMS")
        if self.coms:
            wrapper = ET.Element("COMS")
            for item in self.coms:
                serialized = ARObject._serialize_item(item, "ComManagementMapping")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize crypto_service_refs (list to container "CRYPTO-SERVICE-REFS")
        if self.crypto_service_refs:
            wrapper = ET.Element("CRYPTO-SERVICE-REFS")
            for item in self.crypto_service_refs:
                serialized = ARObject._serialize_item(item, "CryptoServiceMapping")
                if serialized is not None:
                    child_elem = ET.Element("CRYPTO-SERVICE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize data_mapping_refs (list to container "DATA-MAPPING-REFS")
        if self.data_mapping_refs:
            wrapper = ET.Element("DATA-MAPPING-REFS")
            for item in self.data_mapping_refs:
                serialized = ARObject._serialize_item(item, "DataMapping")
                if serialized is not None:
                    child_elem = ET.Element("DATA-MAPPING-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize dds_i_signal_tos (list to container "DDS-I-SIGNAL-TOS")
        if self.dds_i_signal_tos:
            wrapper = ET.Element("DDS-I-SIGNAL-TOS")
            for item in self.dds_i_signal_tos:
                serialized = ARObject._serialize_item(item, "DdsCpISignalToDdsTopicMapping")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize ecu_resource_refs (list to container "ECU-RESOURCE-REFS")
        if self.ecu_resource_refs:
            wrapper = ET.Element("ECU-RESOURCE-REFS")
            for item in self.ecu_resource_refs:
                serialized = ARObject._serialize_item(item, "ECUMapping")
                if serialized is not None:
                    child_elem = ET.Element("ECU-RESOURCE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize j1939_controllers (list to container "J1939-CONTROLLERS")
        if self.j1939_controllers:
            wrapper = ET.Element("J1939-CONTROLLERS")
            for item in self.j1939_controllers:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize mapping_refs (list to container "MAPPING-REFS")
        if self.mapping_refs:
            wrapper = ET.Element("MAPPING-REFS")
            for item in self.mapping_refs:
                serialized = ARObject._serialize_item(item, "MappingConstraint")
                if serialized is not None:
                    child_elem = ET.Element("MAPPING-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize pnc_mapping_refs (list to container "PNC-MAPPING-REFS")
        if self.pnc_mapping_refs:
            wrapper = ET.Element("PNC-MAPPING-REFS")
            for item in self.pnc_mapping_refs:
                serialized = ARObject._serialize_item(item, "PncMapping")
                if serialized is not None:
                    child_elem = ET.Element("PNC-MAPPING-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize port_element_tos (list to container "PORT-ELEMENT-TOS")
        if self.port_element_tos:
            wrapper = ET.Element("PORT-ELEMENT-TOS")
            for item in self.port_element_tos:
                serialized = ARObject._serialize_item(item, "PortElementToCommunicationResourceMapping")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize resources (list to container "RESOURCES")
        if self.resources:
            wrapper = ET.Element("RESOURCES")
            for item in self.resources:
                serialized = ARObject._serialize_item(item, "EcuResourceEstimation")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize resource_tos (list to container "RESOURCE-TOS")
        if self.resource_tos:
            wrapper = ET.Element("RESOURCE-TOS")
            for item in self.resource_tos:
                serialized = ARObject._serialize_item(item, "CpSoftwareCluster")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize rte_event_in_systems (list to container "RTE-EVENT-IN-SYSTEMS")
        if self.rte_event_in_systems:
            wrapper = ET.Element("RTE-EVENT-IN-SYSTEMS")
            for item in self.rte_event_in_systems:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize rte_event_to_oses (list to container "RTE-EVENT-TO-OSES")
        if self.rte_event_to_oses:
            wrapper = ET.Element("RTE-EVENT-TO-OSES")
            for item in self.rte_event_to_oses:
                serialized = ARObject._serialize_item(item, "RteEventInSystemToOsTaskProxyMapping")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize signal_paths (list to container "SIGNAL-PATHS")
        if self.signal_paths:
            wrapper = ET.Element("SIGNAL-PATHS")
            for item in self.signal_paths:
                serialized = ARObject._serialize_item(item, "SignalPathConstraint")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize software_clusters (list to container "SOFTWARE-CLUSTERS")
        if self.software_clusters:
            wrapper = ET.Element("SOFTWARE-CLUSTERS")
            for item in self.software_clusters:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize sw_clusters (list to container "SW-CLUSTERS")
        if self.sw_clusters:
            wrapper = ET.Element("SW-CLUSTERS")
            for item in self.sw_clusters:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize swc_tos (list to container "SWC-TOS")
        if self.swc_tos:
            wrapper = ET.Element("SWC-TOS")
            for item in self.swc_tos:
                serialized = ARObject._serialize_item(item, "SwcToApplicationPartitionMapping")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize sw_impl_mapping_refs (list to container "SW-IMPL-MAPPING-REFS")
        if self.sw_impl_mapping_refs:
            wrapper = ET.Element("SW-IMPL-MAPPING-REFS")
            for item in self.sw_impl_mapping_refs:
                serialized = ARObject._serialize_item(item, "SwcToImplMapping")
                if serialized is not None:
                    child_elem = ET.Element("SW-IMPL-MAPPING-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize sw_mapping_refs (list to container "SW-MAPPING-REFS")
        if self.sw_mapping_refs:
            wrapper = ET.Element("SW-MAPPING-REFS")
            for item in self.sw_mapping_refs:
                serialized = ARObject._serialize_item(item, "SwcToEcuMapping")
                if serialized is not None:
                    child_elem = ET.Element("SW-MAPPING-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize system_signal_group_to_refs (list to container "SYSTEM-SIGNAL-GROUP-TO-REFS")
        if self.system_signal_group_to_refs:
            wrapper = ET.Element("SYSTEM-SIGNAL-GROUP-TO-REFS")
            for item in self.system_signal_group_to_refs:
                serialized = ARObject._serialize_item(item, "SystemSignalGroupToCommunicationResourceMapping")
                if serialized is not None:
                    child_elem = ET.Element("SYSTEM-SIGNAL-GROUP-TO-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize system_signal_tos (list to container "SYSTEM-SIGNAL-TOS")
        if self.system_signal_tos:
            wrapper = ET.Element("SYSTEM-SIGNAL-TOS")
            for item in self.system_signal_tos:
                serialized = ARObject._serialize_item(item, "SystemSignalToCommunicationResourceMapping")
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

        # Parse crypto_service_refs (list from container "CRYPTO-SERVICE-REFS")
        obj.crypto_service_refs = []
        container = ARObject._find_child_element(element, "CRYPTO-SERVICE-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.crypto_service_refs.append(child_value)

        # Parse data_mapping_refs (list from container "DATA-MAPPING-REFS")
        obj.data_mapping_refs = []
        container = ARObject._find_child_element(element, "DATA-MAPPING-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
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

        # Parse ecu_resource_refs (list from container "ECU-RESOURCE-REFS")
        obj.ecu_resource_refs = []
        container = ARObject._find_child_element(element, "ECU-RESOURCE-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
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

        # Parse mapping_refs (list from container "MAPPING-REFS")
        obj.mapping_refs = []
        container = ARObject._find_child_element(element, "MAPPING-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.mapping_refs.append(child_value)

        # Parse pnc_mapping_refs (list from container "PNC-MAPPING-REFS")
        obj.pnc_mapping_refs = []
        container = ARObject._find_child_element(element, "PNC-MAPPING-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
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

        # Parse sw_impl_mapping_refs (list from container "SW-IMPL-MAPPING-REFS")
        obj.sw_impl_mapping_refs = []
        container = ARObject._find_child_element(element, "SW-IMPL-MAPPING-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.sw_impl_mapping_refs.append(child_value)

        # Parse sw_mapping_refs (list from container "SW-MAPPING-REFS")
        obj.sw_mapping_refs = []
        container = ARObject._find_child_element(element, "SW-MAPPING-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.sw_mapping_refs.append(child_value)

        # Parse system_signal_group_to_refs (list from container "SYSTEM-SIGNAL-GROUP-TO-REFS")
        obj.system_signal_group_to_refs = []
        container = ARObject._find_child_element(element, "SYSTEM-SIGNAL-GROUP-TO-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
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
