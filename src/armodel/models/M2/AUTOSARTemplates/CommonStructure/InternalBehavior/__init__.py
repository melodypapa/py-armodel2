"""InternalBehavior module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.internal_behavior import (
        InternalBehavior,
    )
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.executable_entity import (
        ExecutableEntity,
    )
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.exclusive_area import (
        ExclusiveArea,
    )
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.exclusive_area_nesting_order import (
        ExclusiveAreaNestingOrder,
    )
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.executable_entity_activation_reason import (
        ExecutableEntityActivationReason,
    )
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.abstract_event import (
        AbstractEvent,
    )

from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.reentrancy_level_enum import (
    ReentrancyLevelEnum,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.api_principle_enum import (
    ApiPrincipleEnum,
)

__all__ = [
    "AbstractEvent",
    "ApiPrincipleEnum",
    "ExclusiveArea",
    "ExclusiveAreaNestingOrder",
    "ExecutableEntity",
    "ExecutableEntityActivationReason",
    "InternalBehavior",
    "ReentrancyLevelEnum",
]
