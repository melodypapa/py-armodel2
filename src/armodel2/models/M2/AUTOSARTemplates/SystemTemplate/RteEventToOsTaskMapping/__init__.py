"""RteEventToOsTaskMapping module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.RteEventToOsTaskMapping.os_task_proxy import (
        OsTaskProxy,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.RteEventToOsTaskMapping.app_os_task_proxy_to_ecu_task_proxy_mapping import (
        AppOsTaskProxyToEcuTaskProxyMapping,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.RteEventToOsTaskMapping.rte_event_in_composition_to_os_task_proxy_mapping import (
        RteEventInCompositionToOsTaskProxyMapping,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.RteEventToOsTaskMapping.rte_event_in_composition_separation import (
        RteEventInCompositionSeparation,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.RteEventToOsTaskMapping.rte_event_in_system_to_os_task_proxy_mapping import (
        RteEventInSystemToOsTaskProxyMapping,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.RteEventToOsTaskMapping.rte_event_in_system_separation import (
        RteEventInSystemSeparation,
    )

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.RteEventToOsTaskMapping.os_task_preemptability_enum import (
    OsTaskPreemptabilityEnum,
)

__all__ = [
    "AppOsTaskProxyToEcuTaskProxyMapping",
    "OsTaskPreemptabilityEnum",
    "OsTaskProxy",
    "RteEventInCompositionSeparation",
    "RteEventInCompositionToOsTaskProxyMapping",
    "RteEventInSystemSeparation",
    "RteEventInSystemToOsTaskProxyMapping",
]
