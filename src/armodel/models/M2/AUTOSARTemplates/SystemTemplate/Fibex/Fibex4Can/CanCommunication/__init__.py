"""CanCommunication module."""
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

__all__ = [
    "CanFrame",
    "CanFrameTriggering",
    "CanXlFrameTriggeringProps",
    "RxIdentifierRange",
]
