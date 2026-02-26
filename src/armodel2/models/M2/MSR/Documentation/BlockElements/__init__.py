"""BlockElements module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.MSR.Documentation.BlockElements.documentation_block import (
        DocumentationBlock,
    )
    from armodel2.models.M2.MSR.Documentation.BlockElements.caption import (
        Caption,
    )

__all__ = [
    "Caption",
    "DocumentationBlock",
]
