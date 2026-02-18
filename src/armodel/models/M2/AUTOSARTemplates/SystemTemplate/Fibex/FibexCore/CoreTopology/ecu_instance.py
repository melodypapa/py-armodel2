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
