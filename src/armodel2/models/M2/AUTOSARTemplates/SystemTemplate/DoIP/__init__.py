"""DoIP module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.DoIP.do_ip_config import (
        DoIpConfig,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.DoIP.do_ip_interface import (
        DoIpInterface,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.DoIP.do_ip_routing_activation import (
        DoIpRoutingActivation,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.DoIP.abstract_do_ip_logic_address_props import (
        AbstractDoIpLogicAddressProps,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.DoIP.do_ip_logic_target_address_props import (
        DoIpLogicTargetAddressProps,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.DoIP.do_ip_logic_tester_address_props import (
        DoIpLogicTesterAddressProps,
    )

__all__ = [
    "AbstractDoIpLogicAddressProps",
    "DoIpConfig",
    "DoIpInterface",
    "DoIpLogicTargetAddressProps",
    "DoIpLogicTesterAddressProps",
    "DoIpRoutingActivation",
]
