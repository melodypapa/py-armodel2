"""IEEE1722Tp module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.ieee1722_tp_config import (
        IEEE1722TpConfig,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.ieee1722_tp_connection import (
        IEEE1722TpConnection,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.ieee1722_tp_av_connection import (
        IEEE1722TpAvConnection,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.ieee1722_tp_acf_connection import (
        IEEE1722TpAcfConnection,
    )

__all__ = [
    "IEEE1722TpAcfConnection",
    "IEEE1722TpAvConnection",
    "IEEE1722TpConfig",
    "IEEE1722TpConnection",
]
