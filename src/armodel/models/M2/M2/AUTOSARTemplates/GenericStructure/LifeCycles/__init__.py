"""LifeCycles module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.LifeCycles.life_cycle_state_definition_group import (
        LifeCycleStateDefinitionGroup,
    )
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.LifeCycles.life_cycle_state import (
        LifeCycleState,
    )
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.LifeCycles.life_cycle_info_set import (
        LifeCycleInfoSet,
    )
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.LifeCycles.life_cycle_period import (
        LifeCyclePeriod,
    )
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.LifeCycles.life_cycle_info import (
        LifeCycleInfo,
    )

__all__ = [
    "LifeCycleInfo",
    "LifeCycleInfoSet",
    "LifeCyclePeriod",
    "LifeCycleState",
    "LifeCycleStateDefinitionGroup",
]
