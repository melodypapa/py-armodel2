"""Timing module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.Timing.transmission_mode_declaration import (
        TransmissionModeDeclaration,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.Timing.transmission_mode_condition import (
        TransmissionModeCondition,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.Timing.mode_driven_transmission_mode_condition import (
        ModeDrivenTransmissionModeCondition,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.Timing.transmission_mode_timing import (
        TransmissionModeTiming,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.Timing.cyclic_timing import (
        CyclicTiming,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.Timing.event_controlled_timing import (
        EventControlledTiming,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.Timing.time_range_type import (
        TimeRangeType,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.Timing.relative_tolerance import (
        RelativeTolerance,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.Timing.absolute_tolerance import (
        AbsoluteTolerance,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.Timing.trigger_i_pdu_send_condition import (
        TriggerIPduSendCondition,
    )

__all__ = [
    "AbsoluteTolerance",
    "CyclicTiming",
    "EventControlledTiming",
    "ModeDrivenTransmissionModeCondition",
    "RelativeTolerance",
    "TimeRangeType",
    "TransmissionModeCondition",
    "TransmissionModeDeclaration",
    "TransmissionModeTiming",
    "TriggerIPduSendCondition",
]
