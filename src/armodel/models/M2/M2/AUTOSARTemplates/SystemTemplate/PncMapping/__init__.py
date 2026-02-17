"""PncMapping module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.PncMapping.pnc_mapping import (
        PncMapping,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.PncMapping.pnc_mapping_ident import (
        PncMappingIdent,
    )

__all__ = [
    "PncMapping",
    "PncMappingIdent",
]
