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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcuInstance":
        """Deserialize XML element to EcuInstance object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcuInstance object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse associated_com_refs (list)
        obj.associated_com_refs = []
        for child in ARObject._find_all_child_elements(element, "ASSOCIATED-COMS"):
            associated_com_refs_value = ARObject._deserialize_by_tag(child, "ISignalIPduGroup")
            obj.associated_com_refs.append(associated_com_refs_value)

        # Parse associateds (list)
        obj.associateds = []
        for child in ARObject._find_all_child_elements(element, "ASSOCIATEDS"):
            associateds_value = ARObject._deserialize_by_tag(child, "ConsumedProvidedServiceInstanceGroup")
            obj.associateds.append(associateds_value)

        # Parse associated_pdur_refs (list)
        obj.associated_pdur_refs = []
        for child in ARObject._find_all_child_elements(element, "ASSOCIATED-PDURS"):
            associated_pdur_refs_value = ARObject._deserialize_by_tag(child, "PdurIPduGroup")
            obj.associated_pdur_refs.append(associated_pdur_refs_value)

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

        # Parse comm_controllers (list)
        obj.comm_controllers = []
        for child in ARObject._find_all_child_elements(element, "COMM-CONTROLLERS"):
            comm_controllers_value = child.text
            obj.comm_controllers.append(comm_controllers_value)

        # Parse connectors (list)
        obj.connectors = []
        for child in ARObject._find_all_child_elements(element, "CONNECTORS"):
            connectors_value = child.text
            obj.connectors.append(connectors_value)

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

        # Parse ecu_task_proxies (list)
        obj.ecu_task_proxies = []
        for child in ARObject._find_all_child_elements(element, "ECU-TASK-PROXIES"):
            ecu_task_proxies_value = ARObject._deserialize_by_tag(child, "OsTaskProxy")
            obj.ecu_task_proxies.append(ecu_task_proxies_value)

        # Parse eth_switch_port
        child = ARObject._find_child_element(element, "ETH-SWITCH-PORT")
        if child is not None:
            eth_switch_port_value = child.text
            obj.eth_switch_port = eth_switch_port_value

        # Parse firewall_rules (list)
        obj.firewall_rules = []
        for child in ARObject._find_all_child_elements(element, "FIREWALL-RULES"):
            firewall_rules_value = ARObject._deserialize_by_tag(child, "StateDependentFirewall")
            obj.firewall_rules.append(firewall_rules_value)

        # Parse partitions (list)
        obj.partitions = []
        for child in ARObject._find_all_child_elements(element, "PARTITIONS"):
            partitions_value = ARObject._deserialize_by_tag(child, "EcuPartition")
            obj.partitions.append(partitions_value)

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
