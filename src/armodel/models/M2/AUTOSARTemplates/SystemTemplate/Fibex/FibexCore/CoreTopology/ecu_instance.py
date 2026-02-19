"""EcuInstance AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 312)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 985)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 50)
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 59)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.client_id_range import (
    ClientIdRange,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.consumed_provided_service_instance_group import (
    ConsumedProvidedServiceInstanceGroup,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Dlt.dlt_config import (
    DltConfig,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DoIP.do_ip_config import (
    DoIpConfig,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping.ecu_partition import (
    EcuPartition,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.eth_tcp_ip_icmp_props import (
    EthTcpIpIcmpProps,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.eth_tcp_ip_props import (
    EthTcpIpProps,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_i_pdu_group import (
    ISignalIPduGroup,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.RteEventToOsTaskMapping.os_task_proxy import (
    OsTaskProxy,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdur_i_pdu_group import (
    PdurIPduGroup,
)
from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall.state_dependent_firewall import (
    StateDependentFirewall,
)


class EcuInstance(FibexElement):
    """AUTOSAR EcuInstance."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    associated_com_refs: list[ARRef]
    associateds: list[ConsumedProvidedServiceInstanceGroup]
    associated_pdur_refs: list[ARRef]
    channel: Optional[Boolean]
    client_id_range: Optional[ClientIdRange]
    com: Optional[TimeValue]
    com_enable: Optional[Boolean]
    comm_controllers: list[Any]
    connectors: list[Any]
    dlt_config: Optional[DltConfig]
    do_ip_config: Optional[DoIpConfig]
    ecu_task_proxies: list[OsTaskProxy]
    eth_switch_port: Optional[Boolean]
    firewall_rules: list[StateDependentFirewall]
    partitions: list[EcuPartition]
    pnc_nm_request: Optional[Boolean]
    pnc_prepare: Optional[TimeValue]
    pnc: Optional[Boolean]
    pn_reset_time: Optional[TimeValue]
    sleep_mode: Optional[Boolean]
    tcp_ip_icmp_props: Optional[EthTcpIpIcmpProps]
    tcp_ip_props: Optional[EthTcpIpProps]
    v2x_supported: Optional[Any]
    wake_up_over_bus_supported: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize EcuInstance."""
        super().__init__()
        self.associated_com_refs: list[ARRef] = []
        self.associateds: list[ConsumedProvidedServiceInstanceGroup] = []
        self.associated_pdur_refs: list[ARRef] = []
        self.channel: Optional[Boolean] = None
        self.client_id_range: Optional[ClientIdRange] = None
        self.com: Optional[TimeValue] = None
        self.com_enable: Optional[Boolean] = None
        self.comm_controllers: list[Any] = []
        self.connectors: list[Any] = []
        self.dlt_config: Optional[DltConfig] = None
        self.do_ip_config: Optional[DoIpConfig] = None
        self.ecu_task_proxies: list[OsTaskProxy] = []
        self.eth_switch_port: Optional[Boolean] = None
        self.firewall_rules: list[StateDependentFirewall] = []
        self.partitions: list[EcuPartition] = []
        self.pnc_nm_request: Optional[Boolean] = None
        self.pnc_prepare: Optional[TimeValue] = None
        self.pnc: Optional[Boolean] = None
        self.pn_reset_time: Optional[TimeValue] = None
        self.sleep_mode: Optional[Boolean] = None
        self.tcp_ip_icmp_props: Optional[EthTcpIpIcmpProps] = None
        self.tcp_ip_props: Optional[EthTcpIpProps] = None
        self.v2x_supported: Optional[Any] = None
        self.wake_up_over_bus_supported: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize EcuInstance to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcuInstance, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize associated_com_refs (list to container "ASSOCIATED-COMS")
        if self.associated_com_refs:
            wrapper = ET.Element("ASSOCIATED-COMS")
            for item in self.associated_com_refs:
                serialized = ARObject._serialize_item(item, "ISignalIPduGroup")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize associateds (list to container "ASSOCIATEDS")
        if self.associateds:
            wrapper = ET.Element("ASSOCIATEDS")
            for item in self.associateds:
                serialized = ARObject._serialize_item(item, "ConsumedProvidedServiceInstanceGroup")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize associated_pdur_refs (list to container "ASSOCIATED-PDURS")
        if self.associated_pdur_refs:
            wrapper = ET.Element("ASSOCIATED-PDURS")
            for item in self.associated_pdur_refs:
                serialized = ARObject._serialize_item(item, "PdurIPduGroup")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize channel
        if self.channel is not None:
            serialized = ARObject._serialize_item(self.channel, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CHANNEL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize client_id_range
        if self.client_id_range is not None:
            serialized = ARObject._serialize_item(self.client_id_range, "ClientIdRange")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CLIENT-ID-RANGE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize com
        if self.com is not None:
            serialized = ARObject._serialize_item(self.com, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize com_enable
        if self.com_enable is not None:
            serialized = ARObject._serialize_item(self.com_enable, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COM-ENABLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize comm_controllers (list to container "COMM-CONTROLLERS")
        if self.comm_controllers:
            wrapper = ET.Element("COMM-CONTROLLERS")
            for item in self.comm_controllers:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize connectors (list to container "CONNECTORS")
        if self.connectors:
            wrapper = ET.Element("CONNECTORS")
            for item in self.connectors:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize dlt_config
        if self.dlt_config is not None:
            serialized = ARObject._serialize_item(self.dlt_config, "DltConfig")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DLT-CONFIG")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize do_ip_config
        if self.do_ip_config is not None:
            serialized = ARObject._serialize_item(self.do_ip_config, "DoIpConfig")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DO-IP-CONFIG")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ecu_task_proxies (list to container "ECU-TASK-PROXIES")
        if self.ecu_task_proxies:
            wrapper = ET.Element("ECU-TASK-PROXIES")
            for item in self.ecu_task_proxies:
                serialized = ARObject._serialize_item(item, "OsTaskProxy")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize eth_switch_port
        if self.eth_switch_port is not None:
            serialized = ARObject._serialize_item(self.eth_switch_port, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ETH-SWITCH-PORT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize firewall_rules (list to container "FIREWALL-RULES")
        if self.firewall_rules:
            wrapper = ET.Element("FIREWALL-RULES")
            for item in self.firewall_rules:
                serialized = ARObject._serialize_item(item, "StateDependentFirewall")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize partitions (list to container "PARTITIONS")
        if self.partitions:
            wrapper = ET.Element("PARTITIONS")
            for item in self.partitions:
                serialized = ARObject._serialize_item(item, "EcuPartition")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize pnc_nm_request
        if self.pnc_nm_request is not None:
            serialized = ARObject._serialize_item(self.pnc_nm_request, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PNC-NM-REQUEST")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize pnc_prepare
        if self.pnc_prepare is not None:
            serialized = ARObject._serialize_item(self.pnc_prepare, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PNC-PREPARE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize pnc
        if self.pnc is not None:
            serialized = ARObject._serialize_item(self.pnc, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PNC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize pn_reset_time
        if self.pn_reset_time is not None:
            serialized = ARObject._serialize_item(self.pn_reset_time, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PN-RESET-TIME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sleep_mode
        if self.sleep_mode is not None:
            serialized = ARObject._serialize_item(self.sleep_mode, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SLEEP-MODE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tcp_ip_icmp_props
        if self.tcp_ip_icmp_props is not None:
            serialized = ARObject._serialize_item(self.tcp_ip_icmp_props, "EthTcpIpIcmpProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-IP-ICMP-PROPS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tcp_ip_props
        if self.tcp_ip_props is not None:
            serialized = ARObject._serialize_item(self.tcp_ip_props, "EthTcpIpProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-IP-PROPS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize v2x_supported
        if self.v2x_supported is not None:
            serialized = ARObject._serialize_item(self.v2x_supported, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("V2X-SUPPORTED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize wake_up_over_bus_supported
        if self.wake_up_over_bus_supported is not None:
            serialized = ARObject._serialize_item(self.wake_up_over_bus_supported, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("WAKE-UP-OVER-BUS-SUPPORTED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcuInstance":
        """Deserialize XML element to EcuInstance object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcuInstance object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcuInstance, cls).deserialize(element)

        # Parse associated_com_refs (list from container "ASSOCIATED-COMS")
        obj.associated_com_refs = []
        container = ARObject._find_child_element(element, "ASSOCIATED-COMS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.associated_com_refs.append(child_value)

        # Parse associateds (list from container "ASSOCIATEDS")
        obj.associateds = []
        container = ARObject._find_child_element(element, "ASSOCIATEDS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.associateds.append(child_value)

        # Parse associated_pdur_refs (list from container "ASSOCIATED-PDURS")
        obj.associated_pdur_refs = []
        container = ARObject._find_child_element(element, "ASSOCIATED-PDURS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.associated_pdur_refs.append(child_value)

        # Parse channel
        child = ARObject._find_child_element(element, "CHANNEL")
        if child is not None:
            channel_value = child.text
            obj.channel = channel_value

        # Parse client_id_range
        child = ARObject._find_child_element(element, "CLIENT-ID-RANGE")
        if child is not None:
            client_id_range_value = ARObject._deserialize_by_tag(child, "ClientIdRange")
            obj.client_id_range = client_id_range_value

        # Parse com
        child = ARObject._find_child_element(element, "COM")
        if child is not None:
            com_value = child.text
            obj.com = com_value

        # Parse com_enable
        child = ARObject._find_child_element(element, "COM-ENABLE")
        if child is not None:
            com_enable_value = child.text
            obj.com_enable = com_enable_value

        # Parse comm_controllers (list from container "COMM-CONTROLLERS")
        obj.comm_controllers = []
        container = ARObject._find_child_element(element, "COMM-CONTROLLERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.comm_controllers.append(child_value)

        # Parse connectors (list from container "CONNECTORS")
        obj.connectors = []
        container = ARObject._find_child_element(element, "CONNECTORS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.connectors.append(child_value)

        # Parse dlt_config
        child = ARObject._find_child_element(element, "DLT-CONFIG")
        if child is not None:
            dlt_config_value = ARObject._deserialize_by_tag(child, "DltConfig")
            obj.dlt_config = dlt_config_value

        # Parse do_ip_config
        child = ARObject._find_child_element(element, "DO-IP-CONFIG")
        if child is not None:
            do_ip_config_value = ARObject._deserialize_by_tag(child, "DoIpConfig")
            obj.do_ip_config = do_ip_config_value

        # Parse ecu_task_proxies (list from container "ECU-TASK-PROXIES")
        obj.ecu_task_proxies = []
        container = ARObject._find_child_element(element, "ECU-TASK-PROXIES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.ecu_task_proxies.append(child_value)

        # Parse eth_switch_port
        child = ARObject._find_child_element(element, "ETH-SWITCH-PORT")
        if child is not None:
            eth_switch_port_value = child.text
            obj.eth_switch_port = eth_switch_port_value

        # Parse firewall_rules (list from container "FIREWALL-RULES")
        obj.firewall_rules = []
        container = ARObject._find_child_element(element, "FIREWALL-RULES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.firewall_rules.append(child_value)

        # Parse partitions (list from container "PARTITIONS")
        obj.partitions = []
        container = ARObject._find_child_element(element, "PARTITIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.partitions.append(child_value)

        # Parse pnc_nm_request
        child = ARObject._find_child_element(element, "PNC-NM-REQUEST")
        if child is not None:
            pnc_nm_request_value = child.text
            obj.pnc_nm_request = pnc_nm_request_value

        # Parse pnc_prepare
        child = ARObject._find_child_element(element, "PNC-PREPARE")
        if child is not None:
            pnc_prepare_value = child.text
            obj.pnc_prepare = pnc_prepare_value

        # Parse pnc
        child = ARObject._find_child_element(element, "PNC")
        if child is not None:
            pnc_value = child.text
            obj.pnc = pnc_value

        # Parse pn_reset_time
        child = ARObject._find_child_element(element, "PN-RESET-TIME")
        if child is not None:
            pn_reset_time_value = child.text
            obj.pn_reset_time = pn_reset_time_value

        # Parse sleep_mode
        child = ARObject._find_child_element(element, "SLEEP-MODE")
        if child is not None:
            sleep_mode_value = child.text
            obj.sleep_mode = sleep_mode_value

        # Parse tcp_ip_icmp_props
        child = ARObject._find_child_element(element, "TCP-IP-ICMP-PROPS")
        if child is not None:
            tcp_ip_icmp_props_value = ARObject._deserialize_by_tag(child, "EthTcpIpIcmpProps")
            obj.tcp_ip_icmp_props = tcp_ip_icmp_props_value

        # Parse tcp_ip_props
        child = ARObject._find_child_element(element, "TCP-IP-PROPS")
        if child is not None:
            tcp_ip_props_value = ARObject._deserialize_by_tag(child, "EthTcpIpProps")
            obj.tcp_ip_props = tcp_ip_props_value

        # Parse v2x_supported
        child = ARObject._find_child_element(element, "V2X-SUPPORTED")
        if child is not None:
            v2x_supported_value = child.text
            obj.v2x_supported = v2x_supported_value

        # Parse wake_up_over_bus_supported
        child = ARObject._find_child_element(element, "WAKE-UP-OVER-BUS-SUPPORTED")
        if child is not None:
            wake_up_over_bus_supported_value = child.text
            obj.wake_up_over_bus_supported = wake_up_over_bus_supported_value

        return obj



class EcuInstanceBuilder:
    """Builder for EcuInstance."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcuInstance = EcuInstance()

    def build(self) -> EcuInstance:
        """Build and return EcuInstance object.

        Returns:
            EcuInstance instance
        """
        # TODO: Add validation
        return self._obj
