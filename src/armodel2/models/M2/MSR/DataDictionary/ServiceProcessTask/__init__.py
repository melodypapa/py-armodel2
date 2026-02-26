"""ServiceProcessTask module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.MSR.DataDictionary.ServiceProcessTask.sw_service_arg import (
        SwServiceArg,
    )

from armodel2.models.M2.MSR.DataDictionary.ServiceProcessTask.sw_service_impl_policy_enum import (
    SwServiceImplPolicyEnum,
)

__all__ = [
    "SwServiceArg",
    "SwServiceImplPolicyEnum",
]
