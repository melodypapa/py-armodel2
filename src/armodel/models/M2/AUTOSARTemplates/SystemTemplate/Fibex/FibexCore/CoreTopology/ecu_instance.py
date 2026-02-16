"""EcuInstance AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
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
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("associated_coms", None, False, True, ISignalIPduGroup),  # associatedComs
        ("associateds", None, False, True, ConsumedProvidedServiceInstanceGroup),  # associateds
        ("associated_pdurs", None, False, True, PdurIPduGroup),  # associatedPdurs
        ("channel", None, True, False, None),  # channel
        ("client_id_range", None, False, False, ClientIdRange),  # clientIdRange
        ("com", None, True, False, None),  # com
        ("com_enable", None, True, False, None),  # comEnable
        ("comm_controllers", None, False, True, any (Communication)),  # commControllers
        ("connectors", None, False, True, any (Communication)),  # connectors
        ("dlt_config", None, False, False, DltConfig),  # dltConfig
        ("do_ip_config", None, False, False, DoIpConfig),  # doIpConfig
        ("ecu_task_proxies", None, False, True, OsTaskProxy),  # ecuTaskProxies
        ("eth_switch_port", None, True, False, None),  # ethSwitchPort
        ("firewall_rules", None, False, True, StateDependentFirewall),  # firewallRules
        ("partitions", None, False, True, EcuPartition),  # partitions
        ("pnc_nm_request", None, True, False, None),  # pncNmRequest
        ("pnc_prepare", None, True, False, None),  # pncPrepare
        ("pnc", None, True, False, None),  # pnc
        ("pn_reset_time", None, True, False, None),  # pnResetTime
        ("sleep_mode", None, True, False, None),  # sleepMode
        ("tcp_ip_icmp_props", None, False, False, EthTcpIpIcmpProps),  # tcpIpIcmpProps
        ("tcp_ip_props", None, False, False, EthTcpIpProps),  # tcpIpProps
        ("v2x_supported", None, False, False, any (V2xSupportEnum)),  # v2xSupported
        ("wake_up_over_bus_supported", None, True, False, None),  # wakeUpOverBusSupported
    ]

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

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EcuInstance to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcuInstance":
        """Create EcuInstance from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EcuInstance instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EcuInstance since parent returns ARObject
        return cast("EcuInstance", obj)


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
