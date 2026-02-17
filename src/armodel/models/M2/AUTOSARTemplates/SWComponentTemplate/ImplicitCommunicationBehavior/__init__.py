"""ImplicitCommunicationBehavior module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior.consistency_needs import (
        ConsistencyNeeds,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior.runnable_entity_group import (
        RunnableEntityGroup,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior.data_prototype_group import (
        DataPrototypeGroup,
    )

__all__ = [
    "ConsistencyNeeds",
    "DataPrototypeGroup",
    "RunnableEntityGroup",
]
