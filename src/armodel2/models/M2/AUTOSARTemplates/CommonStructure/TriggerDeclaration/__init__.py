"""TriggerDeclaration module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger import (
        Trigger,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger_mapping import (
        TriggerMapping,
    )

__all__ = [
    "Trigger",
    "TriggerMapping",
]
