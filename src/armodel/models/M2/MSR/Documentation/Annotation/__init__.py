"""Annotation module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.MSR.Documentation.Annotation.annotation import (
        Annotation,
    )

__all__ = [
    "Annotation",
]
