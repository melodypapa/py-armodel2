"""IEEE1722TpAcf module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAcf.ieee1722_tp_acf_bus import (
        IEEE1722TpAcfBus,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAcf.ieee1722_tp_acf_bus_part import (
        IEEE1722TpAcfBusPart,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAcf.ieee1722_tp_acf_can import (
        IEEE1722TpAcfCan,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAcf.ieee1722_tp_acf_can_part import (
        IEEE1722TpAcfCanPart,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAcf.ieee1722_tp_acf_lin import (
        IEEE1722TpAcfLin,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAcf.ieee1722_tp_acf_lin_part import (
        IEEE1722TpAcfLinPart,
    )

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAcf.ieee1722_tp_acf_can_message_type_enum import (
    IEEE1722TpAcfCanMessageTypeEnum,
)

__all__ = [
    "IEEE1722TpAcfBus",
    "IEEE1722TpAcfBusPart",
    "IEEE1722TpAcfCan",
    "IEEE1722TpAcfCanMessageTypeEnum",
    "IEEE1722TpAcfCanPart",
    "IEEE1722TpAcfLin",
    "IEEE1722TpAcfLinPart",
]
