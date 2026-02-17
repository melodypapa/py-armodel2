"""Trigger module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.Trigger.external_triggering_point import (
        ExternalTriggeringPoint,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.Trigger.internal_triggering_point import (
        InternalTriggeringPoint,
    )

__all__ = [
    "ExternalTriggeringPoint",
    "InternalTriggeringPoint",
]
