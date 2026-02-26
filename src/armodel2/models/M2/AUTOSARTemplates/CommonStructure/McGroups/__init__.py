"""McGroups module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.McGroups.mc_group import (
        McGroup,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.McGroups.mc_group_data_ref_set import (
        McGroupDataRefSet,
    )

__all__ = [
    "McGroup",
    "McGroupDataRefSet",
]
