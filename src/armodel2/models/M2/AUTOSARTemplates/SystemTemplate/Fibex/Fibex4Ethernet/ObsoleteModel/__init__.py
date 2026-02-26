"""ObsoleteModel module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ObsoleteModel.so_ad_routing_group import (
        SoAdRoutingGroup,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ObsoleteModel.socket_connection import (
        SocketConnection,
    )

__all__ = [
    "SoAdRoutingGroup",
    "SocketConnection",
]
