"""AuxillaryObjects module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.MSR.DataDictionary.AuxillaryObjects.sw_addr_method import (
        SwAddrMethod,
    )

from armodel.models.M2.MSR.DataDictionary.AuxillaryObjects.memory_allocation_keyword_policy_type import (
    MemoryAllocationKeywordPolicyType,
)
from armodel.models.M2.MSR.DataDictionary.AuxillaryObjects.memory_section_type import (
    MemorySectionType,
)

__all__ = [
    "MemoryAllocationKeywordPolicyType",
    "MemorySectionType",
    "SwAddrMethod",
]
