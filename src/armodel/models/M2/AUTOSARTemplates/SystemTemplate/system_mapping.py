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
from armodel.serialization import SerializationHelper
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

        # Serialize applications (list to container "APPLICATIONS")
        if self.applications:
            wrapper = ET.Element("APPLICATIONS")
            for item in self.applications:
                serialized = SerializationHelper.serialize_item(item, "ApplicationPartitionToEcuPartitionMapping")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize app_os_tasks (list to container "APP-OS-TASKS")
        if self.app_os_tasks:
            wrapper = ET.Element("APP-OS-TASKS")
            for item in self.app_os_tasks:
                serialized = SerializationHelper.serialize_item(item, "AppOsTaskProxyToEcuTaskProxyMapping")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize coms (list to container "COMS")
        if self.coms:
            wrapper = ET.Element("COMS")
            for item in self.coms:
                serialized = SerializationHelper.serialize_item(item, "ComManagementMapping")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize crypto_service_refs (list to container "CRYPTO-SERVICE-REFS")
        if self.crypto_service_refs:
            wrapper = ET.Element("CRYPTO-SERVICE-REFS")
            for item in self.crypto_service_refs:
                serialized = SerializationHelper.serialize_item(item, "CryptoServiceMapping")
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
                serialized = SerializationHelper.serialize_item(item, "DataMapping")
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
                serialized = SerializationHelper.serialize_item(item, "DdsCpISignalToDdsTopicMapping")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize ecu_resource_refs (list to container "ECU-RESOURCE-REFS")
        if self.ecu_resource_refs:
            wrapper = ET.Element("ECU-RESOURCE-REFS")
            for item in self.ecu_resource_refs:
                serialized = SerializationHelper.serialize_item(item, "ECUMapping")
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
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize mapping_refs (list to container "MAPPING-REFS")
        if self.mapping_refs:
            wrapper = ET.Element("MAPPING-REFS")
            for item in self.mapping_refs:
                serialized = SerializationHelper.serialize_item(item, "MappingConstraint")
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
                serialized = SerializationHelper.serialize_item(item, "PncMapping")
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
                serialized = SerializationHelper.serialize_item(item, "PortElementToCommunicationResourceMapping")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize resources (list to container "RESOURCES")
        if self.resources:
            wrapper = ET.Element("RESOURCES")
            for item in self.resources:
                serialized = SerializationHelper.serialize_item(item, "EcuResourceEstimation")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize resource_tos (list to container "RESOURCE-TOS")
        if self.resource_tos:
            wrapper = ET.Element("RESOURCE-TOS")
            for item in self.resource_tos:
                serialized = SerializationHelper.serialize_item(item, "CpSoftwareCluster")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize rte_event_in_systems (list to container "RTE-EVENT-IN-SYSTEMS")
        if self.rte_event_in_systems:
            wrapper = ET.Element("RTE-EVENT-IN-SYSTEMS")
            for item in self.rte_event_in_systems:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize rte_event_to_oses (list to container "RTE-EVENT-TO-OSES")
        if self.rte_event_to_oses:
            wrapper = ET.Element("RTE-EVENT-TO-OSES")
            for item in self.rte_event_to_oses:
                serialized = SerializationHelper.serialize_item(item, "RteEventInSystemToOsTaskProxyMapping")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize signal_paths (list to container "SIGNAL-PATHS")
        if self.signal_paths:
            wrapper = ET.Element("SIGNAL-PATHS")
            for item in self.signal_paths:
                serialized = SerializationHelper.serialize_item(item, "SignalPathConstraint")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize software_clusters (list to container "SOFTWARE-CLUSTERS")
        if self.software_clusters:
            wrapper = ET.Element("SOFTWARE-CLUSTERS")
            for item in self.software_clusters:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize sw_clusters (list to container "SW-CLUSTERS")
        if self.sw_clusters:
            wrapper = ET.Element("SW-CLUSTERS")
            for item in self.sw_clusters:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize swc_tos (list to container "SWC-TOS")
        if self.swc_tos:
            wrapper = ET.Element("SWC-TOS")
            for item in self.swc_tos:
                serialized = SerializationHelper.serialize_item(item, "SwcToApplicationPartitionMapping")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize sw_impl_mapping_refs (list to container "SW-IMPL-MAPPING-REFS")
        if self.sw_impl_mapping_refs:
            wrapper = ET.Element("SW-IMPL-MAPPING-REFS")
            for item in self.sw_impl_mapping_refs:
                serialized = SerializationHelper.serialize_item(item, "SwcToImplMapping")
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
                serialized = SerializationHelper.serialize_item(item, "SwcToEcuMapping")
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
                serialized = SerializationHelper.serialize_item(item, "SystemSignalGroupToCommunicationResourceMapping")
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

        # Parse applications (list from container "APPLICATIONS")
        obj.applications = []
        container = SerializationHelper.find_child_element(element, "APPLICATIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.applications.append(child_value)

        # Parse app_os_tasks (list from container "APP-OS-TASKS")
        obj.app_os_tasks = []
        container = SerializationHelper.find_child_element(element, "APP-OS-TASKS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.app_os_tasks.append(child_value)

        # Parse coms (list from container "COMS")
        obj.coms = []
        container = SerializationHelper.find_child_element(element, "COMS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.coms.append(child_value)

        # Parse crypto_service_refs (list from container "CRYPTO-SERVICE-REFS")
        obj.crypto_service_refs = []
        container = SerializationHelper.find_child_element(element, "CRYPTO-SERVICE-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.crypto_service_refs.append(child_value)

        # Parse data_mapping_refs (list from container "DATA-MAPPING-REFS")
        obj.data_mapping_refs = []
        container = SerializationHelper.find_child_element(element, "DATA-MAPPING-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.data_mapping_refs.append(child_value)

        # Parse dds_i_signal_tos (list from container "DDS-I-SIGNAL-TOS")
        obj.dds_i_signal_tos = []
        container = SerializationHelper.find_child_element(element, "DDS-I-SIGNAL-TOS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.dds_i_signal_tos.append(child_value)

        # Parse ecu_resource_refs (list from container "ECU-RESOURCE-REFS")
        obj.ecu_resource_refs = []
        container = SerializationHelper.find_child_element(element, "ECU-RESOURCE-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.ecu_resource_refs.append(child_value)

        # Parse j1939_controllers (list from container "J1939-CONTROLLERS")
        obj.j1939_controllers = []
        container = SerializationHelper.find_child_element(element, "J1939-CONTROLLERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.j1939_controllers.append(child_value)

        # Parse mapping_refs (list from container "MAPPING-REFS")
        obj.mapping_refs = []
        container = SerializationHelper.find_child_element(element, "MAPPING-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.mapping_refs.append(child_value)

        # Parse pnc_mapping_refs (list from container "PNC-MAPPING-REFS")
        obj.pnc_mapping_refs = []
        container = SerializationHelper.find_child_element(element, "PNC-MAPPING-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.pnc_mapping_refs.append(child_value)

        # Parse port_element_tos (list from container "PORT-ELEMENT-TOS")
        obj.port_element_tos = []
        container = SerializationHelper.find_child_element(element, "PORT-ELEMENT-TOS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.port_element_tos.append(child_value)

        # Parse resources (list from container "RESOURCES")
        obj.resources = []
        container = SerializationHelper.find_child_element(element, "RESOURCES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.resources.append(child_value)

        # Parse resource_tos (list from container "RESOURCE-TOS")
        obj.resource_tos = []
        container = SerializationHelper.find_child_element(element, "RESOURCE-TOS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.resource_tos.append(child_value)

        # Parse rte_event_in_systems (list from container "RTE-EVENT-IN-SYSTEMS")
        obj.rte_event_in_systems = []
        container = SerializationHelper.find_child_element(element, "RTE-EVENT-IN-SYSTEMS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.rte_event_in_systems.append(child_value)

        # Parse rte_event_to_oses (list from container "RTE-EVENT-TO-OSES")
        obj.rte_event_to_oses = []
        container = SerializationHelper.find_child_element(element, "RTE-EVENT-TO-OSES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.rte_event_to_oses.append(child_value)

        # Parse signal_paths (list from container "SIGNAL-PATHS")
        obj.signal_paths = []
        container = SerializationHelper.find_child_element(element, "SIGNAL-PATHS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.signal_paths.append(child_value)

        # Parse software_clusters (list from container "SOFTWARE-CLUSTERS")
        obj.software_clusters = []
        container = SerializationHelper.find_child_element(element, "SOFTWARE-CLUSTERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.software_clusters.append(child_value)

        # Parse sw_clusters (list from container "SW-CLUSTERS")
        obj.sw_clusters = []
        container = SerializationHelper.find_child_element(element, "SW-CLUSTERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.sw_clusters.append(child_value)

        # Parse swc_tos (list from container "SWC-TOS")
        obj.swc_tos = []
        container = SerializationHelper.find_child_element(element, "SWC-TOS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.swc_tos.append(child_value)

        # Parse sw_impl_mapping_refs (list from container "SW-IMPL-MAPPING-REFS")
        obj.sw_impl_mapping_refs = []
        container = SerializationHelper.find_child_element(element, "SW-IMPL-MAPPING-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.sw_impl_mapping_refs.append(child_value)

        # Parse sw_mapping_refs (list from container "SW-MAPPING-REFS")
        obj.sw_mapping_refs = []
        container = SerializationHelper.find_child_element(element, "SW-MAPPING-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.sw_mapping_refs.append(child_value)

        # Parse system_signal_group_to_refs (list from container "SYSTEM-SIGNAL-GROUP-TO-REFS")
        obj.system_signal_group_to_refs = []
        container = SerializationHelper.find_child_element(element, "SYSTEM-SIGNAL-GROUP-TO-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.system_signal_group_to_refs.append(child_value)

        # Parse system_signal_tos (list from container "SYSTEM-SIGNAL-TOS")
        obj.system_signal_tos = []
        container = SerializationHelper.find_child_element(element, "SYSTEM-SIGNAL-TOS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.system_signal_tos.append(child_value)

        return obj



class SystemMappingBuilder:
    """Builder for SystemMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: SystemMapping = SystemMapping()


    def with_short_name(self, value: Identifier) -> "SystemMappingBuilder":
        """Set short_name attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.short_name = value
        return self

    def with_short_name_fragments(self, items: list[ShortNameFragment]) -> "SystemMappingBuilder":
        """Set short_name_fragments list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = list(items) if items else []
        return self

    def with_long_name(self, value: Optional[MultilanguageLongName]) -> "SystemMappingBuilder":
        """Set long_name attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.long_name = value
        return self

    def with_admin_data(self, value: Optional[AdminData]) -> "SystemMappingBuilder":
        """Set admin_data attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.admin_data = value
        return self

    def with_annotations(self, items: list[Annotation]) -> "SystemMappingBuilder":
        """Set annotations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.annotations = list(items) if items else []
        return self

    def with_desc(self, value: Optional[MultiLanguageOverviewParagraph]) -> "SystemMappingBuilder":
        """Set desc attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.desc = value
        return self

    def with_category(self, value: Optional[CategoryString]) -> "SystemMappingBuilder":
        """Set category attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.category = value
        return self

    def with_introduction(self, value: Optional[DocumentationBlock]) -> "SystemMappingBuilder":
        """Set introduction attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.introduction = value
        return self

    def with_uuid(self, value: Optional[String]) -> "SystemMappingBuilder":
        """Set uuid attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.uuid = value
        return self

    def with_applications(self, items: list[ApplicationPartitionToEcuPartitionMapping]) -> "SystemMappingBuilder":
        """Set applications list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.applications = list(items) if items else []
        return self

    def with_app_os_tasks(self, items: list[AppOsTaskProxyToEcuTaskProxyMapping]) -> "SystemMappingBuilder":
        """Set app_os_tasks list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.app_os_tasks = list(items) if items else []
        return self

    def with_coms(self, items: list[ComManagementMapping]) -> "SystemMappingBuilder":
        """Set coms list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.coms = list(items) if items else []
        return self

    def with_crypto_services(self, items: list[CryptoServiceMapping]) -> "SystemMappingBuilder":
        """Set crypto_services list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.crypto_services = list(items) if items else []
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

    def with_dds_i_signal_tos(self, items: list[DdsCpISignalToDdsTopicMapping]) -> "SystemMappingBuilder":
        """Set dds_i_signal_tos list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.dds_i_signal_tos = list(items) if items else []
        return self

    def with_ecu_resources(self, items: list[ECUMapping]) -> "SystemMappingBuilder":
        """Set ecu_resources list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.ecu_resources = list(items) if items else []
        return self

    def with_j1939_controllers(self, items: list[any (J1939Controller)]) -> "SystemMappingBuilder":
        """Set j1939_controllers list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.j1939_controllers = list(items) if items else []
        return self

    def with_mappings(self, items: list[MappingConstraint]) -> "SystemMappingBuilder":
        """Set mappings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.mappings = list(items) if items else []
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

    def with_port_element_tos(self, items: list[PortElementToCommunicationResourceMapping]) -> "SystemMappingBuilder":
        """Set port_element_tos list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.port_element_tos = list(items) if items else []
        return self

    def with_resources(self, items: list[EcuResourceEstimation]) -> "SystemMappingBuilder":
        """Set resources list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.resources = list(items) if items else []
        return self

    def with_resource_tos(self, items: list[CpSoftwareCluster]) -> "SystemMappingBuilder":
        """Set resource_tos list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.resource_tos = list(items) if items else []
        return self

    def with_rte_event_in_systems(self, items: list[any (RteEventInSystem)]) -> "SystemMappingBuilder":
        """Set rte_event_in_systems list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.rte_event_in_systems = list(items) if items else []
        return self

    def with_rte_event_to_oses(self, items: list[RteEventInSystemToOsTaskProxyMapping]) -> "SystemMappingBuilder":
        """Set rte_event_to_oses list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.rte_event_to_oses = list(items) if items else []
        return self

    def with_signal_paths(self, items: list[SignalPathConstraint]) -> "SystemMappingBuilder":
        """Set signal_paths list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.signal_paths = list(items) if items else []
        return self

    def with_software_clusters(self, items: list[any (CpSoftwareClusterTo)]) -> "SystemMappingBuilder":
        """Set software_clusters list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.software_clusters = list(items) if items else []
        return self

    def with_sw_clusters(self, items: list[any (CpSoftwareClusterTo)]) -> "SystemMappingBuilder":
        """Set sw_clusters list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.sw_clusters = list(items) if items else []
        return self

    def with_swc_tos(self, items: list[SwcToApplicationPartitionMapping]) -> "SystemMappingBuilder":
        """Set swc_tos list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.swc_tos = list(items) if items else []
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

    def with_system_signal_group_tos(self, items: list[SystemSignalGroupToCommunicationResourceMapping]) -> "SystemMappingBuilder":
        """Set system_signal_group_tos list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.system_signal_group_tos = list(items) if items else []
        return self

    def with_system_signal_tos(self, items: list[SystemSignalToCommunicationResourceMapping]) -> "SystemMappingBuilder":
        """Set system_signal_tos list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.system_signal_tos = list(items) if items else []
        return self


    def add_short_name_fragment(self, item: ShortNameFragment) -> "SystemMappingBuilder":
        """Add a single item to short_name_fragments list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments.append(item)
        return self

    def clear_short_name_fragments(self) -> "SystemMappingBuilder":
        """Clear all items from short_name_fragments list.

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = []
        return self

    def add_annotation(self, item: Annotation) -> "SystemMappingBuilder":
        """Add a single item to annotations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.annotations.append(item)
        return self

    def clear_annotations(self) -> "SystemMappingBuilder":
        """Clear all items from annotations list.

        Returns:
            self for method chaining
        """
        self._obj.annotations = []
        return self

    def add_application(self, item: ApplicationPartitionToEcuPartitionMapping) -> "SystemMappingBuilder":
        """Add a single item to applications list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.applications.append(item)
        return self

    def clear_applications(self) -> "SystemMappingBuilder":
        """Clear all items from applications list.

        Returns:
            self for method chaining
        """
        self._obj.applications = []
        return self

    def add_app_os_task(self, item: AppOsTaskProxyToEcuTaskProxyMapping) -> "SystemMappingBuilder":
        """Add a single item to app_os_tasks list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.app_os_tasks.append(item)
        return self

    def clear_app_os_tasks(self) -> "SystemMappingBuilder":
        """Clear all items from app_os_tasks list.

        Returns:
            self for method chaining
        """
        self._obj.app_os_tasks = []
        return self

    def add_com(self, item: ComManagementMapping) -> "SystemMappingBuilder":
        """Add a single item to coms list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.coms.append(item)
        return self

    def clear_coms(self) -> "SystemMappingBuilder":
        """Clear all items from coms list.

        Returns:
            self for method chaining
        """
        self._obj.coms = []
        return self

    def add_crypto_service(self, item: CryptoServiceMapping) -> "SystemMappingBuilder":
        """Add a single item to crypto_services list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.crypto_services.append(item)
        return self

    def clear_crypto_services(self) -> "SystemMappingBuilder":
        """Clear all items from crypto_services list.

        Returns:
            self for method chaining
        """
        self._obj.crypto_services = []
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

    def add_dds_i_signal_to(self, item: DdsCpISignalToDdsTopicMapping) -> "SystemMappingBuilder":
        """Add a single item to dds_i_signal_tos list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.dds_i_signal_tos.append(item)
        return self

    def clear_dds_i_signal_tos(self) -> "SystemMappingBuilder":
        """Clear all items from dds_i_signal_tos list.

        Returns:
            self for method chaining
        """
        self._obj.dds_i_signal_tos = []
        return self

    def add_ecu_resource(self, item: ECUMapping) -> "SystemMappingBuilder":
        """Add a single item to ecu_resources list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.ecu_resources.append(item)
        return self

    def clear_ecu_resources(self) -> "SystemMappingBuilder":
        """Clear all items from ecu_resources list.

        Returns:
            self for method chaining
        """
        self._obj.ecu_resources = []
        return self

    def add_j1939_controller(self, item: any (J1939Controller)) -> "SystemMappingBuilder":
        """Add a single item to j1939_controllers list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.j1939_controllers.append(item)
        return self

    def clear_j1939_controllers(self) -> "SystemMappingBuilder":
        """Clear all items from j1939_controllers list.

        Returns:
            self for method chaining
        """
        self._obj.j1939_controllers = []
        return self

    def add_mapping(self, item: MappingConstraint) -> "SystemMappingBuilder":
        """Add a single item to mappings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.mappings.append(item)
        return self

    def clear_mappings(self) -> "SystemMappingBuilder":
        """Clear all items from mappings list.

        Returns:
            self for method chaining
        """
        self._obj.mappings = []
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

    def add_port_element_to(self, item: PortElementToCommunicationResourceMapping) -> "SystemMappingBuilder":
        """Add a single item to port_element_tos list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.port_element_tos.append(item)
        return self

    def clear_port_element_tos(self) -> "SystemMappingBuilder":
        """Clear all items from port_element_tos list.

        Returns:
            self for method chaining
        """
        self._obj.port_element_tos = []
        return self

    def add_resource(self, item: EcuResourceEstimation) -> "SystemMappingBuilder":
        """Add a single item to resources list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.resources.append(item)
        return self

    def clear_resources(self) -> "SystemMappingBuilder":
        """Clear all items from resources list.

        Returns:
            self for method chaining
        """
        self._obj.resources = []
        return self

    def add_resource_to(self, item: CpSoftwareCluster) -> "SystemMappingBuilder":
        """Add a single item to resource_tos list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.resource_tos.append(item)
        return self

    def clear_resource_tos(self) -> "SystemMappingBuilder":
        """Clear all items from resource_tos list.

        Returns:
            self for method chaining
        """
        self._obj.resource_tos = []
        return self

    def add_rte_event_in_system(self, item: any (RteEventInSystem)) -> "SystemMappingBuilder":
        """Add a single item to rte_event_in_systems list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.rte_event_in_systems.append(item)
        return self

    def clear_rte_event_in_systems(self) -> "SystemMappingBuilder":
        """Clear all items from rte_event_in_systems list.

        Returns:
            self for method chaining
        """
        self._obj.rte_event_in_systems = []
        return self

    def add_rte_event_to_ose(self, item: RteEventInSystemToOsTaskProxyMapping) -> "SystemMappingBuilder":
        """Add a single item to rte_event_to_oses list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.rte_event_to_oses.append(item)
        return self

    def clear_rte_event_to_oses(self) -> "SystemMappingBuilder":
        """Clear all items from rte_event_to_oses list.

        Returns:
            self for method chaining
        """
        self._obj.rte_event_to_oses = []
        return self

    def add_signal_path(self, item: SignalPathConstraint) -> "SystemMappingBuilder":
        """Add a single item to signal_paths list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.signal_paths.append(item)
        return self

    def clear_signal_paths(self) -> "SystemMappingBuilder":
        """Clear all items from signal_paths list.

        Returns:
            self for method chaining
        """
        self._obj.signal_paths = []
        return self

    def add_software_cluster(self, item: any (CpSoftwareClusterTo)) -> "SystemMappingBuilder":
        """Add a single item to software_clusters list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.software_clusters.append(item)
        return self

    def clear_software_clusters(self) -> "SystemMappingBuilder":
        """Clear all items from software_clusters list.

        Returns:
            self for method chaining
        """
        self._obj.software_clusters = []
        return self

    def add_sw_cluster(self, item: any (CpSoftwareClusterTo)) -> "SystemMappingBuilder":
        """Add a single item to sw_clusters list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.sw_clusters.append(item)
        return self

    def clear_sw_clusters(self) -> "SystemMappingBuilder":
        """Clear all items from sw_clusters list.

        Returns:
            self for method chaining
        """
        self._obj.sw_clusters = []
        return self

    def add_swc_to(self, item: SwcToApplicationPartitionMapping) -> "SystemMappingBuilder":
        """Add a single item to swc_tos list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.swc_tos.append(item)
        return self

    def clear_swc_tos(self) -> "SystemMappingBuilder":
        """Clear all items from swc_tos list.

        Returns:
            self for method chaining
        """
        self._obj.swc_tos = []
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

    def add_system_signal_group_to(self, item: SystemSignalGroupToCommunicationResourceMapping) -> "SystemMappingBuilder":
        """Add a single item to system_signal_group_tos list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.system_signal_group_tos.append(item)
        return self

    def clear_system_signal_group_tos(self) -> "SystemMappingBuilder":
        """Clear all items from system_signal_group_tos list.

        Returns:
            self for method chaining
        """
        self._obj.system_signal_group_tos = []
        return self

    def add_system_signal_to(self, item: SystemSignalToCommunicationResourceMapping) -> "SystemMappingBuilder":
        """Add a single item to system_signal_tos list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.system_signal_tos.append(item)
        return self

    def clear_system_signal_tos(self) -> "SystemMappingBuilder":
        """Clear all items from system_signal_tos list.

        Returns:
            self for method chaining
        """
        self._obj.system_signal_tos = []
        return self


    @staticmethod
    def _coerce_to_int(value: Any) -> int:
        """Coerce value to int.

        Args:
            value: Value to coerce

        Returns:
            Integer value

        Raises:
            ValueError: If value cannot be coerced to int
        """
        if isinstance(value, int):
            return value
        if isinstance(value, str) and value.isdigit():
            return int(value)
        if isinstance(value, float):
            return int(value)
        if isinstance(value, bool):
            return int(value)
        raise ValueError(f"Cannot coerce {type(value).__name__} to int: {value}")

    @staticmethod
    def _coerce_to_float(value: Any) -> float:
        """Coerce value to float.

        Args:
            value: Value to coerce

        Returns:
            Float value

        Raises:
            ValueError: If value cannot be coerced to float
        """
        if isinstance(value, float):
            return value
        if isinstance(value, int):
            return float(value)
        if isinstance(value, str):
            try:
                return float(value)
            except ValueError:
                pass
        raise ValueError(f"Cannot coerce {type(value).__name__} to float: {value}")

    @staticmethod
    def _coerce_to_bool(value: Any) -> bool:
        """Coerce value to bool.

        Args:
            value: Value to coerce

        Returns:
            Boolean value

        Raises:
            ValueError: If value cannot be coerced to bool
        """
        if isinstance(value, bool):
            return value
        if isinstance(value, int):
            return bool(value)
        if isinstance(value, str):
            if value.lower() in ("true", "1", "yes"):
                return True
            if value.lower() in ("false", "0", "no"):
                return False
        raise ValueError(f"Cannot coerce {type(value).__name__} to bool: {value}")

    @staticmethod
    def _coerce_to_str(value: Any) -> str:
        """Coerce value to str.

        Args:
            value: Value to coerce

        Returns:
            String value
        """
        return str(value)


    @staticmethod
    def _coerce_to_list(value: Any, item_type: str) -> list:
        """Coerce value to list.

        Args:
            value: Value to coerce
            item_type: Expected item type (for error messages)

        Returns:
            List value

        Raises:
            ValueError: If value cannot be coerced to list
        """
        if isinstance(value, list):
            return value
        if isinstance(value, tuple):
            return list(value)
        raise ValueError(f"Cannot coerce {type(value).__name__} to list[{item_type}]: {value}")


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