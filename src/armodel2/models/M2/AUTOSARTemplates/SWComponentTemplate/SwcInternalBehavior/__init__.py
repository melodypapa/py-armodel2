"""SwcInternalBehavior module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.runnable_entity import (
        RunnableEntity,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.swc_internal_behavior import (
        SwcInternalBehavior,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.swc_exclusive_area_policy import (
        SwcExclusiveAreaPolicy,
    )

from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.handle_termination_and_restart_enum import (
    HandleTerminationAndRestartEnum,
)

__all__ = [
    "HandleTerminationAndRestartEnum",
    "RunnableEntity",
    "SwcExclusiveAreaPolicy",
    "SwcInternalBehavior",
]
