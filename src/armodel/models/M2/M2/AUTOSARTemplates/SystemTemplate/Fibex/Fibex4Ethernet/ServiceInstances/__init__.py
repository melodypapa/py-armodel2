"""ServiceInstances module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.consumed_event_group import (
        ConsumedEventGroup,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.consumed_service_instance import (
        ConsumedServiceInstance,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.provided_service_instance import (
        ProvidedServiceInstance,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.so_ad_config import (
        SoAdConfig,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.socket_address import (
        SocketAddress,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.service_instance_collection_set import (
        ServiceInstanceCollectionSet,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.abstract_service_instance import (
        AbstractServiceInstance,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.pdu_activation_routing_group import (
        PduActivationRoutingGroup,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.so_con_i_pdu_identifier import (
        SoConIPduIdentifier,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.socket_connection_ipdu_identifier_set import (
        SocketConnectionIpduIdentifierSet,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.event_handler import (
        EventHandler,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.someip_sd_server_service_instance_config import (
        SomeipSdServerServiceInstanceConfig,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.initial_sd_delay_config import (
        InitialSdDelayConfig,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.request_response_delay import (
        RequestResponseDelay,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.someip_sd_server_event_group_timing_config import (
        SomeipSdServerEventGroupTimingConfig,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.someip_sd_client_event_group_timing_config import (
        SomeipSdClientEventGroupTimingConfig,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.consumed_provided_service_instance_group import (
        ConsumedProvidedServiceInstanceGroup,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.static_socket_connection import (
        StaticSocketConnection,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.someip_sd_client_service_instance_config import (
        SomeipSdClientServiceInstanceConfig,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.someip_service_version import (
        SomeipServiceVersion,
    )

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.pdu_collection_trigger_enum import (
    PduCollectionTriggerEnum,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.udp_checksum_calculation_enum import (
    UdpChecksumCalculationEnum,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.event_group_control_type_enum import (
    EventGroupControlTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.pdu_collection_semantics_enum import (
    PduCollectionSemanticsEnum,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.service_version_acceptance_kind_enum import (
    ServiceVersionAcceptanceKindEnum,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.tcp_role_enum import (
    TcpRoleEnum,
)

__all__ = [
    "AbstractServiceInstance",
    "ConsumedEventGroup",
    "ConsumedProvidedServiceInstanceGroup",
    "ConsumedServiceInstance",
    "EventGroupControlTypeEnum",
    "EventHandler",
    "InitialSdDelayConfig",
    "PduActivationRoutingGroup",
    "PduCollectionSemanticsEnum",
    "PduCollectionTriggerEnum",
    "ProvidedServiceInstance",
    "RequestResponseDelay",
    "ServiceInstanceCollectionSet",
    "ServiceVersionAcceptanceKindEnum",
    "SoAdConfig",
    "SoConIPduIdentifier",
    "SocketAddress",
    "SocketConnectionIpduIdentifierSet",
    "SomeipSdClientEventGroupTimingConfig",
    "SomeipSdClientServiceInstanceConfig",
    "SomeipSdServerEventGroupTimingConfig",
    "SomeipSdServerServiceInstanceConfig",
    "SomeipServiceVersion",
    "StaticSocketConnection",
    "TcpRoleEnum",
    "UdpChecksumCalculationEnum",
]
