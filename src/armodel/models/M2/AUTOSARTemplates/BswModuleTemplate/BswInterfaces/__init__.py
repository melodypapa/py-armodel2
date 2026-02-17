"""BswInterfaces module."""
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_module_entry import (
    BswModuleEntry,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_module_dependency import (
    BswModuleDependency,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_entry_relationship_set import (
    BswEntryRelationshipSet,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_entry_relationship import (
    BswEntryRelationship,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_module_client_server_entry import (
    BswModuleClientServerEntry,
)

__all__ = [
    "BswEntryRelationship",
    "BswEntryRelationshipSet",
    "BswModuleClientServerEntry",
    "BswModuleDependency",
    "BswModuleEntry",
]
