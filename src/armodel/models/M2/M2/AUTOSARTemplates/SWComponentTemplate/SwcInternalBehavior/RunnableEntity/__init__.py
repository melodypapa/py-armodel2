"""RunnableEntity module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RunnableEntity.runnable_entity_argument import (
        RunnableEntityArgument,
    )

__all__ = [
    "RunnableEntityArgument",
]
