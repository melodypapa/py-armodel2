"""AccessCount module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount.access_count_set import (
        AccessCountSet,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount.access_count import (
        AccessCount,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount.abstract_access_point import (
        AbstractAccessPoint,
    )

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount.rte_api_return_value_provision_enum import (
    RteApiReturnValueProvisionEnum,
)

__all__ = [
    "AbstractAccessPoint",
    "AccessCount",
    "AccessCountSet",
    "RteApiReturnValueProvisionEnum",
]
