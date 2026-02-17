"""FR module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.FR.global_time_fr_master import (
        GlobalTimeFrMaster,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.FR.global_time_fr_slave import (
        GlobalTimeFrSlave,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.FR.fr_global_time_domain_props import (
        FrGlobalTimeDomainProps,
    )

__all__ = [
    "FrGlobalTimeDomainProps",
    "GlobalTimeFrMaster",
    "GlobalTimeFrSlave",
]
