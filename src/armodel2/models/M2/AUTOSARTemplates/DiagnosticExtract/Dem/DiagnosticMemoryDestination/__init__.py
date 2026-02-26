"""DiagnosticMemoryDestination module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticMemoryDestination.diagnostic_memory_destination import (
        DiagnosticMemoryDestination,
    )
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticMemoryDestination.diagnostic_memory_destination_primary import (
        DiagnosticMemoryDestinationPrimary,
    )
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticMemoryDestination.diagnostic_memory_destination_user_defined import (
        DiagnosticMemoryDestinationUserDefined,
    )

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticMemoryDestination.diagnostic_memory_entry_storage_trigger_enum import (
    DiagnosticMemoryEntryStorageTriggerEnum,
)
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticMemoryDestination.diagnostic_clear_dtc_limitation_enum import (
    DiagnosticClearDtcLimitationEnum,
)
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticMemoryDestination.diagnostic_event_displacement_strategy_enum import (
    DiagnosticEventDisplacementStrategyEnum,
)
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticMemoryDestination.diagnostic_type_of_freeze_frame_record_numeration_enum import (
    DiagnosticTypeOfFreezeFrameRecordNumerationEnum,
)

__all__ = [
    "DiagnosticClearDtcLimitationEnum",
    "DiagnosticEventDisplacementStrategyEnum",
    "DiagnosticMemoryDestination",
    "DiagnosticMemoryDestinationPrimary",
    "DiagnosticMemoryDestinationUserDefined",
    "DiagnosticMemoryEntryStorageTriggerEnum",
    "DiagnosticTypeOfFreezeFrameRecordNumerationEnum",
]
