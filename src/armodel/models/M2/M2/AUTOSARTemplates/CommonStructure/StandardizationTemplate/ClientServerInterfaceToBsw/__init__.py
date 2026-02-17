"""ClientServerInterfaceToBsw module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.ClientServerInterfaceToBsw.client_server_operation_blueprint_mapping import (
        ClientServerOperationBlueprintMapping,
    )
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.ClientServerInterfaceToBsw.client_server_interface_to_bsw_module_entry_blueprint_mapping import (
        ClientServerInterfaceToBswModuleEntryBlueprintMapping,
    )

__all__ = [
    "ClientServerInterfaceToBswModuleEntryBlueprintMapping",
    "ClientServerOperationBlueprintMapping",
]
