"""NvBlockComponent module."""
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent.nv_block_descriptor import (
    NvBlockDescriptor,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent.mode_switch_event_triggered_activity import (
    ModeSwitchEventTriggeredActivity,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent.nv_block_data_mapping import (
    NvBlockDataMapping,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent.bulk_nv_data_descriptor import (
    BulkNvDataDescriptor,
)

__all__ = [
    "BulkNvDataDescriptor",
    "ModeSwitchEventTriggeredActivity",
    "NvBlockDataMapping",
    "NvBlockDescriptor",
]
