"""SwcBswMapping module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.SwcBswMapping.swc_bsw_mapping import (
        SwcBswMapping,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.SwcBswMapping.swc_bsw_runnable_mapping import (
        SwcBswRunnableMapping,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.SwcBswMapping.swc_bsw_synchronized_mode_group_prototype import (
        SwcBswSynchronizedModeGroupPrototype,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.SwcBswMapping.swc_bsw_synchronized_trigger import (
        SwcBswSynchronizedTrigger,
    )

__all__ = [
    "SwcBswMapping",
    "SwcBswRunnableMapping",
    "SwcBswSynchronizedModeGroupPrototype",
    "SwcBswSynchronizedTrigger",
]
