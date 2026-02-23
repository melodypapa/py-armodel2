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
from armodel.serialization.decorators import xml_element_name

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
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
    associated_refs: list[ARRef]
    associated_pdur_refs: list[ARRef]
    channel: Optional[Boolean]
    client_id_range: Optional[ClientIdRange]
    com: Optional[TimeValue]
    com_enable: Optional[Boolean]
    comm_controllers: list[Any]
    connectors: list[Any]
    dlt_config: Optional[DltConfig]
    do_ip_config: Optional[DoIpConfig]
    _ecu_task_proxie_refs: list[ARRef]
    eth_switch_port: Optional[Boolean]
    firewall_rule_refs: list[ARRef]
    partitions: list[EcuPartition]
    pnc_nm_request: Optional[Boolean]
    pnc_prepare: Optional[TimeValue]
    pnc: Optional[Boolean]
    pn_reset_time: Optional[TimeValue]
    sleep_mode: Optional[Boolean]
    tcp_ip_icmp_props_ref: Optional[ARRef]
    tcp_ip_props_ref: Optional[ARRef]
    v2x_supported: Optional[Any]
    wake_up_over_bus_supported: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize EcuInstance."""
        super().__init__()
        self.associated_com_refs: list[ARRef] = []
        self.associated_refs: list[ARRef] = []
        self.associated_pdur_refs: list[ARRef] = []
        self.channel: Optional[Boolean] = None
        self.client_id_range: Optional[ClientIdRange] = None
        self.com: Optional[TimeValue] = None
        self.com_enable: Optional[Boolean] = None
        self.comm_controllers: list[Any] = []
        self.connectors: list[Any] = []
        self.dlt_config: Optional[DltConfig] = None
        self.do_ip_config: Optional[DoIpConfig] = None
        self._ecu_task_proxie_refs: list[ARRef] = []
        self.eth_switch_port: Optional[Boolean] = None
        self.firewall_rule_refs: list[ARRef] = []
        self.partitions: list[EcuPartition] = []
        self.pnc_nm_request: Optional[Boolean] = None
        self.pnc_prepare: Optional[TimeValue] = None
        self.pnc: Optional[Boolean] = None
        self.pn_reset_time: Optional[TimeValue] = None
        self.sleep_mode: Optional[Boolean] = None
        self.tcp_ip_icmp_props_ref: Optional[ARRef] = None
        self.tcp_ip_props_ref: Optional[ARRef] = None
        self.v2x_supported: Optional[Any] = None
        self.wake_up_over_bus_supported: Optional[Boolean] = None
    @property
    @xml_element_name("ECU-TASK-PROXYS")
    def ecu_task_proxie_refs(self) -> list[ARRef]:
        """Get ecu_task_proxie_refs with custom XML element name."""
        return self._ecu_task_proxie_refs

    @ecu_task_proxie_refs.setter
    def ecu_task_proxie_refs(self, value: list[ARRef]) -> None:
        """Set ecu_task_proxie_refs with custom XML element name."""
        self._ecu_task_proxie_refs = value


    def serialize(self) -> ET.Element:
        """Serialize EcuInstance to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcuInstance, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize associated_com_refs (list to container "ASSOCIATED-COM-REFS")
        if self.associated_com_refs:
            wrapper = ET.Element("ASSOCIATED-COM-REFS")
            for item in self.associated_com_refs:
                serialized = SerializationHelper.serialize_item(item, "ISignalIPduGroup")
                if serialized is not None:
                    child_elem = ET.Element("ASSOCIATED-COM-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize associated_refs (list to container "ASSOCIATED-REFS")
        if self.associated_refs:
            wrapper = ET.Element("ASSOCIATED-REFS")
            for item in self.associated_refs:
                serialized = SerializationHelper.serialize_item(item, "ConsumedProvidedServiceInstanceGroup")
                if serialized is not None:
                    child_elem = ET.Element("ASSOCIATED-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize associated_pdur_refs (list to container "ASSOCIATED-PDUR-REFS")
        if self.associated_pdur_refs:
            wrapper = ET.Element("ASSOCIATED-PDUR-REFS")
            for item in self.associated_pdur_refs:
                serialized = SerializationHelper.serialize_item(item, "PdurIPduGroup")
                if serialized is not None:
                    child_elem = ET.Element("ASSOCIATED-PDUR-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize channel
        if self.channel is not None:
            serialized = SerializationHelper.serialize_item(self.channel, "Boolean")
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
            serialized = SerializationHelper.serialize_item(self.client_id_range, "ClientIdRange")
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
            serialized = SerializationHelper.serialize_item(self.com, "TimeValue")
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
            serialized = SerializationHelper.serialize_item(self.com_enable, "Boolean")
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
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize connectors (list to container "CONNECTORS")
        if self.connectors:
            wrapper = ET.Element("CONNECTORS")
            for item in self.connectors:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize dlt_config
        if self.dlt_config is not None:
            serialized = SerializationHelper.serialize_item(self.dlt_config, "DltConfig")
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
            serialized = SerializationHelper.serialize_item(self.do_ip_config, "DoIpConfig")
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

        # Serialize ecu_task_proxie_refs (list to container "ECU-TASK-PROXYS")
        if self.ecu_task_proxie_refs:
            wrapper = ET.Element("ECU-TASK-PROXYS")
            for item in self.ecu_task_proxie_refs:
                serialized = SerializationHelper.serialize_item(item, "OsTaskProxy")
                if serialized is not None:
                    child_elem = ET.Element("ECU-TASK-PROXIE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize eth_switch_port
        if self.eth_switch_port is not None:
            serialized = SerializationHelper.serialize_item(self.eth_switch_port, "Boolean")
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

        # Serialize firewall_rule_refs (list to container "FIREWALL-RULE-REFS")
        if self.firewall_rule_refs:
            wrapper = ET.Element("FIREWALL-RULE-REFS")
            for item in self.firewall_rule_refs:
                serialized = SerializationHelper.serialize_item(item, "StateDependentFirewall")
                if serialized is not None:
                    child_elem = ET.Element("FIREWALL-RULE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize partitions (list to container "PARTITIONS")
        if self.partitions:
            wrapper = ET.Element("PARTITIONS")
            for item in self.partitions:
                serialized = SerializationHelper.serialize_item(item, "EcuPartition")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize pnc_nm_request
        if self.pnc_nm_request is not None:
            serialized = SerializationHelper.serialize_item(self.pnc_nm_request, "Boolean")
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
            serialized = SerializationHelper.serialize_item(self.pnc_prepare, "TimeValue")
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
            serialized = SerializationHelper.serialize_item(self.pnc, "Boolean")
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
            serialized = SerializationHelper.serialize_item(self.pn_reset_time, "TimeValue")
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
            serialized = SerializationHelper.serialize_item(self.sleep_mode, "Boolean")
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

        # Serialize tcp_ip_icmp_props_ref
        if self.tcp_ip_icmp_props_ref is not None:
            serialized = SerializationHelper.serialize_item(self.tcp_ip_icmp_props_ref, "EthTcpIpIcmpProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-IP-ICMP-PROPS-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tcp_ip_props_ref
        if self.tcp_ip_props_ref is not None:
            serialized = SerializationHelper.serialize_item(self.tcp_ip_props_ref, "EthTcpIpProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-IP-PROPS-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize v2x_supported
        if self.v2x_supported is not None:
            serialized = SerializationHelper.serialize_item(self.v2x_supported, "Any")
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
            serialized = SerializationHelper.serialize_item(self.wake_up_over_bus_supported, "Boolean")
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

        # Parse associated_com_refs (list from container "ASSOCIATED-COM-REFS")
        obj.associated_com_refs = []
        container = SerializationHelper.find_child_element(element, "ASSOCIATED-COM-REFS")
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
                    obj.associated_com_refs.append(child_value)

        # Parse associated_refs (list from container "ASSOCIATED-REFS")
        obj.associated_refs = []
        container = SerializationHelper.find_child_element(element, "ASSOCIATED-REFS")
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
                    obj.associated_refs.append(child_value)

        # Parse associated_pdur_refs (list from container "ASSOCIATED-PDUR-REFS")
        obj.associated_pdur_refs = []
        container = SerializationHelper.find_child_element(element, "ASSOCIATED-PDUR-REFS")
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
                    obj.associated_pdur_refs.append(child_value)

        # Parse channel
        child = SerializationHelper.find_child_element(element, "CHANNEL")
        if child is not None:
            channel_value = child.text
            obj.channel = channel_value

        # Parse client_id_range
        child = SerializationHelper.find_child_element(element, "CLIENT-ID-RANGE")
        if child is not None:
            client_id_range_value = SerializationHelper.deserialize_by_tag(child, "ClientIdRange")
            obj.client_id_range = client_id_range_value

        # Parse com
        child = SerializationHelper.find_child_element(element, "COM")
        if child is not None:
            com_value = child.text
            obj.com = com_value

        # Parse com_enable
        child = SerializationHelper.find_child_element(element, "COM-ENABLE")
        if child is not None:
            com_enable_value = child.text
            obj.com_enable = com_enable_value

        # Parse comm_controllers (list from container "COMM-CONTROLLERS")
        obj.comm_controllers = []
        container = SerializationHelper.find_child_element(element, "COMM-CONTROLLERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.comm_controllers.append(child_value)

        # Parse connectors (list from container "CONNECTORS")
        obj.connectors = []
        container = SerializationHelper.find_child_element(element, "CONNECTORS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.connectors.append(child_value)

        # Parse dlt_config
        child = SerializationHelper.find_child_element(element, "DLT-CONFIG")
        if child is not None:
            dlt_config_value = SerializationHelper.deserialize_by_tag(child, "DltConfig")
            obj.dlt_config = dlt_config_value

        # Parse do_ip_config
        child = SerializationHelper.find_child_element(element, "DO-IP-CONFIG")
        if child is not None:
            do_ip_config_value = SerializationHelper.deserialize_by_tag(child, "DoIpConfig")
            obj.do_ip_config = do_ip_config_value

        # Parse ecu_task_proxie_refs (list from container "ECU-TASK-PROXYS")
        obj.ecu_task_proxie_refs = []
        container = SerializationHelper.find_child_element(element, "ECU-TASK-PROXYS")
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
                    obj.ecu_task_proxie_refs.append(child_value)

        # Parse eth_switch_port
        child = SerializationHelper.find_child_element(element, "ETH-SWITCH-PORT")
        if child is not None:
            eth_switch_port_value = child.text
            obj.eth_switch_port = eth_switch_port_value

        # Parse firewall_rule_refs (list from container "FIREWALL-RULE-REFS")
        obj.firewall_rule_refs = []
        container = SerializationHelper.find_child_element(element, "FIREWALL-RULE-REFS")
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
                    obj.firewall_rule_refs.append(child_value)

        # Parse partitions (list from container "PARTITIONS")
        obj.partitions = []
        container = SerializationHelper.find_child_element(element, "PARTITIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.partitions.append(child_value)

        # Parse pnc_nm_request
        child = SerializationHelper.find_child_element(element, "PNC-NM-REQUEST")
        if child is not None:
            pnc_nm_request_value = child.text
            obj.pnc_nm_request = pnc_nm_request_value

        # Parse pnc_prepare
        child = SerializationHelper.find_child_element(element, "PNC-PREPARE")
        if child is not None:
            pnc_prepare_value = child.text
            obj.pnc_prepare = pnc_prepare_value

        # Parse pnc
        child = SerializationHelper.find_child_element(element, "PNC")
        if child is not None:
            pnc_value = child.text
            obj.pnc = pnc_value

        # Parse pn_reset_time
        child = SerializationHelper.find_child_element(element, "PN-RESET-TIME")
        if child is not None:
            pn_reset_time_value = child.text
            obj.pn_reset_time = pn_reset_time_value

        # Parse sleep_mode
        child = SerializationHelper.find_child_element(element, "SLEEP-MODE")
        if child is not None:
            sleep_mode_value = child.text
            obj.sleep_mode = sleep_mode_value

        # Parse tcp_ip_icmp_props_ref
        child = SerializationHelper.find_child_element(element, "TCP-IP-ICMP-PROPS-REF")
        if child is not None:
            tcp_ip_icmp_props_ref_value = ARRef.deserialize(child)
            obj.tcp_ip_icmp_props_ref = tcp_ip_icmp_props_ref_value

        # Parse tcp_ip_props_ref
        child = SerializationHelper.find_child_element(element, "TCP-IP-PROPS-REF")
        if child is not None:
            tcp_ip_props_ref_value = ARRef.deserialize(child)
            obj.tcp_ip_props_ref = tcp_ip_props_ref_value

        # Parse v2x_supported
        child = SerializationHelper.find_child_element(element, "V2X-SUPPORTED")
        if child is not None:
            v2x_supported_value = child.text
            obj.v2x_supported = v2x_supported_value

        # Parse wake_up_over_bus_supported
        child = SerializationHelper.find_child_element(element, "WAKE-UP-OVER-BUS-SUPPORTED")
        if child is not None:
            wake_up_over_bus_supported_value = child.text
            obj.wake_up_over_bus_supported = wake_up_over_bus_supported_value

        return obj



class EcuInstanceBuilder:
    """Builder for EcuInstance with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: EcuInstance = EcuInstance()


    def with_short_name(self, value: Identifier) -> "EcuInstanceBuilder":
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

    def with_short_name_fragments(self, items: list[ShortNameFragment]) -> "EcuInstanceBuilder":
        """Set short_name_fragments list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = list(items) if items else []
        return self

    def with_long_name(self, value: Optional[MultilanguageLongName]) -> "EcuInstanceBuilder":
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

    def with_admin_data(self, value: Optional[AdminData]) -> "EcuInstanceBuilder":
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

    def with_annotations(self, items: list[Annotation]) -> "EcuInstanceBuilder":
        """Set annotations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.annotations = list(items) if items else []
        return self

    def with_desc(self, value: Optional[MultiLanguageOverviewParagraph]) -> "EcuInstanceBuilder":
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

    def with_category(self, value: Optional[CategoryString]) -> "EcuInstanceBuilder":
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

    def with_introduction(self, value: Optional[DocumentationBlock]) -> "EcuInstanceBuilder":
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

    def with_uuid(self, value: Optional[String]) -> "EcuInstanceBuilder":
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

    def with_associated_coms(self, items: list[ISignalIPduGroup]) -> "EcuInstanceBuilder":
        """Set associated_coms list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.associated_coms = list(items) if items else []
        return self

    def with_associateds(self, items: list[ConsumedProvidedServiceInstanceGroup]) -> "EcuInstanceBuilder":
        """Set associateds list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.associateds = list(items) if items else []
        return self

    def with_associated_pdurs(self, items: list[PdurIPduGroup]) -> "EcuInstanceBuilder":
        """Set associated_pdurs list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.associated_pdurs = list(items) if items else []
        return self

    def with_channel(self, value: Optional[Boolean]) -> "EcuInstanceBuilder":
        """Set channel attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.channel = value
        return self

    def with_client_id_range(self, value: Optional[ClientIdRange]) -> "EcuInstanceBuilder":
        """Set client_id_range attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.client_id_range = value
        return self

    def with_com(self, value: Optional[TimeValue]) -> "EcuInstanceBuilder":
        """Set com attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.com = value
        return self

    def with_com_enable(self, value: Optional[Boolean]) -> "EcuInstanceBuilder":
        """Set com_enable attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.com_enable = value
        return self

    def with_comm_controllers(self, items: list[any (Communication)]) -> "EcuInstanceBuilder":
        """Set comm_controllers list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.comm_controllers = list(items) if items else []
        return self

    def with_connectors(self, items: list[any (Communication)]) -> "EcuInstanceBuilder":
        """Set connectors list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.connectors = list(items) if items else []
        return self

    def with_dlt_config(self, value: Optional[DltConfig]) -> "EcuInstanceBuilder":
        """Set dlt_config attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.dlt_config = value
        return self

    def with_do_ip_config(self, value: Optional[DoIpConfig]) -> "EcuInstanceBuilder":
        """Set do_ip_config attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.do_ip_config = value
        return self

    def with_ecu_task_proxies(self, items: list[OsTaskProxy]) -> "EcuInstanceBuilder":
        """Set ecu_task_proxies list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.ecu_task_proxies = list(items) if items else []
        return self

    def with_eth_switch_port(self, value: Optional[Boolean]) -> "EcuInstanceBuilder":
        """Set eth_switch_port attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.eth_switch_port = value
        return self

    def with_firewall_rules(self, items: list[StateDependentFirewall]) -> "EcuInstanceBuilder":
        """Set firewall_rules list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.firewall_rules = list(items) if items else []
        return self

    def with_partitions(self, items: list[EcuPartition]) -> "EcuInstanceBuilder":
        """Set partitions list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.partitions = list(items) if items else []
        return self

    def with_pnc_nm_request(self, value: Optional[Boolean]) -> "EcuInstanceBuilder":
        """Set pnc_nm_request attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.pnc_nm_request = value
        return self

    def with_pnc_prepare(self, value: Optional[TimeValue]) -> "EcuInstanceBuilder":
        """Set pnc_prepare attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.pnc_prepare = value
        return self

    def with_pnc(self, value: Optional[Boolean]) -> "EcuInstanceBuilder":
        """Set pnc attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.pnc = value
        return self

    def with_pn_reset_time(self, value: Optional[TimeValue]) -> "EcuInstanceBuilder":
        """Set pn_reset_time attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.pn_reset_time = value
        return self

    def with_sleep_mode(self, value: Optional[Boolean]) -> "EcuInstanceBuilder":
        """Set sleep_mode attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sleep_mode = value
        return self

    def with_tcp_ip_icmp_props(self, value: Optional[EthTcpIpIcmpProps]) -> "EcuInstanceBuilder":
        """Set tcp_ip_icmp_props attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tcp_ip_icmp_props = value
        return self

    def with_tcp_ip_props(self, value: Optional[EthTcpIpProps]) -> "EcuInstanceBuilder":
        """Set tcp_ip_props attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tcp_ip_props = value
        return self

    def with_v2x_supported(self, value: Optional[any (V2xSupportEnum)]) -> "EcuInstanceBuilder":
        """Set v2x_supported attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.v2x_supported = value
        return self

    def with_wake_up_over_bus_supported(self, value: Optional[Boolean]) -> "EcuInstanceBuilder":
        """Set wake_up_over_bus_supported attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.wake_up_over_bus_supported = value
        return self


    def add_short_name_fragment(self, item: ShortNameFragment) -> "EcuInstanceBuilder":
        """Add a single item to short_name_fragments list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments.append(item)
        return self

    def clear_short_name_fragments(self) -> "EcuInstanceBuilder":
        """Clear all items from short_name_fragments list.

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = []
        return self

    def add_annotation(self, item: Annotation) -> "EcuInstanceBuilder":
        """Add a single item to annotations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.annotations.append(item)
        return self

    def clear_annotations(self) -> "EcuInstanceBuilder":
        """Clear all items from annotations list.

        Returns:
            self for method chaining
        """
        self._obj.annotations = []
        return self

    def add_associated_com(self, item: ISignalIPduGroup) -> "EcuInstanceBuilder":
        """Add a single item to associated_coms list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.associated_coms.append(item)
        return self

    def clear_associated_coms(self) -> "EcuInstanceBuilder":
        """Clear all items from associated_coms list.

        Returns:
            self for method chaining
        """
        self._obj.associated_coms = []
        return self

    def add_associated(self, item: ConsumedProvidedServiceInstanceGroup) -> "EcuInstanceBuilder":
        """Add a single item to associateds list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.associateds.append(item)
        return self

    def clear_associateds(self) -> "EcuInstanceBuilder":
        """Clear all items from associateds list.

        Returns:
            self for method chaining
        """
        self._obj.associateds = []
        return self

    def add_associated_pdur(self, item: PdurIPduGroup) -> "EcuInstanceBuilder":
        """Add a single item to associated_pdurs list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.associated_pdurs.append(item)
        return self

    def clear_associated_pdurs(self) -> "EcuInstanceBuilder":
        """Clear all items from associated_pdurs list.

        Returns:
            self for method chaining
        """
        self._obj.associated_pdurs = []
        return self

    def add_comm_controller(self, item: any (Communication)) -> "EcuInstanceBuilder":
        """Add a single item to comm_controllers list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.comm_controllers.append(item)
        return self

    def clear_comm_controllers(self) -> "EcuInstanceBuilder":
        """Clear all items from comm_controllers list.

        Returns:
            self for method chaining
        """
        self._obj.comm_controllers = []
        return self

    def add_connector(self, item: any (Communication)) -> "EcuInstanceBuilder":
        """Add a single item to connectors list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.connectors.append(item)
        return self

    def clear_connectors(self) -> "EcuInstanceBuilder":
        """Clear all items from connectors list.

        Returns:
            self for method chaining
        """
        self._obj.connectors = []
        return self

    def add_ecu_task_proxie(self, item: OsTaskProxy) -> "EcuInstanceBuilder":
        """Add a single item to ecu_task_proxies list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.ecu_task_proxies.append(item)
        return self

    def clear_ecu_task_proxies(self) -> "EcuInstanceBuilder":
        """Clear all items from ecu_task_proxies list.

        Returns:
            self for method chaining
        """
        self._obj.ecu_task_proxies = []
        return self

    def add_firewall_rule(self, item: StateDependentFirewall) -> "EcuInstanceBuilder":
        """Add a single item to firewall_rules list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.firewall_rules.append(item)
        return self

    def clear_firewall_rules(self) -> "EcuInstanceBuilder":
        """Clear all items from firewall_rules list.

        Returns:
            self for method chaining
        """
        self._obj.firewall_rules = []
        return self

    def add_partition(self, item: EcuPartition) -> "EcuInstanceBuilder":
        """Add a single item to partitions list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.partitions.append(item)
        return self

    def clear_partitions(self) -> "EcuInstanceBuilder":
        """Clear all items from partitions list.

        Returns:
            self for method chaining
        """
        self._obj.partitions = []
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


    def build(self) -> EcuInstance:
        """Build and return the EcuInstance instance with validation."""
        self._validate_instance()
        pass
        return self._obj