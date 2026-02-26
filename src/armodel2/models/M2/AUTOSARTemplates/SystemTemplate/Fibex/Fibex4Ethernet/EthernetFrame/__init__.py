"""EthernetFrame module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetFrame.abstract_ethernet_frame import (
        AbstractEthernetFrame,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetFrame.ethernet_frame_triggering import (
        EthernetFrameTriggering,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetFrame.generic_ethernet_frame import (
        GenericEthernetFrame,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetFrame.user_defined_ethernet_frame import (
        UserDefinedEthernetFrame,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetFrame.ieee1722_tp_ethernet_frame import (
        Ieee1722TpEthernetFrame,
    )

__all__ = [
    "AbstractEthernetFrame",
    "EthernetFrameTriggering",
    "GenericEthernetFrame",
    "Ieee1722TpEthernetFrame",
    "UserDefinedEthernetFrame",
]
