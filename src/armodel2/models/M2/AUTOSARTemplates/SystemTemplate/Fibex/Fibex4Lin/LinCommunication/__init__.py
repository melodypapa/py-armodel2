"""LinCommunication module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_error_response import (
        LinErrorResponse,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_frame import (
        LinFrame,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_frame_triggering import (
        LinFrameTriggering,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_unconditional_frame import (
        LinUnconditionalFrame,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_sporadic_frame import (
        LinSporadicFrame,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_event_triggered_frame import (
        LinEventTriggeredFrame,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_schedule_table import (
        LinScheduleTable,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.schedule_table_entry import (
        ScheduleTableEntry,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.application_entry import (
        ApplicationEntry,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.free_format_entry import (
        FreeFormatEntry,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_configuration_entry import (
        LinConfigurationEntry,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.assign_frame_id import (
        AssignFrameId,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.unassign_frame_id import (
        UnassignFrameId,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.assign_frame_id_range import (
        AssignFrameIdRange,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.frame_pid import (
        FramePid,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.assign_nad import (
        AssignNad,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.conditional_change_nad import (
        ConditionalChangeNad,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.save_configuration_entry import (
        SaveConfigurationEntry,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.data_dump_entry import (
        DataDumpEntry,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.free_format import (
        FreeFormat,
    )

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_checksum_type import (
    LinChecksumType,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.run_mode import (
    RunMode,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.resume_position import (
    ResumePosition,
)

__all__ = [
    "ApplicationEntry",
    "AssignFrameId",
    "AssignFrameIdRange",
    "AssignNad",
    "ConditionalChangeNad",
    "DataDumpEntry",
    "FramePid",
    "FreeFormat",
    "FreeFormatEntry",
    "LinChecksumType",
    "LinConfigurationEntry",
    "LinErrorResponse",
    "LinEventTriggeredFrame",
    "LinFrame",
    "LinFrameTriggering",
    "LinScheduleTable",
    "LinSporadicFrame",
    "LinUnconditionalFrame",
    "ResumePosition",
    "RunMode",
    "SaveConfigurationEntry",
    "ScheduleTableEntry",
    "UnassignFrameId",
]
