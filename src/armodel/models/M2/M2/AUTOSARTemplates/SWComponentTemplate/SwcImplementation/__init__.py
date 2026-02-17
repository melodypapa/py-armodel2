"""SwcImplementation module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcImplementation.swc_implementation import (
        SwcImplementation,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcImplementation.per_instance_memory_size import (
        PerInstanceMemorySize,
    )

__all__ = [
    "PerInstanceMemorySize",
    "SwcImplementation",
]
