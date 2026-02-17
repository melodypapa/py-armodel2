"""UserDefined module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.UserDefined.user_defined_global_time_master import (
        UserDefinedGlobalTimeMaster,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.UserDefined.user_defined_global_time_slave import (
        UserDefinedGlobalTimeSlave,
    )

__all__ = [
    "UserDefinedGlobalTimeMaster",
    "UserDefinedGlobalTimeSlave",
]
