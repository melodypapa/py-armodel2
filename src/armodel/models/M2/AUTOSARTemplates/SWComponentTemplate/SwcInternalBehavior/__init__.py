"""SwcInternalBehavior module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.runnable_entity import (
        RunnableEntity,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.swc_internal_behavior import (
        SwcInternalBehavior,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.swc_exclusive_area_policy import (
        SwcExclusiveAreaPolicy,
    )

__all__ = [
    "RunnableEntity",
    "SwcExclusiveAreaPolicy",
    "SwcInternalBehavior",
]
