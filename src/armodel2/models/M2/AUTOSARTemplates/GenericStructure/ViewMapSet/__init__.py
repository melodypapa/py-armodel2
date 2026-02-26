"""ViewMapSet module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.GenericStructure.ViewMapSet.view_map import (
        ViewMap,
    )
    from armodel2.models.M2.AUTOSARTemplates.GenericStructure.ViewMapSet.view_map_set import (
        ViewMapSet,
    )

__all__ = [
    "ViewMap",
    "ViewMapSet",
]
