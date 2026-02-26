"""Blueprint module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.Blueprint.consistency_needs_blueprint_set import (
        ConsistencyNeedsBlueprintSet,
    )

__all__ = [
    "ConsistencyNeedsBlueprintSet",
]
