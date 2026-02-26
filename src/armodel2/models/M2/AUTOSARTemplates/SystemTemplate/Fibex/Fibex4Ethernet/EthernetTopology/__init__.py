"""EthernetTopology module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ethernet_physical_channel import (
        EthernetPhysicalChannel,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ethernet_cluster import (
        EthernetCluster,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.mac_multicast_group import (
        MacMulticastGroup,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.vlan_config import (
        VlanConfig,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_element import (
        CouplingElement,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port import (
        CouplingPort,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.vlan_membership import (
        VlanMembership,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port_connection import (
        CouplingPortConnection,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ethernet_communication_controller import (
        EthernetCommunicationController,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ethernet_communication_connector import (
        EthernetCommunicationConnector,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port_details import (
        CouplingPortDetails,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port_structural_element import (
        CouplingPortStructuralElement,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port_scheduler import (
        CouplingPortScheduler,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port_shaper import (
        CouplingPortShaper,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port_fifo import (
        CouplingPortFifo,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port_rate_policy import (
        CouplingPortRatePolicy,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ethernet_priority_regeneration import (
        EthernetPriorityRegeneration,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port_traffic_class_assignment import (
        CouplingPortTrafficClassAssignment,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.dhcp_server_configuration import (
        DhcpServerConfiguration,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ipv4_dhcp_server_configuration import (
        Ipv4DhcpServerConfiguration,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ipv6_dhcp_server_configuration import (
        Ipv6DhcpServerConfiguration,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_element_abstract_details import (
        CouplingElementAbstractDetails,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_element_switch_details import (
        CouplingElementSwitchDetails,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.switch_stream_identification import (
        SwitchStreamIdentification,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.switch_stream_filter_rule import (
        SwitchStreamFilterRule,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.stream_filter_rule_data_link_layer import (
        StreamFilterRuleDataLinkLayer,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.stream_filter_mac_address import (
        StreamFilterMACAddress,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.stream_filter_rule_ip_tp import (
        StreamFilterRuleIpTp,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.stream_filter_ipv4_address import (
        StreamFilterIpv4Address,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.stream_filter_ipv6_address import (
        StreamFilterIpv6Address,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.stream_filter_port_range import (
        StreamFilterPortRange,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.stream_filter_ieee1722_tp import (
        StreamFilterIEEE1722Tp,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.switch_stream_filter_action_dest_port_modification import (
        SwitchStreamFilterActionDestPortModification,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.switch_stream_filter_entry import (
        SwitchStreamFilterEntry,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.switch_asynchronous_traffic_shaper_group_entry import (
        SwitchAsynchronousTrafficShaperGroupEntry,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.switch_stream_gate_entry import (
        SwitchStreamGateEntry,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.switch_flow_metering_entry import (
        SwitchFlowMeteringEntry,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.eth_ip_props import (
        EthIpProps,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ipv4_props import (
        Ipv4Props,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ipv4_arp_props import (
        Ipv4ArpProps,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ipv4_auto_ip_props import (
        Ipv4AutoIpProps,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ipv4_fragmentation_props import (
        Ipv4FragmentationProps,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ipv6_props import (
        Ipv6Props,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ipv6_fragmentation_props import (
        Ipv6FragmentationProps,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.dhcpv6_props import (
        Dhcpv6Props,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ipv6_ndp_props import (
        Ipv6NdpProps,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.eth_tcp_ip_props import (
        EthTcpIpProps,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.udp_props import (
        UdpProps,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.tcp_props import (
        TcpProps,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.eth_tcp_ip_icmp_props import (
        EthTcpIpIcmpProps,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.tcp_ip_icmpv4_props import (
        TcpIpIcmpv4Props,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.tcp_ip_icmpv6_props import (
        TcpIpIcmpv6Props,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ethernet_wakeup_sleep_on_dataline_config import (
        EthernetWakeupSleepOnDatalineConfig,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ethernet_wakeup_sleep_on_dataline_config_set import (
        EthernetWakeupSleepOnDatalineConfigSet,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.plca_props import (
        PlcaProps,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.application_endpoint import (
        ApplicationEndpoint,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.transport_protocol_configuration import (
        TransportProtocolConfiguration,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.generic_tp import (
        GenericTp,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.tcp_udp_config import (
        TcpUdpConfig,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.udp_tp import (
        UdpTp,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.tcp_tp import (
        TcpTp,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.rtp_tp import (
        RtpTp,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ieee1722_tp import (
        Ieee1722Tp,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.http_tp import (
        HttpTp,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.tp_port import (
        TpPort,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.network_endpoint import (
        NetworkEndpoint,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.network_endpoint_address import (
        NetworkEndpointAddress,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ipv4_configuration import (
        Ipv4Configuration,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ipv6_configuration import (
        Ipv6Configuration,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.mac_multicast_configuration import (
        MacMulticastConfiguration,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.infrastructure_services import (
        InfrastructureServices,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.time_synchronization import (
        TimeSynchronization,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.time_sync_client_configuration import (
        TimeSyncClientConfiguration,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.time_sync_server_configuration import (
        TimeSyncServerConfiguration,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ordered_master import (
        OrderedMaster,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.do_ip_entity import (
        DoIpEntity,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.global_time_coupling_port_props import (
        GlobalTimeCouplingPortProps,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port_asynchronous_traffic_shaper import (
        CouplingPortAsynchronousTrafficShaper,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port_credit_based_shaper import (
        CouplingPortCreditBasedShaper,
    )

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_element_enum import (
    CouplingElementEnum,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ethernet_connection_negotiation_enum import (
    EthernetConnectionNegotiationEnum,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ethernet_mac_layer_type_enum import (
    EthernetMacLayerTypeEnum,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ethernet_physical_layer_type_enum import (
    EthernetPhysicalLayerTypeEnum,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ethernet_switch_vlan_ingress_tag_enum import (
    EthernetSwitchVlanIngressTagEnum,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ethernet_coupling_port_scheduler_enum import (
    EthernetCouplingPortSchedulerEnum,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port_rate_policy_action_enum import (
    CouplingPortRatePolicyActionEnum,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ethernet_switch_vlan_egress_tagging_enum import (
    EthernetSwitchVlanEgressTaggingEnum,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.switch_stream_filter_action_port_modification_enum import (
    SwitchStreamFilterActionPortModificationEnum,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.flow_metering_color_mode_enum import (
    FlowMeteringColorModeEnum,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ipv4_address_source_enum import (
    Ipv4AddressSourceEnum,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ip_address_keep_enum import (
    IpAddressKeepEnum,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ipv6_address_source_enum import (
    Ipv6AddressSourceEnum,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.time_sync_technology_enum import (
    TimeSyncTechnologyEnum,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.do_ip_entity_role_enum import (
    DoIpEntityRoleEnum,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port_role_enum import (
    CouplingPortRoleEnum,
)

__all__ = [
    "ApplicationEndpoint",
    "CouplingElement",
    "CouplingElementAbstractDetails",
    "CouplingElementEnum",
    "CouplingElementSwitchDetails",
    "CouplingPort",
    "CouplingPortAsynchronousTrafficShaper",
    "CouplingPortConnection",
    "CouplingPortCreditBasedShaper",
    "CouplingPortDetails",
    "CouplingPortFifo",
    "CouplingPortRatePolicy",
    "CouplingPortRatePolicyActionEnum",
    "CouplingPortRoleEnum",
    "CouplingPortScheduler",
    "CouplingPortShaper",
    "CouplingPortStructuralElement",
    "CouplingPortTrafficClassAssignment",
    "DhcpServerConfiguration",
    "Dhcpv6Props",
    "DoIpEntity",
    "DoIpEntityRoleEnum",
    "EthIpProps",
    "EthTcpIpIcmpProps",
    "EthTcpIpProps",
    "EthernetCluster",
    "EthernetCommunicationConnector",
    "EthernetCommunicationController",
    "EthernetConnectionNegotiationEnum",
    "EthernetCouplingPortSchedulerEnum",
    "EthernetMacLayerTypeEnum",
    "EthernetPhysicalChannel",
    "EthernetPhysicalLayerTypeEnum",
    "EthernetPriorityRegeneration",
    "EthernetSwitchVlanEgressTaggingEnum",
    "EthernetSwitchVlanIngressTagEnum",
    "EthernetWakeupSleepOnDatalineConfig",
    "EthernetWakeupSleepOnDatalineConfigSet",
    "FlowMeteringColorModeEnum",
    "GenericTp",
    "GlobalTimeCouplingPortProps",
    "HttpTp",
    "Ieee1722Tp",
    "InfrastructureServices",
    "IpAddressKeepEnum",
    "Ipv4AddressSourceEnum",
    "Ipv4ArpProps",
    "Ipv4AutoIpProps",
    "Ipv4Configuration",
    "Ipv4DhcpServerConfiguration",
    "Ipv4FragmentationProps",
    "Ipv4Props",
    "Ipv6AddressSourceEnum",
    "Ipv6Configuration",
    "Ipv6DhcpServerConfiguration",
    "Ipv6FragmentationProps",
    "Ipv6NdpProps",
    "Ipv6Props",
    "MacMulticastConfiguration",
    "MacMulticastGroup",
    "NetworkEndpoint",
    "NetworkEndpointAddress",
    "OrderedMaster",
    "PlcaProps",
    "RtpTp",
    "StreamFilterIEEE1722Tp",
    "StreamFilterIpv4Address",
    "StreamFilterIpv6Address",
    "StreamFilterMACAddress",
    "StreamFilterPortRange",
    "StreamFilterRuleDataLinkLayer",
    "StreamFilterRuleIpTp",
    "SwitchAsynchronousTrafficShaperGroupEntry",
    "SwitchFlowMeteringEntry",
    "SwitchStreamFilterActionDestPortModification",
    "SwitchStreamFilterActionPortModificationEnum",
    "SwitchStreamFilterEntry",
    "SwitchStreamFilterRule",
    "SwitchStreamGateEntry",
    "SwitchStreamIdentification",
    "TcpIpIcmpv4Props",
    "TcpIpIcmpv6Props",
    "TcpProps",
    "TcpTp",
    "TcpUdpConfig",
    "TimeSyncClientConfiguration",
    "TimeSyncServerConfiguration",
    "TimeSyncTechnologyEnum",
    "TimeSynchronization",
    "TpPort",
    "TransportProtocolConfiguration",
    "UdpProps",
    "UdpTp",
    "VlanConfig",
    "VlanMembership",
]
