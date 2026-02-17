"""TransportProtocols module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.do_ip_tp_config import (
        DoIpTpConfig,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.do_ip_logic_address import (
        DoIpLogicAddress,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_config import (
        TpConfig,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_address import (
        TpAddress,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.flexray_tp_config import (
        FlexrayTpConfig,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.flexray_tp_connection_control import (
        FlexrayTpConnectionControl,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.flexray_tp_connection import (
        FlexrayTpConnection,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.flexray_tp_pdu_pool import (
        FlexrayTpPduPool,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.flexray_tp_node import (
        FlexrayTpNode,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.flexray_tp_ecu import (
        FlexrayTpEcu,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.flexray_ar_tp_config import (
        FlexrayArTpConfig,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.flexray_ar_tp_channel import (
        FlexrayArTpChannel,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.flexray_ar_tp_node import (
        FlexrayArTpNode,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.flexray_ar_tp_connection import (
        FlexrayArTpConnection,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.can_tp_config import (
        CanTpConfig,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.can_tp_channel import (
        CanTpChannel,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.can_tp_connection import (
        CanTpConnection,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.can_tp_address import (
        CanTpAddress,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.can_tp_ecu import (
        CanTpEcu,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.can_tp_node import (
        CanTpNode,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.lin_tp_config import (
        LinTpConfig,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.lin_tp_node import (
        LinTpNode,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.lin_tp_connection import (
        LinTpConnection,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.eth_tp_config import (
        EthTpConfig,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.eth_tp_connection import (
        EthTpConnection,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.someip_tp_config import (
        SomeipTpConfig,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.someip_tp_connection import (
        SomeipTpConnection,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.someip_tp_channel import (
        SomeipTpChannel,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.j1939_tp_config import (
        J1939TpConfig,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.j1939_tp_connection import (
        J1939TpConnection,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.j1939_tp_pg import (
        J1939TpPg,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.j1939_tp_node import (
        J1939TpNode,
    )

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.fr_ar_tp_ack_type import (
    FrArTpAckType,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.maximum_message_length_type import (
    MaximumMessageLengthType,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.can_tp_addressing_format_type import (
    CanTpAddressingFormatType,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.network_target_address_type import (
    NetworkTargetAddressType,
)

__all__ = [
    "CanTpAddress",
    "CanTpAddressingFormatType",
    "CanTpChannel",
    "CanTpConfig",
    "CanTpConnection",
    "CanTpEcu",
    "CanTpNode",
    "DoIpLogicAddress",
    "DoIpTpConfig",
    "EthTpConfig",
    "EthTpConnection",
    "FlexrayArTpChannel",
    "FlexrayArTpConfig",
    "FlexrayArTpConnection",
    "FlexrayArTpNode",
    "FlexrayTpConfig",
    "FlexrayTpConnection",
    "FlexrayTpConnectionControl",
    "FlexrayTpEcu",
    "FlexrayTpNode",
    "FlexrayTpPduPool",
    "FrArTpAckType",
    "J1939TpConfig",
    "J1939TpConnection",
    "J1939TpNode",
    "J1939TpPg",
    "LinTpConfig",
    "LinTpConnection",
    "LinTpNode",
    "MaximumMessageLengthType",
    "NetworkTargetAddressType",
    "SomeipTpChannel",
    "SomeipTpConfig",
    "SomeipTpConnection",
    "TpAddress",
    "TpConfig",
]
