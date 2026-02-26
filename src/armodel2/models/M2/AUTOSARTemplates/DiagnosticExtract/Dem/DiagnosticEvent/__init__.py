"""DiagnosticEvent module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_event import (
        DiagnosticEvent,
    )
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_connected_indicator import (
        DiagnosticConnectedIndicator,
    )
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_iumpr import (
        DiagnosticIumpr,
    )
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_iumpr_group import (
        DiagnosticIumprGroup,
    )
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_iumpr_group_identifier import (
        DiagnosticIumprGroupIdentifier,
    )
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_iumpr_denominator_group import (
        DiagnosticIumprDenominatorGroup,
    )
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_abstract_alias_event import (
        DiagnosticAbstractAliasEvent,
    )
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_fim_alias_event_mapping import (
        DiagnosticFimAliasEventMapping,
    )

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_clear_event_allowed_behavior_enum import (
    DiagnosticClearEventAllowedBehaviorEnum,
)
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_event_clear_allowed_enum import (
    DiagnosticEventClearAllowedEnum,
)
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_event_kind_enum import (
    DiagnosticEventKindEnum,
)
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_connected_indicator_behavior_enum import (
    DiagnosticConnectedIndicatorBehaviorEnum,
)
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_iumpr_kind_enum import (
    DiagnosticIumprKindEnum,
)

__all__ = [
    "DiagnosticAbstractAliasEvent",
    "DiagnosticClearEventAllowedBehaviorEnum",
    "DiagnosticConnectedIndicator",
    "DiagnosticConnectedIndicatorBehaviorEnum",
    "DiagnosticEvent",
    "DiagnosticEventClearAllowedEnum",
    "DiagnosticEventKindEnum",
    "DiagnosticFimAliasEventMapping",
    "DiagnosticIumpr",
    "DiagnosticIumprDenominatorGroup",
    "DiagnosticIumprGroup",
    "DiagnosticIumprGroupIdentifier",
    "DiagnosticIumprKindEnum",
]
