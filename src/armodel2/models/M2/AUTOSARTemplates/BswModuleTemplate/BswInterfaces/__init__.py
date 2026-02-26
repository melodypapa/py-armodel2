"""BswInterfaces module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_module_entry import (
        BswModuleEntry,
    )
    from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_module_dependency import (
        BswModuleDependency,
    )
    from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_entry_relationship_set import (
        BswEntryRelationshipSet,
    )
    from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_entry_relationship import (
        BswEntryRelationship,
    )
    from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_module_client_server_entry import (
        BswModuleClientServerEntry,
    )

from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_entry_kind_enum import (
    BswEntryKindEnum,
)
from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_execution_context import (
    BswExecutionContext,
)
from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_call_type import (
    BswCallType,
)
from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_entry_relationship_enum import (
    BswEntryRelationshipEnum,
)

__all__ = [
    "BswCallType",
    "BswEntryKindEnum",
    "BswEntryRelationship",
    "BswEntryRelationshipEnum",
    "BswEntryRelationshipSet",
    "BswExecutionContext",
    "BswModuleClientServerEntry",
    "BswModuleDependency",
    "BswModuleEntry",
]
