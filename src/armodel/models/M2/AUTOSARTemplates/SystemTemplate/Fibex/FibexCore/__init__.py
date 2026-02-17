"""FibexCore module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
        FibexElement,
    )

__all__ = [
    "FibexElement",
]
