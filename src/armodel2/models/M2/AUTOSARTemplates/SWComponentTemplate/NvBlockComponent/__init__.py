"""NvBlockComponent module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent.nv_block_descriptor import (
        NvBlockDescriptor,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent.mode_switch_event_triggered_activity import (
        ModeSwitchEventTriggeredActivity,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent.nv_block_data_mapping import (
        NvBlockDataMapping,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent.bulk_nv_data_descriptor import (
        BulkNvDataDescriptor,
    )

from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent.ram_block_status_control_enum import (
    RamBlockStatusControlEnum,
)

__all__ = [
    "BulkNvDataDescriptor",
    "ModeSwitchEventTriggeredActivity",
    "NvBlockDataMapping",
    "NvBlockDescriptor",
    "RamBlockStatusControlEnum",
]
