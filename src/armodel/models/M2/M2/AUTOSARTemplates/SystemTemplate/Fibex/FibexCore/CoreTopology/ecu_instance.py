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
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "associated_coms": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=ISignalIPduGroup,
        ),  # associatedComs
        "associateds": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=ConsumedProvidedServiceInstanceGroup,
        ),  # associateds
        "associated_pdurs": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=PdurIPduGroup,
        ),  # associatedPdurs
        "channel": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # channel
        "client_id_range": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ClientIdRange,
        ),  # clientIdRange
        "com": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # com
        "com_enable": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # comEnable
        "comm_controllers": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=Any,
        ),  # commControllers
        "connectors": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=Any,
        ),  # connectors
        "dlt_config": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DltConfig,
        ),  # dltConfig
        "do_ip_config": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DoIpConfig,
        ),  # doIpConfig
        "ecu_task_proxies": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=OsTaskProxy,
        ),  # ecuTaskProxies
        "eth_switch_port": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # ethSwitchPort
        "firewall_rules": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=StateDependentFirewall,
        ),  # firewallRules
        "partitions": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=EcuPartition,
        ),  # partitions
        "pnc_nm_request": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # pncNmRequest
        "pnc_prepare": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # pncPrepare
        "pnc": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # pnc
        "pn_reset_time": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # pnResetTime
        "sleep_mode": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # sleepMode
        "tcp_ip_icmp_props": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=EthTcpIpIcmpProps,
        ),  # tcpIpIcmpProps
        "tcp_ip_props": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=EthTcpIpProps,
        ),  # tcpIpProps
        "v2x_supported": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Any,
        ),  # v2xSupported
        "wake_up_over_bus_supported": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # wakeUpOverBusSupported
    }

    def __init__(self) -> None:
        """Initialize EcuInstance."""
        super().__init__()
        self.associated_coms: list[ISignalIPduGroup] = []
        self.associateds: list[ConsumedProvidedServiceInstanceGroup] = []
        self.associated_pdurs: list[PdurIPduGroup] = []
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
