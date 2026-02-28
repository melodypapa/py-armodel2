"""EcuInstance AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 312)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 985)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 50)
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 59)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import FibexElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    TimeValue,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.client_id_range import (
    ClientIdRange,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_connector import (
    CommunicationConnector,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_controller import (
    CommunicationController,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.consumed_provided_service_instance_group import (
    ConsumedProvidedServiceInstanceGroup,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Dlt.dlt_config import (
    DltConfig,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.DoIP.do_ip_config import (
    DoIpConfig,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping.ecu_partition import (
    EcuPartition,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.eth_tcp_ip_icmp_props import (
    EthTcpIpIcmpProps,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.eth_tcp_ip_props import (
    EthTcpIpProps,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_i_pdu_group import (
    ISignalIPduGroup,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.RteEventToOsTaskMapping.os_task_proxy import (
    OsTaskProxy,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdur_i_pdu_group import (
    PdurIPduGroup,
)
from armodel2.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall.state_dependent_firewall import (
    StateDependentFirewall,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class EcuInstance(FibexElement):
    """AUTOSAR EcuInstance."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "ECU-INSTANCE"


    associated_com_i_pdu_group_refs: list[ARRef]
    associated_consumed_provided_service_instance_group_refs: list[ARRef]
    associated_pdur_i_pdu_group_refs: list[ARRef]
    channel_synchronous_wakeup: Optional[Boolean]
    client_id_range: Optional[ClientIdRange]
    com_configuration_gw_time_base: Optional[TimeValue]
    com_configuration_rx_time_base: Optional[TimeValue]
    com_configuration_tx_time_base: Optional[TimeValue]
    com_enable_mdt_for_cyclic_transmission: Optional[Boolean]
    comm_controllers: list[CommunicationController]
    connectors: list[CommunicationConnector]
    dlt_config: Optional[DltConfig]
    do_ip_config: Optional[DoIpConfig]
    ecu_task_proxy_refs: list[ARRef]
    eth_switch_port_group_derivation: Optional[Boolean]
    firewall_rule_refs: list[ARRef]
    partitions: list[EcuPartition]
    pnc_nm_request: Optional[Boolean]
    pnc_prepare_sleep_timer: Optional[TimeValue]
    pnc_synchronous_wakeup: Optional[Boolean]
    pn_reset_time: Optional[TimeValue]
    sleep_mode_supported: Optional[Boolean]
    tcp_ip_icmp_props_ref: Optional[ARRef]
    tcp_ip_props_ref: Optional[ARRef]
    v2x_supported: Optional[V2xSupportEnum]
    wake_up_over_bus_supported: Optional[Boolean]
    _DESERIALIZE_DISPATCH = {
        "ASSOCIATED-COM-I-PDU-GROUPS": lambda obj, elem: obj.associated_com_i_pdu_group_refs.append(ARRef.deserialize(elem)),
        "ASSOCIATED-CONSUMED-PROVIDED-SERVICE-INSTANCE-GROUPS": lambda obj, elem: obj.associated_consumed_provided_service_instance_group_refs.append(ARRef.deserialize(elem)),
        "ASSOCIATED-PDUR-I-PDU-GROUPS": lambda obj, elem: obj.associated_pdur_i_pdu_group_refs.append(ARRef.deserialize(elem)),
        "CHANNEL-SYNCHRONOUS-WAKEUP": lambda obj, elem: setattr(obj, "channel_synchronous_wakeup", elem.text),
        "CLIENT-ID-RANGE": lambda obj, elem: setattr(obj, "client_id_range", ClientIdRange.deserialize(elem)),
        "COM-CONFIGURATION-GW-TIME-BASE": lambda obj, elem: setattr(obj, "com_configuration_gw_time_base", elem.text),
        "COM-CONFIGURATION-RX-TIME-BASE": lambda obj, elem: setattr(obj, "com_configuration_rx_time_base", elem.text),
        "COM-CONFIGURATION-TX-TIME-BASE": lambda obj, elem: setattr(obj, "com_configuration_tx_time_base", elem.text),
        "COM-ENABLE-MDT-FOR-CYCLIC-TRANSMISSION": lambda obj, elem: setattr(obj, "com_enable_mdt_for_cyclic_transmission", elem.text),
        "COMM-CONTROLLERS": lambda obj, elem: obj.comm_controllers.append(CommunicationController.deserialize(elem)),
        "CONNECTORS": lambda obj, elem: obj.connectors.append(CommunicationConnector.deserialize(elem)),
        "DLT-CONFIG": lambda obj, elem: setattr(obj, "dlt_config", DltConfig.deserialize(elem)),
        "DO-IP-CONFIG": lambda obj, elem: setattr(obj, "do_ip_config", DoIpConfig.deserialize(elem)),
        "ECU-TASK-PROXIES": lambda obj, elem: obj.ecu_task_proxy_refs.append(ARRef.deserialize(elem)),
        "ETH-SWITCH-PORT-GROUP-DERIVATION": lambda obj, elem: setattr(obj, "eth_switch_port_group_derivation", elem.text),
        "FIREWALL-RULES": lambda obj, elem: obj.firewall_rule_refs.append(ARRef.deserialize(elem)),
        "PARTITIONS": lambda obj, elem: obj.partitions.append(EcuPartition.deserialize(elem)),
        "PNC-NM-REQUEST": lambda obj, elem: setattr(obj, "pnc_nm_request", elem.text),
        "PNC-PREPARE-SLEEP-TIMER": lambda obj, elem: setattr(obj, "pnc_prepare_sleep_timer", elem.text),
        "PNC-SYNCHRONOUS-WAKEUP": lambda obj, elem: setattr(obj, "pnc_synchronous_wakeup", elem.text),
        "PN-RESET-TIME": lambda obj, elem: setattr(obj, "pn_reset_time", elem.text),
        "SLEEP-MODE-SUPPORTED": lambda obj, elem: setattr(obj, "sleep_mode_supported", elem.text),
        "TCP-IP-ICMP-PROPS-REF": lambda obj, elem: setattr(obj, "tcp_ip_icmp_props_ref", ARRef.deserialize(elem)),
        "TCP-IP-PROPS-REF": lambda obj, elem: setattr(obj, "tcp_ip_props_ref", ARRef.deserialize(elem)),
        "V2X-SUPPORTED": lambda obj, elem: setattr(obj, "v2x_supported", V2xSupportEnum.deserialize(elem)),
        "WAKE-UP-OVER-BUS-SUPPORTED": lambda obj, elem: setattr(obj, "wake_up_over_bus_supported", elem.text),
    }


    def __init__(self) -> None:
        """Initialize EcuInstance."""
        super().__init__()
        self.associated_com_i_pdu_group_refs: list[ARRef] = []
        self.associated_consumed_provided_service_instance_group_refs: list[ARRef] = []
        self.associated_pdur_i_pdu_group_refs: list[ARRef] = []
        self.channel_synchronous_wakeup: Optional[Boolean] = None
        self.client_id_range: Optional[ClientIdRange] = None
        self.com_configuration_gw_time_base: Optional[TimeValue] = None
        self.com_configuration_rx_time_base: Optional[TimeValue] = None
        self.com_configuration_tx_time_base: Optional[TimeValue] = None
        self.com_enable_mdt_for_cyclic_transmission: Optional[Boolean] = None
        self.comm_controllers: list[CommunicationController] = []
        self.connectors: list[CommunicationConnector] = []
        self.dlt_config: Optional[DltConfig] = None
        self.do_ip_config: Optional[DoIpConfig] = None
        self.ecu_task_proxy_refs: list[ARRef] = []
        self.eth_switch_port_group_derivation: Optional[Boolean] = None
        self.firewall_rule_refs: list[ARRef] = []
        self.partitions: list[EcuPartition] = []
        self.pnc_nm_request: Optional[Boolean] = None
        self.pnc_prepare_sleep_timer: Optional[TimeValue] = None
        self.pnc_synchronous_wakeup: Optional[Boolean] = None
        self.pn_reset_time: Optional[TimeValue] = None
        self.sleep_mode_supported: Optional[Boolean] = None
        self.tcp_ip_icmp_props_ref: Optional[ARRef] = None
        self.tcp_ip_props_ref: Optional[ARRef] = None
        self.v2x_supported: Optional[V2xSupportEnum] = None
        self.wake_up_over_bus_supported: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize EcuInstance to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

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

        # Serialize associated_com_i_pdu_group_refs (list to container "ASSOCIATED-COM-I-PDU-GROUP-REFS")
        if self.associated_com_i_pdu_group_refs:
            wrapper = ET.Element("ASSOCIATED-COM-I-PDU-GROUP-REFS")
            for item in self.associated_com_i_pdu_group_refs:
                serialized = SerializationHelper.serialize_item(item, "ISignalIPduGroup")
                if serialized is not None:
                    child_elem = ET.Element("ASSOCIATED-COM-I-PDU-GROUP-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize associated_consumed_provided_service_instance_group_refs (list to container "ASSOCIATED-CONSUMED-PROVIDED-SERVICE-INSTANCE-GROUP-REFS")
        if self.associated_consumed_provided_service_instance_group_refs:
            wrapper = ET.Element("ASSOCIATED-CONSUMED-PROVIDED-SERVICE-INSTANCE-GROUP-REFS")
            for item in self.associated_consumed_provided_service_instance_group_refs:
                serialized = SerializationHelper.serialize_item(item, "ConsumedProvidedServiceInstanceGroup")
                if serialized is not None:
                    child_elem = ET.Element("ASSOCIATED-CONSUMED-PROVIDED-SERVICE-INSTANCE-GROUP-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize associated_pdur_i_pdu_group_refs (list to container "ASSOCIATED-PDUR-I-PDU-GROUP-REFS")
        if self.associated_pdur_i_pdu_group_refs:
            wrapper = ET.Element("ASSOCIATED-PDUR-I-PDU-GROUP-REFS")
            for item in self.associated_pdur_i_pdu_group_refs:
                serialized = SerializationHelper.serialize_item(item, "PdurIPduGroup")
                if serialized is not None:
                    child_elem = ET.Element("ASSOCIATED-PDUR-I-PDU-GROUP-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize channel_synchronous_wakeup
        if self.channel_synchronous_wakeup is not None:
            serialized = SerializationHelper.serialize_item(self.channel_synchronous_wakeup, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CHANNEL-SYNCHRONOUS-WAKEUP")
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

        # Serialize com_configuration_gw_time_base
        if self.com_configuration_gw_time_base is not None:
            serialized = SerializationHelper.serialize_item(self.com_configuration_gw_time_base, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COM-CONFIGURATION-GW-TIME-BASE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize com_configuration_rx_time_base
        if self.com_configuration_rx_time_base is not None:
            serialized = SerializationHelper.serialize_item(self.com_configuration_rx_time_base, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COM-CONFIGURATION-RX-TIME-BASE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize com_configuration_tx_time_base
        if self.com_configuration_tx_time_base is not None:
            serialized = SerializationHelper.serialize_item(self.com_configuration_tx_time_base, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COM-CONFIGURATION-TX-TIME-BASE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize com_enable_mdt_for_cyclic_transmission
        if self.com_enable_mdt_for_cyclic_transmission is not None:
            serialized = SerializationHelper.serialize_item(self.com_enable_mdt_for_cyclic_transmission, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COM-ENABLE-MDT-FOR-CYCLIC-TRANSMISSION")
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
                serialized = SerializationHelper.serialize_item(item, "CommunicationController")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize connectors (list to container "CONNECTORS")
        if self.connectors:
            wrapper = ET.Element("CONNECTORS")
            for item in self.connectors:
                serialized = SerializationHelper.serialize_item(item, "CommunicationConnector")
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

        # Serialize ecu_task_proxy_refs (list to container "ECU-TASK-PROXY-REFS")
        if self.ecu_task_proxy_refs:
            wrapper = ET.Element("ECU-TASK-PROXY-REFS")
            for item in self.ecu_task_proxy_refs:
                serialized = SerializationHelper.serialize_item(item, "OsTaskProxy")
                if serialized is not None:
                    child_elem = ET.Element("ECU-TASK-PROXY-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize eth_switch_port_group_derivation
        if self.eth_switch_port_group_derivation is not None:
            serialized = SerializationHelper.serialize_item(self.eth_switch_port_group_derivation, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ETH-SWITCH-PORT-GROUP-DERIVATION")
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

        # Serialize pnc_prepare_sleep_timer
        if self.pnc_prepare_sleep_timer is not None:
            serialized = SerializationHelper.serialize_item(self.pnc_prepare_sleep_timer, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PNC-PREPARE-SLEEP-TIMER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize pnc_synchronous_wakeup
        if self.pnc_synchronous_wakeup is not None:
            serialized = SerializationHelper.serialize_item(self.pnc_synchronous_wakeup, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PNC-SYNCHRONOUS-WAKEUP")
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

        # Serialize sleep_mode_supported
        if self.sleep_mode_supported is not None:
            serialized = SerializationHelper.serialize_item(self.sleep_mode_supported, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SLEEP-MODE-SUPPORTED")
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
            serialized = SerializationHelper.serialize_item(self.v2x_supported, "V2xSupportEnum")
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

        # Parse associated_com_i_pdu_group_refs (list from container "ASSOCIATED-COM-I-PDU-GROUP-REFS")
        obj.associated_com_i_pdu_group_refs = []
        container = SerializationHelper.find_child_element(element, "ASSOCIATED-COM-I-PDU-GROUP-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.associated_com_i_pdu_group_refs.append(child_value)

        # Parse associated_consumed_provided_service_instance_group_refs (list from container "ASSOCIATED-CONSUMED-PROVIDED-SERVICE-INSTANCE-GROUP-REFS")
        obj.associated_consumed_provided_service_instance_group_refs = []
        container = SerializationHelper.find_child_element(element, "ASSOCIATED-CONSUMED-PROVIDED-SERVICE-INSTANCE-GROUP-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.associated_consumed_provided_service_instance_group_refs.append(child_value)

        # Parse associated_pdur_i_pdu_group_refs (list from container "ASSOCIATED-PDUR-I-PDU-GROUP-REFS")
        obj.associated_pdur_i_pdu_group_refs = []
        container = SerializationHelper.find_child_element(element, "ASSOCIATED-PDUR-I-PDU-GROUP-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.associated_pdur_i_pdu_group_refs.append(child_value)

        # Parse channel_synchronous_wakeup
        child = SerializationHelper.find_child_element(element, "CHANNEL-SYNCHRONOUS-WAKEUP")
        if child is not None:
            channel_synchronous_wakeup_value = child.text
            obj.channel_synchronous_wakeup = channel_synchronous_wakeup_value

        # Parse client_id_range
        child = SerializationHelper.find_child_element(element, "CLIENT-ID-RANGE")
        if child is not None:
            client_id_range_value = SerializationHelper.deserialize_by_tag(child, "ClientIdRange")
            obj.client_id_range = client_id_range_value

        # Parse com_configuration_gw_time_base
        child = SerializationHelper.find_child_element(element, "COM-CONFIGURATION-GW-TIME-BASE")
        if child is not None:
            com_configuration_gw_time_base_value = child.text
            obj.com_configuration_gw_time_base = com_configuration_gw_time_base_value

        # Parse com_configuration_rx_time_base
        child = SerializationHelper.find_child_element(element, "COM-CONFIGURATION-RX-TIME-BASE")
        if child is not None:
            com_configuration_rx_time_base_value = child.text
            obj.com_configuration_rx_time_base = com_configuration_rx_time_base_value

        # Parse com_configuration_tx_time_base
        child = SerializationHelper.find_child_element(element, "COM-CONFIGURATION-TX-TIME-BASE")
        if child is not None:
            com_configuration_tx_time_base_value = child.text
            obj.com_configuration_tx_time_base = com_configuration_tx_time_base_value

        # Parse com_enable_mdt_for_cyclic_transmission
        child = SerializationHelper.find_child_element(element, "COM-ENABLE-MDT-FOR-CYCLIC-TRANSMISSION")
        if child is not None:
            com_enable_mdt_for_cyclic_transmission_value = child.text
            obj.com_enable_mdt_for_cyclic_transmission = com_enable_mdt_for_cyclic_transmission_value

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

        # Parse ecu_task_proxy_refs (list from container "ECU-TASK-PROXY-REFS")
        obj.ecu_task_proxy_refs = []
        container = SerializationHelper.find_child_element(element, "ECU-TASK-PROXY-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.ecu_task_proxy_refs.append(child_value)

        # Parse eth_switch_port_group_derivation
        child = SerializationHelper.find_child_element(element, "ETH-SWITCH-PORT-GROUP-DERIVATION")
        if child is not None:
            eth_switch_port_group_derivation_value = child.text
            obj.eth_switch_port_group_derivation = eth_switch_port_group_derivation_value

        # Parse firewall_rule_refs (list from container "FIREWALL-RULE-REFS")
        obj.firewall_rule_refs = []
        container = SerializationHelper.find_child_element(element, "FIREWALL-RULE-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
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

        # Parse pnc_prepare_sleep_timer
        child = SerializationHelper.find_child_element(element, "PNC-PREPARE-SLEEP-TIMER")
        if child is not None:
            pnc_prepare_sleep_timer_value = child.text
            obj.pnc_prepare_sleep_timer = pnc_prepare_sleep_timer_value

        # Parse pnc_synchronous_wakeup
        child = SerializationHelper.find_child_element(element, "PNC-SYNCHRONOUS-WAKEUP")
        if child is not None:
            pnc_synchronous_wakeup_value = child.text
            obj.pnc_synchronous_wakeup = pnc_synchronous_wakeup_value

        # Parse pn_reset_time
        child = SerializationHelper.find_child_element(element, "PN-RESET-TIME")
        if child is not None:
            pn_reset_time_value = child.text
            obj.pn_reset_time = pn_reset_time_value

        # Parse sleep_mode_supported
        child = SerializationHelper.find_child_element(element, "SLEEP-MODE-SUPPORTED")
        if child is not None:
            sleep_mode_supported_value = child.text
            obj.sleep_mode_supported = sleep_mode_supported_value

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
            v2x_supported_value = SerializationHelper.deserialize_by_tag(child, "V2xSupportEnum")
            obj.v2x_supported = v2x_supported_value

        # Parse wake_up_over_bus_supported
        child = SerializationHelper.find_child_element(element, "WAKE-UP-OVER-BUS-SUPPORTED")
        if child is not None:
            wake_up_over_bus_supported_value = child.text
            obj.wake_up_over_bus_supported = wake_up_over_bus_supported_value

        return obj



class EcuInstanceBuilder(FibexElementBuilder):
    """Builder for EcuInstance with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EcuInstance = EcuInstance()


    def with_associated_com_i_pdu_groups(self, items: list[ISignalIPduGroup]) -> "EcuInstanceBuilder":
        """Set associated_com_i_pdu_groups list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.associated_com_i_pdu_groups = list(items) if items else []
        return self

    def with_associated_consumed_provided_service_instance_groups(self, items: list[ConsumedProvidedServiceInstanceGroup]) -> "EcuInstanceBuilder":
        """Set associated_consumed_provided_service_instance_groups list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.associated_consumed_provided_service_instance_groups = list(items) if items else []
        return self

    def with_associated_pdur_i_pdu_groups(self, items: list[PdurIPduGroup]) -> "EcuInstanceBuilder":
        """Set associated_pdur_i_pdu_groups list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.associated_pdur_i_pdu_groups = list(items) if items else []
        return self

    def with_channel_synchronous_wakeup(self, value: Optional[Boolean]) -> "EcuInstanceBuilder":
        """Set channel_synchronous_wakeup attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.channel_synchronous_wakeup = value
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

    def with_com_configuration_gw_time_base(self, value: Optional[TimeValue]) -> "EcuInstanceBuilder":
        """Set com_configuration_gw_time_base attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.com_configuration_gw_time_base = value
        return self

    def with_com_configuration_rx_time_base(self, value: Optional[TimeValue]) -> "EcuInstanceBuilder":
        """Set com_configuration_rx_time_base attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.com_configuration_rx_time_base = value
        return self

    def with_com_configuration_tx_time_base(self, value: Optional[TimeValue]) -> "EcuInstanceBuilder":
        """Set com_configuration_tx_time_base attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.com_configuration_tx_time_base = value
        return self

    def with_com_enable_mdt_for_cyclic_transmission(self, value: Optional[Boolean]) -> "EcuInstanceBuilder":
        """Set com_enable_mdt_for_cyclic_transmission attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.com_enable_mdt_for_cyclic_transmission = value
        return self

    def with_comm_controllers(self, items: list[CommunicationController]) -> "EcuInstanceBuilder":
        """Set comm_controllers list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.comm_controllers = list(items) if items else []
        return self

    def with_connectors(self, items: list[CommunicationConnector]) -> "EcuInstanceBuilder":
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

    def with_eth_switch_port_group_derivation(self, value: Optional[Boolean]) -> "EcuInstanceBuilder":
        """Set eth_switch_port_group_derivation attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.eth_switch_port_group_derivation = value
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

    def with_pnc_prepare_sleep_timer(self, value: Optional[TimeValue]) -> "EcuInstanceBuilder":
        """Set pnc_prepare_sleep_timer attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.pnc_prepare_sleep_timer = value
        return self

    def with_pnc_synchronous_wakeup(self, value: Optional[Boolean]) -> "EcuInstanceBuilder":
        """Set pnc_synchronous_wakeup attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.pnc_synchronous_wakeup = value
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

    def with_sleep_mode_supported(self, value: Optional[Boolean]) -> "EcuInstanceBuilder":
        """Set sleep_mode_supported attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sleep_mode_supported = value
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

    def with_v2x_supported(self, value: Optional[V2xSupportEnum]) -> "EcuInstanceBuilder":
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


    def add_associated_com_i_pdu_group(self, item: ISignalIPduGroup) -> "EcuInstanceBuilder":
        """Add a single item to associated_com_i_pdu_groups list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.associated_com_i_pdu_groups.append(item)
        return self

    def clear_associated_com_i_pdu_groups(self) -> "EcuInstanceBuilder":
        """Clear all items from associated_com_i_pdu_groups list.

        Returns:
            self for method chaining
        """
        self._obj.associated_com_i_pdu_groups = []
        return self

    def add_associated_consumed_provided_service_instance_group(self, item: ConsumedProvidedServiceInstanceGroup) -> "EcuInstanceBuilder":
        """Add a single item to associated_consumed_provided_service_instance_groups list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.associated_consumed_provided_service_instance_groups.append(item)
        return self

    def clear_associated_consumed_provided_service_instance_groups(self) -> "EcuInstanceBuilder":
        """Clear all items from associated_consumed_provided_service_instance_groups list.

        Returns:
            self for method chaining
        """
        self._obj.associated_consumed_provided_service_instance_groups = []
        return self

    def add_associated_pdur_i_pdu_group(self, item: PdurIPduGroup) -> "EcuInstanceBuilder":
        """Add a single item to associated_pdur_i_pdu_groups list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.associated_pdur_i_pdu_groups.append(item)
        return self

    def clear_associated_pdur_i_pdu_groups(self) -> "EcuInstanceBuilder":
        """Clear all items from associated_pdur_i_pdu_groups list.

        Returns:
            self for method chaining
        """
        self._obj.associated_pdur_i_pdu_groups = []
        return self

    def add_comm_controller(self, item: CommunicationController) -> "EcuInstanceBuilder":
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

    def add_connector(self, item: CommunicationConnector) -> "EcuInstanceBuilder":
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

    def add_ecu_task_proxy(self, item: OsTaskProxy) -> "EcuInstanceBuilder":
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



    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

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