"""MemorySectionUsage module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.MemorySectionUsage.memory_section import (
        MemorySection,
    )
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.MemorySectionUsage.section_name_prefix import (
        SectionNamePrefix,
    )

__all__ = [
    "MemorySection",
    "SectionNamePrefix",
]
