"""CanCommunication module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication.can_frame import (
        CanFrame,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication.can_frame_triggering import (
        CanFrameTriggering,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication.rx_identifier_range import (
        RxIdentifierRange,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication.can_xl_frame_triggering_props import (
        CanXlFrameTriggeringProps,
    )

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication.can_addressing_mode_type import (
    CanAddressingModeType,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication.can_frame_rx_behavior_enum import (
    CanFrameRxBehaviorEnum,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication.can_frame_tx_behavior_enum import (
    CanFrameTxBehaviorEnum,
)

__all__ = [
    "CanAddressingModeType",
    "CanFrame",
    "CanFrameRxBehaviorEnum",
    "CanFrameTriggering",
    "CanFrameTxBehaviorEnum",
    "CanXlFrameTriggeringProps",
    "RxIdentifierRange",
]
