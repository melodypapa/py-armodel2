"""SystemConstant module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.MSR.DataDictionary.SystemConstant.sw_systemconst import (
        SwSystemconst,
    )

__all__ = [
    "SwSystemconst",
]
