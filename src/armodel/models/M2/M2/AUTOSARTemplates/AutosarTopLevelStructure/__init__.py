"""AutosarTopLevelStructure module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.autosar import (
        AUTOSAR,
    )
    from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.file_info_comment import (
        FileInfoComment,
    )

__all__ = [
    "AUTOSAR",
    "FileInfoComment",
]
