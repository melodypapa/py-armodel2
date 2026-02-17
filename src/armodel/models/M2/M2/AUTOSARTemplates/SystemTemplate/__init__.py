"""SystemTemplate module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.system import (
        System,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.root_sw_composition_prototype import (
        RootSwCompositionPrototype,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.client_id_definition_set import (
        ClientIdDefinitionSet,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.client_id_definition import (
        ClientIdDefinition,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.system_mapping import (
        SystemMapping,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.com_management_mapping import (
        ComManagementMapping,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.j1939_shared_address_cluster import (
        J1939SharedAddressCluster,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.port_element_to_communication_resource_mapping import (
        PortElementToCommunicationResourceMapping,
    )

__all__ = [
    "ClientIdDefinition",
    "ClientIdDefinitionSet",
    "ComManagementMapping",
    "J1939SharedAddressCluster",
    "PortElementToCommunicationResourceMapping",
    "RootSwCompositionPrototype",
    "System",
    "SystemMapping",
]
